# Local LLM Serving Demo

基于本地 **Ollama** 的工具调用单次任务 demo，从 [`../local_llm_serving`](../local_llm_serving) 复制核心代码，**完全独立**，不依赖父目录。

与父项目的交互模式不同：运行 `python main.py` 即执行固定任务，无需 CMD 输入。

本项目为 **模式 A**（API `stream=True` + Python `yield` + 逐字打印）。同目录下还有两个独立兄弟项目，便于对比展示策略：

| 模式 | 目录 | Ollama API | 展示 |
|------|------|------------|------|
| **A（本项目）** | `local-llm-serving-demo` | `stream=True` | `yield` + `print(end="")` 打字机 |
| B | [`local-llm-serving-demo-buffer`](../local-llm-serving-demo-buffer) | `stream=True` | 内存缓冲，整段一次打印 |
| C | [`local-llm-serving-demo-blocking`](../local-llm-serving-demo-blocking) | `stream=False` | 阻塞响应，整段一次打印（近 `web-search-demo`） |

Agent 工具调用逻辑相同；差别仅在 API 是否流式、以及 `main.py` 如何展示结果。

## 前置条件

1. 安装 [Ollama](https://ollama.com)
2. 启动服务并拉取默认模型：

```cmd
ollama serve
ollama pull qwen3:0.6b
```

### Ollama 常用命令

`<model>` 为模型名，本项目默认 `qwen3:0.6b`。

| 命令 | 作用 |
|------|------|
| `ollama list` | 查看已安装模型 |
| `ollama pull <model>` | 下载模型 |
| `ollama run <model>` | 交互测试（`/bye` 退出） |
| `ollama stop <model>` | 从内存卸载模型，释放显存（不删磁盘文件） |
| `ollama rm <model>` | 删除本机模型文件 |

### Windows 服务管理

| 命令 | 作用 |
|------|------|
| `tasklist \| findstr ollama` | 查看 Ollama 进程，最后一列为 PID |
| `taskkill /F /PID <pid>` | 结束指定进程（如 `taskkill /F /PID 6012`） |
| `ollama serve` | 重新启动 Ollama 服务 |

## 快速开始

```bash
cd week2/local-llm-serving-demo
pip install -r requirements.txt
python main.py
```

Windows 上 `get_current_time` 依赖 IANA 时区库，请确保已安装 `tzdata`（已写入 `requirements.txt`）。

默认任务（温哥华当前时间与天气）：

> What's the current time and weather like in Vancouver right now?

## 配置

复制 `env.example` 为 `.env`，或在 `config.py` 中修改：

| 变量 | 说明 | 默认 |
|------|------|------|
| `OLLAMA_MODEL` | Ollama 模型名 | `qwen3:0.6b` |
| `TASK` | 固定任务文本 | 温哥华时间+天气 |
| `STREAM` | 是否流式输出 | `true` |
| `DEFAULT_TEMPERATURE` | 采样温度 | `0.7` |

## 可用工具

与父项目相同，由 `tools.py` 注册：

- `get_current_temperature` — Open-Meteo 天气
- `get_current_time` — 时区时间
- `convert_currency` — 货币换算
- `code_interpreter` — Python 代码执行

## Agent 执行流程与调试要点

与 [`week1/web-search-demo`](../../week1/web-search-demo) 相同：任务入口在 `execute_task()` 里**一次性**初始化 `messages`（`system` + `user`），循环内只追加 `assistant` / `tool`。

温哥华时间+天气题，正常一次运行会有 **2 次** `POST /api/chat`：

| 次序 | 作用 |
|------|------|
| 第 1 次 | 模型返回 `tool_calls`（如 `get_current_time`、`get_current_temperature`） |
| 中间 | **无 HTTP** — Python 在本地执行 `tools.py` |
| 第 2 次 | 模型根据 `role: tool` 结果生成最终自然语言答案 |

控制台里的 `🔧 Tool Calls` / `✓` **不是 Ollama 打印的**，而是 `main.py` 根据 `ollama_native.py` 发出的 chunk 展示的。

### 消息初始化（对齐 week1 demo）

```python
# ollama_native.execute_task()
self.conversation_history = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": task},
]
```

### Generator 与 yield 入门

流式模式依赖 Python 的 **generator（生成器）**。若不熟悉，可先读本节，再看下一节的执行顺序图。

#### 普通函数 vs 生成器函数

普通函数一次性跑完并 `return`：

```python
def normal():
    print("A")
    print("B")
    return "结束"   # 函数结束，无法再回到中间

normal()  # 连续输出 A、B
```

带 `yield` 的函数是 **生成器函数**，调用后得到 generator 对象，**不会立刻执行完函数体**：

```python
def stream_events():
    print("步骤1：请求模型")
    yield {"type": "tool_call", "name": "get_current_time"}  # 暂停，交出结果
    print("步骤2：执行工具")
    yield {"type": "tool_result", "content": "..."}            # 再暂停
    print("步骤3：完成")

gen = stream_events()  # 此时还不会打印「步骤1」
```

#### `yield` 是什么意思？

`yield` = **在这里停一下，把当前值交给外面；等外面处理完再来，从下一行继续执行**。

`main.py` 用 `for` 循环「消费」generator：

```python
for chunk in agent.execute_task(task, stream=True):
    print(chunk)   # 每收到一个 yield 出来的 chunk，处理一次
```

可运行的最小示例（帮助理解「先打印、后执行工具」的现象）。完整文件见 [`generator_demo.py`](generator_demo.py)：

```python
def demo():
    print("  [agent] 开始")
    yield {"type": "tool_call", "name": "get_time"}
    print("  [agent] 执行工具中...")
    yield {"type": "tool_result", "data": "19:32"}
    print("  [agent] 结束")

for chunk in demo():
    print(f"[main] 收到: {chunk}")
```

输出顺序：

```text
  [agent] 开始
[main] 收到: {'type': 'tool_call', 'name': 'get_time'}
  [agent] 执行工具中...          ← 在第一次「收到」之后才执行
[main] 收到: {'type': 'tool_result', 'data': '19:32'}
  [agent] 结束

[main] 全部结束
```

运行：

```bash
python generator_demo.py
```

#### 为什么要用 generator？

| 方式 | 行为 |
|------|------|
| `return` 整个列表 | 全部做完后一次性返回 |
| `yield` 逐个产出 | 每完成一小步就交给 `main.py` 打印 |

本 demo 需要分阶段展示：`tool_call` → `tool_result` → 最终 `content`，因此用 generator 在**不同时刻**把事件送给 `main.py`。

#### 与本项目的对应关系

| 概念 | 本项目中的位置 |
|------|----------------|
| 生成器函数 | `execute_task(..., stream=True)` → `_react_stream()` |
| `for chunk in ...` | `main.py` 第 63 行起 |
| `yield tool_call` | `ollama_native.py` 解析到 `tool_calls` 后 |
| `yield` 下一行 | `execute_tool(...)` 真正调用 `tools.py` |
| `yield content` | 第 2 轮 API 的最终答案 |

### 流式模式下的执行顺序（结合 generator）

`execute_task(..., stream=True)` 返回 generator。每次 `yield` 会暂停 `ollama_native.py`，把控制权交回 `main.py` 的 `for chunk in ...`；`main.py` 处理完当前 chunk 后，for 循环进入下一轮，generator 从 `yield` **下一行**继续执行。

因此调试时常见顺序如下（每个工具都类似）：

```text
main.py          for chunk in execute_task(...)
                       ↓
ollama_native    client.chat(stream=True)     ← 第 1 次 POST
                       ↓ 流式 chunk 中出现 tool_calls
ollama_native    yield {"type": "tool_call"}  ← 暂停，尚未执行工具
                       ↓
main.py          打印  🔧 Tool Calls: → get_current_time: {...}
                       ↓ for 循环继续 = 恢复 generator
ollama_native    execute_tool(...)            ← 真正调用 tools.py
ollama_native    yield {"type": "tool_result"}
                       ↓
main.py          打印  ✓ {"timezone": "America/Vancouver", ...}
```

`get_current_temperature` 重复上述模式。两个工具都完成后，`conversation_history` 中已有 `tool` 消息，进入 **第 2 轮** API：

```text
ollama_native    client.chat(stream=True)     ← 第 2 次 POST
ollama_native    yield {"type": "content", ...}
main.py          打印  🤖 Assistant: ...
```

**要点**：`yield tool_call` 只表示「模型决定要调工具」；`execute_tool` 在**下一次**恢复 generator 时才运行。先看到 `main.py` 打印、再进入 `tools.py`，是 generator 的正常行为，不是 bug。

### `stream=True`、`yield` 与逐字输出（两层 chunk）

调试时容易把两个都叫「chunk」的东西混在一起，其实分两层：

| 层级 | 是什么 | 代码位置 |
|------|--------|----------|
| **Ollama HTTP 流** | 模型 `stream=True` 时，网络上一包一包推 JSON，每包 `message.content` 可能只有 `"The"` 或 `" current"` | `for chunk in stream_response`（`ollama_native.py`） |
| **应用事件** | 你们定义的 `{"type": "tool_call" \| "tool_result" \| "content", ...}` | `yield ...` → `main.py` 的 `for chunk in execute_task(...)` |

#### 第二次 POST：答案如何「一个词一个词」出来

工具执行完后，第 2 轮 `client.chat(stream=True)` 时，模型**不是**先写好整段话再一次返回，而是边生成边推送 token 片段，例如：

```text
Ollama 第 1 小包:  message.content = "The"
Ollama 第 2 小包:  message.content = " current"
Ollama 第 3 小包:  message.content = " time"
...
拼成完整句:        "The current time in Vancouver is 01:45, with ..."
```

（实际是 **token 片段**，不一定是完整英文单词。）

对应代码链路：

```text
Ollama 推 "The"     →  yield {type:content, content:"The"}     →  print("The", end="", flush=True)
Ollama 推 " current"→  yield {type:content, content:" current"}→  print(" current", end="", flush=True)
...
流结束              →  ''.join(collected_content) 写入 conversation_history
```

```python
# ollama_native.py — 每收到 Ollama 一小段就 yield
yield {"type": "content", "content": content_chunk}

# main.py — 不换行、立刻刷新，所以多片在同一行连成整句
print(content, end="", flush=True)
```

#### 整句话是 `yield` 的结果还是 `stream=True` 的结果？

**两者分工不同，共同造成你看到的打字机效果：**

| 环节 | 作用 | 没有它会怎样 |
|------|------|----------------|
| **`stream=True`（Ollama API）** | 响应被拆成很多小片 `content` 陆续到达 | 一次 HTTP 返回整句，没有逐 token |
| **`yield`（Python generator）** | 每收到一小片就立刻交给 `main.py` | 可在内部攒齐再一次性返回，控制台不边收边印 |
| **`print(..., end="", flush=True)`** | 每片接到就接着上一片打印 | 多片可能不会即时显示在同一行 |

- **「拆成很多小片」** → 主要是 **`stream=True`**
- **「每来一片就立刻显示」** → **`yield` + `for` 循环 + `print(end="")`**
- **「语义上是一整句话」** → 模型生成的完整答案；流式只是**传输方式**分段，`join(collected_content)` 也会拼成完整字符串记入 `messages`

#### 一次性输出（模式 B / C）

若不需要逐字展示，请使用兄弟项目：

- **模式 B** [`local-llm-serving-demo-buffer`](../local-llm-serving-demo-buffer) — API 仍 `stream=True`，内部缓冲后一次打印
- **模式 C** [`local-llm-serving-demo-blocking`](../local-llm-serving-demo-blocking) — API `stream=False`，最接近 [`web-search-demo`](../../week1/web-search-demo)

本仓库（模式 A）的 `config.STREAM=false` 路径未单独维护；推荐直接用模式 C。

#### 与 `web-search-demo` 为何不用 chunk

| | `web-search-demo` | 本项目（`STREAM=true`） |
|--|-------------------|-------------------------|
| 发 API | `completions.create()` **无** `stream=True`，等完整响应 | `client.chat(stream=True)`，token 流式 |
| Agent 循环 | `while` + `return answer` | 相同思路的 ReAct 循环 |
| 交给 main | 一个字符串 | `yield` 多个事件（`tool_call` / `tool_result` / `content`） |
| 工具过程 | `logger.info` | chunk 打印 + 日志 |
| 最终答案 | 一次性 `print(answer)` | 多片 `content` 连续 `print` 成一行 |

**Agent 大脑一样**（初始化 messages → tool_calls → 执行工具 → 再问模型）；差别在是否流式 API、是否用 generator 把中间步骤实时展示给用户。

### chunk 类型对照

| `chunk["type"]` | 产生位置 | `main.py` 表现 |
|-----------------|----------|----------------|
| `tool_call` | 解析 Ollama 响应中的 `message.tool_calls` | `🔧 Tool Calls:` + 工具名与参数 |
| `tool_result` | `tools.py` 执行完毕 | `✓` + JSON 结果 |
| `content` | 第 2 轮 API 的流式文本 | `🤖 Assistant:` + 最终答案 |
| `thinking` | 模型思考片段（若有） | 灰色 `🧠 Thinking:` |

`tool_call` chunk 示例：

```python
{
    "type": "tool_call",
    "content": {
        "name": "get_current_time",
        "arguments": {"location": "Vancouver, Canada"},
    },
}
```

### 调试建议

| 想看什么 | 建议断点 |
|----------|----------|
| 模型是否返回 `tool_calls` | `ollama_native.py` 中 `'tool_calls' in message_chunk` |
| 本地工具是否执行 | `tool_registry.execute_tool(...)` 或 `tools.py` 内具体函数 |
| 控制台为何先打印再执行 | `main.py` 的 `elif chunk_type == "tool_call"`（generator 在 yield 处暂停） |

若只有 **1 次** POST、没有 `🔧 Tool Calls`，说明 `qwen3:0.6b` 本轮未走工具分支，直接编造了答案（小模型偶发）。日志里出现 `Executing tool:` 且 `✓` 中含 `Open-Meteo` / `America/Vancouver` 等字段，可确认工具已真实执行。

### 与 week1 demo 的差异

| | `web-search-demo` | 本项目 |
|--|-------------------|--------|
| 工具执行方 | Kimi 服务端（`$web_search`） | 本地 `tools.py` |
| 模型发起工具 | `finish_reason: tool_calls` | `message.tool_calls` |
| API 流式 | 否（一次拿完整响应） | 是（`stream=True`，见上一节） |
| 展示层 | 日志 + 最终 `print(answer)` | `yield` chunk + `main.py` 流式打印 |

## 与 `local_llm_serving` 的关系

| | `local_llm_serving` | 本项目 |
|--|---------------------|--------|
| 入口 | 交互模式 `/sample 3` | `python main.py` 直接跑 |
| 后端 | vLLM / Ollama 自动选择 | 仅 Ollama |
| 代码 | 完整工程 | 复制 `tools.py`、`ollama_native.py`，独立维护 |

## 文件结构

```
local-llm-serving-demo/
├── main.py           # 非交互入口
├── config.py         # 模型与固定任务
├── ollama_native.py  # Ollama 工具调用 Agent
├── tools.py          # 工具注册与实现
├── generator_demo.py # generator/yield 最小示例
├── requirements.txt
└── env.example
```
