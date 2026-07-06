# Local LLM Serving Demo — Mode C（阻塞）

**模式 C**：Ollama API `stream=False`，每次请求等完整响应后再处理；`main.py` 一次性打印答案。展示方式最接近 [`week1/web-search-demo`](../../week1/web-search-demo)。

**定位：调试学习项目** — 默认打印每次阻塞响应的 `thinking` / `tool_calls` / `content` 分解，与模式 B 对照；不需要时设 `DEBUG_RESPONSE=0`。

与 [`../local-llm-serving-demo`](../local-llm-serving-demo)（模式 A）和 [`../local-llm-serving-demo-buffer`](../local-llm-serving-demo-buffer)（模式 B）并列。

## 三种模式对照

| | 模式 A（流式 yield） | 模式 B（流式缓冲） | **模式 C（本项目）** |
|--|---------------------|----------------------|----------------------|
| 目录 | `local-llm-serving-demo` | `local-llm-serving-demo-buffer` | `local-llm-serving-demo-blocking` |
| Ollama API | `stream=True` | `stream=True` | `stream=False` |
| Agent 返回 | `yield` 事件 generator | `dict` | `dict` |
| 控制台答案 | 逐 token 打印 | 整段一次打印 | **整段一次打印** |
| 与 web-search-demo | 展示不同 | 展示相近 | **API 与展示均相近** |

**模式 C 特点**：无 HTTP token 流；每次 `client.chat()` 返回完整 `message` 对象，逻辑最简单，适合对照学习「Agent 循环」本身，而不被流式细节干扰。

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
| `DEBUG_RESPONSE` | 打印阻塞响应分解 | `1`（默认开） |

### 调试输出说明

与模式 B 的逐 `[chunk]` 对照，模式 C 每次 POST **一次返回完整 message**：

调试时直接打印 Ollama 返回的原始 JSON（含 `message.thinking`、`tool_calls`、`content` 等字段的真实值）：

```text
[response] iteration=1
{
  "model": "qwen3:0.6b",
  "message": {
    "role": "assistant",
    "content": "",
    "thinking": "Okay, the user is asking...",
    "tool_calls": [...]
  },
  "done": true
}
```

| 工具结果 | 每个工具执行后立刻打印 `→` / `✓` | 同左 |

Iteration 2 的 JSON 中 `tool_calls` 为 `null`、`content` 有正文。安静运行：`DEBUG_RESPONSE=0 python main.py`

## `stream=False` 响应与最终判断

与模式 B 共用同一套 Agent 分支（见 [`buffer` README](../local-llm-serving-demo-buffer/README.md)「对照模式 C」），此处仅强调阻塞 API 特点。

每次 `client.chat(stream=False)` 返回**一份完整 JSON**；`done=True` 只表示本轮 HTTP 结束，**不**表示整个任务结束。

**结束条件**：`message.tool_calls` 为空 → `message.content` 为最终答案并 `return`；否则执行工具后 `continue` 下一轮 POST。

## 执行流程

```text
ollama_native   response = client.chat(..., stream=False)
                message = response["message"]
                if tool_calls: execute_tool → continue
                else: return {"answer": message["content"], ...}
main.py         print(result["answer"])
```

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
├── config.py
├── ollama_native.py  # stream=False，阻塞响应
├── tools.py
├── requirements.txt
└── env.example
```

## 延伸阅读

- 流式 yield 与两层 chunk：[`../local-llm-serving-demo/README.md`](../local-llm-serving-demo/README.md)
- API 流式但展示缓冲：[`../local-llm-serving-demo-buffer`](../local-llm-serving-demo-buffer)
