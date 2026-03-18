# 开启工具调用后 400 错误的本质分析（对齐版）

## 最终结论

- **不是** GPT-5 不支持内置工具。
- **而是** 当前这条调用链路**根本没有接到「支持这些工具的 GPT-5 运行环境」**。

---

## 一、你以为的调用路径 vs 实际发生的路径

### 你以为

```text
你 → OpenRouter → GPT-5（带 web_search / code_interpreter）
```

### 实际发生的是

```text
你 → OpenRouter → Azure（Chat Completions）→ GPT 模型（无工具执行环境）
```

关键点：

> **Azure 这一层，把「GPT-5 + tools」降级成了「普通 GPT + function calling 协议」。**

---

## 二、一句话的适用范围

「GPT-5 支持内置工具：web search 和 code interpreter」：

- 在 **OpenAI 官方环境** → 正确  
- 在 **OpenRouter → Azure 这条链路** → 不成立  

---

## 三、为什么会发生这种「能力丢失」？

### 原因 1：OpenRouter 只是「模型路由器」

它根据可用性 / 成本 / 延迟，把请求转发给某个 provider（如 OpenAI、Azure 等），**不保证带上传过去的「原生工具能力」**。

### 原因 2：不同 provider 能力不一样

本次命中的是 `provider_name: "Azure"`，Azure 的特点是：

| 能力 | 支持情况 |
|------|----------|
| GPT 推理 | ✅ |
| function calling | ✅ |
| web_search（原生） | ❌ |
| code_interpreter（原生） | ❌ |

### 结果

> **模型还在，但「工具执行系统」没了。**

---

## 四、为什么报的是「function 错误」而不是「tools 不支持」？

Azure 的理解是：**tools = function calling**，所以它在校验：

```json
{
  "type": "function",
  "function": { ... }
}
```

而你给的是：

```json
{
  "type": "web_search"
}
```

在 Azure 看来就是：「你连 function 都没写完整」，所以报 `expected "function"`。

---

## 五、真正的本质（终极答案）

问题不是：

- ❌ GPT-5 支不支持 tools  

而是：

- **你有没有接入「提供 tools 执行环境的 GPT-5 平台」。**

当前链路：接的是 **OpenRouter → Azure**，没有接入「带原生工具执行系统的 OpenAI 环境」。

---

## 六、工程视角抽象：GPT-5 tools = 两部分

```text
① 模型能力（会不会用工具）  ← GPT-5
② 执行环境（能不能执行）    ← 平台（OpenAI）
```

当前链路：

```text
GPT-5 ✔（部分能力）
执行环境 ❌（Azure 没有）
```

所以：**模型「理论上会用工具」，但「现实中没工具可用」。**

---

## 七、为什么「明明选了 GPT-5」还是不行？

关键点：

> **「模型名字 ≠ 能力全集」**

你写的是 `model = "openai/gpt-5"`，但实际执行的是：

```text
OpenRouter → Azure → GPT 模型（兼容模式）
```

相当于：点了「高配车」，但被分配到「只开引擎、不带导航的版本」。

---

## 八、分析中「差的那一步」

已经说对的是：Azure 只支持 function calling。

还差的一句：

> **因为这条链路根本没有「GPT-5 原生工具执行系统」。**

---

## 九、本意 vs 结果

- **本意**：用 GPT-5 → 用内置工具  
- **现实**：用 GPT-5（模型）✔，但没用 GPT-5（工具系统）❌  

---

## 最终一句话总结（建议记住）

- **GPT-5 的内置工具，只存在于「OpenAI 官方运行环境」中。**
- **一旦通过 OpenRouter / Azure 转发，这些工具能力就不会被带过去。**

---

## 十、为什么指定了 openai/gpt-5 还会被路由到 Azure？

代码里写的是 `model = "openai/gpt-5-2025-08-07"`，按理说是「要 OpenAI 的 GPT-5」，为什么 OpenRouter 会把请求发到 Azure？常见疑惑有三点，对应关系如下。

### 1. 为什么指定了 GPT-5，OpenRouter 还会路由到 Azure？

**OpenRouter 对同一个 model id 可以有多个 provider。**

