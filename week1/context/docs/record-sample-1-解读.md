# 理解 LLM Agent 的工作原理 —— Sample 1 三轮迭代解读

本文结合 [record-sample-1.md](./record-sample-1.md) 中的完整请求/响应 JSON 与 [agent.py](../agent.py) 中 `execute_task` 的代码逻辑，说明 LLM Agent 如何通过**多轮迭代**完成任务，重点说明：**上下文累积**、**工具调用与结果回填**、以及**何时不再调用工具并输出最终结果**。

**理解自检（两轮概括）**

- **第一轮**：request 包含 `role: system`、`role: user`（系统提示词与用户提示词）和 `tools`（工具定义）；response 返回 `tool_calls`，表示大模型**要调用工具**。
- **第二轮**：request 包含 `role: system`、`role: user`、`role: assistant`（第一轮时大模型返回的整条响应）、以及多条 `role: tool`（**工具执行后的结果**）。

---

## 一、核心概念

### 1.1 Agent 工作原理概览

本项目中，Agent 完成一个任务（如 Sample 1 的货币换算）的流程：

1. **初始化上下文**：`messages` = [系统提示, 用户任务]。
2. **循环**（每轮 = 一次「请求 → 响应」）：
  - **发请求**：将当前 `messages` 与工具描述 `tools` 发给 LLM。
  - **收响应**：LLM 返回一条 `message`（可能含 `content` 和/或 `tool_calls`）。
  - **分支**：
    - 若响应含 **"FINAL ANSWER:"**：从 `content` 截取最终答案，将本条 assistant 消息追加到 `messages`，**结束循环**。
    - 若响应含 **tool_calls**：将本条 assistant 消息追加到 `messages`；**执行工具**，将每个结果以 `role: "tool"` 的消息**回填**进 `messages`；**进入下一轮**。
3. **输出**：返回 `final_answer`、轨迹（迭代次数、工具调用记录）等。

### 1.2 关键术语

- **finish_reason（响应的结束原因）**：模型每轮响应中都有一个 `**finish_reason`** 字段，表示本轮为何结束。取值通常有两种：
  - `**"tool_calls"**`：模型决定调用工具，返回了 `tool_calls`，本轮回合结束；agent 需要执行工具并将结果回填，再发起下一轮请求。
  - `**"stop"**`：模型生成了完整文本回复（如包含 "FINAL ANSWER:"），本轮回合结束；agent 解析最终答案并结束循环，不再调用工具。
  因此：**看 `finish_reason` 即可判断本轮是「还要调工具」还是「已经给出最终答案」**。
- **上下文累积**：每轮请求的 `messages` = 上一轮的 messages + 本轮新追加的 assistant（及 tool 结果）；对话历史逐轮变长。
- **工具调用与结果回填**：LLM 返回 `tool_calls` 后，agent 在本地执行工具，将每个结果以 `role: "tool"`、`tool_call_id` 对应地追加到 `messages`，供下一轮 LLM 使用。
- **终止条件**：当 LLM 不再返回 `tool_calls`，而在 `content` 中给出 "FINAL ANSWER:" 时（此时 `finish_reason` 为 `"stop"`），agent 解析答案并结束循环。

**谁调用并执行了工具？**  
**不是大模型，是 agent（我们的客户端代码）。** 大模型只负责「**决定**」调哪些工具、传什么参数——即在本轮响应的 `tool_calls` 里写出工具名和参数。真正在本地**调用并执行**工具的是 **agent**（如 agent.py 里的 `_execute_tool`）：收到响应后，根据 `tool_calls` 逐个执行 convert_currency、calculate 等，得到结果，再把结果以 `role: "tool"` 的消息追加到 `messages`，下一轮请求里才会出现这些「工具执行结果」。所以：第 1 轮大模型「说」要调 3 次工具；第 1 轮结束后、第 2 轮请求发出前，**是 agent 执行了这 3 次工具**并把结果写进 messages；第 2 轮请求里看到的 3 条 `role: "tool"` 就是这次执行的返回值。

