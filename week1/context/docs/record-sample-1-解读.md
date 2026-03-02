# 理解 LLM Agent 的工作原理 —— Sample 1 三轮迭代解读

本文结合 **record-sample-1.md** 中记录的「Sample 1」完整请求/响应与 **agent.py** 中 `execute_task` 的代码逻辑，说明 LLM Agent 如何通过**多轮迭代**完成任务，重点说明：**上下文累积**、**工具调用与结果回填**、以及**何时不再调用工具并输出最终结果**。

原始请求/响应的完整 JSON 见 [record-sample-1.md](./record-sample-1.md)，此处只做逻辑梳理与代码对照。

---

## 一、LLM Agent 工作原理概览

本项目中，Agent 完成一个任务（如 Sample 1 的货币换算）的流程可以概括为：

1. **初始化上下文**：`messages` = [系统提示, 用户任务]。
2. **循环**（每次循环 = 一轮「请求 → 响应」）：
   - **发请求**：把当前 `messages` 和工具描述（`tools`）发给 LLM。
   - **收响应**：LLM 返回一条 `message`（可能带 `content` 和/或 `tool_calls`）。
   - **分支**：
     - 若响应中包含 **`"FINAL ANSWER:"`**：从 `content` 中截取最终答案，把本条 assistant 消息追加到 `messages`，**结束循环**，不再调用工具。
     - 若响应中包含 **`tool_calls`**：把本条 assistant 消息追加到 `messages`；**逐个执行工具**，把每个工具的结果以 `role: "tool"` 的消息**回填**进 `messages`；然后**进入下一轮循环**，用变长后的 `messages` 再请求 LLM。
3. **输出**：循环结束后返回提取出的 `final_answer` 以及轨迹（迭代次数、工具调用记录等）。

因此，理解 Agent 的关键就是理解：**每一轮发出去的 `messages` 是怎么在上轮基础上「长出来的」**（上下文累积），以及**工具结果如何作为新消息回填**（工具调用与结果回填），直到**某一轮 LLM 不再返回 tool_calls 而是返回 FINAL ANSWER**（终止）。

下面用 Sample 1 的三轮迭代与 agent 代码逐轮对照说明。

---

## 二、任务与代码入口

- **任务**（Sample 1）：  
  `Convert $1000 USD to EUR, GBP, and JPY. Then calculate the average value across all three converted currencies.`
- **代码入口**：`agent.py` 中 `execute_task(task, max_iterations=10)`。  
  - 首先把用户任务加入对话：`messages = self.conversation_history`（初始已含 system；再 `append({"role": "user", "content": task})`）。  
  - 然后进入 `while iteration < max_iterations` 循环，每轮 `iteration += 1`，用当前 `messages` 调用 `client.chat.completions.create(...)`，再根据响应是「FINAL ANSWER」还是「tool_calls」决定是 break 还是执行工具并追加消息。

---

## 三、第 1 轮迭代：首次请求与三次货币换算

### 3.1 发送的上下文（request messages）

- **条数**：2 条  
- **内容**：  
  - `role: "system"`：系统提示（使用工具、步骤思考、最终必须以 `"FINAL ANSWER:"` 结尾等）。  
  - `role: "user"`：用户任务（1000 USD 换 EUR/GBP/JPY 并求平均）。

对应代码：第一轮循环时，`messages` 就是初始化后的 `[system, user]`，直接作为请求体中的 `messages` 发出（见 `execute_task` 中 `request_data["messages"] = messages` 与 `client.chat.completions.create(..., messages=messages, tools=..., tool_choice="auto")`）。

### 3.2 收到的响应（response）

- **finish_reason**：`"tool_calls"`  
- **message.content**：空或仅推理内容。  
- **message.tool_calls**：3 个，均为 `convert_currency`：  
  - 1000 USD → EUR  
  - 1000 USD → GBP  
  - 1000 USD → JPY  

即 LLM 决定「先做三次换算」，尚未给出最终答案。

### 3.3 代码在收到响应后做的事

1. **不包含 "FINAL ANSWER:"** → 不进入 `if message.content and "FINAL ANSWER:" in message.content` 分支。  
2. **存在 `message.tool_calls`** → 进入 `if hasattr(message, 'tool_calls') and message.tool_calls` 分支（agent.py 约 623–661 行）：  
   - 将当前 assistant 消息（含 3 个 tool_calls）经 `_prepare_assistant_message` 后 **append 到 `messages`**。  
   - 对每个 tool_call：  
     - `_execute_tool(function_name, function_args)` 执行工具（如 `convert_currency(1000, "USD", "EUR")`），得到 `result`。  
     - 将结果以 `{"role": "tool", "tool_call_id": ..., "content": json.dumps(result)}` **append 到 `messages`**。  

因此，第一轮结束后 **`messages` 从 2 条变为 2 + 1 + 3 = 6 条**：  
`[system, user, assistant(3个tool_calls), tool(EUR结果), tool(GBP结果), tool(JPY结果)]`。

这就是**上下文累积**和**工具调用与结果回填**在第一轮的具体表现：**同一轮内**，先追加「助手说要调 3 个工具」，再追加「3 个工具的执行结果」，这些都会成为下一轮请求的上下文。

