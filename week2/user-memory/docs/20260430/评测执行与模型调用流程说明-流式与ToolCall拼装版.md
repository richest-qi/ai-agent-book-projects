# User Memory 评测执行与模型调用流程说明（流式与 ToolCall 拼装版）

本文档在 `20260428` 版本基础上，补充本次排查的最新理解，重点回答：

- `stream=True` 后，大模型返回的数据长什么样
- 为什么会看到很多条 `🔧 Tool Call [i]: add_memory...`
- `current_tool_calls / collected_content / collected_reasoning` 最终如何进入 `conversation`
- `conversation` 的消息结构到底有哪些角色

## 1. Evaluation Mode 的双阶段主流程（复述）

在 `main.py` 的评测模式中，本质是两次模型主调用：

1. **记忆提取阶段**：`processor.process_conversation_batch(...)`
   - 内部走到 `analysis_agent.execute_task(...)`
   - 调用 `self.client.chat.completions.create(..., stream=True)`
   - 模型主要产出工具调用（如 `add_memory`），写入 memory

2. **问答阶段**：`agent.chat(test_case.user_question)`
   - 再次调用 `self.client.chat.completions.create(..., stream=True)`
   - 基于已保存并重载的结构化记忆回答问题

这也是为什么日志里会出现两次“看起来都在调模型”的原因。

## 2. 流式模式下返回的不是“完整消息”，而是“增量片段”

在 `agent.py` 中：

- 请求时设置 `stream=True`
- 收包时循环 `for chunk in stream`
- 每个 `chunk` 里取 `delta = chunk.choices[0].delta`

`delta` 可能包含三类增量字段：

- `reasoning`：推理片段（部分模型会给）
- `content`：普通文本片段
- `tool_calls`：工具调用片段（可能被拆成很多小段）

所以处理逻辑必须是“边接收边拼接”，而不是“一次拿到完整 JSON”。

## 3. 为什么会打印很多条 `add_memory`

当模型认为需要提取多条记忆时，它会在同一轮 assistant 响应中生成多个 tool call。

- 每个 tool call 用 `index` 标识（0, 1, 2...）
- 代码按 `index` 把对应片段拼进 `current_tool_calls[index]`
- `verbose=True` 时，会实时打印：
  - 首次识别到函数名：`🔧 Tool Call [i]: add_memory`
  - 参数分片到达时继续打印 `arguments` 片段（`end=""` 直接连在后面）

因此你在日志里会看到连续多条 `add_memory`，这通常表示：**模型在这一轮里主动规划了多次记忆写入**，不是代码重复调用同一条固定命令。

## 4. 单次 Tool Call 的拼装时间线（从空壳到完整）

以 `index=0` 为例，流式拼装可抽象为：

1. **初始化空壳**
   - 若 `current_tool_calls` 长度不够，先补：
   - `{"id":"","type":"function","function":{"name":"","arguments":""}}`

2. **收到函数名**
   - 设置 `current_tool_calls[0]["function"]["name"] = "add_memory"`

3. **收到参数分片（多次）**
   - 每到一片，执行：
   - `current_tool_calls[0]["function"]["arguments"] += <当前分片>`

4. **流结束后形成完整调用**
   - `name` 和 `arguments` 都就位
   - 后续 `json.loads(arguments)` 解析并执行工具

这也是 `arguments` 必须使用 `+=` 的原因：它常常是多片段拼出来的。

## 5. `collected_*` 与 `current_tool_calls` 如何进入 conversation

流结束后代码会组装 `complete_message`（assistant 消息）：

- 若有推理：写入 `complete_message["reasoning"]`
- 若有文本：写入 `complete_message["content"]`，否则 `content=None`
- 若有工具调用：写入 `complete_message["tool_calls"] = current_tool_calls`

只要三者之一存在，就会：

- `self.conversation.append(complete_message)`

随后若存在 `tool_calls`，逐条执行工具，并把工具结果追加为 `role="tool"` 消息（带 `tool_call_id`）。

## 6. `conversation` 的角色结构（精确版）

不是只有 `user/system/assistant` 三类。实际常见序列是：

1. `system`（初始化时写入）
2. `user`（当前任务与记忆上下文）
3. `assistant`（可能是 `content` 或 `reasoning` 或 `tool_calls`）
4. `tool`（每个工具调用对应一条工具结果）
5. 再次 `assistant`（读取工具结果后继续生成，直到最终答案）

因此评测/抽取过程中，`tool` 角色是关键一环。

## 7. 关于你给出的长 tool_calls 示例

你给出的结构方向是对的：`assistant + tool_calls[]`。  
但若某些 `arguments` 字符串出现引号不闭合、额外 `:0/:1` 等，`json.loads(...)` 会失败。

排查时应区分两种情况：

- 手工整理日志时引入了转义噪音（常见）
- 模型实际生成了坏 JSON（需要容错解析或重试策略）

## 8. 一句话总结

`stream=True` 下，模型返回的是 `delta` 增量流；代码通过 `collected_reasoning / collected_content / current_tool_calls` 三条通道完成拼接，再写入 `conversation` 并驱动工具执行。  
看到多条 `add_memory` 通常意味着模型在该轮已决定拆分多次记忆写入，这是预期行为。

## 9. 检查清单（Checklist）

使用下面清单快速判断自己是否已正确理解流式执行链路：

- [ ] 初始请求 `messages` 至少包含 `system` 与 `user`
- [ ] 开启 `stream=True` 后，模型返回的是增量 `chunk`，不是一次性完整消息
- [ ] 每个 `chunk` 的核心读取入口是 `delta = chunk.choices[0].delta`
- [ ] `collected_content` 用于拼接普通文本输出
- [ ] `collected_reasoning` 用于拼接推理片段（若模型提供）
- [ ] `current_tool_calls` 用于按 `index` 拼接工具调用（`id/name/arguments`）
- [ ] `arguments` 常常是分片到达，因此代码使用 `+=` 追加拼接
- [ ] `complete_message` 是 assistant 消息容器，可能含 `content`、`reasoning`、`tool_calls`
- [ ] `complete_message` 只要上述任一字段存在，就会被追加到 `conversation`
- [ ] 若存在 `tool_calls`，会先追加 assistant(tool_calls) 再执行工具
- [ ] 每个工具执行结果会以 `role="tool"` 消息追加到 `conversation`
- [ ] 有工具调用时会进入下一轮模型调用，直到没有新的 tool call 并得到最终答案
- [ ] 日志中出现多条 `🔧 Tool Call [i]: add_memory...` 通常表示模型同轮规划了多次记忆写入（预期行为）

