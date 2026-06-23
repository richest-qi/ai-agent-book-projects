# Currency Conversion Demo

从 `week1/context` 抽取的**独立精简工程**，直接运行货币换算示例（Sample 1），无需交互式输入。

## 任务

将 $1000 USD 转换为 EUR、GBP、JPY，并计算三者换算结果的平均值。

## 运行

```bash
cd week1/currency-conversion
pip install -r requirements.txt
cp env.example .env   # 填入 ARK_API_KEY 等
python main.py
```

所有配置在 `.env` 中设置（`ARK_API_KEY`、`MODEL_NAME`），见 `env.example`。

## 豆包 API 地址说明

火山方舟文档中的 Chat API 完整地址为：

```text
https://ark.cn-beijing.volces.com/api/v3/chat/completions
```

本工程使用 OpenAI 兼容 SDK（`openai` 包），`agent.py` 中配置的是 **API 根路径** `base_url`，而不是完整 endpoint：

```python
OpenAI(
    api_key=api_key,
    base_url="https://ark.cn-beijing.volces.com/api/v3",  # 不含 /chat/completions
)
```

调用 `client.chat.completions.create(...)` 时，SDK 会自动拼接路径：

```text
base_url + /chat/completions
= https://ark.cn-beijing.volces.com/api/v3/chat/completions
```

因此 `base_url` 与文档中的完整 URL **并不矛盾**，写法是正确的。

常见误配：

| 写法 | 结果 |
|------|------|
| `base_url=".../api/v3"` + `chat.completions.create()` | 正确 |
| `base_url=".../api/v3/chat/completions"` | 错误，SDK 会再拼 `/chat/completions`，导致 404 |
| `base_url="https://ark.cn-beijing.volces.com"` | 错误，缺少 `/api/v3` 前缀 |

## Chat API 请求与响应

本工程使用 **Chat Completions API**（`client.chat.completions.create`），每轮 Agent 循环都会发起一次 HTTP 请求。

### 请求参数

`agent.py` 中每次调用传入的参数如下：

| 参数 | 本工程取值 | 说明 |
|------|-----------|------|
| `model` | `.env` 中的 `MODEL_NAME` | 模型 ID，如 `doubao-seed-2-0-lite-260428` |
| `messages` | 累积的对话历史数组 | 含 system、user、assistant、tool 等角色消息 |
| `tools` | `TOOLS_SCHEMA` | 可用工具定义（`convert_currency`、`calculate`） |
| `tool_choice` | `"auto"` | 由模型自行决定是否调用工具 |
| `temperature` | `0.3` | 采样温度，越低输出越稳定 |
| `max_tokens` | `8192` | 单次回复最大 token 数 |
| `timeout` | `180` | 请求超时（秒） |

货币换算任务通常需要 **3 轮** Chat API 调用（3 次 iteration），`messages` 会随工具调用结果不断增长。

### 响应结构（首轮示例）

首轮响应中，模型选择并行调用 3 次 `convert_currency`，典型字段如下：

| 字段 | 含义 |
|------|------|
| `id` | 本次 completion 的唯一 ID |
| `choices[0].finish_reason` | `"tool_calls"` 表示模型要调用工具，而非直接给最终文本 |
| `choices[0].message.tool_calls` | 工具调用列表（可一次返回多个） |
| `choices[0].message.content` | 面向用户的可见回复（调用工具时可能为空字符串） |
| `model` | 实际使用的模型 |
| `usage.prompt_tokens` / `completion_tokens` | token 用量统计 |

### `tool_calls` 对象结构

当 `finish_reason` 为 `"tool_calls"` 时，模型不直接给最终文本（`content` 常为空），而是在 `choices[0].message.tool_calls` 里列出要执行的工具。它是一个**数组**，每个元素形如：

```json
{
  "id": "call_e21osh8haywubjdgm1ixm3yd",
  "type": "function",
  "function": {
    "name": "convert_currency",
    "arguments": "{\"amount\": 1000, \"from_currency\": \"USD\", \"to_currency\": \"EUR\"}"
  }
}
```

| 字段 | 类型 | 含义 |
|------|------|------|
| `id` | string | 本次工具调用的唯一 ID；后续 `role: "tool"` 消息必须用 `tool_call_id` 回指它 |
| `type` | string | 固定为 `"function"`（OpenAI function calling 格式） |
| `function.name` | string | 工具名，如 `convert_currency`、`calculate` |
| `function.arguments` | string | **JSON 字符串**（不是对象），需 `json.loads()` 解析 |