---

## 二、本示例设定

- **任务（Sample 1）**：`Convert $1000 USD to EUR, GBP, and JPY. Then calculate the average value across all three converted currencies.`
- **代码入口**：`agent.py` 中 `execute_task(task, max_iterations=10)`。初始化 `messages`（含 system、user），进入 `while` 循环，每轮调用 `client.chat.completions.create(...)`，按响应为 FINAL ANSWER 或 tool_calls 决定 break 或执行工具并追加消息。
- **数据来源**：完整请求/响应 JSON 见 [record-sample-1.md](./record-sample-1.md)。

---

## 三、第一轮迭代

### 3.1 请求

- **messages**（2 条）：`role: system`（系统提示）、`role: user`（用户任务）。
- **tools**：工具定义（parse_pdf、convert_currency、calculate、code_interpreter 等），供 LLM 决定是否及如何调用。

### 3.2 响应

- **finish_reason**：`"tool_calls"` —— 本轮的结束原因是「模型请求调用工具」，而非生成完整回答（`"stop"`）。
- **message.content**：空 —— 模型本轮的「回复」全部在 `tool_calls` 里，未写进 `content`。
- **function_call**：null —— 旧版单次函数调用字段；当前使用 `tool_calls` 数组。
- **tool_calls**：3 个 `convert_currency`（1000 USD → EUR / GBP / JPY）。表示模型**请求**调用这些工具；**实际执行**由 agent 在本地完成，结果在**下一轮请求**中以 `role: "tool"` 回填。

**小结**：ITERATION 1 的响应 = 模型说「要调 3 次 convert_currency」；工具尚未在 API 端执行，agent 收到后才执行并将结果放进下一轮 messages。

### 3.3 代码动作与 messages 变化

- 将 assistant 消息（含 3 个 tool_calls）append 到 `messages`。
- 对每个 tool_call 执行 `_execute_tool`，将结果以 `{"role": "tool", "tool_call_id", "content": json.dumps(result)}` append 到 `messages`。
- **messages**：2 条 → 6 条。`[system, user, assistant(3个tool_calls), tool(EUR), tool(GBP), tool(JPY)]`。

---

## 四、第二轮迭代

### 4.1 请求

- **messages**（6 条）：仍含 system、user；新增 **assistant**（第一轮响应的 message，含 3 个 tool_calls）和 3 条 **role: "tool"**（第一轮 3 次 convert_currency 的**执行结果**）。即：上一轮模型输出 + 工具结果回填，共同成为本轮上下文。
- **role: "tool"** = 某次工具调用的**执行结果**，由 agent 执行后写入 messages，下一轮一并发给模型。

### 4.2 响应

- **finish_reason**：`"tool_calls"`。
- **message.tool_calls**：1 个 `calculate`，表达式 `"(920 + 790 + 149500) / 3"`。LLM 根据三个换算结果决定再调计算器求平均，仍未输出 FINAL ANSWER。

### 4.3 代码动作与 messages 变化

- 将本条 assistant 消息 append 到 `messages`；执行 `calculate(...)`；将结果以一条 `role: "tool"` append 到 `messages`。
- **messages**：6 条 → 8 条。`[..., assistant(3 calls), tool, tool, tool, assistant(1 call), tool(calculate 结果)]`。

---

## 五、第三轮迭代

### 5.1 请求

- **messages**（8 条）：含用户任务、前两轮 assistant 与全部 tool 结果（3 次换算 + 1 次求平均）。

### 5.2 响应

- **finish_reason**：`"stop"`。
- **message.content**：含 `"FINAL ANSWER: The average value across the three converted currencies is approximately 50403.33."`
- **message.tool_calls**：null。不再请求调用工具。

### 5.3 代码动作与终止

- 进入 FINAL ANSWER 分支：截取 `final_answer`，将本条 assistant 消息 append 到 `messages`，**break** 跳出循环。
- `execute_task` 返回 `final_answer`、`trajectory`、`iterations`（3）等。Agent 对 Sample 1 的执行结束。

