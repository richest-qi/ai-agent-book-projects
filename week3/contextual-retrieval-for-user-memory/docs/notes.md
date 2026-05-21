# Contextual Retrieval for User Memory — 主要逻辑与实现说明

本文结合 **`python main.py` 交互**、**`docs/main.md` 中的调试记录**（以 `layer1_01_bank_account` 为例），梳理本项目的双层记忆设计与源码对应关系。

---

## 1. 项目定位（与菜单文案一致）

- **上下文感知检索**：对话按轮次分块，对每块用 LLM 生成「块在整通对话中的定位说明」，与原文拼成 `contextualized_text`，写入本机检索管道（`POST …/index`），查询时可通过 `POST …/search` 召回。
- **结构化记忆卡片（Advanced Memory Cards）**：在处理完对话后，用 **另一路 LLM 调用** 从对话文本中抽取 JSON 事实，经 `AdvancedMemoryManager` **落盘**；答题 Agent 构建 system prompt 时通过 **`get_context_string`** 把卡片全文注入模型上下文。

入口与 Rich 菜单见 `main.py`（`InteractiveContextualRAG`）；评测单用例对应菜单 **「6. Evaluate Specific Test Case」**，与 `docs/main.md` 中操作一致。

---

## 2. 运行依赖（与 `main.md` 日志现象相关）

| 依赖 | 说明 |
|------|------|
| **检索管道** | `ContextualMemoryIndexer` 会检查 `http://localhost:4242/health`；索引 chunk 时对管道 `POST /index`（见 `contextual_indexer.py`）。 |
| **LLM API Key** | `contextual_chunking`（块上下文）、`_generate_summary_cards`（抽卡片）、`ContextualUserMemoryAgent`（答题）、评测均需 Kimi/Moonshot 等。密钥通过 **`config.py` 顶部 `load_dotenv(…/.env)`** 加载，见仓库内 `env.example`。 |
| **LLM Judge** | `main.md` 中 `Could not import LLM evaluation modules` 表示未接入 `week2/user-memory-evaluation` 的 `llm_evaluator`；会走 **Fallback LLM Evaluation**（仍在 `contextual_evaluator.py` 内用当前 LLM 打分）。 |

---

## 3. 单用例评测流水线（对应 `main.md` 第 181–339 行日志）

### 3.1 加载用例

`ContextualMemoryEvaluator` 从 `week2/user-memory-evaluation/test_cases` 读 YAML，构造带 `conversation_histories`、`user_question` 的 `TestCase`（`contextual_evaluator.py`）。

### 3.2 分块（基础块）

`ConversationChunker` 按配置（如每块 20 轮、重叠 2 轮）切分；日志：`Created 3 chunks for conversation bank_setup_001`。

### 3.3 上下文感知（每块一次 LLM）

`ContextualConversationChunker.contextualize_chunks`（`contextual_chunking.py`）对**每个基础块**调用 API，生成 `context`，并拼出：

`contextualized_text = context + 原始块文本（original_text / to_text 风格）`。

日志中「📝 CONTEXTUAL CHUNK … / Context Generated」即此步骤。

### 3.4 写入检索索引（与对话检索对应）

`ContextualMemoryIndexer.process_conversation_history` 中 **`_index_contextual_chunks`** 将每块的 **`contextualized_text`** 作为 `text` 发往管道 **`/index`**（每条带 `chunk_id` 等 metadata）。日志：`Indexed 3/3 contextual chunks`。

### 3.5 记忆卡片抽取（与「答题 Agent」不是同一次对话）

仍在 `process_conversation_history` 的 **Step 3**：若 `generate_summary_cards=True`，调用 **`_generate_summary_cards(chunks, conversation_id)`**。

**重要**：此处入参 **`chunks` 是基础 `ConversationChunk` 列表**，拼接全文用的是 **`chunk.to_text()`**，用于「结构化抽取」；**不是**上一步写入索引的 `contextualized_text`（避免把冗长英文 context 再喂给抽卡模型，语义上仍以对话正文为主）。

