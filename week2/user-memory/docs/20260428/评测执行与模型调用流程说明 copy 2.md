# User Memory 评测执行与模型调用流程说明

本文档补充说明 Evaluation Mode 中这几个常见疑问：

- 为什么会同时出现 `agent.memory_manager`、`agent.conversation_history`、`processor.memory_manager`、`processor.conversation_history`
- 选择 test case 后，清空 history 之后，究竟从哪里开始调用大模型
- 为什么会出现两次“清空历史”

## 1. 四个对象分别是什么

在 `week2/user-memory/main.py` 的 `run_evaluation_mode(...)` 中，会同时初始化两个核心组件：

- `agent = ConversationalAgent(...)`
- `processor = BackgroundMemoryProcessor(...)`

因此会看到两套状态对象：

- `agent.memory_manager`
- `agent.conversation_history`
- `processor.memory_manager`
- `processor.conversation_history`

它们不是重复，而是职责分离：

- `processor` 负责“从对话中抽取并写入结构化记忆”
- `agent` 负责“读取结构化记忆并回答最终问题”

## 2. 选择 test case 后的主流程

当你在菜单中输入 test id（例如 `layer1_01_bank_account`）后，核心流程如下：

1. 清空两侧 memory 和 conversation（确保本轮测试干净）
2. 把 test case 里的 `conversation_histories` 组装成 `conversation_contexts`
3. 调用 `processor.process_conversation_batch(conversation_contexts)` 做记忆提取
4. 再次清空 `agent` 的原始对话历史（模拟新会话）
5. `agent.memory_manager.load_memory()` 从文件重新加载处理后的记忆
6. 调用 `agent.chat(test_case.user_question)` 回答用户问题
7. 将回答交给评测框架打分

## 3. 清空 history 后，哪里开始调用大模型

### 3.1 记忆提取阶段（第一次模型主调用链）

入口在 `main.py`：

- `processor.process_conversation_batch(conversation_contexts)`

进入 `background_memory_processor.py` 后调用链：

- `process_conversation_batch(...)`
- `analyze_conversation(...)`
- `self.analysis_agent.execute_task(task)`
- `agent.py` 中 `execute_task(...)`
- `self.client.chat.completions.create(..., stream=True)`  ← 这里真正请求模型

这一阶段模型会产出工具调用（`add_memory/update_memory/delete_memory`），并把记忆写到 memory 文件中。

### 3.2 问答阶段（第二次模型主调用链）

入口在 `main.py`：

- `response = agent.chat(test_case.user_question)`

进入 `conversational_agent.py` 后调用链：

- `chat(...)`
- `self.client.chat.completions.create(..., stream=True)`  ← 再次请求模型

这一阶段模型基于“已保存并重新加载的结构化记忆”来回答测试问题。

## 4. 为什么会有两次“清空历史”

这是一种刻意的评测设计：

1. **测试前清空**：防止上一轮测试污染当前测试
2. **记忆抽取后再次清空**：模拟“新会话”场景，避免模型直接利用原始对话文本；要求它只能依赖结构化记忆进行回答

所以你会在日志中看到两类提示都出现，这属于预期行为。

## 5. conversations 文件有数据，但 memories 可能为空的原因

两者写入链路不同：

- `data/conversations/default_user_history.json`：在组装/回放对话时就会逐轮写入
- `data/memories/default_user_memory.json`：依赖“记忆提取阶段”的模型调用和工具调用成功执行

如果记忆提取阶段发生流式中断、工具参数截断、请求失败等异常，就可能出现“conversations 有数据，但 memories 为空或很少”的现象。

## 6. 一句话总结

Evaluation Mode 是“先让 `processor` 调模型提取记忆，再让 `agent` 调模型回答问题”的双阶段流程；  
两次清空历史是为了保证评测公平，确保最终回答依赖的是结构化记忆而不是原始对话缓存。

## 7. memory_mode 如何决定“怎么提取记忆”