---

## 六、总结

### 6.1 Sample 1 三轮上下文变化（线框示意）

```
ITERATION 1 请求的 messages           ITERATION 1 响应
┌────────────────────────┐           ┌────────────────────────┐
│ [0] system  系统提示词   │           │ assistant + tool_calls  │
│ [1] user    用户任务     │  ──请求──►│ (3× convert_currency)  │
└────────────────────────┘    ◄──响应─└────────────────────────┘
         │                                    │
         │                                    │ agent 执行 3 次工具，
         │                                    │ 得到 3 个 result
         │                                    ▼
         │                           ┌────────────────────────┐
         │                           │ 结果回填到 messages：    │
         │                           │ [2] assistant           │
         │                           │ [3] tool (EUR)          │
         │                           │ [4] tool (GBP)          │
         │                           │ [5] tool (JPY)          │
         │                           └────────────────────────┘
         │                                    │
         ▼                                    ▼
ITERATION 2 请求的 messages           ITERATION 2 响应
┌────────────────────────┐           ┌────────────────────────┐
│ [0] system             │           │ assistant + tool_calls  │
│ [1] user               │  ──请求──►│ (1× calculate)          │
│ [2] assistant (上轮)   │    ◄──响应─└────────────────────────┘
│ [3] tool (EUR 结果)     │                    │
│ [4] tool (GBP 结果)     │                    │ 执行 1 次工具，回填
│ [5] tool (JPY 结果)     │                    ▼
└────────────────────────┘           messages 变为 8 条
         │                                    │
         ▼                                    ▼
ITERATION 3 请求的 messages           ITERATION 3 响应
┌────────────────────────┐           ┌────────────────────────┐
│ [0] system             │           │ assistant               │
│ [1] user               │  ──请求──►│ content: "FINAL ANSWER: │
│ [2] assistant          │    ◄──响应─│  ... 50403.33"          │
│ [3] tool                │           │ tool_calls: null        │
│ [4] tool                │           └────────────────────────┘
│ [5] tool                │                    │
│ [6] assistant           │                    │ 不再调用工具，结束
│ [7] tool (calculate结果) │                    ▼
└────────────────────────┘           返回 final_answer
```

### 6.2 三轮对照表


| 轮次  | 发送的 messages 条数  | 响应 finish_reason | 响应类型                                   | 代码关键动作                             | 下一轮 messages 变化 |
| --- | ---------------- | ---------------- | -------------------------------------- | ---------------------------------- | --------------- |
| 1   | 2（system + user） | **tool_calls**   | tool_calls（3×convert_currency）         | 追加 assistant；执行 3 次工具；追加 3 条 tool  | 2 → 6           |
| 2   | 6                | **tool_calls**   | tool_calls（1×calculate）                | 追加 assistant；执行 1 次工具；追加 1 条 tool  | 6 → 8           |
| 3   | 8                | **stop**         | content 含 FINAL ANSWER，tool_calls=null | 提取 final_answer；追加 assistant；break | 结束              |


**说明**：模型的 `finish_reason` 只有两种可能 —— `**tool_calls`**（本轮要调工具，继续迭代）或 `**stop**`（本轮已给出完整回答，结束循环）。

### 6.3 要点回顾

- **上下文累积**：每轮请求的 `messages` 在上轮基础上增加本轮 assistant 与 tool 结果，对话历史逐轮变长。
- **工具调用与结果回填**：LLM 返回 `tool_calls` 后，agent 执行工具并将结果以 `role: "tool"` 追加到 `messages`，供下一轮使用。
- **终止**：当 LLM 在 `content` 中给出 "FINAL ANSWER:" 且无 tool_calls 时，agent 解析答案并结束循环。

### 6.4 延伸阅读

结合 [record-sample-1.md](./record-sample-1.md) 的完整 JSON 与 [agent.py](../agent.py) 中 `execute_task` 的 `while` 循环与分支逻辑对照阅读，可进一步理解 LLM Agent 的运作细节。