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