---

## 四、第 2 轮迭代：用换算结果求平均

### 4.1 发送的上下文（request messages）

- **条数**：6 条（即第一轮结束时的 `messages`）。  
- **内容**：  
  - 第 1–2 条：system、user（与第一轮相同）。  
  - 第 3 条：assistant，带 3 个 `tool_calls`（同上轮响应）。  
  - 第 4–6 条：3 条 `role: "tool"`，内容分别为 EUR/GBP/JPY 的换算结果（如 `converted_amount: 920.0, 790.0, 149500.0` 等）。

对应代码：第二轮循环开始时，`messages` 已是上一轮追加后的 6 条，直接作为本轮的请求 `messages` 发出。LLM 看到「自己上一轮调了 3 次 convert_currency」和「三次的结果」，就能基于这些**回填的上下文**继续推理。

### 4.2 收到的响应（response）

- **finish_reason**：`"tool_calls"`  
- **message.tool_calls**：1 个，`calculate`，表达式为 `"(920 + 790 + 149500) / 3"`。  

即 LLM 根据三个换算结果，决定再调用一次计算器求平均，仍未输出 FINAL ANSWER。

### 4.3 代码在收到响应后做的事

- 再次进入「处理 tool_calls」分支：  
  - 将本条 assistant 消息（含 1 个 tool_call）append 到 `messages`。  
  - 执行 `calculate("(920 + 790 + 149500) / 3")`，得到 `result: 50403.333...`。  
  - 将该结果以一条 `role: "tool"` 消息 append 到 `messages`。  

第二轮结束后 **`messages` 从 6 条变为 6 + 1 + 1 = 8 条**：  
`[system, user, assistant(3 calls), tool, tool, tool, assistant(1 call), tool(calculate 结果)]`。

再次体现**上下文累积**与**工具结果回填**：第二轮发出的 6 条是上一轮累积的结果；第二轮又追加了 1 条 assistant + 1 条 tool，供第三轮使用。

---

## 五、第 3 轮迭代：不再调用工具，输出最终结果

### 5.1 发送的上下文（request messages)

- **条数**：8 条（即第二轮结束时的 `messages`）。  
- **内容**：在前 8 条中，LLM 已经拥有：用户任务、自己前两轮的 tool_calls 以及全部工具返回（3 次换算 + 1 次求平均）。

### 5.2 收到的响应（response）

- **finish_reason**：`"stop"`  
- **message.content**：包含 `"FINAL ANSWER: The average value across the three converted currencies is approximately 50403.33."`  
- **message.tool_calls**：`null`（不再请求调用工具）。

即 LLM 在已有完整工具结果的前提下，直接给出最终答案并遵守了「FINAL ANSWER:」格式，不再发起新的工具调用。

### 5.3 代码在收到响应后做的事

1. 进入 `if message.content and "FINAL ANSWER:" in message.content` 分支（agent.py 约 614–619 行）：  
   - 从 `message.content` 中截取 `"FINAL ANSWER:"` 之后的文本，赋给 `final_answer`。  
   - 将本条 assistant 消息经 `_prepare_assistant_message` 后 append 到 `messages`（保留对话完整性）。  
   - **break** 跳出循环，不再执行工具，也不再发起新一轮请求。  
2. 循环结束后，`execute_task` 返回 `final_answer`、`trajectory`（含工具调用记录）、`iterations`（3）等。

至此，**不再调用工具，并输出最终结果**，Agent 对 Sample 1 的一次完整执行结束。

---

## 六、小结：上下文累积、工具回填与终止

| 轮次 | 发送的 messages 条数 | 响应类型 | 代码关键动作 | 下一轮 messages 变化 |
|------|----------------------|----------|--------------|------------------------|
| 1 | 2（system + user） | tool_calls（3×convert_currency） | 追加 assistant；执行 3 次工具；追加 3 条 tool | 2 → 6 |
| 2 | 6 | tool_calls（1×calculate） | 追加 assistant；执行 1 次工具；追加 1 条 tool | 6 → 8 |
| 3 | 8 | content 含 FINAL ANSWER，tool_calls=null | 提取 final_answer；追加 assistant；break | 结束，不再发请求 |

- **上下文累积**：每一轮请求的 `messages` 都是「上一轮的 messages + 本轮新追加的 assistant（及可能的 tool 结果）」；随着轮次增加，LLM 看到的对话越来越长，包含全部历史工具调用与结果。  
- **工具调用与结果回填**：每当 LLM 返回 `tool_calls`，agent 就执行对应工具，并把每个结果以 `role: "tool"` 的消息按 `tool_call_id` 顺序追加到 `messages`，供下一轮 LLM 使用。  
- **直到不再调用工具、输出最终结果**：当某一轮 LLM 不再返回 `tool_calls`，而是在 `content` 中给出 `"FINAL ANSWER:"` 时，agent 解析出最终答案并结束循环，不再进行新的工具调用或请求。

结合 [record-sample-1.md](./record-sample-1.md) 中的完整请求/响应 JSON 与 [agent.py](./agent.py) 中 `execute_task` 的 `while` 循环、分支判断和 `messages.append(...)` 逻辑对照阅读，可以更直观地理解上述 LLM Agent 工作原理。
