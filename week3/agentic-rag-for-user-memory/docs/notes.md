如果没有缓存，则会走`prepare_test_case`：分块→`add_chunks`→`save_index`;   
如果命中缓存，则不再走完整的「分块+首次建索引」，而是走「从磁盘恢复块→再向管道重建索引」。   

- 45 rounds：
    - chunk_index:0/1/2 
    - start_round/end_round
        - 1-20
        - 19-38
        - 37-45   

分块结果：   
    - 若干轮对话  
    - metadata  
    - context_before/context_after（可选）      

对话YAML   
    → 按轮次切换成多块  
    → 每块的「结构化抬头+可选前后文摘要+标签」→ 合成一条text   
    → POST /index     

用户提问    
    → POST /search （hybrid = 同一段text上 dense+parse 两路算分，再融合/重排）  
    → Agent 读返回块 → 组织自然语言答案    

**Hybrid检索里的「稠密+稀疏」**  
- `/search`在**hybrid**模式下会同时利用**向量相似度**（`4240`）、**BM25词面匹配**（`4241`），再在`4242`里融合、重排。


## main.py
```python
result = self.evaluator.evaluate_test_case(test_id)
```

## evaluator.py
```python
if self.config.evaluation.enable_caching:
    cache_path = self.results_dir / f"index_{test_id}"
    if Path(f"{cache_path}_chunks.json").exists():
        logger.info(f"Loading cached index for {test_id}")
        self.indexer = MemoryIndexer(self.config.index)
        self.indexer.load_index(str(cache_path))
        self.agent = UserMemoryRAGAgent(self.indexer, self.config)
        chunk_count = len(self.indexer.chunks)
    else:
        chunk_count, indexing_time = self.prepare_test_case(test_id)
else:
    chunk_count, indexing_time = self.prepare_test_case(test_id)
```

```python
all_chunks = []
for conv_history in test_case.conversation_histories:
    chunks = self.chunker.chunk_conversation(
        conversation_id=conv_history['conversation_id'],
        test_id=test_id,
        messages=conv_history['messages'],
        metadata=conv_history.get('metadata', {})
    )
    all_chunks.extend(chunks)
```

```python
self.indexer.add_chunks(all_chunks)
```

```python
self.indexer.save_index(str(cache_path))
```

```python
self.agent = UserMemoryRAGAgent(self.indexer, self.config)
```

```python
result = self.agent.answer_question(
    question=test_case.user_question,
    test_id=test_id,
    stream=False
)
```

## chunker.py
```python
conv_messages = []
for msg in messages:
    conv_messages.append(ConversationMessage(
        role=msg.get('role', 'user'),
        content=msg.get('content', ''),
        timestamp=msg.get('timestamp')
    ))

# Calculate rounds (1 round = 1 user message + 1 assistant response)
rounds = []
current_round = []

for msg in conv_messages:
    current_round.append(msg)
    if msg.role == "assistant" and len(current_round) >= 2:
        rounds.append(current_round)
        current_round = []

# Add remaining messages as incomplete round if any
if current_round:
    rounds.append(current_round)

total_rounds = len(rounds)
logger.info(f"Processing conversation {conversation_id} with {total_rounds} rounds")

# Choose chunking strategy
if self.config.strategy == ChunkingStrategy.FIXED_ROUNDS:
    chunks = self._chunk_fixed_rounds(
        conversation_id, test_id, rounds, metadata
    )

return chunks
```