在这套实现里，**记忆提取策略**和**记忆存储结构**是两层职责：

- `analysis_agent`（`UserMemoryAgent`）负责“怎么从对话里抽取”
- `memory_manager` 负责“抽取结果按什么结构落盘、更新、删除、读取”

换句话说：你看到的 `NOTES | ENHANCED_NOTES | JSON_CARDS | ADVANCED_JSON_CARDS`，本质上由同一个 `memory_mode` 同时驱动这两层，但两层关注点不同。

### 7.1 谁在决定提取方式

在 `main.py` 初始化 `BackgroundMemoryProcessor(...)` 时传入 `memory_mode` 后：

1. `BackgroundMemoryProcessor` 会用该 `memory_mode` 初始化 `analysis_agent`
2. 也会用同一个 `memory_mode` 初始化 `memory_manager`

因此，“提取成什么风格”与“最后存成什么格式”是联动的。

### 7.2 analysis_agent 的 system prompt 是否不同

**是的，不同，而且这是提取差异的核心来源。**

`agent.py` 中 `_init_system_prompt()` 会按 `memory_mode` 选择不同的 memory instructions：

- `NOTES`：强调记录简洁事实/偏好
- `ENHANCED_NOTES`：强调完整上下文段落（不是短 key-value）
- `JSON_CARDS`：强调 `category -> subcategory -> key -> value` 的分层结构
- `ADVANCED_JSON_CARDS`：强调完整 card 对象（如 `backstory/person/relationship/...`）

所以同一段 USER/ASSISTANT 对话，在不同模式下会被引导成不同形态的记忆。

### 7.3 memory_manager 在做什么

`memory_manager.py` 的工厂函数 `create_memory_manager(...)` 会根据 `memory_mode` 选实现：

- `NOTES` / `ENHANCED_NOTES` -> `NotesMemoryManager`
- `JSON_CARDS` -> `JSONMemoryManager`
- `ADVANCED_JSON_CARDS` -> `AdvancedJSONMemoryManager`

这说明：

- `NOTES` 与 `ENHANCED_NOTES` 的**存储层是同一个**（差异主要在 prompt 和抽取表达风格）
- 两种 JSON 模式分别对应不同的卡片结构与更新规则

### 7.4 一个实现注意点

当前工具描述里 `add_memory/update_memory` 的 `content` 参数偏向字符串描述；  
但 JSON 模式提示词要求结构化 JSON。运行时通常依赖模型输出可解析的 JSON（或 JSON 字符串）并在工具层解析。  
因此当流式输出中断、参数截断或 JSON 不完整时，更容易出现“对话有了，但 memories 落盘失败或偏少”的现象。

## 8. 调试视角下的对象结构图（含修正）

下面这份结构树可用于快速定位评测期的状态对象：

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
    - `conversation_history`（在当前 processor 场景下默认关闭）
    - `tool_calls`
    - `conversation`
      - `{role: "system", content: system prompt}`
        - system prompt = `base prompt + memory_instructions`
          - `base prompt`: `"You are an intelligent assistant with persistent memory across conversations..."`
          - `memory_instructions` 会随 `MemoryMode.NOTES / ENHANCED_NOTES / JSON_CARDS / ADVANCED_JSON_CARDS` 变化

### 8.1 三个容易混淆但很关键的点

1. `processor` 自身不维护类似 agent 的 `conversation=[{system...}, ...]` 消息列表；  
   这个对话消息栈是在 `analysis_agent` 内部维护的。

2. `analysis_agent` 在 `BackgroundMemoryProcessor` 初始化时显式设置了  
   `enable_conversation_history=False`，所以它的 `conversation_history` 不参与常规历史持久化。

3. `NOTES` 与 `ENHANCED_NOTES` 使用同一个 `NotesMemoryManager`；  
   两者差异主要来自 `analysis_agent` 的提示词约束（提取表达风格不同），而不是底层存储结构不同。