- 你只指定了**模型名**（`openai/gpt-5-2025-08-07`），没有指定「必须用哪家厂商」。
- OpenRouter 会按自己的策略（可用性、成本、延迟、配额等）在「能提供这个模型的供应商」里选一个，把请求发过去。
- **Azure 完全可以是「提供 openai/gpt-5-2025-08-07 的其中一个供应商」**，所以路由到 Azure 并不矛盾。

也就是说：**「指定了 GPT-5」只决定了用哪个模型，没有决定「必须走 OpenAI 官网」**；路由到 Azure 是 OpenRouter 的调度结果。

### 2. Azure 支不支持这种模型？

**可以支持。**

- **Azure OpenAI** 会部署 OpenAI 的模型（包括 GPT-4 / GPT-5 等），所以从「模型能力」上，Azure 可以跑的就是你指定的那类 GPT-5 模型。
- 差别在于 **API 形态**：
  - **OpenAI 官方**：有 Responses API、原生 web_search / code_interpreter 等。
  - **Azure**：主要是 **Chat Completions + 标准 function calling**，不提供那套原生工具。

所以：**Azure 支持「这个模型」，但不支持「带原生工具执行环境的那套 API」**。你指定的是模型 id，OpenRouter 选到了「用 Azure 来提供这个模型」的一条路。

### 3. OpenRouter 为什么不把请求路由到 OpenAI？

可能原因包括（具体以 OpenRouter 的策略为准）：

- **负载 / 可用性**：当时 OpenAI 直连不可用或排队，Azure 有空闲。
- **成本 / 合约**：你的账号或套餐更便宜 / 更优先走 Azure。
- **多 provider 配置**：同一 model id 在 OpenRouter 后台被配置成「可由 OpenAI 或 Azure 提供」，调度时选到了 Azure。

所以：**不是「OpenRouter 搞错了」，而是「OpenRouter 认为当前请求可以由 Azure 来满足这个 model id」**。满足的是「用 GPT-5 模型」，没满足的是「用 OpenAI 官方的工具执行环境」。

### 小结

| 问题 | 结论 |
|------|------|
| 指定了 gpt-5，为什么还会到 Azure？ | 因为 OpenRouter 对同一 model 会多 provider 路由，你只选了模型，没选厂商；这次被调度到了 Azure。 |
| Azure 支持这个模型吗？ | 支持。Azure OpenAI 可以跑这类模型，但只暴露 Chat Completions + function calling，不暴露原生 web_search / code_interpreter。 |
| 为什么 OpenRouter 不路由到 OpenAI？ | 路由策略（可用性 / 成本 / 配置）让这次请求落在了 Azure；要「一定走 OpenAI 且带原生工具」，需要在 OpenRouter 里指定只走 OpenAI，或直接用 OpenAI 官方 API。 |

---

## 十一、如果 OpenRouter 路由到 OpenAI 的 GPT-5，是不是就不会遇到以上问题了？

**不一定「完全没问题」，但「这类 400（type 不是 function）就不会再出现」。**

### 1. 当前这个 400，换成「OpenRouter → OpenAI」后会怎样？

- 当前 400 的直接原因是：**Azure 端只认 `type: "function"` 的 tools**，你发了 `type: "web_search"` / `"code_interpreter"`，所以报错。
- 如果同一份请求变成：**你 → OpenRouter → OpenAI（官方 GPT-5 + Responses API）**：
  - OpenAI 官方**认识** `web_search`、`code_interpreter` 这些原生工具 type；
  - 就不会再给你「expected "function"」这类 400。

所以：**这个具体错误在「路由到 OpenAI 官方环境」时基本不会出现。**

### 2. 但会不会就「一切 OK、稳稳能用工具」？

还要满足几个前提：

- OpenRouter 确实把这个 model id 路由到了 **OpenAI 官方**，而不是别的 provider；
- 用的是 **OpenAI 的 Responses / tools 形态**，而不是再套一层「只支持 function calling」的兼容层；
- 你的账号在 OpenAI 那边有权限、配额使用 GPT-5 及其内置 tools。

一旦这些都满足：

