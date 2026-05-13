## 前提：4240 4241 4242服务启起来
1. 把4240、4241这两个服务启起来
    - 4240服务启起来：dense-embedding下执行`python main.py`
    - 4241服务启起来：sparse-embedding下执行`python server.py`
2. 把4242这个服务启起来：retrieval-pipeline
    - 安装依赖：`pip install -r requirements.txt`
    - 服务器跑起来：`python main.py`
## agentic rag 跑起来
1. 安装依赖：`pip install -r requirements.txt`
2. 跑程序建索引：`python index_local_laws.py`
3. 跑程序知识检索：`python main.py`  
    - 输入问题1：`宪法第一条是什么`
    - 输入问题2：`宪法最后一条是什么`
    - 输入问题3：`关于国旗保护法有哪些`