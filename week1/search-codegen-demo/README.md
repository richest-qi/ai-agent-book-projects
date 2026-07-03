# Search Codegen Demo

从 `week1/search-codegen` 抽取的**独立精简工程**，固定问题、无命令行交互，直接运行 OpenRouter + GPT-5 联网推理示例。

## 任务

> 东盟 10 国首都之间，距离最近的两个首都是？给出你的详细分析推理过程。

## 运行

```bash
cd week1/search-codegen-demo
pip install -r requirements.txt
cp env.example .env   # 填入 OPENROUTER_API_KEY
python main.py
```

配置见 `env.example`（`OPENROUTER_API_KEY`、`MODEL_NAME`、`REASONING_EFFORT` 等）。

## 技术要点

- **API**：OpenRouter `POST /chat/completions`
- **联网**：OpenRouter `plugins: [{ "id": "web" }]`（非 Kimi 的 `$web_search`）
- **推理**：`reasoning.effort` 默认 **`low`**（可通过 `REASONING_EFFORT` 覆盖）
- **Token 上限**：`DEFAULT_MAX_TOKENS` 默认 `16000`（推理 + 联网任务较耗 token，4000 可能截断）
- **模型**：默认 `openai/gpt-5-2025-08-07`
- **代码执行**：OpenRouter **不提供** GPT-5 原生 `code_interpreter`；本工程**不**使用本地替代
- **Agent 循环**：多轮请求，每轮记录 REQUEST/RESPONSE；若响应含 `tool_calls` 则执行并写入 `messages`

更多背景见 `week1/search-codegen/NOTE.md`（OpenRouter 与 GPT-5 原生工具格式的差异）。

## Agent 轨迹与 messages

本工程在 `execute_task` 中维护 **`messages`**，每轮 API 调用打印完整 REQUEST/RESPONSE（对齐 `currency-conversion` 的调试风格）。

### 实测 REQUEST / RESPONSE 示例

以下为东盟首都距离题、**Iteration 1** 的真实结构（`system` 内容已截断；`reasoning_details` 中加密段省略）。

**REQUEST**（`POST /chat/completions`）：

```json
{
  "model": "openai/gpt-5-2025-08-07",
  "messages": [
    {
      "role": "system",
      "content": "You are an advanced AI assistant powered by GPT-5 with native tool capabilities.\n\nYou have access to two powerful native tools:\n\n1. **web_search**: ...\n2. **code_interpreter**: ...\n..."
    },
    {
      "role": "user",
      "content": "东盟 10 国首都之间，距离最近的两个首都是？给出你的详细分析推理过程。"
    }
  ],
  "stream": false,
  "reasoning": {
    "effort": "low",
    "generate_summary": false
  },
  "background": false,
  "temperature": 0.3,
  "max_tokens": 16000,
  "plugins": [
    {
      "id": "web",
      "max_results": 5
    }
  ]
}
```

**RESPONSE**（节选关键字段）：

```json
{
  "id": "gen-1783039746-ENVyt7mgQkgyg9VgEoLc",
  "object": "chat.completion",
  "model": "openai/gpt-5-2025-08-07",
  "provider": "OpenAI",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "native_finish_reason": "completed",
      "message": {
        "role": "assistant",
        "content": "结论\n- 最接近的一对东盟十国首都是：新加坡（新加坡）与吉隆坡（马来西亚），两城中心的直线距离约为316–317公里。([distancecalculator.net](https://www.distancecalculator.net/from-singapore-to-kuala-lumpur?utm_source=openai))\n\n为什么是这一对（方法与要点说明）\n- 我以东盟10国及其现行首都为对象：文莱（斯里巴加湾市）、柬埔寨（金边）...",
        "refusal": null,
        "reasoning": "**Analyzing ASEAN capitals**\n\nAs of 2024, ASEAN consists of 10 members... I'll go ahead and search for this information!",
        "reasoning_details": [
          {
            "type": "reasoning.summary",
            "summary": "**Analyzing ASEAN capitals**... I'll need to verify those distances!"
          },
          {
            "type": "reasoning.encrypted",
            "data": "gAAAAABqRwcR...(省略)"
          }
        ],
        "annotations": [
          {
            "type": "url_citation",
            "url_citation": {
              "url": "https://www.distancecalculator.net/from-singapore-to-kuala-lumpur?utm_source=openai",
              "title": "Distance from Singapore to Kuala Lumpur",
              "start_index": 59,
              "end_index": 170
            }
          },
          {
            "type": "url_citation",
            "url_citation": {
              "url": "https://www.flightsfrom.com/HAN-VTE?utm_source=openai",
              "title": "Direct (non-stop) flights from Hanoi to Vientiane - schedules - FlightsFrom.com",
              "start_index": 811,
              "end_index": 885
            }
          }
        ]
      }
    }
  ],
  "usage": {
    "prompt_tokens": 18073,
    "completion_tokens": 2641,
    "total_tokens": 20714,
    "cost": 0.07424925,
    "prompt_tokens_details": {
      "cached_tokens": 4224
    },
    "completion_tokens_details": {
      "reasoning_tokens": 1792
    },
    "server_tool_use_details": {
      "web_search_requests": 3
    }
  }
}
```

