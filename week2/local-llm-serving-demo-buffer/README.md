# Local LLM Serving Demo — Mode B（流式缓冲）

**模式 B**：Ollama API `stream=True`，在内存中拼齐 token 后再一次性打印；**无** Python `yield`、**无**逐字打字机效果。

**定位：调试学习项目** — 默认打印每个 HTTP chunk（`thinking` / `tool_calls` / `content`），观察流式响应过程；不需要时设 `DEBUG_CHUNKS=0`。

与 [`../local-llm-serving-demo`](../local-llm-serving-demo)（模式 A）和 [`../local-llm-serving-demo-blocking`](../local-llm-serving-demo-blocking)（模式 C）并列，便于对比三种展示策略。

## 三种模式对照

| | 模式 A（流式 yield） | **模式 B（本项目）** | 模式 C（阻塞） |
|--|---------------------|----------------------|----------------|
| 目录 | `local-llm-serving-demo` | `local-llm-serving-demo-buffer` | `local-llm-serving-demo-blocking` |
| Ollama API | `stream=True` | `stream=True` | `stream=False` |
| Agent 返回 | `yield` 事件 generator | `dict`（`answer` + `tool_records`） | `dict` |
| 控制台答案 | 逐 token `print(end="")` | **整段一次 `print`** | 整段一次 `print` |
| 工具过程 | 实时 chunk 展示 | 执行后立刻 `→` / `✓` | 同左 |

**模式 B 与 A 的差别**：HTTP 仍是流式收包，但 `ollama_native.py` 用 `collected` 列表攒齐后再返回，用户看不到边收边印。

**模式 B 与 C 的差别**：API 层仍 `stream=True`（包陆续到达），展示层与 C 一样是一次性输出。Agent **结束判断逻辑相同**（见下文「对照模式 C」），差别只在 HTTP 传输形态。

## 前置条件

```cmd
ollama serve
ollama pull qwen3:0.6b
```

## 快速开始

```bash
cd week2/local-llm-serving-demo-buffer
pip install -r requirements.txt
python main.py
```

默认任务：温哥华当前时间与天气（与 A/C 相同）。

## 配置

复制 `env.example` 为 `.env`：

| 变量 | 说明 | 默认 |
|------|------|------|
| `OLLAMA_MODEL` | 模型名 | `qwen3:0.6b` |
| `TASK` | 固定任务 | 温哥华时间+天气 |
| `DEFAULT_TEMPERATURE` | 采样温度 | `0.7` |
| `DEBUG_CHUNKS` | 打印每个 stream chunk | `1`（默认开） |

安静运行：`DEBUG_CHUNKS=0 python main.py`

## 执行流程

与模式 A 相同：第 1 次 POST → `tool_calls` → 本地 `tools.py` → 第 2 次 POST → 最终 `content`。

区别在 **展示层**（模式 B）：

```text
ollama_native   for chunk in stream_response: collected.append(piece)   ← 只缓冲，不 yield
ollama_native   return {"answer": "".join(collected), ...}
main.py         print(result["answer"])                                ← 一次性输出
```

工具结果在 `ollama_native.py` 内每个工具执行后立刻打印 `→` / `✓`（与模式 C 相同）。

## 对照：模式 C（`stream=False`）

与模式 B 并排学习时，重点对比 **HTTP 传输** 与 **结束判断**（后者两者相同）。

| | 模式 B `stream=True` | 模式 C `stream=False` |
|--|---------------------|----------------------|
| 每轮 HTTP | 多包 `[chunk]` 陆续到达 | 一份 JSON 一次返回 |
| 调试前缀 | `[chunk]` / `[response]` | `[response]` + 原始 JSON |
| 结束判断 | 看 `tool_calls` 是否为空 | 同左 |

### `stream=False` 时响应长什么样

模式 C 每次 `client.chat(stream=False)` **只发一次 HTTP**，等模型生成完毕后，**整份 JSON 一次返回**。调试时（`DEBUG_RESPONSE=1`，默认开）打印 Ollama 原始响应：

```text
[response] iteration=1
{
  "model": "qwen3:0.6b",
  "message": {
    "role": "assistant",
    "content": "",
    "thinking": "Okay, the user is asking...",
    "tool_calls": [
      {"function": {"name": "get_current_time", "arguments": {...}}},
      {"function": {"name": "get_current_temperature", "arguments": {...}}}
    ]
  },
  "done": true
}
```

要点：

| 字段 | Iteration 1（调工具） | Iteration 2（写答案） |
|------|----------------------|----------------------|
| `thinking` | 通常有整段推理文字 | 通常有 |
| `tool_calls` | 数组，含 1～N 个工具 | `null` 或 `[]` |
| `content` | 常为 `""` | 最终给用户看的正文 |
| `done` | `true`（仅表示**本轮 HTTP 传完**） | `true` |

与模式 B 不同：**没有** `[chunk]` 逐包过程；`thinking` / `tool_calls` / `content` 在同一时刻全部可用。

工具执行后立刻打印（不等到任务结束）：

```text
🔧 Tool Calls:
  → get_current_time: {'location': 'Vancouver, Canada'}
    ✓ {"timezone": "America/Vancouver", "datetime": "..."}
  → get_current_temperature: {'location': 'Vancouver, Canada'}
    ✓ {"temperature": 15.9, ...}
```

### 如何判断「最终响应」（模式 B / C 相同）

`ollama_native.py` 的 Agent 循环（B、C 共用同一套分支逻辑）：

```python
tool_calls = message.tool_calls or []

if tool_calls:
    # 模型还要调工具 → 执行 tools.py → continue 进入下一轮 POST
    ...
    continue

# 没有 tool_calls → 本轮 content 即为最终答案
answer = clean_content(message.content)
return {"success": True, "answer": answer, ...}
```

| 本轮 `message.tool_calls` | 行为 |
|---------------------------|------|
| 有内容（数组非空） | 执行工具，**继续**下一轮 `client.chat()` |
| 无（`null` / `[]`） | 取 `message.content` 作为答案，**`return` 结束** |

**不是**根据 `done` 判断任务是否结束：`done=True` 只表示这一轮阻塞响应已传完；Iteration 1 也可以是 `done=True` 但仍带 `tool_calls`，必须再 POST 一次。

温哥华时间+天气题正常 **2 次 POST**：

```text
POST #1   tool_calls 有值  → 执行 get_current_time / get_current_temperature
POST #2   tool_calls 为空  → content 为最终答案 → return
```

若连续 10 轮都有 `tool_calls`、始终没有纯文本结束，返回 `Error: Maximum iterations reached`。

完整阻塞模式说明与源码：[`../local-llm-serving-demo-blocking`](../local-llm-serving-demo-blocking)。

## 文件结构

```
local-llm-serving-demo-buffer/
├── main.py           # 调用 execute_task()，打印最终 answer
├── config.py
├── ollama_native.py  # stream=True，内存缓冲
├── tools.py
├── requirements.txt
└── env.example
```

## 延伸阅读

- 模式 A 的 generator / yield 详解：[`../local-llm-serving-demo/README.md`](../local-llm-serving-demo/README.md)
- 与 `web-search-demo` 最接近的阻塞模式：[`../local-llm-serving-demo-blocking`](../local-llm-serving-demo-blocking)
