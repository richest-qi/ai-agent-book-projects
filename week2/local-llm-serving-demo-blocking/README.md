# Local LLM Serving Demo — Mode C（阻塞）

**模式 C**：Ollama API `stream=False`，每次请求等完整响应后再处理；`main.py` 一次性打印答案。展示方式最接近 [`week1/web-search-demo`](../../week1/web-search-demo)。

**定位：调试学习项目** — 默认打印 Ollama 返回的**原始 JSON**（`DEBUG_RESPONSE=1`），与模式 B 的逐 `[chunk]` 对照；不需要时设 `DEBUG_RESPONSE=0`。

与 [`../local-llm-serving-demo`](../local-llm-serving-demo)（模式 A）和 [`../local-llm-serving-demo-buffer`](../local-llm-serving-demo-buffer)（模式 B）并列。

## 三种模式对照

| | 模式 A（流式 yield） | 模式 B（流式缓冲） | **模式 C（本项目）** |
|--|---------------------|----------------------|----------------------|
| 目录 | `local-llm-serving-demo` | `local-llm-serving-demo-buffer` | `local-llm-serving-demo-blocking` |
| Ollama API | `stream=True` | `stream=True` | `stream=False` |
| HTTP 传输 | 多包 chunk 陆续到达 | 同左 | **一份 JSON 一次返回** |
| Agent 返回 | `yield` 事件 generator | `dict` | `dict` |
| 控制台答案 | 逐 token 打印 | 整段一次打印 | 整段一次打印 |
| 工具结果 | 随 chunk 展示 | 执行后立刻 `→` / `✓` | 同左 |
| 调试输出 | — | `[chunk]` 逐包 | `[response]` + 原始 JSON |
| 与 web-search-demo | 展示不同 | 展示相近 | **API 与展示均相近** |

**模式 C 特点**：无 HTTP token 流；`thinking` / `tool_calls` / `content` 在同一时刻全部可用，适合先学 Agent 循环，再对照模式 B 的流式细节。

## 前置条件

```cmd
ollama serve
ollama pull qwen3:0.6b
```

## 快速开始

```bash
cd week2/local-llm-serving-demo-blocking
pip install -r requirements.txt
python main.py
```

## 配置

复制 `env.example` 为 `.env`：

| 变量 | 说明 | 默认 |
|------|------|------|
| `OLLAMA_MODEL` | 模型名 | `qwen3:0.6b` |
| `TASK` | 固定任务 | 温哥华时间+天气 |
| `DEFAULT_TEMPERATURE` | 采样温度 | `0.7` |
| `DEBUG_RESPONSE` | 打印阻塞响应原始 JSON | `1`（默认开） |

安静运行：`DEBUG_RESPONSE=0 python main.py`

---

## `stream=False` 阻塞响应详解

### 与模式 B 的核心差别

| | 模式 B `stream=True` | **模式 C `stream=False`** |
|--|----------------------|---------------------------|
| 一次 POST 内 | 几十～几百个 `[chunk]` 陆续到达 | **无 chunk**；等 3～10 秒后一次返回 |
| `thinking` | 拆成很多 `thinking 片段` 包 | **整段字符串**已在 `message.thinking` |
| `tool_calls` | 可能每工具 1 包，需 `_merge_tool_calls` | **数组一次给全**（常含 2 个工具） |
| `content` | Iteration 2 拆成很多 `content` 包 | **整段字符串**已在 `message.content` |
| 调试 | 观察「包如何陆续到达」 | 观察「一次拿到的完整 message」 |

### 一轮 POST 内的代码路径

```python
response = self.client.chat(..., stream=False)   # 阻塞，直到模型生成完毕
message = response["message"]
tool_calls = message.tool_calls or []

if DEBUG_RESPONSE:
    print(json.dumps(response))                  # 原始 JSON，不做改写

if tool_calls:
    for each: execute_tool → 立刻 print → / ✓
    continue                                     # 下一轮 POST

answer = clean_content(message.content)
return {"answer": answer, ...}
```

无 `for chunk` 循环；**收到 `response` 的那一刻**，`message` 里各字段已是最终形态。

### 调试输出：`[response]` + 原始 JSON

`DEBUG_RESPONSE=1` 时，每轮 Iteration 打印 Ollama **原样返回**的 JSON（非自定义摘要、无本地切分）：

**Iteration 1（调工具）** — 典型字段：

```json
{
  "model": "qwen3:0.6b",
  "done": true,
  "message": {
    "role": "assistant",
    "content": "",
    "thinking": "Okay, the user is asking for the current time and weather...",
    "tool_calls": [
      {"function": {"name": "get_current_time", "arguments": {"location": "Vancouver, Canada"}}},
      {"function": {"name": "get_current_temperature", "arguments": {"location": "Vancouver, Canada"}}}
    ]
  }
}
```

**Iteration 2（最终答案）** — 典型字段：