对照要点：

| 请求侧 | 响应侧 |
|--------|--------|
| `plugins.web` 启用联网 | **无** `message.tool_calls` |
| `reasoning.effort: low` | `finish_reason: "stop"`，一轮结束 |
| `messages` 仅 system + user | `content` 为最终答案；`annotations` 为引用来源 |
| 未传 `tools` 数组 | `server_tool_use_details.web_search_requests: 3` 表明内部已搜网 |

运行 `python main.py` 时，控制台会打印完整的 `ITERATION 1 - REQUEST` / `ITERATION 1 - RESPONSE`（与上表结构一致，字段更全）。

### 联网其实发生了——看哪里？

响应里**没有 `tool_calls`，不代表没有搜索**。应查看：

```json
"usage": {
  "server_tool_use_details": {
    "web_search_requests": 3
  }
}
```

表示 OpenRouter 在服务端执行了 **3 次** web 搜索。

还可对照响应中的其他字段：

| 字段 | 说明 |
|------|------|
| `message.annotations` | `url_citation` 引用（如 distancecalculator.net） |
| `message.reasoning` | GPT-5 推理文本（`reasoning.effort` 开启时出现） |
| `message.reasoning_details` | `reasoning.summary` / `reasoning.encrypted` 等 |
| `message.content` | 最终答案，常含 Markdown 引用链接 |
| `provider` | 本次命中的 Provider（如 `OpenAI`） |

### 为什么看不到「模型说要调用工具」？

这是 **两种工具机制** 的差异：

```text
currency-conversion / web-search-demo（显式 tool_calls）
  模型 → finish_reason: tool_calls
       → messages 追加 assistant + tool_calls
       → 本地执行 → role: tool
       → 再发下一轮请求

search-codegen-demo（OpenRouter plugins.web，本工程默认）
  请求带 plugins.web
       → OpenRouter 内部：搜网 + 推理 + 生成答案
       → 一次返回 content，finish_reason: stop
       → messages 只有 assistant，无 tool_calls
```

本工程当前 **未注册** `TOOLS_SCHEMA`，请求里只有 `plugins.web`，因此：

- 不会出现 `finish_reason: "tool_calls"`
- 不会出现 `role: tool` 消息
- Agent 循环在该类任务上通常 **只跑 1 轮**

### `reasoning`

响应中可能出现：

```json
"reasoning": "**Analyzing ASEAN capitals**...",
"reasoning_details": [
  { "type": "reasoning.summary", "summary": "..." },
  { "type": "reasoning.encrypted", "data": "..." }
]
```

这是 GPT-5 的**内部推理过程**（由 `reasoning.effort` 控制）。

### 与 `currency-conversion` 对比

| | `currency-conversion` | `search-codegen-demo`（典型一次运行） |
|--|----------------------|-------------------------------------|
| API 次数 | 通常 3+ 轮 | **1 轮** |
| `finish_reason` | 中间轮 `tool_calls`，末轮 `stop` | 直接 **`stop`** |
| 工具在 `messages` 里 | ✅ `tool_calls` + `tool` | ❌ 无 |
| 工具谁执行 | 本地 Python（`convert_currency` 等） | OpenRouter 内部 `web_search` |
| 搜索次数从哪看 | 不适用 | `usage.server_tool_use_details.web_search_requests` |
| 轨迹可读性 | `messages` 完整可审计 | `messages` 简短；细节在 `usage` / `annotations` / 完整 RESPONSE 日志 |