- GPT-5 会按 `type: "web_search"` / `"code_interpreter"` 理解并调起工具；
- 不需要你写 `function: { name, parameters }`；
- 不会再被「只认 type: function」的后端拦下。

### 一句话总结

> **问题不是「GPT-5 会不会用工具」，而是「你到底打到了哪一家的 GPT-5 服务」。**
> - 打到 **Azure 这一层** → 工具能力被「降级成 function calling」，于是出现当前这个 400。
> - 真正打到 **OpenAI 官方 GPT-5 + tools 环境** → `web_search` / `code_interpreter` 这类原生 tools 就能正常走，不会报你现在看到的这个错。

---

## 十二、指定了 model 为什么还能被路由到 Azure？—— model 与 provider 是两回事

[OpenRouter Provider Routing](https://openrouter.ai/docs/guides/routing/provider-selection) 里写得很清楚：

- **model**（如 `openai/gpt-5-2025-08-07`）只表示「用哪个模型」；
- **provider**（如 `openai`、`azure`）表示「由哪家厂商来提供」；
- 二者独立：**指定 model 并不会指定 provider**。

OpenRouter 默认会对「能提供该 model 的多个 provider」做**负载均衡**（按价格、可用性等），所以同一 model 可能这次走 OpenAI、下次走 Azure。因此即便你在代码里写了 `model = "openai/gpt-5-2025-08-07"`，也只是指定了模型 id，**没有指定必须用 OpenAI 这家 provider**，请求被分到 Azure 是符合当前设计的。

若要用原生 tools（web_search / code_interpreter），需要请求实际落到 **OpenAI 官方环境**，则必须在请求里**显式指定 provider**，例如：

- `provider: { "order": ["openai"] }` — 优先使用 openai，仍可 fallback；
- 或 `provider: { "only": ["openai"] }` — 只允许 openai。

本仓库曾尝试在 `agent.py` 中增加 `provider: { "only": ["openai"] }` 或 `order: ["openai"]`，以强制只走 OpenAI。实测发现：**即使请求已落到 OpenAI（响应里 `provider_name: "OpenAI"`），仍返回同样的 400**（expected "function"）。说明 **OpenRouter 转发到 OpenAI 时使用的是只支持 `type: "function"` 的 Chat Completions 接口，而非支持 web_search/code_interpreter 的 Responses API**，故经 OpenRouter 无法使用 GPT-5 原生工具格式。当前实现已改为使用 OpenRouter 的 **plugins**（`plugins: [{ "id": "web" }]`）启用联网，所有 provider 均支持，可正常回答需联网的问题；code_interpreter 在 OpenRouter 上无等价能力，需自行用标准 function calling 实现。

---

## 十三、指定只走 OpenAI 后仍 400：结论与当前方案

### 现象

使用 `provider: { "only": ["openai"] }` 后，响应中 `metadata.provider_name` 已为 `"OpenAI"`，但依然返回 400，错误信息仍为：`expected "function"`、`0.function: expected object, received undefined` 等。

### 结论

- **不是** provider 选错（已确认为 OpenAI）。
- **而是**：OpenRouter 在转发到 OpenAI 时，走的是**只支持 `type: "function"` 的 Chat Completions 接口**，而不是支持 `web_search` / `code_interpreter` 的 **Responses API**。因此无论指定 Azure 还是 OpenAI，经 OpenRouter 的请求都无法使用 GPT-5 原生工具格式。

### 代码上的改动（当前实现）

| 原来 | 现在 |
|------|------|
| 请求里带 `tools: [ { type: "web_search", ... }, { type: "code_interpreter", ... } ]` | **不再**传上述 tools（会触发 400） |
| 依赖「原生工具」做联网 | 使用 OpenRouter 的 **plugins** 做联网：`plugins: [ { "id": "web", "max_results": 5 } ]` |

- 文档：[Web Search \| OpenRouter](https://openrouter.ai/docs/guides/features/plugins/web-search)
- 效果：在 OpenRouter 上可正常做联网搜索，所有 provider 均支持，不再出现 400。
- **code_interpreter**：OpenRouter 无等价能力；若需要，可自行用标准 function calling 实现一个「执行代码」的工具。
