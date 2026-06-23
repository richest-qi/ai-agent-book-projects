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
| `usage.completion_tokens_details.reasoning_tokens` | 思考过程消耗的 token 数（豆包 thinking 模型） |
| `model` | 实际使用的模型 |
| `usage.prompt_tokens` / `completion_tokens` | token 用量统计 |

**关于 `reasoning_content`**

你在原始 JSON / `repr()` 输出里可能看到 `reasoning_content` 和 `encrypted_content`，这是**豆包 thinking 模型的厂商扩展字段**，不是 OpenAI 标准 Chat API 的固定 schema。

因此：

- 在**响应 JSON** 或 `message.model_dump()` 里通常能读到 `reasoning_content`
- 用 SDK 对象做 **`.` 属性访问不一定可靠**（取决于 `openai` 包版本；较旧版本可能没有该属性，IDE 补全也常不显示）

较稳妥的读取方式：

```python
msg = response.choices[0].message
data = msg.model_dump()  # 或 msg.dict()
reasoning = data.get("reasoning_content")  # 可能为 None
```

若只需知道「有没有思考、花了多少 token」，可看 `response.usage.completion_tokens_details.reasoning_tokens`。

工具执行完毕后，代码将 `assistant` 消息和 `tool` 结果追加到 `messages`，再发起下一轮请求，直到模型输出含 `FINAL ANSWER:` 的文本。

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