### 若想要「像 currency-conversion」的 messages 轨迹

需同时满足：

1. 请求中带 `tools: [{ "type": "function", ... }]`（自定义 function 工具）
2. 模型返回 `tool_calls`，本地执行后写入 `role: tool`
3. 再发起下一轮 Chat API

在当前 **仅 `plugins.web`** 的配置下，不会出现上述多轮 `tool_calls` 轨迹；若日后在 `TOOLS_SCHEMA` / `TOOL_HANDLERS` 中注册自定义工具，才可能看到多轮 `messages`，但联网部分仍可能在 OpenRouter 内部完成、不一定进入 `tool_calls`。


## OpenRouter：Model Routing vs Provider Routing

本工程通过 OpenRouter 调用模型（如 `openai/gpt-5-2025-08-07`）。OpenRouter 里最容易误解的一点是：**「模型」和「真正执行计算的节点」不是同一层概念**。

### 为什么一个模型下面有多个 Provider？

在 OpenRouter 页面中，同一个逻辑模型（例如 **OpenAI: GPT-5.5**）下列出多个 Provider（OpenAI、Azure、Azure EU 等）：

![OpenRouter 模型页：同一模型对应多个 Provider](images/openrouter.jpg)

含义是：

> **同一个模型名，可以由多个不同算力提供商托管运行**——它们是同一模型能力的不同托管节点（hosted instances），而不是三个不同的模型。

### 两层路由

OpenRouter 实际是两层路由：

```text
第 1 层：模型路由（Model Routing）
  你填写 model: "openai/gpt-5.5"
  → 表示「我要用 GPT-5.5 这一能力族」

第 2 层：提供商路由（Provider Routing）
  OpenRouter 再决定请求交给谁执行
  → OpenAI 官方节点 / Azure OpenAI / Azure EU 等
```

```text
同一个模型抽象（openai/gpt-5.5）
        ↓
多个运行节点（multi-host inference layer）
        ↓
OpenRouter 动态选择 Provider
```

### 默认会用哪个 Provider？

**不额外配置时**，OpenRouter 不会固定某一个 Provider，而是每次请求可能不同。流程大致为：

1. **过滤**：是否可用、是否超时、是否限流、是否支持当前参数
2. **排序**：按路由模式在成本、延迟、稳定性之间权衡（如 Balanced / Nitro / Exacto）

可理解为：**动态竞价 + 健康检查 + 负载均衡**——不保证永远走 OpenAI 官方，也不保证永远走 Azure。

若要**固定 Provider**，需在请求中显式指定，例如：

```json
{
  "model": "openai/gpt-5.5",
  "provider": {
    "order": ["openai"],
    "allow_fallbacks": false
  }
}
```

这样才会始终使用 `openai` 节点，且不允许 fallback 到其他 Provider。

### 为何同一 Model 挂多个 Provider？

| 原因 | 说明 |
|------|------|
| 成本 | OpenAI 原生与 Azure 托管价格可能不同 |
| 区域 | EU 节点满足数据合规，US 节点延迟可能更低 |
| 稳定性 | 某 Provider 故障时可切换 |
| 吞吐 | 不同节点延迟、TPS、可用率不同 |

### 与 OpenAI 官网 Model ID 的区别

OpenAI 开发者文档中的模型 ID（如 `gpt-5.5-2026-04-23`）是**官方模型版本快照**：

![OpenAI 官网：固定版本 Model ID](images/openai.jpg)

| 系统 | `model` 含义 | Provider 概念 |
|------|-------------|---------------|
| **OpenAI 官网** | 固定版本（如 `gpt-5.5-2026-04-23`） | 不存在，一个模型对应官方部署 |
| **OpenRouter** | 逻辑模型（如 `openai/gpt-5.5`） | 存在，多节点可选、可路由 |

**一句话**：OpenRouter 的「模型」是**抽象能力**；**Provider 才是真正执行推理的算力池**。本 demo 的 `MODEL_NAME` 走的是 OpenRouter 逻辑模型名；实际命中哪个 Provider 由 OpenRouter 路由决定，响应里的 `provider_name` 可用来核对（详见 `week1/search-codegen/NOTE.md` 中关于 Azure 与工具能力的讨论）。

