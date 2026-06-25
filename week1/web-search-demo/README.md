# Web Search Demo

从 `week1/web-search-agent` 抽取的**独立精简工程**，固定问题、无命令行交互，直接运行联网搜索示例。

## 任务

回答：**2024年诺贝尔物理学奖获得者是谁？**

## 运行

```bash
cd week1/web-search-demo
pip install -r requirements.txt
cp env.example .env   # 填入 MOONSHOT_API_KEY
python main.py
```

配置见 `env.example`（`MOONSHOT_API_KEY`、`DEFAULT_MODEL` 等）。

## 与 web-search-agent 的区别

| 项目 | 说明 |
|------|------|
| `web-search-agent` | 完整版，支持交互式问答、示例脚本 |
| `web-search-demo` | 精简版，固定单题，`python main.py` 直接跑 |

## 技术要点

- 使用 Kimi 内置工具 `$web_search`（`type: builtin_function`）
- 默认模型 `kimi-k2.5`（`kimi-k2-0905-preview` 已下线）
- `temperature` 固定为 `1`（kimi-k2.5 要求）
- assistant 消息以普通 `dict` 回传，避免 OpenAI SDK 对 `builtin_function` 的 Pydantic 警告

官方文档：[Use Web Search](https://platform.moonshot.cn/docs/guide/use-web-search)

## 本工程使用的工具

本工程使用的是 **Moonshot 平台提供的内置联网搜索工具 `$web_search`**，配合默认模型 `kimi-k2.5` 使用。

在 `agent.py` 中的声明如下：

```python
{
    "type": "builtin_function",
    "function": {"name": "$web_search"},
}
```

`search_impl` 将模型返回的参数原样交回，**不在本地执行搜索**：

```python
def search_impl(arguments):
    return arguments  # Kimi 服务端执行实际搜索
```

更准确地说：`$web_search` 不是你在本地写的 Python 函数，而是 **Moonshot API 平台封装好的能力**——模型决定何时调用，真正的搜网、读页、整理由 **Kimi 服务端**完成。

## 「内置」是什么意思？

**「内置」= 内置在模型提供商的平台（Moonshot / Kimi API）里，不是内置在模型权重里。**

三层职责如下：

```text
你的 Python 代码
    ↓  HTTP 请求
Moonshot 平台（API 网关 + 工具执行环境）  ← 「内置工具」在这一层
    ↓
Kimi 模型（kimi-k2.5）                    ← 负责「要不要调工具、参数是什么」
```

| 层级 | 职责 |
|------|------|
| **模型** | 分析问题，决定是否调用 `$web_search`，生成 `tool_calls` 和参数 |
| **平台** | 收到 `role: tool` 消息后，在服务端执行搜索（调搜索引擎、读网页、整理结果） |
| **你的代码** | 声明工具、维护 `messages`、把参数原样回传；不自己搜网 |

Moonshot API 用 `type: "builtin_function"` 区分工具类型：名字里的 **builtin = built into the API platform**，不是 built into the neural network（神经网络权重）。

模型通过训练/对齐，学会在 `tools` 中出现 `$web_search` 时如何发起调用；但搜网、抓页、汇总等重活不在模型推理里完成，而是由平台在收到 tool 消息后代为执行。这也解释了为什么 `search_impl` 只需原样返回 `arguments`——你是在把「调用凭证」交回给平台，而不是自己在搜。

## 内置工具 vs 自定义工具

| | **内置工具（`builtin_function`）** | **自定义工具（`function`）** |
|--|-------------------------------------|------------------------------|
| **声明方式** | `type: "builtin_function"`，通常只需 `name`（如 `$web_search`） | `type: "function"`，需完整 JSON Schema（`name`、`description`、`parameters`） |
| **谁执行** | **Moonshot 服务端** | **你的代码**（本地或自建后端） |
| **你要写什么** | 几乎不用实现搜索逻辑；把模型返回的 `arguments` 原样作为 `role: tool` 消息回传 | 自己写函数，解析参数、调 API/查库/算数，把**真实结果**回传给模型 |
| **本仓库示例** | 本工程、`web-search-chat` | `week1/currency-conversion`（`convert_currency`、`calculate`） |

### 调用流程对比

**内置 `$web_search`（本工程）：**

```text
用户提问
  → 模型决定调用 $web_search，返回 tool_calls
  → 你把 arguments 原样塞回 messages（role: tool）
  → Kimi 服务端自己去搜网、读网页、整理结果
  → 模型基于搜索结果生成最终答案
```

**自定义工具（以 `currency-conversion` 为例）：**

```text
用户提问
  → 模型决定调用 convert_currency，返回参数 {amount, from_currency, ...}
  → 你的 Python 代码执行 convert_currency(...)
  → 你把换算结果 JSON 回传给模型
  → 模型继续推理或给出最终答案
```

若要做「自己接搜索引擎 API、自己爬网页」的联网搜索，需走**自定义 `function` 工具**路线（类似早期手搓 `search` + `crawl` 的方式），而不是 `$web_search` 内置工具。

