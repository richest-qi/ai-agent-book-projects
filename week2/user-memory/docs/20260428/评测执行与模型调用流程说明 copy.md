# User Memory 评测执行与模型调用流程说明

本文档用于统一说明 Evaluation Mode 的核心逻辑，重点回答以下问题：

- 为什么会同时看到 `agent.*` 与 `processor.*` 两套对象
- 选择测试用例后，模型调用从哪里开始，调用几次
- 为什么会有两次“清空历史”
- `memory_mode` 如何影响记忆提取方式与落盘结构
- 为什么会出现“conversations 有数据但 memories 为空/偏少”

## 1. 总览：这是一个“双阶段”评测流程

Evaluation Mode 的设计目标是：  
**先抽取记忆，再基于记忆回答问题**。

完整路径如下：

1. 加载并回放测试对话（历史对话上下文）
2. 由 `processor` 触发记忆提取（第一次模型调用）
3. 清理原始对话痕迹，重新加载记忆
4. 由 `agent` 基于结构化记忆回答问题（第二次模型调用）
5. 将回答交给评测器打分

因此，这不是一次模型调用完成全部任务，而是“抽取”和“问答”解耦的两次调用。

## 2. 组件分工与对象关系

在 `run_evaluation_mode(...)` 中，会初始化两类核心组件：

- `agent = ConversationalAgent(...)`
- `processor = BackgroundMemoryProcessor(...)`

它们分别负责不同职责：

- `processor`：从 USER/ASSISTANT 对话中提取记忆，并写入 memory 文件
- `agent`：读取 memory 文件中的结构化记忆，生成最终回答

### 2.1 调试视角的结构树

- `agent = ConversationalAgent(...)`
  - `memory_manager`
  - `conversation_history`
  - `conversation`
    - `{role: "system", content: system prompt}`
      - system prompt 形如：`"You are a helpful and personalized assistant..."`

- `processor = BackgroundMemoryProcessor(...)`
  - `memory_manager`
  - `conversation_history`
  - `analysis_agent = UserMemoryAgent(...)`
    - `memory_manager`
    - `conversation_history`（在该场景下默认关闭）
    - `tool_calls`
    - `conversation`
      - `{role: "system", content: system prompt}`
        - system prompt = `base prompt + memory_instructions`
          - `base prompt`: `"You are an intelligent assistant with persistent memory across conversations..."`
          - `memory_instructions` 会随 `MemoryMode` 变化

## 3. 测试用例执行主流程（顺序版）

当选择某个 test case（如 `layer1_01_bank_account`）后，主流程可按时间顺序理解为：

1. 清空两侧状态（memory 与 conversation）  
   目的是保证当前测试不受上一轮污染。

2. 将 test case 的 `conversation_histories` 组装为 `conversation_contexts`  
   作为待提取记忆的输入材料。

3. 调用 `processor.process_conversation_batch(conversation_contexts)`  
   进入“记忆提取阶段”。

4. 再次清空 `agent` 的原始对话痕迹  
   模拟新会话，避免直接利用原始文本作答。

5. 调用 `agent.memory_manager.load_memory()`  
   从文件加载已提取的结构化记忆。

6. 调用 `agent.chat(test_case.user_question)`  
   进入“基于记忆回答阶段”。

7. 评测器对最终回答打分并记录结果。

## 4. 模型调用链：两次调用分别发生在哪里

### 4.1 记忆提取阶段（第一次主调用）

入口：

- `processor.process_conversation_batch(conversation_contexts)`

调用链：

- `process_conversation_batch(...)`
- `analyze_conversation(...)`
- `self.analysis_agent.execute_task(task)`
- `agent.py` 中 `execute_task(...)`
- `self.client.chat.completions.create(..., stream=True)`（真正请求模型）

该阶段输出的不是“最终用户答案”，而是工具调用：

- `add_memory`
- `update_memory`
- `delete_memory`

工具执行成功后，记忆会写入 memory 文件。

### 4.2 问答阶段（第二次主调用）

入口：

- `response = agent.chat(test_case.user_question)`

调用链：

- `chat(...)`
- `self.client.chat.completions.create(..., stream=True)`（再次请求模型）

该阶段模型基于“已抽取并重新加载的记忆”回答用户问题。

## 5. 为什么会出现两次“清空历史”

两次清空是刻意设计，不是冗余操作：

1. **测试前清空**：隔离不同 test case，防止互相污染。
2. **抽取后再次清空**：强制进入“新会话”语境，避免模型直接读取原始对话内容，确保回答确实依赖结构化记忆。

这正是评测公平性的关键机制之一。

## 6. memory_mode 如何决定提取与存储

同一个 `memory_mode` 同时影响两层逻辑，但影响方向不同：

- 对 `analysis_agent`：决定“提取提示词怎么写”（语义抽取策略）
- 对 `memory_manager`：决定“记忆按什么结构存储”（数据结构与更新规则）

### 6.1 提取策略：analysis_agent 的 system prompt 会变化

`analysis_agent`（`UserMemoryAgent`）的 system prompt 由：

- `base_prompt`
- `memory_instructions`

组成。`memory_instructions` 按模式变化：

- `NOTES`：偏简洁事实/偏好
- `ENHANCED_NOTES`：偏完整上下文段落
- `JSON_CARDS`：要求 `category -> subcategory -> key -> value`
- `ADVANCED_JSON_CARDS`：要求完整 card 对象（如 `backstory/person/relationship/...`）

因此，同一段对话在不同模式下会被抽取成不同形态。

### 6.2 存储策略：memory_manager 工厂映射

`create_memory_manager(...)` 的模式映射为：

- `NOTES` / `ENHANCED_NOTES` -> `NotesMemoryManager`
- `JSON_CARDS` -> `JSONMemoryManager`
- `ADVANCED_JSON_CARDS` -> `AdvancedJSONMemoryManager`

关键结论：

- `NOTES` 与 `ENHANCED_NOTES` 的底层存储是同一个 manager  
  （差异主要来自提示词和提取表达风格）
- 两种 JSON 模式对应不同的数据结构与更新规则

## 7. 常见异常：为什么 conversations 有数据，但 memories 为空

根因通常在于两条写入链路本身不同：

- `data/conversations/default_user_history.json`  
  在对话回放/记录阶段就会写入。

- `data/memories/default_user_memory.json`  
  依赖“记忆提取阶段”的模型调用和工具调用成功。

因此，只要提取阶段出现异常（流式中断、工具参数截断、JSON 不可解析、请求失败等），就会出现：

- conversations 看起来正常
- memories 为空或明显偏少

## 8. 三个最容易混淆的点（速查）

1. `processor` 本身不维护 agent 那种完整 `conversation` 消息栈；  
   该消息栈在 `analysis_agent` 内部维护。

2. 在 `BackgroundMemoryProcessor` 场景下，`analysis_agent` 初始化时会设置  
   `enable_conversation_history=False`，其 `conversation_history` 不参与常规历史持久化。

3. “提取策略”和“存储结构”是两层职责：  
   前者主要由 `analysis_agent` prompt 决定，后者由 `memory_manager` 实现决定。

## 9. 一句话结论

Evaluation Mode 的本质是：  
**先由 `processor` 调模型做记忆抽取，再由 `agent` 调模型基于结构化记忆回答问题；两次清空历史用于隔离测试并保证评测公平。**

