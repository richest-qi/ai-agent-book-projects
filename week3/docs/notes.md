RAG，Retrieve Augment Generate，检索增强生成   


稀疏检索 精确匹配

sparse-embedding   
pip install -r requirements.txt   
python serve.py  
python main.py  
bm25_engine.py  

找到所有单词，每个单词出现的频率。   
 
 
稠密检索、稠密嵌入  


dense-embedding   
python main.py   


不同的检索算法：   
- ANNOY
- HNSW   
区别在于计算向量相似度的不同  
判断向量相似度的一个算法  
在开发AI Agent时，通常不会去折腾算法，用现成的、开源的，算法、向量数据库。    
向量，词之间的关系。  
- investment bank
- river bank    

word2vec,google 
国王-男人+女人=王后   
程序员-男人+女人=家庭主妇     


文字 → 向量 （依靠嵌入模型，embedding model）
计算向量的相似度   
相似度检索   （向量数据库做这个事情）  

智谱的一款开源的、比较小的嵌入模型，embedding model：BGE-M3，不大，2G，运行也挺快  
嵌入模型把文本转为向量，文本→向量  

