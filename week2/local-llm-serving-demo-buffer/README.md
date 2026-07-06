# Local LLM Serving Demo — Mode B（流式缓冲）

**模式 B**：Ollama API `stream=True`，在内存中拼齐 token 后再一次性打印；**无** Python `yield`、**无**逐字打字机效果。

**定位：调试学习项目** — 默认打印每个 HTTP chunk（`thinking` / `tool_calls` / `content`），观察流式响应过程；不需要时设 `DEBUG_CHUNKS=0`。

与 [`../local-llm-serving-demo`](../local-llm-serving-demo)（模式 A）和 [`../local-llm-serving-demo-blocking`](../local-llm-serving-demo-blocking)（模式 C）并列，便于对比三种展示策略。

## 三种模式对照

| | 模式 A（流式 yield） | **模式 B（本项目）** | 模式 C（阻塞） |
|--|---------------------|----------------------|----------------|
| 目录 | `local-llm-serving-demo` | `local-llm-serving-demo-buffer` | `local-llm-serving-demo-blocking` |
| Ollama API | `stream=True` | `stream=True` | `stream=False` |
| HTTP 传输 | 多包 chunk 陆续到达 | 同左 | 一份 JSON 一次返回 |
| Agent 返回 | `yield` 事件 generator | `dict`（`answer` + `tool_records`） | `dict` |
| 控制台答案 | 逐 token `print(end="")` | **整段一次 `print`** | 整段一次 `print` |
| 工具结果 | 随 chunk 实时展示 | 执行后立刻 `→` / `✓` | 同左 |
| 调试前缀 | — | `[chunk]` | `[response]` + 原始 JSON |

**模式 B 与 A**：API 同为 `stream=True`；A 每片 `yield` 给 `main` 边收边印，B 用 `collected` 缓冲后一次返回。

**模式 B 与 C**：Agent 结束判断相同；差别在 HTTP 是分包还是一次返回。阻塞模式见 [`blocking` README](../local-llm-serving-demo-blocking/README.md)。

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

---

## `stream=True` 流式响应详解

本节说明模式 B 的核心：Ollama **真实流式 HTTP** 下，每一包 `chunk` 是什么、代码如何处理、如何判断任务结束。

### 两层分工

| 层级 | 是什么 | 模式 B 的行为 |
|------|--------|----------------|
| **Ollama HTTP 流** | `stream=True` 时，一次 POST 内推很多 JSON 小包 | `for chunk in stream_response` 逐包接收（约 3～5 秒） |
| **展示层** | `main.py` 如何给用户看 | **不**边收边印；`join(collected)` 后一次性 `print(answer)` |

「拆成很多小片」来自 **`stream=True`**；「最后整段输出」是模式 B 的**刻意选择**（与模式 A 的 `yield` + `print(end="")` 不同）。

### 一轮 POST 内的代码路径

```python
stream_response = self.client.chat(..., stream=True)  # 返回迭代器，非列表

collected: List[str] = []
tool_calls: List = []

for chunk in stream_response:                    # 每来一个网络小包，循环一次
    piece = chunk["message"].get("content", "")
    if piece:
        collected.append(piece)                  # 有字就拼进列表（模式 B 不打印）
    if chunk["message"].get("tool_calls"):
        tool_calls = _merge_tool_calls(...)      # 工具信息可能分多包，需合并

# for 循环结束 = 本轮 HTTP 流结束
if tool_calls:
    execute_tool(...) → continue               # 进入下一轮 POST
else:
    answer = "".join(collected)                  # 无工具 → 拼好的 content 即最终答案
    return {"answer": answer, ...}
```

要点：`stream_response` 是**还在路上的管道**，不是已经拼好的完整句子；必须跑完整个 `for` 循环，才能知道本轮是「要调工具」还是「给最终答案」。

### `message` 里三个字段（qwen3）

每一包 `chunk["message"]` 可能携带：

| 字段 | 含义 | 用户最终答案里出现吗 |
|------|------|----------------------|
| `thinking` | 模型内部推理（草稿纸） | 否 |
| `tool_calls` | 要调用的工具名与参数 | 否（由 `tools.py` 执行） |
| `content` | 给用户看的正文 | 是（Iteration 2） |

调试时（`DEBUG_CHUNKS=1`）常见打印：

| 调试行 | 含义 |
|--------|------|
| `[chunk] content 空，thinking 片段: ' the'` | 本包没有 `content`，推理 token 在 `thinking` |
| `[chunk] content 空，但有 tool_calls (1)` + `name=...` | 本包携带工具调用信息 |
| `[chunk content] 'The'` | 本包有用户可见正文片段 |
| `[chunk] 结束包 done=true` | 本轮 HTTP 流结束（不等于整个任务结束） |

### 为什么很多包 `content` 为空？

`content` 空**不是**传了无意义数据，而是**这一小包没有新的用户可见文字**。模型可能在：

- 往 `thinking` 写字（Iteration 1 大量此类包）
- 往 `tool_calls` 拼工具名/参数 JSON
- 等待下一个 token（`content` 暂时为空）

只有 **Iteration 2 后半段** 才会大量出现 `[chunk content] 'The'`、`' current'` …

### Iteration 1：调工具（典型顺序）

温哥华时间+天气题，第 1 次 POST 内大致经历：

