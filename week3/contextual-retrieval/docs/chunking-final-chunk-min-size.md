# 分块收尾：`min_chunk_size` 与文档尾部丢失

## 背景

在调试 `ContextualChunker._chunk_by_paragraphs` 时，可能观察到：**文档末尾一小段正文没有进入 `chunks` 列表**，后续也就不会参与嵌入与检索。该行为与收尾处对 `min_chunk_size` 的判断有关。

## 相关代码

收尾逻辑位于 `contextual_chunking.py`：

```python
# Save final chunk
if current_chunk:
    chunk_text = '\n\n'.join(current_chunk)
    if len(chunk_text) >= self.chunking_config.min_chunk_size:
        chunks.append(self._create_basic_chunk(chunk_text, doc_id, len(chunks)))
```

同一文件中，按固定窗口切分的 `_chunk_by_size` 也对每个窗口使用了 `len(chunk_text) >= min_chunk_size` 的过滤（最后一段若过短同样可能不落库）。

配置默认值见 `config.py` 中的 `ChunkingConfig.min_chunk_size`（例如默认 `100`）；部分脚本（如 `index_local_laws_contextual.py`）可能传入更大的 `min_chunk_size`（例如 `500`），会放大「尾段过短」出现的概率。

## 原因说明

- 仅当 **`len(chunk_text) >= min_chunk_size`** 时，才把**最后一个** `current_chunk` 加入 `chunks`。
- 若文档在按段落累积结束后，**留在缓冲区里的最后一段**字符总数 **严格小于** `min_chunk_size`，则**不会 `append`**，相当于**静默丢弃**整段尾部文本。
- 典型触发场景：上一块已在接近 `chunk_size` 时刷新，**仅剩最后一条或数条很短的段落**（例如单行法条、标题加一句正文），合并后仍低于阈值。

注意：条件方向常被口语说反——**会丢内容的是「不满足最小长度」**，而不是「满足最小长度」。

## 对 RAG / 问答的影响

- 被丢弃的尾部**不会进入向量索引或 BM25 索引**（取决于下游是否只消费 `chunks`）。
- 用户问题若依赖**文档末尾的精确事实**（例如「宪法的最后一条是什么」「某法规最后一款如何表述」），检索可能**召不回**对应片段，模型只能依赖参数记忆或胡猜，**答案容易错误或不完整**。
- 若尾部实际很长、已超过 `min_chunk_size`，则按当前逻辑**不应**在此处被丢弃；若仍看不到末尾，需在**切块边界、重叠策略或其它管线步骤**上继续排查。

## 改进方向（建议）

1. **尾块特殊处理**：对**最后一个** chunk，不因 `min_chunk_size` 丢弃；或不足阈值时**合并入前一个 chunk**。
2. **可观测性**：在丢弃前打 **warning 日志**（含 `doc_id`、尾段长度、预览），避免静默丢文。
3. **配置语义**：区分「中间块最小长度」与「是否允许极短尾块」两类策略，避免用大 `min_chunk_size` 误伤法规、条号等短尾结构。

---

*本文档对应实现讨论时的代码版本以仓库内 `week3/contextual-retrieval/contextual_chunking.py` 为准。*
