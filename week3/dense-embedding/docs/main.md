### main.py源码解读
1. 文本 → 向量  
```python
# main.py Line192
embedding_result = embedding_service.encode_text(request.text)
embedding = embedding_result['dense']
```
2. 用户查询 → 向量
```python
# main.py Line251
embedding_result = embedding_service.encode_text(request.query)
query_embedding = embedding_result['dense']
```
3. 相关度搜索，得到结果。这里就会用到检索算法：ANNOY/HNSW 
```python
# main.py Line260
doc_ids, distances = vector_index.search(query_embedding, request.top_k)
```
4. 对结果进行排序

### 跑程序
1. 启动服务器：`python main.py`，localhost:4240 起来了
```txt
================================================================================
2026-05-09 15:56:47 - vector_search - [INFO] - main.py:98 - lifespan() - 🚀 Starting Vector Similarity Search Service
================================================================================
2026-05-09 15:56:47 - vector_search - [INFO] - main.py:102 - lifespan() - Initializing BGE-M3 embedding service...
2026-05-09 15:56:47 - vector_search - [INFO] - embedding_service.py:39 - _initialize_model() - 🚀 Initializing BGE-M3 model: BAAI/bge-m3
2026-05-09 16:35:56 - vector_search - [INFO] - embedding_service.py:59 - _initialize_model() - ✅ Model loaded successfully in 2348.39 seconds
2026-05-09 16:35:56 - vector_search - [INFO] - main.py:112 - lifespan() - Initializing HNSW vector index...
2026-05-09 16:35:56 - vector_search - [INFO] - indexing.py:267 - __init__() - 📚 Initialized HNSW index
2026-05-09 16:35:56 - vector_search - [INFO] - main.py:133 - lifespan() - Initializing document store...
2026-05-09 16:35:56 - vector_search - [INFO] - document_store.py:34 - __init__() - 📦 Initialized in-memory document store
================================================================================
2026-05-09 16:35:56 - vector_search - [INFO] - main.py:137 - lifespan() - ✅ Service initialized successfully!
2026-05-09 16:35:56 - vector_search - [INFO] - main.py:138 - lifespan() - 📍 API available at http://0.0.0.0:4240
2026-05-09 16:35:56 - vector_search - [INFO] - main.py:139 - lifespan() - 📚 Docs available at http://0.0.0.0:4240/docs
```   
下载的embedding model，BGM-M3，其保存路径为：C:\Users\admin\.cache\huggingface\hub\models--BAAI--bge-m3       
2. 把qucik_demo启起来：`python quick_demo.py` 
```txt
============================================================
  Vector Similarity Search - Quick Demo
============================================================

This educational service demonstrates vector similarity search
using BGE-M3 embeddings with ANNOY/HNSW indexing.

EDUCATIONAL CONCEPTS DEMONSTRATED:
1. Text → Vector embedding generation
2. Approximate nearest neighbor search
3. Cosine similarity for semantic matching
4. Trade-offs between index types (ANNOY vs HNSW)


📚 STEP 1: Start the service
----------------------------------------

Option A - Using HNSW (high precision):
  python main.py --index-type hnsw --debug

Option B - Using ANNOY (fast, memory-efficient):
  python main.py --index-type annoy --debug

Option C - Using the startup script:
  ./start_service.sh hnsw 4240 true

📝 STEP 2: Index some documents
----------------------------------------

Example using curl:

curl -X POST http://localhost:4240/index \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Machine learning is a subset of AI that enables systems to learn from data.",
    "metadata": {"category": "AI", "level": "beginner"}
  }'


🔍 STEP 3: Search for similar documents
----------------------------------------

Example search:

curl -X POST http://localhost:4240/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is deep learning?",
    "top_k": 5
  }'


🎯 STEP 4: Run the test client
----------------------------------------

The test client will:
- Index 10 sample documents about AI, programming, and DevOps
- Perform 5 different similarity searches
- Demonstrate document deletion
- Show performance metrics

Run it with:
  python test_client.py

For performance testing (100 documents):
  python test_client.py --performance


📊 KEY LEARNING POINTS
----------------------------------------

1. EMBEDDINGS: BGE-M3 converts text → 1024-dimensional vectors
   - Semantic meaning is captured in vector space
   - Similar texts have similar vectors

2. INDEXING: Two algorithms for efficient similarity search
   - ANNOY: Tree-based, fast but approximate
   - HNSW: Graph-based, slower but more accurate

3. SIMILARITY: Cosine distance measures semantic similarity
   - Score close to 1.0 = very similar
   - Score close to 0.0 = not similar

4. TRADE-OFFS:
   - Speed vs Accuracy (ANNOY vs HNSW)
   - Memory vs Performance (index parameters)
   - Build time vs Search time


🔗 USEFUL ENDPOINTS
----------------------------------------

- API Documentation: http://localhost:4240/docs
- Service Status: http://localhost:4240/
- Statistics: http://localhost:4240/stats
- List Documents: http://localhost:4240/documents


💡 EXPERIMENT IDEAS
----------------------------------------

1. Compare ANNOY vs HNSW accuracy on same queries
2. Measure indexing time for different document sizes
3. Test multilingual search (BGE-M3 supports 100+ languages)
4. Analyze how different parameters affect performance
5. Try searching with synonyms and paraphrases


============================================================
  Ready to Start!
============================================================

Next steps:
1. Start the service: python main.py --debug
2. Run the demo: python test_client.py
3. Explore the API: http://localhost:4240/docs
```

3. 发送以下请求：
    - 放入一篇文档
    - 查相似文档
```bash
curl -X POST http://localhost:4240/index -H "Content-Type: application/json" -d "{\"text\": \"Machine learning is a subset of AI that enables systems to learn from data.\",\"metadata\": {\"category\": \"AI\", \"level\": \"beginner\"}}"
```      

```bash
curl -X POST http://localhost:4240/search -H "Content-Type: application/json" -d "{\"query\": \"What is deep learning?\",\"top_k\": 5}"
```

```bash
curl -X POST http://localhost:4240/index -H "Content-Type: application/json" -d "{\"text\": \"Machine learning is a subset of AI that enables systems to learn from data.\",\"metadata\": {\"category\": \"AI\", \"level\": \"beginner\"}}"
{"success":true,"doc_id":"f82773e7-7956-4f82-8b02-b255699925cc","message":"Document indexed successfully using HNSW","index_size":1}


curl -X POST http://localhost:4240/search -H "Content-Type: application/json" -d "{\"query\": \"What is deep learning?\",\"top_k\": 5}"
{"success":true,"query":"What is deep learning?","results":[{"doc_id":"f82773e7-7956-4f82-8b02-b255699925cc","score":0.7126293739947784,"text":"Machine learning is a subset of AI that enables systems to learn from data.","metadata":{"category":"AI","level":"beginner"},"rank":1}],"total_results":1,"search_time_ms":189.00108337402344}
```