抽卡 LLM 在 `_generate_summary_cards` 内单独建 `OpenAI` 客户端（`Config.from_env()`），解析 JSON 后 `AdvancedMemoryCard` + **`memory_manager.add_card`**，落盘到 **`{chunk_store_path}/{user_id}_advanced_memory.json`**（默认配置下多为 `data/chunk_store.json/test_user_layer1_01_bank_account_advanced_memory.json` 这类路径）。日志：`Generated 1 summary cards`（张数**不保证**等于 chunk 数）。

### 3.6 构造答题 Agent

`ContextualUserMemoryAgent(indexer, …)`（`contextual_agent.py`），日志：`Memory cards loaded: 1`。

### 3.7 用户问题与轨迹统计

`answer_question` 用 **`_build_system_prompt()`** 生成 system 内容，其中 **`memory_context = memory_manager.get_context_string(max_cards=20)`**，即把所有（最多 20 张）卡片格式化成多行文本塞进 system（`advanced_memory_manager.py` 的 `get_context_string`）。

因此在本例中：**支票账号、路由号已在 system 的卡片段落里**，模型常 **不再调用** `search_conversation_history`，于是 `docs/main.md` 出现：

- **`Chunks Retrieved: 0`**：未走工具 → 未对管道做本次问答的 chunk 检索。
- **`Memory Cards Used: 1`**：来自 **`_find_relevant_memory_cards(question)`** 的简单词面匹配，用于 **trajectory 标注「可能与问题相关的卡片 id」**，不是「只有这张卡被读入模型」的含义；**实际所有卡片内容已在 system**。

工具 **`search_conversation_history`** 若被调用，内部 `indexer.search_with_context(..., include_memory_cards=False)`，避免检索结果里再重复合并卡片（卡片已在 system）。

---

## 4. 双层记忆在「问与答」中的分工（源码级）

| 层级 | 存储形态 | 写入时机 | 查询时如何进入模型 |
|------|-----------|-----------|---------------------|
| **Contextual chunks** | 检索管道中的向量/BM25 等（由 4242 协调） | `process_conversation_history` → `_index_contextual_chunks` | Agent 调用 **`search_conversation_history`** → `search_with_context` → **`/search`** |
| **Memory cards** | `{chunk_store_path}/*_advanced_memory.json`（见 `config.IndexConfig.chunk_store_path`） | `_generate_summary_cards` → `add_card` | **`get_context_string` 拼入 system prompt**（每问必带，上限 `max_cards`） |

**不是**严格的「先判断卡片有没有答案再决定是否注入 system」；当前实现是 **卡片常驻 system**，是否再检索由 **模型是否发起 tool call** 决定。

---

## 5. 常见误解：3 个 chunks ≠ 3 张记忆卡片

### 5.1 误解从哪来

看到日志里 **`Created 3 chunks`**、**`Indexed 3/3 contextual chunks`**，再打开  
`data/chunk_store.json/test_user_layer1_01_bank_account_advanced_memory.json`  
发现 **`categories` 里只有 1 张卡**（例如 `financial.fn_premium_checking_4429853327`），很容易推断：**「是不是每块对话应对应一张记忆卡片？」**

在本项目里，**这不是设计目标**。Chunk 与 Memory card 是**两条并行产物**，数量**没有 1:1 绑定**。

### 5.2 设计上各自解决什么问题

| | Contextual chunk（检索块） | Memory card（结构化卡片） |
|---|---------------------------|---------------------------|
| **粒度** | 按轮次切分（如每 20 轮一块，可重叠） | 按「事实主题」汇总（如一张「支票账户」卡） |
| **数量** | 长对话 → **多块**（本例 **3**） | 一次抽取 → **0～N 张**，由 LLM 决定 |
| **写入** | 每块一条 **`POST /index`** | 一次 **`add_card`** 可写多张，也可只写一张 |
| **用途** | hybrid **`/search`** 召回对话片段 | **`get_context_string`** 常驻 system，便于直接答结构化事实 |

本例是一通连续的「开户电话」，主题高度集中，LLM 常把账号、路由号、开户金额等**合并进 1 张 `financial` 卡**，而不是按 chunk 边界拆成 3 张。

