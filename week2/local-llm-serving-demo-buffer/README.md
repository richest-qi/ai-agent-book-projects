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
| 工具过程 | 实时 chunk 展示 | 任务结束后统一打印 | 任务结束后统一打印 |

**模式 B 与 A 的差别**：HTTP 仍是流式收包，但 `ollama_native.py` 用 `collected` 列表攒齐后再返回，用户看不到边收边印。

**模式 B 与 C 的差别**：API 层仍 `stream=True`（适合将来做进度条或内部监控），展示层与 C 一样是一次性输出。

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

区别在 **展示层**：

```text
ollama_native   for chunk in stream_response: collected.append(piece)   ← 只缓冲，不 yield
ollama_native   return {"answer": "".join(collected), ...}
main.py         print(result["answer"])                                ← 一次性输出
```

## 文件结构

```
local-llm-serving-demo-buffer/
├── main.py           # 调用 execute_task()，打印 tool_records + answer
├── config.py
├── ollama_native.py  # stream=True，内存缓冲
├── tools.py
├── requirements.txt
└── env.example
```

## 延伸阅读

- 模式 A 的 generator / yield 详解：[`../local-llm-serving-demo/README.md`](../local-llm-serving-demo/README.md)
- 与 `web-search-demo` 最接近的阻塞模式：[`../local-llm-serving-demo-blocking`](../local-llm-serving-demo-blocking)