```json
{
  "done": true,
  "message": {
    "content": "The current time in Vancouver is **01:01:00**, and the weather is ...",
    "thinking": "Okay, the user asked for the current time and weather...",
    "tool_calls": null
  }
}
```

两轮字段对照：

| 字段 | Iteration 1（调工具） | Iteration 2（写答案） |
|------|----------------------|----------------------|
| `thinking` | 整段推理文字 | 整段推理文字 |
| `tool_calls` | 数组，含 1～N 个工具 | `null` 或 `[]` |
| `content` | 常为 `""` | 最终给用户看的正文 |
| `done` | `true`（仅表示**本轮 HTTP 结束**） | `true` |

JSON 顶层还可能包含 `total_duration`、`eval_count` 等性能字段，为 Ollama 原样输出，与 Agent 逻辑无关。

### 工具执行与打印顺序

`[response]` JSON 打印后，**立刻**按时间顺序执行工具并打印结果（不等到任务结束）：

```text
[response] iteration=1
{ ... "tool_calls": [ get_current_time, get_current_temperature ] }

🔧 Tool Calls:
  → get_current_time: {'location': 'Vancouver, Canada'}
    ✓ {"timezone": "America/Vancouver", "datetime": "..."}
  → get_current_temperature: {'location': 'Vancouver, Canada'}
    ✓ {"temperature": 15.6, ...}
```

这与模式 B 相同：工具结果紧跟 `Executing tool:` 日志，便于按时间线阅读。

### 如何判断「最终响应」

与模式 B **完全相同**（见 [`buffer` README](../local-llm-serving-demo-buffer/README.md#如何判断最终响应)）：

```python
tool_calls = message.tool_calls or []

if tool_calls:
    ...  # 执行 tools.py
    continue              # 进入下一轮 POST

answer = clean_content(message.content)
return {"answer": answer, ...}
```

| 本轮 `message.tool_calls` | 行为 |
|---------------------------|------|
| 非空 | 执行工具 → **`continue`** |
| `null` / `[]` | 取 `message.content` → **`return` 结束** |

注意：

- **`done: true` 不等于任务结束** — Iteration 1 也可以是 `done: true` 且带 `tool_calls`，必须再 POST 一次。
- **`thinking` 不参与 `answer`** — 只用于调试观察；返回给用户的是 `content`。
- 阻塞模式下 **不需要** `_merge_tool_calls` — 多个工具通常在同一个 `tool_calls` 数组里一次返回。

温哥华时间+天气题正常 **2 次 POST**：

```text
POST #1   tool_calls 数组有 2 项 → 执行工具 → continue
POST #2   tool_calls 为 null     → content 为答案 → return
```

### 完整时间线（模式 C）

```text
execute_task()
│
├─ Iteration 1 ── POST stream=False（等待 ~6s）────────────────
│    [response] iteration=1  → 打印完整 JSON
│    execute_tool × 2          → 立刻 → / ✓
│
├─ Iteration 2 ── POST stream=False（等待 ~9s）────────────────
│    [response] iteration=2  → 打印完整 JSON（content 有正文）
│    return answer
│
└─ main.py  print(answer)    ← 用户看到 🤖 Assistant 整段
```

对比模式 B：同样 2 次 POST，但模式 B 每次 POST 内有大量 `[chunk]`；模式 C 每次 POST 只有一行 `[response]` + 一整块 JSON。

### 与模式 A、B 一句话对比

| | HTTP | 收到响应时 | 用户看到答案的时机 |
|--|------|-----------|-------------------|
| **A** | `stream=True` | 多包，边收边 `yield` | 边收边印 |
| **B** | `stream=True` | 多包，缓冲后 `join` | `for chunk` 结束后 `main` 一次打印 |
| **C** | `stream=False` | **一包全有** | 同 B（`main` 一次打印） |

---

## 与 web-search-demo 对比

| | `web-search-demo` | 模式 C |
|--|-------------------|--------|
| 后端 | Kimi API | 本地 Ollama |
| 流式 | 否 | 否 |
| 工具 | 服务端 `$web_search` | 本地 `tools.py` |
| 返回给 main | 字符串 | `dict`（含 `tool_records`） |

Agent 核心循环一致：初始化 messages → 模型 tool_calls → 执行工具 → 再问模型 → 最终答案。

## 文件结构

```
local-llm-serving-demo-blocking/
├── main.py           # 调用 execute_task()，打印最终 answer
├── config.py         # DEBUG_RESPONSE 等
├── ollama_native.py  # stream=False，原始 JSON 调试打印
├── tools.py
├── requirements.txt
├── env.example
└── response.md       # 一次真实运行的 JSON 日志样例（可选参考）
```

## 延伸阅读

- 模式 A 的 generator / yield：[`../local-llm-serving-demo/README.md`](../local-llm-serving-demo/README.md)
- `stream=True` 流式 chunk 详解：[`../local-llm-serving-demo-buffer/README.md`](../local-llm-serving-demo-buffer/README.md)