### 5.3 源码：为什么只会「整通对话抽一次卡」

`contextual_indexer.py` 的 **`_generate_summary_cards`** 逻辑是：

1. 把**所有**基础块的正文拼成一段 **`full_text`**（`"\n".join([chunk.to_text() for chunk in chunks])`），**不是**对每个 chunk 循环抽卡。
2. **只调用一次** LLM，prompt 要求从**整段对话**里抽出 JSON 数组（或单个对象）。
3. 若返回的是单个 JSON 对象（无 `cards` / `memory_cards` 包装），解析为 **`extracted_cards = [extracted_data]`**，即 **1 张卡**。
4. 若 LLM 失败走 **`_fallback_extraction`**，代码里还有 **`break  # Only add one card per conversation`**，fallback 路径**最多 1 张**。

因此：**3 chunks → 3 次 contextualize + 3 次 index**；**3 chunks → 1 次 `_generate_summary_cards` → 往往 1 张（或少量）卡片**。这与 `docs/main.md` 中 `Generated 1 summary cards` 一致。

### 5.4 落盘文件里应看到什么

`test_user_layer1_01_bank_account_advanced_memory.json` 结构大致为：

- `user_id`、`type: advanced_json_cards`
- `categories.financial.{card_key}`：一张卡里包含 `account_number`、`routing_number`、`opening_deposit` 等**整通对话里抽出的字段**

**不会**出现「chunk_0 / chunk_1 / chunk_2 各一张卡」的固定布局，除非 LLM 在单次抽取中主动返回了多张（例如同时抽出支票账户卡 + 储蓄账户卡）。

### 5.5 若业务上需要「多块就多张卡」

当前仓库**未实现**「每个 chunk 自动生成一张 card」。若要接近「3 块 3 卡」，需要改实现，例如：

- 对每个 `ConversationChunk` 单独调用 `_generate_summary_cards([chunk], …)`，或  
- 在抽取 prompt 中明确要求「按段落/轮次范围分别建卡，且至少 N 张」。

否则请把预期调整为：**chunk 管检索切片，card 管结构化事实条数**。

---

## 6. 关键源码索引（便于跳转）

- **菜单 / Demo / 单测入口**：`main.py`（`InteractiveContextualRAG`）
- **评测编排**：`contextual_evaluator.py`（加载 YAML、调 indexer、调 agent、评测）
- **分块**：`chunker.py`（`ConversationChunk`、`to_text`）
- **块级上下文 LLM**：`contextual_chunking.py`（`ContextualConversationChunker`）
- **索引 + 抽卡**：`contextual_indexer.py`（`process_conversation_history`、`_index_contextual_chunks`、`_generate_summary_cards`）
- **卡片存取与 `memory_context`**：`advanced_memory_manager.py`（`AdvancedMemoryCard`、`get_context_string`）
- **答题 Agent**：`contextual_agent.py`（`_build_system_prompt`、`answer_question`、`_execute_tool`、`_find_relevant_memory_cards`）

---

## 7. 与 `docs/main.md` 的对应关系小结

| `main.md` 现象 | 实现含义 |
|----------------|----------|
| 三次 contextual chunk 日志 | 三块对话各自经 LLM 生成 `context` |
| `Indexed 3/3` | 三块 `contextualized_text` 已送检索管道 |
| `Generated 1 summary cards` | 整通对话**一次**抽卡，本例合并为 **1** 张（≠ 3 chunks，见 **§5**） |
| `categories` 里仅 1 张 `financial.*` | 落盘 JSON 反映的是「事实条数」，不是 chunk 个数 |
| `Memory cards loaded: 1` | `AdvancedMemoryManager` 已加载落盘 JSON |
| `Chunks Retrieved: 0` | 本轮未调用 `search_conversation_history` |
| `Memory Cards Used: 1` | trajectory 上关键词命中的卡片 id 列表长度（非「仅加载一张卡」） |

更完整的交互原文与 LLM 输出见 **`docs/main.md`**。

---

*若检索管道或 `.env` 变更，请以当前仓库代码与环境为准。*
