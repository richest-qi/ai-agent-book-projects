1. 把4240、4241这两个服务启起来
    - 4240服务启起来：dense-embedding下执行`python main.py`
    - 4241服务启起来：sparse-embedding下执行`python server,py`
2. 把4242这个服务启起来：retrieval-pipeline
    - 下载依赖：`pip install -r requirements.txt`
    - 服务器跑起来：`python main.py`，会下载ge-reranker-v2重排序模型。
3. 跑demo：`python demo.py`



### 小结
- 稀疏检索，sparse embedding，BM25
- 稠密检索/嵌入，dense embeddnig，BGE-M3
- 混合，retrieval-pipeline，bge-reranker-v2-m3