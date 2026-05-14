
## 分块
把长文档切成多段文本（法规按段落；对话按轮次），便于写入向量库和BM25。实现上先走`_create_basic_chunks`:  

```python
# week3\contextual-retrieval\contextual_chunking.py
# Step 1: Create basic chunks
basic_chunks = self._create_basic_chunks(text, doc_id)
logger.info(f"Created {len(basic_chunks)} basic chunks")
```  


## 上下文感知 
对每个basic chunk，用LLM读「整篇文档 + 当前这一块」，生成一句极短的、用来给检索用的「定位说明」(`context`)，再把它接到原文前面，得到真正送去索引的字符串`contextualized_text`。        
对每一块，用LLM在看过整篇原文的前提下，写一句很短的前缀，说明「这块在全文里是什么角色」，再拼到块前面去建索引。   
解决的问题只有一个：小块单独拿出来时语义不完整，检索容易飘。前缀把「它是谁、在讲什么」钉住。   

1. 把 整篇原文 和 当前这一块文字 一起放进prompt；  
2. 让模型只输出一两句极短的说明：这段在整篇里大概在讲什么、处于什么位置（方便以后检索能对上query）；  
3. 温度设得很低（你项目里是`0.3`），字数也限制得很紧（`max_tokens`约为100），所以更像「给检索用的定位标签」，而不是长篇摘要。  


生成逻辑核心两处：   
（1）Prompt：整篇文档 + 当前chunk    
```python
            prompt = f"""<document>
{full_document}
</document>

Here is the chunk we want to situate within the whole document

<chunk>
{chunk_text}
</chunk>

Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else. You MUST use the same language as the document."""
```   
也就是说：模型始终能看到全文，再判断「这一块再整体叙事里扮演什么角色」，用一两句话概括。    
（2）写入索引的文本 = 说明 + 原块   
```python
contextualized_text = f"{context}\n\n{chunk['text']}" if context else chunk['text']

contextual_chunk = ContextualChunk(
    chunk_id=chunk["chunk_id"],
    doc_id=doc_id,
    text=chunk["text"],
    context=context,
    contextualized_text=contextualized_text,
```  
- 稠密向量（4240）：对「前缀+正文」整段一起编码 → 向量里会带上「这是宪法序言」「这是讲第四条」这类语义；
- BM25（4241）：会对整段分词 → 查询里若出现「宪法」「第四条」等词，更容易和这块对上。    

如果没有前缀，索引里只有一块孤零零的正文（例如只有「任何组织或者个人......」），用户问「宪法第四条」时，块里可能没有「第四条」这几个字，稀疏检索就弱。前缀里往往会出现章节/主题词，等于给这块人工挂了一个检索用的「标题条」，但内容是模型生成的。     

### 没有前缀 vs 有了前缀
用户问：宪法第四条是什么？   

没有前缀时：索引里只有chunk原文。常见问题包括：
- 正文里没有用户问题里的词，块里只有法条正文、没有「第四条」字样，BM25很难给高分。
- 语义上「这一段其实是第四条」要靠模型自己悟，只靠这一小段向量有时和问句embedding不够近。  

有了前缀后：同一条索引文本变成「一句短说明+原文」。模型写前缀时读过全文，往往会带上章节/主题/在文档中的角色（「宪法开篇...」「序言中关于...」这种）。于是：   
- BM25：多了一堆和问题可能重叠的词，倒排索引更容易把这块捞进候选；
- 稠密向量：编码的是整段（前缀+正文），语义中心更接近「这段在讲什么」，和用户自然语言问句更容易近邻。   
- 重排：后续里本来就更常出现「对题」的块，交叉编码重排更稳。

## 结构化记忆卡片  
两条并行的记忆通道 
- 细节通道：**上下文感知**，这一层是**可检索的原始细节**
- 事实通道：**结构化记忆卡片**，这一层是**抽出来的结构化事实**     


JSON卡片：提高的是 事实是否容易被模型看到、是否稳定、是否可交叉引用，更像随身小抄。  


```python
# Step 1: Generate contextual chunks
...
# Step 2: Index contextual chunks
self._index_contextual_chunks(contextual_chunks)

# Step 3: Generate summary cards if requested
if generate_summary_cards:
    summary_cards = self._generate_summary_cards(chunks, conversation_id)
    for card in summary_cards:
        self.memory_manager.add_card(card)
```  

## 分块 上下文感知 结构化记忆卡片
contextual-retrieval
  文档：法规 .md
  ├─ 分块
  ├─ 每块：LLM 写一句「在全文中的位置/主题」→ 拼进索引文本
  └─ 检索：4242 → 回答问题（如「宪法第四条」）

contextual-retrieval-for-user-memory
  文档：对话历史
  ├─ 分块
  ├─ 每块：同样思路 → 上下文前缀 → 送进检索管道（细节通道）
  └─ 另：从对话抽 JSON 卡片 → 文件里长期保存（事实通道）    


  用生活类比：  
  - 分块：把一本书撕成纸条，每条只有几句话。  
  - 上下文感知：每条纸条上贴一行便利贴:「这是第三章讲合同违约的那一段」。  
  - 结构化记忆卡片：另外一个小本子，按表格记「客户A、航班B、截至日C」——不是纸条全文，而是填好的表。需要细节再去纸条堆里搜。  