```python
chunks = []
total_rounds = len(rounds)

# Calculate chunk boundaries with overlap
chunk_size = self.config.rounds_per_chunk
overlap = self.config.overlap_rounds
step = max(1, chunk_size - overlap)

chunk_index = 0
for start_idx in range(0, total_rounds, step):
    end_idx = min(start_idx + chunk_size, total_rounds)
    
    # Skip if chunk is too small (except for the last chunk)
    if end_idx - start_idx < self.config.min_chunk_size and end_idx < total_rounds:
        continue
    
    # Flatten rounds into messages
    chunk_messages = []
    for round_idx in range(start_idx, end_idx):
        chunk_messages.extend(rounds[round_idx])
    
    # Generate chunk ID
    chunk_content = f"{conversation_id}_{chunk_index}_{start_idx}_{end_idx}"
    chunk_id = hashlib.md5(chunk_content.encode()).hexdigest()[:12]
    
    # Create context summaries if enabled
    context_before = None
    context_after = None
    
    if self.config.include_metadata:
        # Add summary of previous context
        if start_idx > 0:
            prev_rounds = min(3, start_idx)
            context_msgs = []
            for i in range(max(0, start_idx - prev_rounds), start_idx):
                for msg in rounds[i]:
                    if msg.role == "user":
                        context_msgs.append(f"User asked: {msg.content[:100]}...")
            if context_msgs:
                context_before = "Previous discussion: " + " | ".join(context_msgs[-2:])
        
        # Add preview of next context
        if end_idx < total_rounds:
            next_rounds = min(2, total_rounds - end_idx)
            context_msgs = []
            for i in range(end_idx, min(end_idx + next_rounds, total_rounds)):
                for msg in rounds[i]:
                    if msg.role == "user":
                        context_msgs.append(f"Next: {msg.content[:100]}...")
            if context_msgs:
                context_after = " | ".join(context_msgs[:2])
    
    # Create chunk
    chunk = ConversationChunk(
        chunk_id=f"{test_id}_{conversation_id}_{chunk_id}",
        conversation_id=conversation_id,
        test_id=test_id,
        chunk_index=chunk_index,
        start_round=start_idx + 1,  # 1-indexed for display
        end_round=end_idx,  # Inclusive
        messages=chunk_messages,
        metadata=metadata or {},
        context_before=context_before,
        context_after=context_after
    )
    
    chunks.append(chunk)
    chunk_index += 1
    
    # Stop if we've reached the end
    if end_idx >= total_rounds:
        break

return chunks
```

## indexer.py
```python
documents = []

for chunk in chunks:
    chunk_id = chunk.chunk_id
    
    # Store chunk locally
    self.chunks[chunk_id] = chunk
    
    # Prepare text for indexing
    chunk_text = self._prepare_chunk_text(chunk)
    self.chunk_texts[chunk_id] = chunk_text
    
    # Prepare document for retrieval pipeline
    # 必须传顶层 doc_id：否则 pipeline 会自生成 id，search 结果可能无法与本地 chunk 对齐
    doc = {
        "text": chunk_text,
        "doc_id": chunk_id,
        "metadata": {
            "doc_id": chunk_id,
            "test_id": chunk.test_id,
            "conversation_id": chunk.conversation_id,
            "chunk_index": chunk.chunk_index,
            "start_round": chunk.start_round,
            "end_round": chunk.end_round,
            **chunk.metadata
        }
    }
    documents.append(doc)
    logger.debug(f"Added chunk {chunk_id} to index")

if rebuild and documents:
    self._index_documents(documents)
```

```python 
for doc in documents:
    try:
        response = requests.post(
            f"{self.retrieval_url}/index",
            json=doc  # Send individual document
        )
        
        if response.status_code == 200:
            result = response.json()
            generated_doc_id = result.get("doc_id")
            our_chunk_id = doc.get("metadata", {}).get("doc_id")
            
            # Store the mapping between generated doc_id and our chunk_id
            if generated_doc_id and our_chunk_id:
                self.doc_id_mapping[generated_doc_id] = our_chunk_id
                
            indexed_count += 1
```

```python
path = path or self.config.index_path

# Save chunks
chunks_data = {
    chunk_id: chunk.to_dict() 
    for chunk_id, chunk in self.chunks.items()
}

with open(f"{path}_chunks.json", 'w', encoding='utf-8') as f:
    json.dump(chunks_data, f, ensure_ascii=False, indent=2)

# Save chunk texts
with open(f"{path}_texts.json", 'w', encoding='utf-8') as f:
    json.dump(self.chunk_texts, f, ensure_ascii=False, indent=2)

logger.info(f"Chunks saved to {path}. Total chunks: {len(self.chunks)}")
```

## agent.py
```python
```