```text
① thinking 流（60～100+ 包）
   [chunk] content 空，thinking 片段: 'Okay'
   [chunk] content 空，thinking 片段: ' the'
   ...
   [chunk] content 空，thinking 片段: ' get_current_time'

② tool_calls 流（常 1 工具 1 包，可能 2 包）
   [chunk] content 空，但有 tool_calls (1)
            [1] name='get_current_time' arguments={"location": "Vancouver, Canada"}
   [chunk] content 空，但有 tool_calls (1)
            [1] name='get_current_temperature' arguments={"location": "Vancouver, Canada"}

③ 结束
   [chunk] 结束包 done=true
```

`for` 循环结束后，代码执行工具（立刻打印，不等到任务结束）：

```text
🔧 Tool Calls:
  → get_current_time: {'location': 'Vancouver, Canada'}
    ✓ {"timezone": "America/Vancouver", "datetime": "..."}
  → get_current_temperature: {'location': 'Vancouver, Canada'}
    ✓ {"temperature": 15.6, ...}
```

#### `tool_calls` 分包与 `_merge_tool_calls`

Ollama 流式下，多个工具可能**各占一包**，每包 `tool_calls` 长度仅为 1。若用 `tool_calls = chunk_tool_calls` 直接覆盖，会**丢掉前面的工具**（只保留最后一包）。

本项目使用 `_merge_tool_calls()` 按工具名合并，确保两包：

```text
包1: tool_calls → get_current_time
包2: tool_calls → get_current_temperature
```

合并后得到 2 个工具一并执行。

### Iteration 2：写最终答案（典型顺序）

第 2 次 POST 内：

```text
① thinking 流（模型根据工具结果组织答案）
   [chunk] content 空，thinking 片段: 'Okay'
   ...

② content 流（给用户看的正文，token 一片一片来）
   [chunk content] 'The'
   [chunk content] ' current'
   [chunk content] ' time'
   ...
   [chunk content] '!'

③ 结束
   [chunk] 结束包 done=true
```

模式 B 在 `for` 内只 `collected.append(piece)`，**不打印**；循环结束后 `"".join(collected)` 得到整句，再由 `main.py` 一次性输出：

```text
🤖 Assistant:
----------------------------------------
The current time in Vancouver, Canada is **01:05:16** ...
----------------------------------------
```

若开模式 A，同样的 `content` 包会 `yield` 给 `main` 并 `print(end="")`，产生打字机效果。

### 如何判断「最终响应」

**一轮 `for chunk` 跑完后**（不是某个 chunk 到达时）：

| 合并后的 `tool_calls` | 行为 |
|-----------------------|------|
| 非空 | 记入 `conversation_history` → 执行工具 → **`continue` 下一轮 POST** |
| 空 | `"".join(collected)` 为最终答案 → **`return` 结束任务** |

```python
if tool_calls:
    ...  # 执行工具
    continue

answer = self._clean_content("".join(collected))
return {"success": True, "answer": answer, ...}
```

注意：

- **`done=true` 的 chunk** 只表示**本轮 HTTP 流结束**；Iteration 1 也可以是 `done=true` 但仍带 `tool_calls`，必须再 POST。
- **结束条件与模式 C 相同**：看合并后的 `tool_calls` 是否为空，不是看 `done`。
- `thinking` 不参与 `answer` 返回，仅供调试观察。

温哥华题正常 **2 次 POST**：

```text
POST #1   for chunk… → thinking + tool_calls → 执行 2 个工具
POST #2   for chunk… → thinking + content   → return 最终答案
```

超过 10 轮仍有 `tool_calls`、始终没有纯 `content` 结束 → `Error: Maximum iterations reached`。

### 完整时间线（模式 B）

```text
execute_task()
│
├─ Iteration 1 ── POST stream=True ─────────────────────────────
│    for chunk: thinking 片段 × N
│    for chunk: tool_calls 包 × 1～2  → _merge_tool_calls
│    for chunk: done=true
│    execute_tool × 2（立刻 → / ✓）
│
├─ Iteration 2 ── POST stream=True ─────────────────────────────
│    for chunk: thinking 片段 × M
│    for chunk: content 片段 × K  → collected.append
│    for chunk: done=true
│    return answer = join(collected)
│
└─ main.py  print(answer)   ← 用户此时才看到 Assistant 整段
```

### 与模式 A、模式 C 一句话对比

| | HTTP | `for chunk` 内 | 用户看到答案的时机 |
|--|------|----------------|-------------------|
| **A** | `stream=True` | `yield` 每片给 `main` | 边收边印（打字机） |
| **B** | `stream=True` | `collected.append`，不 yield | `for` 跑完后 `main` 一次打印 |
| **C** | `stream=False` | 无 `for chunk` | 一次 JSON 到达后处理 |

---

## 文件结构

```
local-llm-serving-demo-buffer/
├── main.py           # 调用 execute_task()，打印最终 answer
├── config.py         # DEBUG_CHUNKS 等
├── ollama_native.py  # stream=True，chunk 缓冲 + 调试打印
├── tools.py
├── requirements.txt
├── env.example
└── response.md       # 一次真实运行的 chunk 日志样例（可选参考）
```

## 延伸阅读

- 模式 A 的 generator / yield 详解：[`../local-llm-serving-demo/README.md`](../local-llm-serving-demo/README.md)
- `stream=False` 阻塞响应与相同结束判断：[`../local-llm-serving-demo-blocking/README.md`](../local-llm-serving-demo-blocking/README.md)