## OpenRouter 请求体说明

`agent.py` 中 `execute_task` 会向 `POST /chat/completions` 发送如下结构的 `request_body`（首轮示例）：

```json
{
  "background": false,
  "max_tokens": 16000,
  "messages": [
    {
      "role": "system",
      "content": "You are an advanced AI assistant with web search and reasoning capabilities.\n..."
    },
    {
      "role": "user",
      "content": "东盟 10 国首都之间，距离最近的两个首都是？给出你的详细分析推理过程。"
    }
  ],
  "model": "openai/gpt-5-2025-08-07",
  "plugins": [
    { "id": "web", "max_results": 5 }
  ],
  "reasoning": {
    "effort": "low",
    "generate_summary": false
  },
  "stream": false,
  "temperature": 0.3
}
```

### 顶层字段

| 字段 | 本工程取值 | 含义 |
|------|-----------|------|
| `model` | `openai/gpt-5-2025-08-07` | OpenRouter **逻辑模型 ID**（见上文 Model / Provider 路由）；非 OpenAI 官网的固定快照 ID |
| `messages` | system + user | 对话历史，Chat API 的核心输入 |
| `plugins` | `[{ "id": "web", "max_results": 5 }]` | 启用 OpenRouter 联网搜索插件 |
| `reasoning` | `{ "effort": "low", "generate_summary": false }` | GPT-5 推理模型专用配置 |
| `stream` | `false` | 非流式，等待完整响应一次返回 |
| `temperature` | `0.3` | 采样温度，越低输出越稳定 |
| `max_tokens` | `16000` | 本次回复（推理 + 正文）的 token 上限 |
| `background` | `false` | 同步请求，非后台异步任务 |

### `messages`

| 消息 | `role` | 来源 | 作用 |
|------|--------|------|------|
| 系统提示 | `system` | `agent.py` → `_create_system_prompt()` | 定义 Agent 角色：何时搜索、展示推理、引用来源 |
| 用户问题 | `user` | `main.py` → `TASK` | 本次要回答的任务 |

多轮对话时还会追加 `assistant`、`user` 等；本 demo 首轮仅上述两条。

### `plugins`（联网搜索）

```json
"plugins": [{ "id": "web", "max_results": 5 }]
```

- OpenRouter 的**插件机制**，不是 Kimi 的 `builtin_function` + `$web_search`
- `id: "web"`：启用联网；模型需要查资料时由 OpenRouter 代为搜索
- `max_results`：每次搜索最多返回的结果条数（来自 `WEB_SEARCH_MAX_RESULTS`）
- 仅当 `use_tools=True` 时由 `_build_openrouter_request` 加入

### `reasoning`（推理配置）

| 子字段 | 含义 |
|--------|------|
| `effort` | 推理强度：`low` / `medium` / `high` |
| `generate_summary` | `false` 表示不单独生成推理摘要，只要最终 `content` |

### 其他字段

- **`stream: false`**：一次性返回完整 JSON；`true` 则为 SSE 流式输出
- **`temperature: 0.3`**：偏保守，适合地理、距离等事实类问题
- **`max_tokens: 16000`**：含推理 token 与最终正文；过小会导致截断
- **`background: false`**：HTTP 连接保持到请求完成

### 请求体如何组装

```text
_build_request_body()           →  model, messages, stream, reasoning, background, plugins
execute_task() 内追加           →  temperature, max_tokens（及 tools，若 TOOLS_SCHEMA 非空）
```

一次请求的语义串联：

```text
用 GPT-5（model）
读 system + user（messages）
开启联网（plugins.web）
以 low 强度先推理（reasoning.effort）
再以较低随机性写答案（temperature）
总输出不超过 16000 tokens（max_tokens）
非流式、同步返回（stream=false, background=false）
```

## 与 web-search-demo 的对比

| 项目 | 联网方式 | 推理配置 |
|------|----------|----------|
| `web-search-demo` | Kimi `builtin_function` + `$web_search` | 无 `reasoning` 字段 |
| `search-codegen-demo` | OpenRouter `plugins: [{ "id": "web" }]` | `reasoning.effort`（默认 `low`） |
