# System Hint 机制总结（基于 `agent.py` 与 `notes.md`）

## 结论先行

这段实现的核心判断是正确的：  
`conversation_history` 负责维护长期对话轨迹；`messages_to_send` 是每轮发给模型的临时输入；`system_hint` 在请求前追加到末尾参与本轮推理，但不写回长期历史。

一句话概括：**System Hint 参与计算，不参与记忆。**

## 关键数据结构职责

- `conversation_history`
  - 长期历史（持久语义），包含 `system / user / assistant / tool` 等真实事件。
  - 后续轮次会继续基于它累积上下文。

- `messages_to_send`
  - 每轮请求前由 `conversation_history.copy()` 生成的临时列表。
  - 本轮会把 `system_hint` 追加到末尾后再发送给模型。
  - 不作为长期存储使用。

## 请求阶段的真实流程

在 `agent.py` 对应逻辑中，流程可以抽象为：

1. 从 `conversation_history` 复制得到 `messages_to_send`
2. 通过 `_get_system_hint()` 生成本轮状态提示
3. 若提示存在，作为最后一条 `user` 消息追加到 `messages_to_send`
4. 用 `messages_to_send` 调用模型
5. 将模型真实响应（assistant/tool）写回 `conversation_history`

这保证了动态提示只作用于“当轮决策”，不污染“长期轨迹”。

## 与 `notes.md` 的契合点

和 `notes.md` 的主张是对齐的：

- “将隐式状态显式化”
- “将分散信息集中化”
- “追加在末尾供模型使用，但不进入持久轨迹”

因此，`notes.md` 中“便利贴”类比成立：当前轮看得到，历史轨迹不固化。

## 一个实现层面的细化说明

概念上，`notes.md` 提到的系统提示实践包括：

- `system_state`
- `todo_list`
- `tool_call_counts`
- `timestamp`
- `detail_error`

但在当前代码里，它们的注入位置并不完全相同：

- `_get_system_hint()` 直接拼接的是：
  - `SYSTEM STATE`
  - `CURRENT TASKS`（TODO 非空时）
- `timestamp`、`tool_call_counts` 目前主要作为工具结果消息的 metadata 前缀加入 `tool` 消息内容，而非 `_get_system_hint()` 主体。

所以更准确的表述是：  
**这些信息共同构成“系统状态增强”，但落点分布在 system hint 与 tool 消息元数据两条通道。**

## 设计价值

这种设计的收益可以总结为四点：

1. 不污染长期记忆：动态状态不会被误当成长期事实。
2. 保持轨迹可审计：历史只记录真实事件，回放更清晰。
3. 控制上下文膨胀：避免每轮把提示永久写入导致 token 不断增长。
4. 便于策略演进：可随时调整 hint 生成逻辑，而不依赖旧轨迹重写。

## 最终总结

你的理解是正确的，并且与文档精神一致。  
如果进一步追求“术语精确”，可以这样说：

- 当前实现中，`system_hint` 的核心载荷是 `system_state + todo_list`；
- 其余状态信息（如时间戳、工具调用计数）更多通过 `tool` 消息 metadata 注入；
- 二者共同实现了“给模型持续、低污染的状态反馈”。