`agent.py` 中的解析方式：

```python
for tool_call in message.tool_calls:
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
```

工具执行完后，须为**每个** `tool_calls` 条目追加一条 `role: "tool"` 消息：

```json
{
  "role": "tool",
  "tool_call_id": "call_e21osh8haywubjdgm1ixm3yd",
  "content": "{\"converted_amount\": 920.0, ...}"
}
```

对应关系：`tool_calls[i].id` ↔ `tool` 消息的 `tool_call_id`；`content` 为工具返回结果的 JSON 字符串。

### 本例完整 `tool_calls` 轨迹（3 轮 API、4 次工具）

**Iteration 1** — 模型一次返回 3 个 `convert_currency`（并行）：

| # | id（示例） | name | arguments |
|---|-----------|------|-----------|
| 1 | `call_e21osh8...` | `convert_currency` | `amount=1000, USD → EUR` |
| 2 | `call_tzfk9n...` | `convert_currency` | `amount=1000, USD → GBP` |
| 3 | `call_w4p4oz...` | `convert_currency` | `amount=1000, USD → JPY` |

本地执行结果 → 920.0 EUR、790.0 GBP、149500.0 JPY，各写回一条 `role: "tool"` 消息。

**Iteration 2** — 模型返回 1 个 `calculate`：

| # | id（示例） | name | arguments |
|---|-----------|------|-----------|
| 4 | `call_1jvh3f...` | `calculate` | `"(920 + 790 + 149500) / 3"` |

工具返回 `result: 50403.333...`，再写回一条 `role: "tool"` 消息。

**Iteration 3** — 无 `tool_calls`（`tool_calls: null`，`finish_reason: "stop"`），`content` 含 `FINAL ANSWER:` 及最终总结。

`messages` 数组随轮次增长示意：

```text
[system]
[user]              ← 换算任务
[assistant]         ← tool_calls ×3（第 1 轮）
[tool] ×3           ← 3 个换算结果
[assistant]         ← tool_calls ×1（第 2 轮）
[tool] ×1           ← 平均值计算结果
[assistant]         ← FINAL ANSWER（第 3 轮）
```

因此 Chat API **每轮都要把完整 `messages` 再传一遍**；`tool_calls` 与 `tool` 结果必须成对出现，模型才能继续推理。

### Chat API vs Responses API

| | **Chat API**（本工程） | **Responses API** |
|---|---|---|
| 调用方式 | `client.chat.completions.create(...)` | `client.responses.create(...)` |
| 上下文管理 | **每次请求传入完整 `messages` 数组** | 默认**服务端持久化**，后续轮次传 `previous_response_id` 即可 |
| 适用场景 | Agent 工具循环、需精确控制每条消息 | 多轮闲聊、上下文由平台托管 |
| 本仓库示例 | `week1/currency-conversion` | `review/demos/demo1/main_multiturn.py` |

Chat API 下，Agent 必须在本地维护 `conversation_history`，每轮把 system prompt、用户任务、历史 assistant 回复、工具调用及 tool 结果全部放进 `messages`——这正是 `agent.py` 中 `execute_task` 循环所做的工作。

Responses API 则类似：

```python
# 第 1 轮
response = client.responses.create(model=MODEL, input=user_1)

# 第 2 轮：只需传上一轮 id + 新输入，无需重复历史
second = client.responses.create(
    model=MODEL,
    previous_response_id=response.id,
    input=[{"role": "user", "content": user_2}],
)
```

本工程选用 Chat API，是因为工具调用（function calling）需要显式地在 `messages` 中往返 `tool_calls` 与 `tool` 结果，便于学习和调试完整 Agent 轨迹。

## 与 week1/context 的区别

| | `week1/context` | 本工程 |
|---|---|---|
| 入口 | 交互式 REPL | `python main.py` 直接跑完 |
| 任务 | 5 个 sample + 消融实验 | 仅货币换算任务 |
| 工具 | PDF、code_interpreter 等 | `convert_currency`、`calculate` |
| 依赖 | 较多 | 仅 `openai`、`python-dotenv` |

代码为独立副本，修改 `week1/context` 不会影响本目录。
