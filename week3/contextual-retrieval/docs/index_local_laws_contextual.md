## 4240 dense-embedding：python main.py
```
You may be able to resolve this warning by setting `model_config['protected_namespaces'] = ()`.
  warnings.warn(
INFO:     Started server process [21104]
INFO:     Waiting for application startup.
2026-05-13 08:52:17 - vector_search - [INFO] - main.py:97 - lifespan() - ================================================================================
2026-05-13 08:52:17 - vector_search - [INFO] - main.py:98 - lifespan() - 🚀 Starting Vector Similarity Search Service
2026-05-13 08:52:17 - vector_search - [INFO] - main.py:99 - lifespan() - ================================================================================
2026-05-13 08:52:17 - vector_search - [INFO] - main.py:102 - lifespan() - Initializing BGE-M3 embedding service...
2026-05-13 08:52:17 - vector_search - [INFO] - embedding_service.py:39 - _initialize_model() - 🚀 Initializing BGE-M3 model: BAAI/bge-m3
Fetching 30 files: 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:00<00:00, 45311.17it/s]
2026-05-13 08:52:24 - vector_search - [INFO] - embedding_service.py:59 - _initialize_model() - ✅ Model loaded successfully in 7.41 seconds
2026-05-13 08:52:24 - vector_search - [INFO] - main.py:112 - lifespan() - Initializing HNSW vector index...
2026-05-13 08:52:24 - vector_search - [INFO] - indexing.py:267 - __init__() - 📚 Initialized HNSW index
2026-05-13 08:52:24 - vector_search - [INFO] - main.py:133 - lifespan() - Initializing document store...
2026-05-13 08:52:24 - vector_search - [INFO] - document_store.py:34 - __init__() - 📦 Initialized in-memory document store
2026-05-13 08:52:24 - vector_search - [INFO] - main.py:136 - lifespan() - ================================================================================
2026-05-13 08:52:24 - vector_search - [INFO] - main.py:137 - lifespan() - ✅ Service initialized successfully!
2026-05-13 08:52:24 - vector_search - [INFO] - main.py:138 - lifespan() - 📍 API available at http://0.0.0.0:4240
2026-05-13 08:52:24 - vector_search - [INFO] - main.py:139 - lifespan() - 📚 Docs available at http://0.0.0.0:4240/docs
2026-05-13 08:52:24 - vector_search - [INFO] - main.py:140 - lifespan() - ================================================================================
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:4240 (Press CTRL+C to quit)
2026-05-13 08:54:32 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:54:36 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 4.4543 seconds
2026-05-13 08:54:36 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:63034 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:54:45 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:54:50 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 4.5280 seconds
2026-05-13 08:54:50 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:63075 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:01 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:55:06 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.1210 seconds
2026-05-13 08:55:06 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:60975 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:15 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:55:20 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.0400 seconds
2026-05-13 08:55:20 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:61035 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:30 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:55:35 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 4.7210 seconds
2026-05-13 08:55:35 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:61063 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:45 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:55:50 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 4.9140 seconds
2026-05-13 08:55:50 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:61091 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:01 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:56:07 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.3670 seconds
2026-05-13 08:56:07 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:49170 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:16 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:56:21 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.3990 seconds
2026-05-13 08:56:21 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:49202 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:32 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:56:37 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 4.4760 seconds
2026-05-13 08:56:37 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51206 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:46 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:56:51 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.4350 seconds
2026-05-13 08:56:51 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51220 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:59 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:57:04 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 4.9240 seconds
2026-05-13 08:57:04 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51234 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:13 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:57:18 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 4.4180 seconds
2026-05-13 08:57:18 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51256 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:27 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:57:32 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.7270 seconds
2026-05-13 08:57:32 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51276 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:43 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:57:49 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.6350 seconds
2026-05-13 08:57:49 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51307 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:57 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:58:03 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.1620 seconds
2026-05-13 08:58:03 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51320 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:14 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:58:20 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.7950 seconds
2026-05-13 08:58:20 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51333 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:28 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:58:33 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.3470 seconds
2026-05-13 08:58:33 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51368 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:42 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:58:47 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.0300 seconds
2026-05-13 08:58:47 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:51388 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:56 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:59:02 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 6.0290 seconds
2026-05-13 08:59:02 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:60424 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:59:15 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:59:20 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 5.1980 seconds
2026-05-13 08:59:20 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:63324 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:59:30 - vector_search - [INFO] - logger.py:103 - log_indexing_start() - 📝 Starting INDEXING operation
2026-05-13 08:59:35 - vector_search - [INFO] - logger.py:78 - wrapper() - ✅ encode_text completed successfully in 4.6610 seconds
2026-05-13 08:59:35 - vector_search - [INFO] - logger.py:123 - log_index_update() - 📊 Updating HNSW index
INFO:     127.0.0.1:63341 - "POST /index HTTP/1.1" 200 OK

```
## 4241 sparse-embedding：python server.py
```
2026-05-13 08:51:31,023 - bm25_engine - INFO - InvertedIndex initialized
2026-05-13 08:51:31,023 - bm25_engine - INFO - SparseSearchEngine initialized
2026-05-13 08:51:31,033 - __main__ - INFO - Starting Educational Sparse Vector Search Engine Server
2026-05-13 08:51:31,034 - __main__ - INFO - Server will run on http://localhost:4241
2026-05-13 08:51:31,034 - __main__ - INFO - Visit http://localhost:4241 for the web interface
2026-05-13 08:51:31,034 - __main__ - INFO - API documentation available at http://localhost:4241/docs
2026-05-13 08:51:31,039 - asyncio - DEBUG - Using proactor: IocpProactor
INFO:     Started server process [5520]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:4241 (Press CTRL+C to quit)
2026-05-13 08:54:32,518 - __main__ - INFO - Received index request for document of length 1015
2026-05-13 08:54:32,519 - __main__ - INFO - External doc_id provided: 宪法_chunk_0
2026-05-13 08:54:32,519 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_0' (internal ID 0)
2026-05-13 08:54:32,519 - bm25_engine - INFO - Adding document 0 to index
2026-05-13 08:54:32,519 - bm25_engine - DEBUG - Document text: 宪法开篇：通过及历次修正日期＋历史背景与政权合法性总述，为全文纲领。

# 中华人民共和国宪法

1982年12月4日 第五届全国人民代表大会第五次会议通过

1982年12月4日 全国人民代表大会公...
2026-05-13 08:54:32,519 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 979, 'context_char_count': 34, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '# 中华人民共和国宪法\n\n1982年12月4日 第五届全国人民代表大会第五次会议通过\n\n1982年12月4日 全国人民代表大会公告公布施行\n\n1988年4月12日 第七届全国人民代表大会第一次会议通过的《中华人民共和国宪法修正案》\n\n1993年3月29日 第八届全国人民代表大会第一次会议通过的《中华人民共和国宪法修正案》\n\n1999年3月15日 第九届全国人民代表大会第二次会议通过的《中华人民共和国宪法修正案》\n\n2004年3月14日 第十届全国人民代表大会第二次会议通过的《中华人民共和国宪法修正案》\n\n2018年3月11日 第十三届全国人民代表大会第一次会议通过的《中华人民共和国宪法修正案》\n\n<!-- INFO END -->\n\n## 序言\n\n中国是世界上历史最悠久的国家之一。中国各族人民共同创造了光辉灿烂的文化，具有光荣的革命传统。\n\n一八四○年以后，封建的中国逐渐变成半殖民地、半封建的国家。中国人民为国家独立、民族解放和民主自由进行了前仆后继的英勇奋斗。\n\n二十世纪，中国发生了翻天覆地的伟大历史变革。\n\n一九一一年孙中山先生领导的辛亥革命，废除了封建帝制，创立了中华民国。但是，中国人民反对帝国主义和封建主义的历史任务还没有完成。\n\n一九四九年，以毛泽东主席为领袖的中国共产党领导中国各族人民，在经历了长期的艰难曲折的武装斗争和其他形式的斗争以后，终于推翻了帝国主义、封建主义和官僚资本主义的统治，取得了新民主主义革命的伟大胜利，建立了中华人民共和国。从此，中国人民掌握了国家的权力，成为国家的主人。\n\n<!-- FORCE BREAK -->\n\n中华人民共和国成立以后，我国社会逐步实现了由新民主主义到社会主义的过渡。生产资料私有制的社会主义改造已经完成，人剥削人的制度已经消灭，社会主义制度已经确立。工人阶级领导的、以工农联盟为基础的人民民主专政，实质上即无产阶级专政，得到巩固和发展。中国人民和中国人民解放军战胜了帝国主义、霸权主义的侵略、破坏和武装挑衅，维护了国家的独立和安全，增强了国防。经济建设取得了重大的成就，独立的、比较完整的社会主义工业体系已经基本形成，农业生产显著提高。教育、科学、文化等事业有了很大的发展，社会主义思想教育取得了明显的成效。广大人民的生活有了较大的改善。\n\n<!-- FORCE BREAK -->', 'context': '宪法开篇：通过及历次修正日期＋历史背景与政权合法性总述，为全文纲领。', 'chunk_index': 0, 'char_count': 1015}
2026-05-13 08:54:32,519 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:54:32,520 - bm25_engine - DEBUG - Tokenizing text of length 1015
2026-05-13 08:54:32,523 - bm25_engine - DEBUG - Found 6 raw tokens
2026-05-13 08:54:32,523 - bm25_engine - DEBUG - After removing stop words: 6 tokens
2026-05-13 08:54:32,523 - bm25_engine - DEBUG - Document 0: 6 tokens, 4 unique terms
2026-05-13 08:54:32,524 - bm25_engine - DEBUG - Index statistics: 1 documents, 4 unique terms, 6 total terms
2026-05-13 08:54:32,524 - bm25_engine - INFO - Document 0 indexed successfully
2026-05-13 08:54:32,524 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=6.00
2026-05-13 08:54:32,524 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_0
INFO:     127.0.0.1:63035 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:54:45,596 - __main__ - INFO - Received index request for document of length 1044
2026-05-13 08:54:45,596 - __main__ - INFO - External doc_id provided: 宪法_chunk_1
2026-05-13 08:54:45,596 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_1' (internal ID 1)
2026-05-13 08:54:45,597 - bm25_engine - INFO - Adding document 1 to index
2026-05-13 08:54:45,597 - bm25_engine - DEBUG - Document text: 宪法序言中关于国家根本任务、指导思想、统一大业、爱国统一战线与民族关系的集中表述

<!-- FORCE BREAK -->

中国新民主主义革命的胜利和社会主义事业的成就，是中国共产党领导中国各族人...
2026-05-13 08:54:45,597 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1002, 'context_char_count': 40, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '<!-- FORCE BREAK -->\n\n中国新民主主义革命的胜利和社会主义事业的成就，是中国共产党领导中国各族人民，在马克思列宁主义、毛泽东思想的指引下，坚持真理，修正错误，战胜许多艰难险阻而取得的。我国将长期处于社会主义初级阶段。国家的根本任务是，沿着中国特色社会主义道路，集中力量进行社会主义现代化建设。中国各族人民将继续在中国共产党领导下，在马克思列宁主义、毛泽东思想、邓小平理论、“三个代表”重要思想、科学发展观、习近平新时代中国特色社会主义思想指引下，坚持人民民主专政，坚持社会主义道路，坚持改革开放，不断完善社会主义的各项制度，发展社会主义市场经济，发展社会主义民主，健全社会主义法治，贯彻新发展理念，自力更生，艰苦奋斗，逐步实现工业、农业、国防和科学技术的现代化，推动物质文明、政治文明、精神文明、社会文明、生态文明协调发展，把我国建设成为富强民主文明和谐美丽的社会主义现代化强国，实现中华民族伟大复兴。\n\n<!-- FORCE BREAK -->\n\n在我国，剥削阶级作为阶级已经消灭，但是阶级斗争还将在一定范围内长期存在。中国人民对敌视和破坏我国社会主义制度的国内外的敌对势力和敌对分子，必须进行斗争。\n\n台湾是中华人民共和国的神圣领土的一部分。完成统一祖国的大业是包括台湾同胞在内的全中国人民的神圣职责。\n\n社会主义的建设事业必须依靠工人、农民和知识分子，团结一切可以团结的力量。在长期的革命、建设、改革过程中，已经结成由中国共产党领导的，有各民主党派和各人民团体参加的，包括全体社会主义劳动者、社会主义事业的建设者、拥护社会主义的爱国者、拥护祖国统一和致力于中华民族伟大复兴的爱国者的广泛的爱国统一战线，这个统一战线将继续巩固和发展。中国人民政治协商会议是有广泛代表性的统一战线组织，过去发挥了重要的历史作用，今后在国家政治生活、社会生活和对外友好活动中，在进行社会主义现代化建设、维护国家的统一和团结的斗争中，将进一步发挥它的重要作用。中国共产党领导的多党合作和政治协商制度将长期存在和发展。\n\n<!-- FORCE BREAK -->\n\n中华人民共和国是全国各族人民共同缔造的统一的多民族国家。平等团结互助和谐的社会主义民族关系已经确立，并将继续加强。在维护民族团结的斗争中，要反对大民族主义，主要是大汉族主义，也要反对地方民族主义。国家尽一切努力，促进全国各民族的共同繁荣。', 'context': '宪法序言中关于国家根本任务、指导思想、统一大业、爱国统一战线与民族关系的集中表述', 'chunk_index': 1, 'char_count': 1044}
2026-05-13 08:54:45,597 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:54:45,597 - bm25_engine - DEBUG - Tokenizing text of length 1044
2026-05-13 08:54:45,598 - bm25_engine - DEBUG - Found 6 raw tokens
2026-05-13 08:54:45,598 - bm25_engine - DEBUG - After removing stop words: 6 tokens
2026-05-13 08:54:45,598 - bm25_engine - DEBUG - Document 1: 6 tokens, 2 unique terms
2026-05-13 08:54:45,598 - bm25_engine - DEBUG - Index statistics: 2 documents, 4 unique terms, 12 total terms
2026-05-13 08:54:45,598 - bm25_engine - INFO - Document 1 indexed successfully
2026-05-13 08:54:45,598 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=6.00
2026-05-13 08:54:45,598 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_1
INFO:     127.0.0.1:63076 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:01,398 - __main__ - INFO - Received index request for document of length 1100
2026-05-13 08:55:01,398 - __main__ - INFO - External doc_id provided: 宪法_chunk_2
2026-05-13 08:55:01,398 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_2' (internal ID 2)
2026-05-13 08:55:01,399 - bm25_engine - INFO - Adding document 2 to index
2026-05-13 08:55:01,399 - bm25_engine - DEBUG - Document text: 该段位于宪法序言末尾与第一章“总纲”开头之间，概括了国家民族政策、对外政策及宪法地位，并紧接引出国家性质、政权组织形式与民族平等原则，是连接宪法序言与总纲的过渡性关键段落。

中华人民共和国是全国各族...
2026-05-13 08:55:01,399 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1012, 'context_char_count': 86, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '中华人民共和国是全国各族人民共同缔造的统一的多民族国家。平等团结互助和谐的社会主义民族关系已经确立，并将继续加强。在维护民族团结的斗争中，要反对大民族主义，主要是大汉族主义，也要反对地方民族主义。国家尽一切努力，促进全国各民族的共同繁荣。\n\n中国革命、建设、改革的成就是同世界人民的支持分不开的。中国的前途是同世界的前途紧密地联系在一起的。中国坚持独立自主的对外政策，坚持互相尊重主权和领土完整、互不侵犯、互不干涉内政、平等互利、和平共处的五项原则，坚持和平发展道路，坚持互利共赢开放战略，发展同各国的外交关系和经济、文化交流，推动构建人类命运共同体；坚持反对帝国主义、霸权主义、殖民主义，加强同世界各国人民的团结，支持被压迫民族和发展中国家争取和维护民族独立、发展民族经济的正义斗争，为维护世界和平和促进人类进步事业而努力。\n\n本宪法以法律的形式确认了中国各族人民奋斗的成果，规定了国家的根本制度和根本任务，是国家的根本法，具有最高的法律效力。全国各族人民、一切国家机关和武装力量、各政党和各社会团体、各企业事业组织，都必须以宪法为根本的活动准则，并且负有维护宪法尊严、保证宪法实施的职责。\n\n## 第一章 总纲\n\n第一条 中华人民共和国是工人阶级领导的、以工农联盟为基础的人民民主专政的社会主义国家。\n\n社会主义制度是中华人民共和国的根本制度。中国共产党领导是中国特色社会主义最本质的特征。禁止任何组织或者个人破坏社会主义制度。\n\n第二条 中华人民共和国的一切权力属于人民。\n\n人民行使国家权力的机关是全国人民代表大会和地方各级人民代表大会。\n\n人民依照法律规定，通过各种途径和形式，管理国家事务，管理经济和文化事业，管理社会事务。\n\n第三条 中华人民共和国的国家机构实行民主集中制的原则。\n\n全国人民代表大会和地方各级人民代表大会都由民主选举产生，对人民负责，受人民监督。\n\n国家行政机关、监察机关、审判机关、检察机关都由人民代表大会产生，对它负责，受它监督。\n\n中央和地方的国家机构职权的划分，遵循在中央的统一领导下，充分发挥地方的主动性、积极性的原则。\n\n第四条 中华人民共和国各民族一律平等。国家保障各少数民族的合法的权利和利益，维护和发展各民族的平等团结互助和谐关系。禁止对任何民族的歧视和压迫，禁止破坏民族团结和制造民族分裂的行为。\n\n国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。', 'context': '该段位于宪法序言末尾与第一章“总纲”开头之间，概括了国家民族政策、对外政策及宪法地位，并紧接引出国家性质、政权组织形式与民族平等原则，是连接宪法序言与总纲的过渡性关键段落。', 'chunk_index': 2, 'char_count': 1100}
2026-05-13 08:55:01,399 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:55:01,399 - bm25_engine - DEBUG - Tokenizing text of length 1100
2026-05-13 08:55:01,400 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:55:01,400 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:55:01,400 - bm25_engine - DEBUG - Document 2: 0 tokens, 0 unique terms
2026-05-13 08:55:01,400 - bm25_engine - DEBUG - Index statistics: 3 documents, 4 unique terms, 12 total terms
2026-05-13 08:55:01,400 - bm25_engine - INFO - Document 2 indexed successfully
2026-05-13 08:55:01,400 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=4.00
2026-05-13 08:55:01,400 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_2
INFO:     127.0.0.1:60974 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:15,524 - __main__ - INFO - Received index request for document of length 1083
2026-05-13 08:55:15,524 - __main__ - INFO - External doc_id provided: 宪法_chunk_3
2026-05-13 08:55:15,524 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_3' (internal ID 3)
2026-05-13 08:55:15,524 - bm25_engine - INFO - Adding document 3 to index
2026-05-13 08:55:15,524 - bm25_engine - DEBUG - Document text: 总纲中关于民族区域自治、法治国家、基本经济制度及土地与自然资源的宪法条款。

国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。

各少数民族聚居的地方实行区域自治，设立自治机关...
2026-05-13 08:55:15,524 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1044, 'context_char_count': 37, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。\n\n各少数民族聚居的地方实行区域自治，设立自治机关，行使自治权。各民族自治地方都是中华人民共和国不可分离的部分。\n\n各民族都有使用和发展自己的语言文字的自由，都有保持或者改革自己的风俗习惯的自由。\n\n第五条 中华人民共和国实行依法治国，建设社会主义法治国家。\n\n国家维护社会主义法制的统一和尊严。\n\n一切法律、行政法规和地方性法规都不得同宪法相抵触。\n\n一切国家机关和武装力量、各政党和各社会团体、各企业事业组织都必须遵守宪法和法律。一切违反宪法和法律的行为，必须予以追究。\n\n任何组织或者个人都不得有超越宪法和法律的特权。\n\n第六条 中华人民共和国的社会主义经济制度的基础是生产资料的社会主义公有制，即全民所有制和劳动群众集体所有制。社会主义公有制消灭人剥削人的制度，实行各尽所能、按劳分配的原则。\n\n国家在社会主义初级阶段，坚持公有制为主体、多种所有制经济共同发展的基本经济制度，坚持按劳分配为主体、多种分配方式并存的分配制度。\n\n第七条 国有经济，即社会主义全民所有制经济，是国民经济中的主导力量。国家保障国有经济的巩固和发展。\n\n第八条 农村集体经济组织实行家庭承包经营为基础、统分结合的双层经营体制。农村中的生产、供销、信用、消费等各种形式的合作经济，是社会主义劳动群众集体所有制经济。参加农村集体经济组织的劳动者，有权在法律规定的范围内经营自留地、自留山、家庭副业和饲养自留畜。\n\n城镇中的手工业、工业、建筑业、运输业、商业、服务业等行业的各种形式的合作经济，都是社会主义劳动群众集体所有制经济。\n\n国家保护城乡集体经济组织的合法的权利和利益，鼓励、指导和帮助集体经济的发展。\n\n第九条 矿藏、水流、森林、山岭、草原、荒地、滩涂等自然资源，都属于国家所有，即全民所有；由法律规定属于集体所有的森林和山岭、草原、荒地、滩涂除外。\n\n国家保障自然资源的合理利用，保护珍贵的动物和植物。禁止任何组织或者个人用任何手段侵占或者破坏自然资源。\n\n第十条 城市的土地属于国家所有。\n\n农村和城市郊区的土地，除由法律规定属于国家所有的以外，属于集体所有；宅基地和自留地、自留山，也属于集体所有。\n\n国家为了公共利益的需要，可以依照法律规定对土地实行征收或者征用并给予补偿。\n\n任何组织或者个人不得侵占、买卖或者以其他形式非法转让土地。土地的使用权可以依照法律的规定转让。\n\n一切使用土地的组织和个人必须合理地利用土地。', 'context': '总纲中关于民族区域自治、法治国家、基本经济制度及土地与自然资源的宪法条款。', 'chunk_index': 3, 'char_count': 1083}
2026-05-13 08:55:15,524 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:55:15,525 - bm25_engine - DEBUG - Tokenizing text of length 1083
2026-05-13 08:55:15,525 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:55:15,526 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:55:15,526 - bm25_engine - DEBUG - Document 3: 0 tokens, 0 unique terms
2026-05-13 08:55:15,526 - bm25_engine - DEBUG - Index statistics: 4 documents, 4 unique terms, 12 total terms
2026-05-13 08:55:15,526 - bm25_engine - INFO - Document 3 indexed successfully
2026-05-13 08:55:15,526 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=3.00
2026-05-13 08:55:15,526 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_3
INFO:     127.0.0.1:61034 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:30,666 - __main__ - INFO - Received index request for document of length 1137
2026-05-13 08:55:30,666 - __main__ - INFO - External doc_id provided: 宪法_chunk_4
2026-05-13 08:55:30,666 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_4' (internal ID 4)
2026-05-13 08:55:30,667 - bm25_engine - INFO - Adding document 4 to index
2026-05-13 08:55:30,667 - bm25_engine - DEBUG - Document text: 位于《宪法》第一章“总纲”第十条至第十九条，集中规定土地制度、多种所有制经济、财产保护、国家经济政策、教育文化方针等社会主义基本经济制度与社会发展原则。

一切使用土地的组织和个人必须合理地利用土地。...
2026-05-13 08:55:30,667 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1059, 'context_char_count': 76, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '一切使用土地的组织和个人必须合理地利用土地。\n\n第十一条 在法律规定范围内的个体经济、私营经济等非公有制经济，是社会主义市场经济的重要组成部分。\n\n国家保护个体经济、私营经济等非公有制经济的合法的权利和利益。国家鼓励、支持和引导非公有制经济的发展，并对非公有制经济依法实行监督和管理。\n\n第十二条 社会主义的公共财产神圣不可侵犯。\n\n国家保护社会主义的公共财产。禁止任何组织或者个人用任何手段侵占或者破坏国家的和集体的财产。\n\n第十三条 公民的合法的私有财产不受侵犯。\n\n国家依照法律规定保护公民的私有财产权和继承权。\n\n国家为了公共利益的需要，可以依照法律规定对公民的私有财产实行征收或者征用并给予补偿。\n\n第十四条 国家通过提高劳动者的积极性和技术水平，推广先进的科学技术，完善经济管理体制和企业经营管理制度，实行各种形式的社会主义责任制，改进劳动组织，以不断提高劳动生产率和经济效益，发展社会生产力。\n\n国家厉行节约，反对浪费。\n\n国家合理安排积累和消费，兼顾国家、集体和个人的利益，在发展生产的基础上，逐步改善人民的物质生活和文化生活。\n\n国家建立健全同经济发展水平相适应的社会保障制度。\n\n第十五条 国家实行社会主义市场经济。\n\n国家加强经济立法，完善宏观调控。\n\n国家依法禁止任何组织或者个人扰乱社会经济秩序。\n\n第十六条 国有企业在法律规定的范围内有权自主经营。\n\n国有企业依照法律规定，通过职工代表大会和其他形式，实行民主管理。\n\n第十七条 集体经济组织在遵守有关法律的前提下，有独立进行经济活动的自主权。\n\n集体经济组织实行民主管理，依照法律规定选举和罢免管理人员，决定经营管理的重大问题。\n\n第十八条 中华人民共和国允许外国的企业和其他经济组织或者个人依照中华人民共和国法律的规定在中国投资，同中国的企业或者其他经济组织进行各种形式的经济合作。\n\n在中国境内的外国企业和其他外国经济组织以及中外合资经营的企业，都必须遵守中华人民共和国的法律。它们的合法的权利和利益受中华人民共和国法律的保护。\n\n第十九条 国家发展社会主义的教育事业，提高全国人民的科学文化水平。\n\n国家举办各种学校，普及初等义务教育，发展中等教育、职业教育和高等教育，并且发展学前教育。\n\n国家发展各种教育设施，扫除文盲，对工人、农民、国家工作人员和其他劳动者进行政治、文化、科学、技术、业务的教育，鼓励自学成才。\n\n国家鼓励集体经济组织、国家企业事业组织和其他社会力量依照法律规定举办各种教育事业。\n\n国家推广全国通用的普通话。', 'context': '位于《宪法》第一章“总纲”第十条至第十九条，集中规定土地制度、多种所有制经济、财产保护、国家经济政策、教育文化方针等社会主义基本经济制度与社会发展原则。', 'chunk_index': 4, 'char_count': 1137}
2026-05-13 08:55:30,667 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:55:30,667 - bm25_engine - DEBUG - Tokenizing text of length 1137
2026-05-13 08:55:30,668 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:55:30,668 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:55:30,668 - bm25_engine - DEBUG - Document 4: 0 tokens, 0 unique terms
2026-05-13 08:55:30,668 - bm25_engine - DEBUG - Index statistics: 5 documents, 4 unique terms, 12 total terms
2026-05-13 08:55:30,668 - bm25_engine - INFO - Document 4 indexed successfully
2026-05-13 08:55:30,668 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=2.40
2026-05-13 08:55:30,669 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_4
INFO:     127.0.0.1:61062 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:45,396 - __main__ - INFO - Received index request for document of length 1126
2026-05-13 08:55:45,396 - __main__ - INFO - External doc_id provided: 宪法_chunk_5
2026-05-13 08:55:45,396 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_5' (internal ID 5)
2026-05-13 08:55:45,396 - bm25_engine - INFO - Adding document 5 to index
2026-05-13 08:55:45,396 - bm25_engine - DEBUG - Document text: 总纲中关于国家发展教育、科学、文化、卫生、体育、语言、人才、精神文明、计划生育、生态环保、国家机关原则、社会秩序、国防建设及行政区划的连续条款群。

国家推广全国通用的普通话。

第二十条 国家发展自...
2026-05-13 08:55:45,397 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1051, 'context_char_count': 73, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '国家推广全国通用的普通话。\n\n第二十条 国家发展自然科学和社会科学事业，普及科学和技术知识，奖励科学研究成果和技术发明创造。\n\n第二十一条 国家发展医疗卫生事业，发展现代医药和我国传统医药，鼓励和支持农村集体经济组织、国家企业事业组织和街道组织举办各种医疗卫生设施，开展群众性的卫生活动，保护人民健康。\n\n国家发展体育事业，开展群众性的体育活动，增强人民体质。\n\n第二十二条 国家发展为人民服务、为社会主义服务的文学艺术事业、新闻广播电视事业、出版发行事业、图书馆博物馆文化馆和其他文化事业，开展群众性的文化活动。\n\n国家保护名胜古迹、珍贵文物和其他重要历史文化遗产。\n\n第二十三条 国家培养为社会主义服务的各种专业人才，扩大知识分子的队伍，创造条件，充分发挥他们在社会主义现代化建设中的作用。\n\n第二十四条 国家通过普及理想教育、道德教育、文化教育、纪律和法制教育，通过在城乡不同范围的群众中制定和执行各种守则、公约，加强社会主义精神文明的建设。\n\n国家倡导社会主义核心价值观，提倡爱祖国、爱人民、爱劳动、爱科学、爱社会主义的公德，在人民中进行爱国主义、集体主义和国际主义、共产主义的教育，进行辩证唯物主义和历史唯物主义的教育，反对资本主义的、封建主义的和其他的腐朽思想。\n\n第二十五条 国家推行计划生育，使人口的增长同经济和社会发展计划相适应。\n\n第二十六条 国家保护和改善生活环境和生态环境，防治污染和其他公害。\n\n国家组织和鼓励植树造林，保护林木。\n\n第二十七条 一切国家机关实行精简的原则，实行工作责任制，实行工作人员的培训和考核制度，不断提高工作质量和工作效率，反对官僚主义。\n\n一切国家机关和国家工作人员必须依靠人民的支持，经常保持同人民的密切联系，倾听人民的意见和建议，接受人民的监督，努力为人民服务。\n\n国家工作人员就职时应当依照法律规定公开进行宪法宣誓。\n\n第二十八条 国家维护社会秩序，镇压叛国和其他危害国家安全的犯罪活动，制裁危害社会治安、破坏社会主义经济和其他犯罪的活动，惩办和改造犯罪分子。\n\n第二十九条 中华人民共和国的武装力量属于人民。它的任务是巩固国防，抵抗侵略，保卫祖国，保卫人民的和平劳动，参加国家建设事业，努力为人民服务。\n\n国家加强武装力量的革命化、现代化、正规化的建设，增强国防力量。\n\n第三十条 中华人民共和国的行政区域划分如下：\n\n（一）全国分为省、自治区、直辖市；\n\n（二）省、自治区分为自治州、县、自治县、市；\n\n（三）县、自治县分为乡、民族乡、镇。', 'context': '总纲中关于国家发展教育、科学、文化、卫生、体育、语言、人才、精神文明、计划生育、生态环保、国家机关原则、社会秩序、国防建设及行政区划的连续条款群。', 'chunk_index': 5, 'char_count': 1126}
2026-05-13 08:55:45,397 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:55:45,397 - bm25_engine - DEBUG - Tokenizing text of length 1126
2026-05-13 08:55:45,397 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:55:45,398 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:55:45,398 - bm25_engine - DEBUG - Document 5: 0 tokens, 0 unique terms
2026-05-13 08:55:45,398 - bm25_engine - DEBUG - Index statistics: 6 documents, 4 unique terms, 12 total terms
2026-05-13 08:55:45,398 - bm25_engine - INFO - Document 5 indexed successfully
2026-05-13 08:55:45,398 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=2.00
2026-05-13 08:55:45,398 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_5
INFO:     127.0.0.1:61092 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:01,687 - __main__ - INFO - Received index request for document of length 1161
2026-05-13 08:56:01,687 - __main__ - INFO - External doc_id provided: 宪法_chunk_6
2026-05-13 08:56:01,687 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_6' (internal ID 6)
2026-05-13 08:56:01,687 - bm25_engine - INFO - Adding document 6 to index
2026-05-13 08:56:01,687 - bm25_engine - DEBUG - Document text: 该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的...
2026-05-13 08:56:01,687 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1054, 'context_char_count': 105, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '（三）县、自治县分为乡、民族乡、镇。\n\n直辖市和较大的市分为区、县。自治州分为县、自治县、市。\n\n自治区、自治州、自治县都是民族自治地方。\n\n第三十一条 国家在必要时得设立特别行政区。在特别行政区内实行的制度按照具体情况由全国人民代表大会以法律规定。\n\n第三十二条 中华人民共和国保护在中国境内的外国人的合法权利和利益，在中国境内的外国人必须遵守中华人民共和国的法律。\n\n中华人民共和国对于因为政治原因要求避难的外国人，可以给予受庇护的权利。\n\n## 第二章 公民的基本权利和义务\n\n第三十三条 凡具有中华人民共和国国籍的人都是中华人民共和国公民。\n\n中华人民共和国公民在法律面前一律平等。\n\n国家尊重和保障人权。\n\n任何公民享有宪法和法律规定的权利，同时必须履行宪法和法律规定的义务。\n\n第三十四条 中华人民共和国年满十八周岁的公民，不分民族、种族、性别、职业、家庭出身、宗教信仰、教育程度、财产状况、居住期限，都有选举权和被选举权；但是依照法律被剥夺政治权利的人除外。\n\n第三十五条 中华人民共和国公民有言论、出版、集会、结社、游行、示威的自由。\n\n第三十六条 中华人民共和国公民有宗教信仰自由。\n\n任何国家机关、社会团体和个人不得强制公民信仰宗教或者不信仰宗教，不得歧视信仰宗教的公民和不信仰宗教的公民。\n\n国家保护正常的宗教活动。任何人不得利用宗教进行破坏社会秩序、损害公民身体健康、妨碍国家教育制度的活动。\n\n宗教团体和宗教事务不受外国势力的支配。\n\n第三十七条 中华人民共和国公民的人身自由不受侵犯。\n\n任何公民，非经人民检察院批准或者决定或者人民法院决定，并由公安机关执行，不受逮捕。\n\n禁止非法拘禁和以其他方法非法剥夺或者限制公民的人身自由，禁止非法搜查公民的身体。\n\n第三十八条 中华人民共和国公民的人格尊严不受侵犯。禁止用任何方法对公民进行侮辱、诽谤和诬告陷害。\n\n第三十九条 中华人民共和国公民的住宅不受侵犯。禁止非法搜查或者非法侵入公民的住宅。\n\n第四十条 中华人民共和国公民的通信自由和通信秘密受法律的保护。除因国家安全或者追查刑事犯罪的需要，由公安机关或者检察机关依照法律规定的程序对通信进行检查外，任何组织或者个人不得以任何理由侵犯公民的通信自由和通信秘密。\n\n第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。', 'context': '该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的过渡段落。', 'chunk_index': 6, 'char_count': 1161}
2026-05-13 08:56:01,687 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:56:01,688 - bm25_engine - DEBUG - Tokenizing text of length 1161
2026-05-13 08:56:01,688 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:56:01,688 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:56:01,689 - bm25_engine - DEBUG - Document 6: 0 tokens, 0 unique terms
2026-05-13 08:56:01,689 - bm25_engine - DEBUG - Index statistics: 7 documents, 4 unique terms, 12 total terms
2026-05-13 08:56:01,689 - bm25_engine - INFO - Document 6 indexed successfully
2026-05-13 08:56:01,689 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=1.71
2026-05-13 08:56:01,689 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_6
INFO:     127.0.0.1:49171 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:16,491 - __main__ - INFO - Received index request for document of length 1139
2026-05-13 08:56:16,491 - __main__ - INFO - External doc_id provided: 宪法_chunk_7
2026-05-13 08:56:16,491 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_7' (internal ID 7)
2026-05-13 08:56:16,491 - bm25_engine - INFO - Adding document 7 to index
2026-05-13 08:56:16,491 - bm25_engine - DEBUG - Document text: 第二章“公民的基本权利和义务”中段，集中列举公民在政治、劳动、休息、社会保障、教育、文化、性别平等、婚姻家庭及侨务等方面享有的基本权利与对应国家保障义务。

第四十一条 中华人民共和国公民对于任何国家...
2026-05-13 08:56:16,491 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1060, 'context_char_count': 77, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。\n\n对于公民的申诉、控告或者检举，有关国家机关必须查清事实，负责处理。任何人不得压制和打击报复。\n\n由于国家机关和国家工作人员侵犯公民权利而受到损失的人，有依照法律规定取得赔偿的权利。\n\n第四十二条 中华人民共和国公民有劳动的权利和义务。\n\n国家通过各种途径，创造劳动就业条件，加强劳动保护，改善劳动条件，并在发展生产的基础上，提高劳动报酬和福利待遇。\n\n劳动是一切有劳动能力的公民的光荣职责。国有企业和城乡集体经济组织的劳动者都应当以国家主人翁的态度对待自己的劳动。国家提倡社会主义劳动竞赛，奖励劳动模范和先进工作者。国家提倡公民从事义务劳动。\n\n国家对就业前的公民进行必要的劳动就业训练。\n\n第四十三条 中华人民共和国劳动者有休息的权利。\n\n国家发展劳动者休息和休养的设施，规定职工的工作时间和休假制度。\n\n第四十四条 国家依照法律规定实行企业事业组织的职工和国家机关工作人员的退休制度。退休人员的生活受到国家和社会的保障。\n\n第四十五条 中华人民共和国公民在年老、疾病或者丧失劳动能力的情况下，有从国家和社会获得物质帮助的权利。国家发展为公民享受这些权利所需要的社会保险、社会救济和医疗卫生事业。\n\n国家和社会保障残废军人的生活，抚恤烈士家属，优待军人家属。\n\n国家和社会帮助安排盲、聋、哑和其他有残疾的公民的劳动、生活和教育。\n\n第四十六条 中华人民共和国公民有受教育的权利和义务。\n\n国家培养青年、少年、儿童在品德、智力、体质等方面全面发展。\n\n第四十七条 中华人民共和国公民有进行科学研究、文学艺术创作和其他文化活动的自由。国家对于从事教育、科学、技术、文学、艺术和其他文化事业的公民的有益于人民的创造性工作，给以鼓励和帮助。\n\n第四十八条 中华人民共和国妇女在政治的、经济的、文化的、社会的和家庭的生活等各方面享有同男子平等的权利。\n\n国家保护妇女的权利和利益，实行男女同工同酬，培养和选拔妇女干部。\n\n第四十九条 婚姻、家庭、母亲和儿童受国家的保护。\n\n夫妻双方有实行计划生育的义务。\n\n父母有抚养教育未成年子女的义务，成年子女有赡养扶助父母的义务。\n\n禁止破坏婚姻自由，禁止虐待老人、妇女和儿童。\n\n第五十条 中华人民共和国保护华侨的正当的权利和利益，保护归侨和侨眷的合法的权利和利益。', 'context': '第二章“公民的基本权利和义务”中段，集中列举公民在政治、劳动、休息、社会保障、教育、文化、性别平等、婚姻家庭及侨务等方面享有的基本权利与对应国家保障义务。', 'chunk_index': 7, 'char_count': 1139}
2026-05-13 08:56:16,492 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:56:16,492 - bm25_engine - DEBUG - Tokenizing text of length 1139
2026-05-13 08:56:16,492 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:56:16,493 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:56:16,493 - bm25_engine - DEBUG - Document 7: 0 tokens, 0 unique terms
2026-05-13 08:56:16,493 - bm25_engine - DEBUG - Index statistics: 8 documents, 4 unique terms, 12 total terms
2026-05-13 08:56:16,493 - bm25_engine - INFO - Document 7 indexed successfully
2026-05-13 08:56:16,493 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=1.50
2026-05-13 08:56:16,493 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_7
INFO:     127.0.0.1:49201 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:32,869 - __main__ - INFO - Received index request for document of length 1085
2026-05-13 08:56:32,869 - __main__ - INFO - External doc_id provided: 宪法_chunk_8
2026-05-13 08:56:32,869 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_8' (internal ID 8)
2026-05-13 08:56:32,869 - bm25_engine - INFO - Adding document 8 to index
2026-05-13 08:56:32,870 - bm25_engine - DEBUG - Document text: 该段条文位于《宪法》第二章“公民的基本权利和义务”末尾，紧接其后即进入第三章“国家机构”第一节“全国人民代表大会”，标志从基本权利义务向国家权力机关规定的过渡。

第五十条 中华人民共和国保护华侨的正...
2026-05-13 08:56:32,870 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1003, 'context_char_count': 80, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '第五十条 中华人民共和国保护华侨的正当的权利和利益，保护归侨和侨眷的合法的权利和利益。\n\n第五十一条 中华人民共和国公民在行使自由和权利的时候，不得损害国家的、社会的、集体的利益和其他公民的合法的自由和权利。\n\n第五十二条 中华人民共和国公民有维护国家统一和全国各民族团结的义务。\n\n第五十三条 中华人民共和国公民必须遵守宪法和法律，保守国家秘密，爱护公共财产，遵守劳动纪律，遵守公共秩序，尊重社会公德。\n\n第五十四条 中华人民共和国公民有维护祖国的安全、荣誉和利益的义务，不得有危害祖国的安全、荣誉和利益的行为。\n\n第五十五条 保卫祖国、抵抗侵略是中华人民共和国每一个公民的神圣职责。\n\n依照法律服兵役和参加民兵组织是中华人民共和国公民的光荣义务。\n\n第五十六条 中华人民共和国公民有依照法律纳税的义务。\n\n## 第三章 国家机构\n\n### 第一节 全国人民代表大会\n\n第五十七条 中华人民共和国全国人民代表大会是最高国家权力机关。它的常设机关是全国人民代表大会常务委员会。\n\n第五十八条 全国人民代表大会和全国人民代表大会常务委员会行使国家立法权。\n\n第五十九条 全国人民代表大会由省、自治区、直辖市、特别行政区和军队选出的代表组成。各少数民族都应当有适当名额的代表。\n\n全国人民代表大会代表的选举由全国人民代表大会常务委员会主持。\n\n全国人民代表大会代表名额和代表产生办法由法律规定。\n\n第六十条 全国人民代表大会每届任期五年。\n\n全国人民代表大会任期届满的两个月以前，全国人民代表大会常务委员会必须完成下届全国人民代表大会代表的选举。如果遇到不能进行选举的非常情况，由全国人民代表大会常务委员会以全体组成人员的三分之二以上的多数通过，可以推迟选举，延长本届全国人民代表大会的任期。在非常情况结束后一年内，必须完成下届全国人民代表大会代表的选举。\n\n第六十一条 全国人民代表大会会议每年举行一次，由全国人民代表大会常务委员会召集。如果全国人民代表大会常务委员会认为必要，或者有五分之一以上的全国人民代表大会代表提议，可以临时召集全国人民代表大会会议。\n\n全国人民代表大会举行会议的时候，选举主席团主持会议。\n\n第六十二条 全国人民代表大会行使下列职权：\n\n（一）修改宪法；\n\n（二）监督宪法的实施；\n\n（三）制定和修改刑事、民事、国家机构的和其他的基本法律；\n\n（四）选举中华人民共和国主席、副主席；', 'context': '该段条文位于《宪法》第二章“公民的基本权利和义务”末尾，紧接其后即进入第三章“国家机构”第一节“全国人民代表大会”，标志从基本权利义务向国家权力机关规定的过渡。', 'chunk_index': 8, 'char_count': 1085}
2026-05-13 08:56:32,870 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:56:32,870 - bm25_engine - DEBUG - Tokenizing text of length 1085
2026-05-13 08:56:32,870 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:56:32,871 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:56:32,871 - bm25_engine - DEBUG - Document 8: 0 tokens, 0 unique terms
2026-05-13 08:56:32,871 - bm25_engine - DEBUG - Index statistics: 9 documents, 4 unique terms, 12 total terms
2026-05-13 08:56:32,871 - bm25_engine - INFO - Document 8 indexed successfully
2026-05-13 08:56:32,871 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=1.33
2026-05-13 08:56:32,871 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_8
INFO:     127.0.0.1:51207 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:46,311 - __main__ - INFO - Received index request for document of length 1145
2026-05-13 08:56:46,311 - __main__ - INFO - External doc_id provided: 宪法_chunk_9
2026-05-13 08:56:46,312 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_9' (internal ID 9)
2026-05-13 08:56:46,312 - bm25_engine - INFO - Adding document 9 to index
2026-05-13 08:56:46,312 - bm25_engine - DEBUG - Document text: 位于《宪法》第三章“国家机构”第一节“全国人民代表大会”第六十二条至第六十七条，集中规定全国人大及其常委会的职权、人事选举与罢免、宪法修改程序及常委会组成与任期。

（四）选举中华人民共和国主席、副主...
2026-05-13 08:56:46,312 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1062, 'context_char_count': 81, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '（四）选举中华人民共和国主席、副主席；\n\n（五）根据中华人民共和国主席的提名，决定国务院总理的人选；根据国务院总理的提名，决定国务院副总理、国务委员、各部部长、各委员会主任、审计长、秘书长的人选；\n\n（六）选举中央军事委员会主席；根据中央军事委员会主席的提名，决定中央军事委员会其他组成人员的人选；\n\n（七）选举国家监察委员会主任；\n\n（八）选举最高人民法院院长；\n\n（九）选举最高人民检察院检察长；\n\n（十）审查和批准国民经济和社会发展计划和计划执行情况的报告；\n\n（十一）审查和批准国家的预算和预算执行情况的报告；\n\n（十二）改变或者撤销全国人民代表大会常务委员会不适当的决定；\n\n（十三）批准省、自治区和直辖市的建置；\n\n（十四）决定特别行政区的设立及其制度；\n\n（十五）决定战争和和平的问题；\n\n（十六）应当由最高国家权力机关行使的其他职权。\n\n第六十三条 全国人民代表大会有权罢免下列人员：\n\n（一）中华人民共和国主席、副主席；\n\n（二）国务院总理、副总理、国务委员、各部部长、各委员会主任、审计长、秘书长；\n\n（三）中央军事委员会主席和中央军事委员会其他组成人员；\n\n（四）国家监察委员会主任；\n\n（五）最高人民法院院长；\n\n（六）最高人民检察院检察长。\n\n第六十四条 宪法的修改，由全国人民代表大会常务委员会或者五分之一以上的全国人民代表大会代表提议，并由全国人民代表大会以全体代表的三分之二以上的多数通过。\n\n法律和其他议案由全国人民代表大会以全体代表的过半数通过。\n\n第六十五条 全国人民代表大会常务委员会由下列人员组成：\n\n委员长，\n\n副委员长若干人，\n\n秘书长，\n\n委员若干人。\n\n全国人民代表大会常务委员会组成人员中，应当有适当名额的少数民族代表。\n\n全国人民代表大会选举并有权罢免全国人民代表大会常务委员会的组成人员。\n\n全国人民代表大会常务委员会的组成人员不得担任国家行政机关、监察机关、审判机关和检察机关的职务。\n\n第六十六条 全国人民代表大会常务委员会每届任期同全国人民代表大会每届任期相同，它行使职权到下届全国人民代表大会选出新的常务委员会为止。\n\n委员长、副委员长连续任职不得超过两届。\n\n第六十七条 全国人民代表大会常务委员会行使下列职权：\n\n（一）解释宪法，监督宪法的实施；\n\n（二）制定和修改除应当由全国人民代表大会制定的法律以外的其他法律；\n\n（三）在全国人民代表大会闭会期间，对全国人民代表大会制定的法律进行部分补充和修改，但是不得同该法律的基本原则相抵触；\n\n（四）解释法律；', 'context': '位于《宪法》第三章“国家机构”第一节“全国人民代表大会”第六十二条至第六十七条，集中规定全国人大及其常委会的职权、人事选举与罢免、宪法修改程序及常委会组成与任期。', 'chunk_index': 9, 'char_count': 1145}
2026-05-13 08:56:46,312 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:56:46,312 - bm25_engine - DEBUG - Tokenizing text of length 1145
2026-05-13 08:56:46,313 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:56:46,313 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:56:46,313 - bm25_engine - DEBUG - Document 9: 0 tokens, 0 unique terms
2026-05-13 08:56:46,313 - bm25_engine - DEBUG - Index statistics: 10 documents, 4 unique terms, 12 total terms
2026-05-13 08:56:46,313 - bm25_engine - INFO - Document 9 indexed successfully
2026-05-13 08:56:46,313 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=1.20
2026-05-13 08:56:46,313 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_9
INFO:     127.0.0.1:51219 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:59,519 - __main__ - INFO - Received index request for document of length 1070
2026-05-13 08:56:59,519 - __main__ - INFO - External doc_id provided: 宪法_chunk_10
2026-05-13 08:56:59,519 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_10' (internal ID 10)
2026-05-13 08:56:59,519 - bm25_engine - INFO - Adding document 10 to index
2026-05-13 08:56:59,519 - bm25_engine - DEBUG - Document text: 第六十七条 全国人民代表大会常务委员会行使下列职权：

（四）解释法律；

（五）在全国人民代表大会闭会期间，审查和批准国民经济和社会发展计划、国家预算在执行过程中所必须作的部分调整方案；

（六）监...
2026-05-13 08:56:59,520 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1042, 'context_char_count': 26, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '（四）解释法律；\n\n（五）在全国人民代表大会闭会期间，审查和批准国民经济和社会发展计划、国家预算在执行过程中所必须作的部分调整方案；\n\n（六）监督国务院、中央军事委员会、国家监察委员会、最高人民法院和最高人民检察院的工作；\n\n（七）撤销国务院制定的同宪法、法律相抵触的行政法规、决定和命令；\n\n（八）撤销省、自治区、直辖市国家权力机关制定的同宪法、法律和行政法规相抵触的地方性法规和决议；\n\n（九）在全国人民代表大会闭会期间，根据国务院总理的提名，决定部长、委员会主任、审计长、秘书长的人选；\n\n（十）在全国人民代表大会闭会期间，根据中央军事委员会主席的提名，决定中央军事委员会其他组成人员的人选；\n\n（十一）根据国家监察委员会主任的提请，任免国家监察委员会副主任、委员；\n\n（十二）根据最高人民法院院长的提请，任免最高人民法院副院长、审判员、审判委员会委员和军事法院院长；\n\n（十三）根据最高人民检察院检察长的提请，任免最高人民检察院副检察长、检察员、检察委员会委员和军事检察院检察长，并且批准省、自治区、直辖市的人民检察院检察长的任免；\n\n（十四）决定驻外全权代表的任免；\n\n（十五）决定同外国缔结的条约和重要协定的批准和废除；\n\n（十六）规定军人和外交人员的衔级制度和其他专门衔级制度；\n\n（十七）规定和决定授予国家的勋章和荣誉称号；\n\n（十八）决定特赦；\n\n（十九）在全国人民代表大会闭会期间，如果遇到国家遭受武装侵犯或者必须履行国际间共同防止侵略的条约的情况，决定战争状态的宣布；\n\n（二十）决定全国总动员或者局部动员；\n\n（二十一）决定全国或者个别省、自治区、直辖市进入紧急状态；\n\n（二十二）全国人民代表大会授予的其他职权。\n\n第六十八条 全国人民代表大会常务委员会委员长主持全国人民代表大会常务委员会的工作，召集全国人民代表大会常务委员会会议。副委员长、秘书长协助委员长工作。\n\n委员长、副委员长、秘书长组成委员长会议，处理全国人民代表大会常务委员会的重要日常工作。\n\n第六十九条 全国人民代表大会常务委员会对全国人民代表大会负责并报告工作。\n\n第七十条 全国人民代表大会设立民族委员会、宪法和法律委员会、财政经济委员会、教育科学文化卫生委员会、外事委员会、华侨委员会和其他需要设立的专门委员会。在全国人民代表大会闭会期间，各专门委员会受全国人民代表大会常务委员会的领导。\n\n各专门委员会在全国人民代表大会和全国人民代表大会常务委员会领导下，研究、审议和拟订有关议案。', 'context': '第六十七条 全国人民代表大会常务委员会行使下列职权：', 'chunk_index': 10, 'char_count': 1070}
2026-05-13 08:56:59,520 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:56:59,520 - bm25_engine - DEBUG - Tokenizing text of length 1070
2026-05-13 08:56:59,520 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:56:59,520 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:56:59,521 - bm25_engine - DEBUG - Document 10: 0 tokens, 0 unique terms
2026-05-13 08:56:59,521 - bm25_engine - DEBUG - Index statistics: 11 documents, 4 unique terms, 12 total terms
2026-05-13 08:56:59,521 - bm25_engine - INFO - Document 10 indexed successfully
2026-05-13 08:56:59,521 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=1.09
2026-05-13 08:56:59,521 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_10
INFO:     127.0.0.1:51233 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:13,781 - __main__ - INFO - Received index request for document of length 1054
2026-05-13 08:57:13,781 - __main__ - INFO - External doc_id provided: 宪法_chunk_11
2026-05-13 08:57:13,781 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_11' (internal ID 11)
2026-05-13 08:57:13,781 - bm25_engine - INFO - Adding document 11 to index
2026-05-13 08:57:13,781 - bm25_engine - DEBUG - Document text: 位于《宪法》第三章“国家机构”第一节“全国人民代表大会”末尾，衔接第二节“中华人民共和国主席”，规定全国人大及其常委会的组织运作、代表权利义务及与主席的职权交接。

各专门委员会在全国人民代表大会和全...
2026-05-13 08:57:13,781 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 971, 'context_char_count': 81, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '各专门委员会在全国人民代表大会和全国人民代表大会常务委员会领导下，研究、审议和拟订有关议案。\n\n第七十一条 全国人民代表大会和全国人民代表大会常务委员会认为必要的时候，可以组织关于特定问题的调查委员会，并且根据调查委员会的报告，作出相应的决议。\n\n调查委员会进行调查的时候，一切有关的国家机关、社会团体和公民都有义务向它提供必要的材料。\n\n第七十二条 全国人民代表大会代表和全国人民代表大会常务委员会组成人员，有权依照法律规定的程序分别提出属于全国人民代表大会和全国人民代表大会常务委员会职权范围内的议案。\n\n第七十三条 全国人民代表大会代表在全国人民代表大会开会期间，全国人民代表大会常务委员会组成人员在常务委员会开会期间，有权依照法律规定的程序提出对国务院或者国务院各部、各委员会的质询案。受质询的机关必须负责答复。\n\n第七十四条 全国人民代表大会代表，非经全国人民代表大会会议主席团许可，在全国人民代表大会闭会期间非经全国人民代表大会常务委员会许可，不受逮捕或者刑事审判。\n\n第七十五条 全国人民代表大会代表在全国人民代表大会各种会议上的发言和表决，不受法律追究。\n\n第七十六条 全国人民代表大会代表必须模范地遵守宪法和法律，保守国家秘密，并且在自己参加的生产、工作和社会活动中，协助宪法和法律的实施。\n\n全国人民代表大会代表应当同原选举单位和人民保持密切的联系，听取和反映人民的意见和要求，努力为人民服务。\n\n第七十七条 全国人民代表大会代表受原选举单位的监督。原选举单位有权依照法律规定的程序罢免本单位选出的代表。\n\n第七十八条 全国人民代表大会和全国人民代表大会常务委员会的组织和工作程序由法律规定。\n\n### 第二节 中华人民共和国主席\n\n第七十九条 中华人民共和国主席、副主席由全国人民代表大会选举。\n\n有选举权和被选举权的年满四十五周岁的中华人民共和国公民可以被选为中华人民共和国主席、副主席。\n\n中华人民共和国主席、副主席每届任期同全国人民代表大会每届任期相同。\n\n第八十条 中华人民共和国主席根据全国人民代表大会的决定和全国人民代表大会常务委员会的决定，公布法律，任免国务院总理、副总理、国务委员、各部部长、各委员会主任、审计长、秘书长，授予国家的勋章和荣誉称号，发布特赦令，宣布进入紧急状态，宣布战争状态，发布动员令。', 'context': '位于《宪法》第三章“国家机构”第一节“全国人民代表大会”末尾，衔接第二节“中华人民共和国主席”，规定全国人大及其常委会的组织运作、代表权利义务及与主席的职权交接。', 'chunk_index': 11, 'char_count': 1054}
2026-05-13 08:57:13,782 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:57:13,782 - bm25_engine - DEBUG - Tokenizing text of length 1054
2026-05-13 08:57:13,782 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:57:13,783 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:57:13,783 - bm25_engine - DEBUG - Document 11: 0 tokens, 0 unique terms
2026-05-13 08:57:13,783 - bm25_engine - DEBUG - Index statistics: 12 documents, 4 unique terms, 12 total terms
2026-05-13 08:57:13,783 - bm25_engine - INFO - Document 11 indexed successfully
2026-05-13 08:57:13,783 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=1.00
2026-05-13 08:57:13,783 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_11
INFO:     127.0.0.1:51255 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:27,101 - __main__ - INFO - Received index request for document of length 1158
2026-05-13 08:57:27,101 - __main__ - INFO - External doc_id provided: 宪法_chunk_12
2026-05-13 08:57:27,101 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_12' (internal ID 12)
2026-05-13 08:57:27,101 - bm25_engine - INFO - Adding document 12 to index
2026-05-13 08:57:27,102 - bm25_engine - DEBUG - Document text: 国家主席、副主席的职权与国务院的组成、任期及行政权——位于《宪法》第三章“国家机构”第二节与第三节之间，衔接元首制度与最高行政机关。

第八十条 中华人民共和国主席根据全国人民代表大会的决定和全国人民...
2026-05-13 08:57:27,102 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1090, 'context_char_count': 66, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '第八十条 中华人民共和国主席根据全国人民代表大会的决定和全国人民代表大会常务委员会的决定，公布法律，任免国务院总理、副总理、国务委员、各部部长、各委员会主任、审计长、秘书长，授予国家的勋章和荣誉称号，发布特赦令，宣布进入紧急状态，宣布战争状态，发布动员令。\n\n第八十一条 中华人民共和国主席代表中华人民共和国，进行国事活动，接受外国使节；根据全国人民代表大会常务委员会的决定，派遣和召回驻外全权代表，批准和废除同外国缔结的条约和重要协定。\n\n第八十二条 中华人民共和国副主席协助主席工作。\n\n中华人民共和国副主席受主席的委托，可以代行主席的部分职权。\n\n第八十三条 中华人民共和国主席、副主席行使职权到下届全国人民代表大会选出的主席、副主席就职为止。\n\n第八十四条 中华人民共和国主席缺位的时候，由副主席继任主席的职位。\n\n中华人民共和国副主席缺位的时候，由全国人民代表大会补选。\n\n中华人民共和国主席、副主席都缺位的时候，由全国人民代表大会补选；在补选以前，由全国人民代表大会常务委员会委员长暂时代理主席职位。\n\n### 第三节 国务院\n\n第八十五条 中华人民共和国国务院，即中央人民政府，是最高国家权力机关的执行机关，是最高国家行政机关。\n\n第八十六条 国务院由下列人员组成：\n\n总理，\n\n副总理若干人，\n\n国务委员若干人，\n\n各部部长，\n\n各委员会主任，\n\n审计长，\n\n秘书长。\n\n国务院实行总理负责制。各部、各委员会实行部长、主任负责制。\n\n国务院的组织由法律规定。\n\n第八十七条 国务院每届任期同全国人民代表大会每届任期相同。\n\n总理、副总理、国务委员连续任职不得超过两届。\n\n第八十八条 总理领导国务院的工作。副总理、国务委员协助总理工作。\n\n总理、副总理、国务委员、秘书长组成国务院常务会议。\n\n总理召集和主持国务院常务会议和国务院全体会议。\n\n第八十九条 国务院行使下列职权：\n\n（一）根据宪法和法律，规定行政措施，制定行政法规，发布决定和命令；\n\n（二）向全国人民代表大会或者全国人民代表大会常务委员会提出议案；\n\n（三）规定各部和各委员会的任务和职责，统一领导各部和各委员会的工作，并且领导不属于各部和各委员会的全国性的行政工作；\n\n（四）统一领导全国地方各级国家行政机关的工作，规定中央和省、自治区、直辖市的国家行政机关的职权的具体划分；\n\n（五）编制和执行国民经济和社会发展计划和国家预算；\n\n（六）领导和管理经济工作和城乡建设、生态文明建设；\n\n（七）领导和管理教育、科学、文化、卫生、体育和计划生育工作；\n\n（八）领导和管理民政、公安、司法行政等工作；', 'context': '国家主席、副主席的职权与国务院的组成、任期及行政权——位于《宪法》第三章“国家机构”第二节与第三节之间，衔接元首制度与最高行政机关。', 'chunk_index': 12, 'char_count': 1158}
2026-05-13 08:57:27,102 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:57:27,102 - bm25_engine - DEBUG - Tokenizing text of length 1158
2026-05-13 08:57:27,103 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:57:27,103 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:57:27,103 - bm25_engine - DEBUG - Document 12: 0 tokens, 0 unique terms
2026-05-13 08:57:27,103 - bm25_engine - DEBUG - Index statistics: 13 documents, 4 unique terms, 12 total terms
2026-05-13 08:57:27,103 - bm25_engine - INFO - Document 12 indexed successfully
2026-05-13 08:57:27,103 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.92
2026-05-13 08:57:27,103 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_12
INFO:     127.0.0.1:51275 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:43,677 - __main__ - INFO - Received index request for document of length 1177
2026-05-13 08:57:43,677 - __main__ - INFO - External doc_id provided: 宪法_chunk_13
2026-05-13 08:57:43,677 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_13' (internal ID 13)
2026-05-13 08:57:43,677 - bm25_engine - INFO - Adding document 13 to index
2026-05-13 08:57:43,678 - bm25_engine - DEBUG - Document text: 该段位于《宪法》第三章“国家机构”第三节“国务院”末尾至第五节“地方各级人民代表大会和地方各级人民政府”开头，列举国务院第（八）至（十八）项职权、部委职责、审计署设置及其对全国人大负责的关系，并衔接过...
2026-05-13 08:57:43,678 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1052, 'context_char_count': 123, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '（八）领导和管理民政、公安、司法行政等工作；\n\n（九）管理对外事务，同外国缔结条约和协定；\n\n（十）领导和管理国防建设事业；\n\n（十一）领导和管理民族事务，保障少数民族的平等权利和民族自治地方的自治权利；\n\n（十二）保护华侨的正当的权利和利益，保护归侨和侨眷的合法的权利和利益；\n\n（十三）改变或者撤销各部、各委员会发布的不适当的命令、指示和规章；\n\n（十四）改变或者撤销地方各级国家行政机关的不适当的决定和命令；\n\n（十五）批准省、自治区、直辖市的区域划分，批准自治州、县、自治县、市的建置和区域划分；\n\n（十六）依照法律规定决定省、自治区、直辖市的范围内部分地区进入紧急状态；\n\n（十七）审定行政机构的编制，依照法律规定任免、培训、考核和奖惩行政人员；\n\n（十八）全国人民代表大会和全国人民代表大会常务委员会授予的其他职权。\n\n第九十条 国务院各部部长、各委员会主任负责本部门的工作；召集和主持部务会议或者委员会会议、委务会议，讨论决定本部门工作的重大问题。\n\n各部、各委员会根据法律和国务院的行政法规、决定、命令，在本部门的权限内，发布命令、指示和规章。\n\n第九十一条 国务院设立审计机关，对国务院各部门和地方各级政府的财政收支，对国家的财政金融机构和企业事业组织的财务收支，进行审计监督。\n\n审计机关在国务院总理领导下，依照法律规定独立行使审计监督权，不受其他行政机关、社会团体和个人的干涉。\n\n第九十二条 国务院对全国人民代表大会负责并报告工作；在全国人民代表大会闭会期间，对全国人民代表大会常务委员会负责并报告工作。\n\n### 第四节 中央军事委员会\n\n第九十三条 中华人民共和国中央军事委员会领导全国武装力量。\n\n中央军事委员会由下列人员组成：\n\n主席，\n\n副主席若干人，\n\n委员若干人。\n\n中央军事委员会实行主席负责制。\n\n中央军事委员会每届任期同全国人民代表大会每届任期相同。\n\n第九十四条 中央军事委员会主席对全国人民代表大会和全国人民代表大会常务委员会负责。\n\n### 第五节 地方各级人民代表大会和地方各级人民政府\n\n第九十五条 省、直辖市、县、市、市辖区、乡、民族乡、镇设立人民代表大会和人民政府。\n\n地方各级人民代表大会和地方各级人民政府的组织由法律规定。\n\n自治区、自治州、自治县设立自治机关。自治机关的组织和工作根据宪法第三章第五节、第六节规定的基本原则由法律规定。\n\n第九十六条 地方各级人民代表大会是地方国家权力机关。\n\n县级以上的地方各级人民代表大会设立常务委员会。', 'context': '该段位于《宪法》第三章“国家机构”第三节“国务院”末尾至第五节“地方各级人民代表大会和地方各级人民政府”开头，列举国务院第（八）至（十八）项职权、部委职责、审计署设置及其对全国人大负责的关系，并衔接过渡到中央军事委员会与地方人大、政府的组织规定。', 'chunk_index': 13, 'char_count': 1177}
2026-05-13 08:57:43,678 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:57:43,678 - bm25_engine - DEBUG - Tokenizing text of length 1177
2026-05-13 08:57:43,679 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:57:43,679 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:57:43,679 - bm25_engine - DEBUG - Document 13: 0 tokens, 0 unique terms
2026-05-13 08:57:43,679 - bm25_engine - DEBUG - Index statistics: 14 documents, 4 unique terms, 12 total terms
2026-05-13 08:57:43,679 - bm25_engine - INFO - Document 13 indexed successfully
2026-05-13 08:57:43,679 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.86
2026-05-13 08:57:43,679 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_13
INFO:     127.0.0.1:51306 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:57,895 - __main__ - INFO - Received index request for document of length 1073
2026-05-13 08:57:57,895 - __main__ - INFO - External doc_id provided: 宪法_chunk_14
2026-05-13 08:57:57,895 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_14' (internal ID 14)
2026-05-13 08:57:57,895 - bm25_engine - INFO - Adding document 14 to index
2026-05-13 08:57:57,895 - bm25_engine - DEBUG - Document text: 地方各级人民代表大会及其常务委员会的组织、选举、任期与职权规定，位于《宪法》第三章“国家机构”第五节“地方各级人民代表大会和地方各级人民政府”。

县级以上的地方各级人民代表大会设立常务委员会。

第...
2026-05-13 08:57:57,896 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 999, 'context_char_count': 72, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '县级以上的地方各级人民代表大会设立常务委员会。\n\n第九十七条 省、直辖市、设区的市的人民代表大会代表由下一级的人民代表大会选举；县、不设区的市、市辖区、乡、民族乡、镇的人民代表大会代表由选民直接选举。\n\n地方各级人民代表大会代表名额和代表产生办法由法律规定。\n\n第九十八条 地方各级人民代表大会每届任期五年。\n\n第九十九条 地方各级人民代表大会在本行政区域内，保证宪法、法律、行政法规的遵守和执行；依照法律规定的权限，通过和发布决议，审查和决定地方的经济建设、文化建设和公共事业建设的计划。\n\n县级以上的地方各级人民代表大会审查和批准本行政区域内的国民经济和社会发展计划、预算以及它们的执行情况的报告；有权改变或者撤销本级人民代表大会常务委员会不适当的决定。\n\n民族乡的人民代表大会可以依照法律规定的权限采取适合民族特点的具体措施。\n\n第一百条 省、直辖市的人民代表大会和它们的常务委员会，在不同宪法、法律、行政法规相抵触的前提下，可以制定地方性法规，报全国人民代表大会常务委员会备案。\n\n设区的市的人民代表大会和它们的常务委员会，在不同宪法、法律、行政法规和本省、自治区的地方性法规相抵触的前提下，可以依照法律规定制定地方性法规，报本省、自治区人民代表大会常务委员会批准后施行。\n\n第一百零一条 地方各级人民代表大会分别选举并且有权罢免本级人民政府的省长和副省长、市长和副市长、县长和副县长、区长和副区长、乡长和副乡长、镇长和副镇长。\n\n县级以上的地方各级人民代表大会选举并且有权罢免本级监察委员会主任、本级人民法院院长和本级人民检察院检察长。选出或者罢免人民检察院检察长，须报上级人民检察院检察长提请该级人民代表大会常务委员会批准。\n\n第一百零二条 省、直辖市、设区的市的人民代表大会代表受原选举单位的监督；县、不设区的市、市辖区、乡、民族乡、镇的人民代表大会代表受选民的监督。\n\n地方各级人民代表大会代表的选举单位和选民有权依照法律规定的程序罢免由他们选出的代表。\n\n第一百零三条 县级以上的地方各级人民代表大会常务委员会由主任、副主任若干人和委员若干人组成，对本级人民代表大会负责并报告工作。\n\n县级以上的地方各级人民代表大会选举并有权罢免本级人民代表大会常务委员会的组成人员。\n\n县级以上的地方各级人民代表大会常务委员会的组成人员不得担任国家行政机关、监察机关、审判机关和检察机关的职务。', 'context': '地方各级人民代表大会及其常务委员会的组织、选举、任期与职权规定，位于《宪法》第三章“国家机构”第五节“地方各级人民代表大会和地方各级人民政府”。', 'chunk_index': 14, 'char_count': 1073}
2026-05-13 08:57:57,896 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:57:57,896 - bm25_engine - DEBUG - Tokenizing text of length 1073
2026-05-13 08:57:57,896 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:57:57,897 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:57:57,897 - bm25_engine - DEBUG - Document 14: 0 tokens, 0 unique terms
2026-05-13 08:57:57,897 - bm25_engine - DEBUG - Index statistics: 15 documents, 4 unique terms, 12 total terms
2026-05-13 08:57:57,897 - bm25_engine - INFO - Document 14 indexed successfully
2026-05-13 08:57:57,897 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.80
2026-05-13 08:57:57,897 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_14
INFO:     127.0.0.1:51319 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:14,743 - __main__ - INFO - Received index request for document of length 1172
2026-05-13 08:58:14,743 - __main__ - INFO - External doc_id provided: 宪法_chunk_15
2026-05-13 08:58:14,743 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_15' (internal ID 15)
2026-05-13 08:58:14,743 - bm25_engine - INFO - Adding document 15 to index
2026-05-13 08:58:14,743 - bm25_engine - DEBUG - Document text: 地方国家机构设置与职权划分：在宪法“国家机构”章第五节“地方各级人民代表大会和地方各级人民政府”中，规定县级以上人大常委会组成人员不得兼任行政、监察、审判、检察机关职务，并列举常委会重大事项决定权、监...
2026-05-13 08:58:14,743 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1035, 'context_char_count': 135, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '县级以上的地方各级人民代表大会常务委员会的组成人员不得担任国家行政机关、监察机关、审判机关和检察机关的职务。\n\n第一百零四条 县级以上的地方各级人民代表大会常务委员会讨论、决定本行政区域内各方面工作的重大事项；监督本级人民政府、监察委员会、人民法院和人民检察院的工作；撤销本级人民政府的不适当的决定和命令；撤销下一级人民代表大会的不适当的决议；依照法律规定的权限决定国家机关工作人员的任免；在本级人民代表大会闭会期间，罢免和补选上一级人民代表大会的个别代表。\n\n第一百零五条 地方各级人民政府是地方各级国家权力机关的执行机关，是地方各级国家行政机关。\n\n地方各级人民政府实行省长、市长、县长、区长、乡长、镇长负责制。\n\n第一百零六条 地方各级人民政府每届任期同本级人民代表大会每届任期相同。\n\n第一百零七条 县级以上地方各级人民政府依照法律规定的权限，管理本行政区域内的经济、教育、科学、文化、卫生、体育事业、城乡建设事业和财政、民政、公安、民族事务、司法行政、计划生育等行政工作，发布决定和命令，任免、培训、考核和奖惩行政工作人员。\n\n乡、民族乡、镇的人民政府执行本级人民代表大会的决议和上级国家行政机关的决定和命令，管理本行政区域内的行政工作。\n\n省、直辖市的人民政府决定乡、民族乡、镇的建置和区域划分。\n\n第一百零八条 县级以上的地方各级人民政府领导所属各工作部门和下级人民政府的工作，有权改变或者撤销所属各工作部门和下级人民政府的不适当的决定。\n\n第一百零九条 县级以上的地方各级人民政府设立审计机关。地方各级审计机关依照法律规定独立行使审计监督权，对本级人民政府和上一级审计机关负责。\n\n第一百一十条 地方各级人民政府对本级人民代表大会负责并报告工作。县级以上的地方各级人民政府在本级人民代表大会闭会期间，对本级人民代表大会常务委员会负责并报告工作。\n\n地方各级人民政府对上一级国家行政机关负责并报告工作。全国地方各级人民政府都是国务院统一领导下的国家行政机关，都服从国务院。\n\n第一百一十一条 城市和农村按居民居住地区设立的居民委员会或者村民委员会是基层群众性自治组织。居民委员会、村民委员会的主任、副主任和委员由居民选举。居民委员会、村民委员会同基层政权的相互关系由法律规定。\n\n居民委员会、村民委员会设人民调解、治安保卫、公共卫生等委员会，办理本居住地区的公共事务和公益事业，调解民间纠纷，协助维护社会治安，并且向人民政府反映群众的意见、要求和提出建议。', 'context': '地方国家机构设置与职权划分：在宪法“国家机构”章第五节“地方各级人民代表大会和地方各级人民政府”中，规定县级以上人大常委会组成人员不得兼任行政、监察、审判、检察机关职务，并列举常委会重大事项决定权、监督权及政府执行机关地位、任期、职权、审计设置与基层群众自治组织等内容。', 'chunk_index': 15, 'char_count': 1172}
2026-05-13 08:58:14,744 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:58:14,744 - bm25_engine - DEBUG - Tokenizing text of length 1172
2026-05-13 08:58:14,744 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:58:14,744 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:58:14,744 - bm25_engine - DEBUG - Document 15: 0 tokens, 0 unique terms
2026-05-13 08:58:14,745 - bm25_engine - DEBUG - Index statistics: 16 documents, 4 unique terms, 12 total terms
2026-05-13 08:58:14,745 - bm25_engine - INFO - Document 15 indexed successfully
2026-05-13 08:58:14,745 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.75
2026-05-13 08:58:14,745 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_15
INFO:     127.0.0.1:51334 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:28,487 - __main__ - INFO - Received index request for document of length 1075
2026-05-13 08:58:28,487 - __main__ - INFO - External doc_id provided: 宪法_chunk_16
2026-05-13 08:58:28,487 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_16' (internal ID 16)
2026-05-13 08:58:28,488 - bm25_engine - INFO - Adding document 16 to index
2026-05-13 08:58:28,488 - bm25_engine - DEBUG - Document text: 基层群众自治组织（居民/村民委员会）职责与民族区域自治制度衔接条款

居民委员会、村民委员会设人民调解、治安保卫、公共卫生等委员会，办理本居住地区的公共事务和公益事业，调解民间纠纷，协助维护社会治安，...
2026-05-13 08:58:28,488 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1040, 'context_char_count': 33, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '居民委员会、村民委员会设人民调解、治安保卫、公共卫生等委员会，办理本居住地区的公共事务和公益事业，调解民间纠纷，协助维护社会治安，并且向人民政府反映群众的意见、要求和提出建议。\n\n### 第六节 民族自治地方的自治机关\n\n第一百一十二条 民族自治地方的自治机关是自治区、自治州、自治县的人民代表大会和人民政府。\n\n第一百一十三条 自治区、自治州、自治县的人民代表大会中，除实行区域自治的民族的代表外，其他居住在本行政区域内的民族也应当有适当名额的代表。\n\n自治区、自治州、自治县的人民代表大会常务委员会中应当有实行区域自治的民族的公民担任主任或者副主任。\n\n第一百一十四条 自治区主席、自治州州长、自治县县长由实行区域自治的民族的公民担任。\n\n第一百一十五条 自治区、自治州、自治县的自治机关行使宪法第三章第五节规定的地方国家机关的职权，同时依照宪法、民族区域自治法和其他法律规定的权限行使自治权，根据本地方实际情况贯彻执行国家的法律、政策。\n\n第一百一十六条 民族自治地方的人民代表大会有权依照当地民族的政治、经济和文化的特点，制定自治条例和单行条例。自治区的自治条例和单行条例，报全国人民代表大会常务委员会批准后生效。自治州、自治县的自治条例和单行条例，报省或者自治区的人民代表大会常务委员会批准后生效，并报全国人民代表大会常务委员会备案。\n\n第一百一十七条 民族自治地方的自治机关有管理地方财政的自治权。凡是依照国家财政体制属于民族自治地方的财政收入，都应当由民族自治地方的自治机关自主地安排使用。\n\n第一百一十八条 民族自治地方的自治机关在国家计划的指导下，自主地安排和管理地方性的经济建设事业。\n\n国家在民族自治地方开发资源、建设企业的时候，应当照顾民族自治地方的利益。\n\n第一百一十九条 民族自治地方的自治机关自主地管理本地方的教育、科学、文化、卫生、体育事业，保护和整理民族的文化遗产，发展和繁荣民族文化。\n\n第一百二十条 民族自治地方的自治机关依照国家的军事制度和当地的实际需要，经国务院批准，可以组织本地方维护社会治安的公安部队。\n\n第一百二十一条 民族自治地方的自治机关在执行职务的时候，依照本民族自治地方自治条例的规定，使用当地通用的一种或者几种语言文字。\n\n第一百二十二条 国家从财政、物资、技术等方面帮助各少数民族加速发展经济建设和文化建设事业。\n\n国家帮助民族自治地方从当地民族中大量培养各级干部、各种专业人才和技术工人。\n\n### 第七节 监察委员会', 'context': '基层群众自治组织（居民/村民委员会）职责与民族区域自治制度衔接条款', 'chunk_index': 16, 'char_count': 1075}
2026-05-13 08:58:28,488 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:58:28,488 - bm25_engine - DEBUG - Tokenizing text of length 1075
2026-05-13 08:58:28,489 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:58:28,489 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:58:28,489 - bm25_engine - DEBUG - Document 16: 0 tokens, 0 unique terms
2026-05-13 08:58:28,489 - bm25_engine - DEBUG - Index statistics: 17 documents, 4 unique terms, 12 total terms
2026-05-13 08:58:28,489 - bm25_engine - INFO - Document 16 indexed successfully
2026-05-13 08:58:28,489 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.71
2026-05-13 08:58:28,490 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_16
INFO:     127.0.0.1:51367 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:42,676 - __main__ - INFO - Received index request for document of length 1093
2026-05-13 08:58:42,677 - __main__ - INFO - External doc_id provided: 宪法_chunk_17
2026-05-13 08:58:42,677 - bm25_engine - INFO - Indexing document with external ID '宪法_chunk_17' (internal ID 17)
2026-05-13 08:58:42,677 - bm25_engine - INFO - Adding document 17 to index
2026-05-13 08:58:42,677 - bm25_engine - DEBUG - Document text: 第三章“国家机构”第八节、第九节，分别规定国家的监察、审判与法律监督机关的组织、任期、职权及其与人大之间的负责关系。

### 第七节 监察委员会

第一百二十三条 中华人民共和国各级监察委员会是国家...
2026-05-13 08:58:42,677 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1033, 'context_char_count': 58, 'category': '1-宪法', 'doc_title': '宪法', 'original_text': '### 第七节 监察委员会\n\n第一百二十三条 中华人民共和国各级监察委员会是国家的监察机关。\n\n第一百二十四条 中华人民共和国设立国家监察委员会和地方各级监察委员会。\n\n监察委员会由下列人员组成：\n\n主任，\n\n副主任若干人，\n\n委员若干人。\n\n监察委员会主任每届任期同本级人民代表大会每届任期相同。国家监察委员会主任连续任职不得超过两届。\n\n监察委员会的组织和职权由法律规定。\n\n第一百二十五条 中华人民共和国国家监察委员会是最高监察机关。\n\n国家监察委员会领导地方各级监察委员会的工作，上级监察委员会领导下级监察委员会的工作。\n\n第一百二十六条 国家监察委员会对全国人民代表大会和全国人民代表大会常务委员会负责。地方各级监察委员会对产生它的国家权力机关和上一级监察委员会负责。\n\n第一百二十七条 监察委员会依照法律规定独立行使监察权，不受行政机关、社会团体和个人的干涉。\n\n监察机关办理职务违法和职务犯罪案件，应当与审判机关、检察机关、执法部门互相配合，互相制约。\n\n### 第八节 人民法院和人民检察院\n\n第一百二十八条 中华人民共和国人民法院是国家的审判机关。\n\n第一百二十九条 中华人民共和国设立最高人民法院、地方各级人民法院和军事法院等专门人民法院。\n\n最高人民法院院长每届任期同全国人民代表大会每届任期相同，连续任职不得超过两届。\n\n人民法院的组织由法律规定。\n\n第一百三十条 人民法院审理案件，除法律规定的特别情况外，一律公开进行。被告人有权获得辩护。\n\n第一百三十一条 人民法院依照法律规定独立行使审判权，不受行政机关、社会团体和个人的干涉。\n\n第一百三十二条 最高人民法院是最高审判机关。\n\n最高人民法院监督地方各级人民法院和专门人民法院的审判工作，上级人民法院监督下级人民法院的审判工作。\n\n第一百三十三条 最高人民法院对全国人民代表大会和全国人民代表大会常务委员会负责。地方各级人民法院对产生它的国家权力机关负责。\n\n第一百三十四条 中华人民共和国人民检察院是国家的法律监督机关。\n\n第一百三十五条 中华人民共和国设立最高人民检察院、地方各级人民检察院和军事检察院等专门人民检察院。\n\n最高人民检察院检察长每届任期同全国人民代表大会每届任期相同，连续任职不得超过两届。\n\n人民检察院的组织由法律规定。\n\n第一百三十六条 人民检察院依照法律规定独立行使检察权，不受行政机关、社会团体和个人的干涉。\n\n第一百三十七条 最高人民检察院是最高检察机关。', 'context': '第三章“国家机构”第八节、第九节，分别规定国家的监察、审判与法律监督机关的组织、任期、职权及其与人大之间的负责关系。', 'chunk_index': 17, 'char_count': 1093}
2026-05-13 08:58:42,677 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:58:42,678 - bm25_engine - DEBUG - Tokenizing text of length 1093
2026-05-13 08:58:42,678 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:58:42,678 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:58:42,678 - bm25_engine - DEBUG - Document 17: 0 tokens, 0 unique terms
2026-05-13 08:58:42,678 - bm25_engine - DEBUG - Index statistics: 18 documents, 4 unique terms, 12 total terms
2026-05-13 08:58:42,679 - bm25_engine - INFO - Document 17 indexed successfully
2026-05-13 08:58:42,679 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.67
2026-05-13 08:58:42,679 - __main__ - INFO - Document indexed successfully with ID 宪法_chunk_17
INFO:     127.0.0.1:51389 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:56,429 - __main__ - INFO - Received index request for document of length 1110
2026-05-13 08:58:56,429 - __main__ - INFO - External doc_id provided: 专属经济区和大陆架法_1998_06_26_chunk_0
2026-05-13 08:58:56,429 - bm25_engine - INFO - Indexing document with external ID '专属经济区和大陆架法_1998_06_26_chunk_0' (internal ID 18)
2026-05-13 08:58:56,429 - bm25_engine - INFO - Adding document 18 to index
2026-05-13 08:58:56,429 - bm25_engine - DEBUG - Document text: 本法开篇界定专属经济区与大陆架的法定范围及中国在其中的主权权利、管辖权，并确立对外国渔业、资源勘查、科研等活动的审批与管理框架，为后续条款奠定权利基础与适用范围。

# 中华人民共和国专属经济区和大陆...
2026-05-13 08:58:56,430 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 1027, 'context_char_count': 81, 'category': '2-宪法相关法', 'doc_title': '专属经济区和大陆架法（1998-06-26）', 'original_text': '# 中华人民共和国专属经济区和大陆架法\n\n1998年6月26日 第九届全国人民代表大会常务委员会第三次会议通过\n\n<!-- INFO END -->\n\n第一条 为保障中华人民共和国对专属经济区和大陆架行使主权权利和管辖权，维护国家海洋权益，制定本法。\n\n第二条 中华人民共和国的专属经济区，为中华人民共和国领海以外并邻接领海的区域，从测算领海宽度的基线量起延至二百海里。\n\n中华人民共和国的大陆架，为中华人民共和国领海以外依本国陆地领土的全部自然延伸，扩展到大陆边外缘的海底区域的海床和底土；如果从测算领海宽度的基线量起至大陆边外缘的距离不足二百海里，则扩展至二百海里。\n\n中华人民共和国与海岸相邻或者相向国家关于专属经济区和大陆架的主张重叠的，在国际法的基础上按照公平原则以协议划定界限。\n\n第三条 中华人民共和国在专属经济区为勘查、开发、养护和管理海床上覆水域、海床及其底土的自然资源，以及进行其他经济性开发和勘查，如利用海水、海流和风力生产能等活动，行使主权权利。\n\n中华人民共和国对专属经济区的人工岛屿、设施和结构的建造、使用和海洋科学研究、海洋环境的保护和保全，行使管辖权。\n\n本法所称专属经济区的自然资源，包括生物资源和非生物资源。\n\n第四条 中华人民共和国为勘查大陆架和开发大陆架的自然资源，对大陆架行使主权权利。\n\n中华人民共和国对大陆架的人工岛屿、设施和结构的建造、使用和海洋科学研究、海洋环境的保护和保全，行使管辖权。\n\n中华人民共和国拥有授权和管理为一切目的在大陆架上进行钻探的专属权利。\n\n本法所称大陆架的自然资源，包括海床和底土的矿物和其他非生物资源，以及属于定居种的生物，即在可捕捞阶段在海床上或者海床下不能移动或者其躯体须与海床或者底土保持接触才能移动的生物。\n\n第五条 任何国际组织、外国的组织或者个人进入中华人民共和国的专属经济区从事渔业活动，必须经中华人民共和国主管机关批准，并遵守中华人民共和国的法律、法规及中华人民共和国与有关国家签订的条约、协定。\n\n中华人民共和国主管机关有权采取各种必要的养护和管理措施，确保专属经济区的生物资源不受过度开发的危害。\n\n第六条 中华人民共和国主管机关有权对专属经济区的跨界种群、高度洄游鱼种、海洋哺乳动物、源自中华人民共和国河流的溯河产卵种群、在中华人民共和国水域内度过大部分生命周期的降河产卵鱼种，进行养护和管理。\n\n中华人民共和国对源自本国河流的溯河产卵种群，享有主要利益。', 'context': '本法开篇界定专属经济区与大陆架的法定范围及中国在其中的主权权利、管辖权，并确立对外国渔业、资源勘查、科研等活动的审批与管理框架，为后续条款奠定权利基础与适用范围。', 'chunk_index': 0, 'char_count': 1110}
2026-05-13 08:58:56,430 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:58:56,430 - bm25_engine - DEBUG - Tokenizing text of length 1110
2026-05-13 08:58:56,430 - bm25_engine - DEBUG - Found 2 raw tokens
2026-05-13 08:58:56,431 - bm25_engine - DEBUG - After removing stop words: 2 tokens
2026-05-13 08:58:56,431 - bm25_engine - DEBUG - Document 18: 2 tokens, 2 unique terms
2026-05-13 08:58:56,431 - bm25_engine - DEBUG - Index statistics: 19 documents, 4 unique terms, 14 total terms
2026-05-13 08:58:56,431 - bm25_engine - INFO - Document 18 indexed successfully
2026-05-13 08:58:56,431 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.74
2026-05-13 08:58:56,431 - __main__ - INFO - Document indexed successfully with ID 专属经济区和大陆架法_1998_06_26_chunk_0
INFO:     127.0.0.1:60423 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:59:15,068 - __main__ - INFO - Received index request for document of length 1115
2026-05-13 08:59:15,068 - __main__ - INFO - External doc_id provided: 专属经济区和大陆架法_1998_06_26_chunk_1
2026-05-13 08:59:15,068 - bm25_engine - INFO - Indexing document with external ID '专属经济区和大陆架法_1998_06_26_chunk_1' (internal ID 19)
2026-05-13 08:59:15,068 - bm25_engine - INFO - Adding document 19 to index
2026-05-13 08:59:15,068 - bm25_engine - DEBUG - Document text: 本段位于《中华人民共和国专属经济区和大陆架法》第六条至第十六条，集中规定了中国对专属经济区和大陆架生物资源（特别是溯河产卵种群）的主权利益、对外国勘查开发及科研活动的审批权、人工岛屿与设施的专属建造管...
2026-05-13 08:59:15,068 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 942, 'context_char_count': 171, 'category': '2-宪法相关法', 'doc_title': '专属经济区和大陆架法（1998-06-26）', 'original_text': '中华人民共和国对源自本国河流的溯河产卵种群，享有主要利益。\n\n第七条 任何国际组织、外国的组织或者个人对中华人民共和国的专属经济区和大陆架的自然资源进行勘查、开发活动或者在中华人民共和国的大陆架上为任何目的进行钻探，必须经中华人民共和国主管机关批准，并遵守中华人民共和国的法律、法规。\n\n第八条 中华人民共和国在专属经济区和大陆架有专属权利建造并授权和管理建造、操作和使用人工岛屿、设施和结构。\n\n中华人民共和国对专属经济区和大陆架的人工岛屿、设施和结构行使专属管辖权，包括有关海关、财政、卫生、安全和出境入境的法律和法规方面的管辖权。\n\n中华人民共和国主管机关有权在专属经济区和大陆架的人工岛屿、设施和结构周围设置安全地带，并可以在该地带采取适当措施，确保航行安全以及人工岛屿、设施和结构的安全。\n\n第九条 任何国际组织、外国的组织或者个人在中华人民共和国的专属经济区和大陆架进行海洋科学研究，必须经中华人民共和国主管机关批准，并遵守中华人民共和国的法律、法规。\n\n第十条 中华人民共和国主管机关有权采取必要的措施，防止、减少和控制海洋环境的污染，保护和保全专属经济区和大陆架的海洋环境。\n\n第十一条 任何国家在遵守国际法和中华人民共和国的法律、法规的前提下，在中华人民共和国的专属经济区享有航行、飞越的自由，在中华人民共和国的专属经济区和大陆架享有铺设海底电缆和管道的自由，以及与上述自由有关的其他合法使用海洋的便利。铺设海底电缆和管道的路线，必须经中华人民共和国主管机关同意。\n\n第十二条 中华人民共和国在行使勘查、开发、养护和管理专属经济区的生物资源的主权权利时，为确保中华人民共和国的法律、法规得到遵守，可以采取登临、检查、逮捕、扣留和进行司法程序等必要的措施。\n\n中华人民共和国对在专属经济区和大陆架违反中华人民共和国法律、法规的行为，有权采取必要措施、依法追究法律责任，并可以行使紧追权。\n\n第十三条 中华人民共和国在专属经济区和大陆架享有的权利，本法未作规定的，根据国际法和中华人民共和国其他有关法律、法规行使。\n\n第十四条 本法的规定不影响中华人民共和国享有的历史性权利。\n\n第十五条 中华人民共和国政府可以根据本法制定有关规定。\n\n第十六条 本法自公布之日起施行。', 'context': '本段位于《中华人民共和国专属经济区和大陆架法》第六条至第十六条，集中规定了中国对专属经济区和大陆架生物资源（特别是溯河产卵种群）的主权利益、对外国勘查开发及科研活动的审批权、人工岛屿与设施的专属建造管辖权、海洋环保措施、航行与电缆管道自由、执法手段（登临、检查、逮捕、紧追权）以及历史性权利的保留，是对国家海洋权益具体行使和管控的核心条款群。', 'chunk_index': 1, 'char_count': 1115}
2026-05-13 08:59:15,069 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:59:15,069 - bm25_engine - DEBUG - Tokenizing text of length 1115
2026-05-13 08:59:15,069 - bm25_engine - DEBUG - Found 0 raw tokens
2026-05-13 08:59:15,069 - bm25_engine - DEBUG - After removing stop words: 0 tokens
2026-05-13 08:59:15,069 - bm25_engine - DEBUG - Document 19: 0 tokens, 0 unique terms
2026-05-13 08:59:15,070 - bm25_engine - DEBUG - Index statistics: 20 documents, 4 unique terms, 14 total terms
2026-05-13 08:59:15,070 - bm25_engine - INFO - Document 19 indexed successfully
2026-05-13 08:59:15,070 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.70
2026-05-13 08:59:15,070 - __main__ - INFO - Document indexed successfully with ID 专属经济区和大陆架法_1998_06_26_chunk_1
INFO:     127.0.0.1:63325 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:59:30,474 - __main__ - INFO - Received index request for document of length 1071
2026-05-13 08:59:30,474 - __main__ - INFO - External doc_id provided: 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法_2021_04_29_chunk_0
2026-05-13 08:59:30,474 - bm25_engine - INFO - Indexing document with external ID '中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法_2021_04_29_chunk_0' (internal ID 20)
2026-05-13 08:59:30,474 - bm25_engine - INFO - Adding document 20 to index
2026-05-13 08:59:30,474 - bm25_engine - DEBUG - Document text: 位于《中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法》全文之首，涵盖立法沿革、总则及选举委员会设立与领导体制，为后续各章选举程序、代表名额、选区划分、候选人提出、投票选举、...
2026-05-13 08:59:30,475 - bm25_engine - DEBUG - Document metadata: {'contextual': True, 'original_char_count': 948, 'context_char_count': 121, 'category': '2-宪法相关法', 'doc_title': '中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法（2021-04-29）', 'original_text': '# 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法\n\n1981年6月10日 第五届全国人民代表大会常务委员会第十九次会议通过\n\n1996年10月29日 第八届全国人民代表大会常务委员会第二十二次会议修订\n\n2012年6月30日 第十一届全国人民代表大会常务委员会第二十七次会议《关于修改〈中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法〉的决定》第一次修正\n\n2021年4月29日 第十三届全国人民代表大会常务委员会第二十八次会议《关于修改〈中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法〉的决定》第二次修正\n\n<!-- INFO END -->\n\n## 第一章\u3000总\u3000则\n\n第一条 根据《中华人民共和国宪法》和《中华人民共和国全国人民代表大会和地方各级人民代表大会选举法》的有关规定，制定本办法。\n\n第二条 人民解放军军人和参加军队选举的其他人员依照本办法选举全国人民代表大会和县级以上地方各级人民代表大会代表。\n\n第三条 人民解放军及人民解放军团级以上单位设立选举委员会。\n\n人民解放军选举委员会领导全军的选举工作，其他各级选举委员会主持本单位的选举工作。\n\n第四条 连和其他基层单位的军人委员会，主持本单位的选举工作。\n\n第五条 人民解放军军人、文职人员，军队管理的离休、退休人员和其他人员，参加军队选举。\n\n驻军的驻地距离当地居民的居住地较远，随军家属参加地方选举有困难的，经选举委员会或者军人委员会批准，可以参加军队选举。\n\n第六条 驻地方工厂、铁路、水运、科研等单位的军代表，在地方院校学习的军队人员，可以参加地方选举。\n\n第七条 本办法第五条所列人员，凡年满十八周岁，不分民族、种族、性别、职业、家庭出身、宗教信仰、教育程度、财产状况、居住期限，都具有选民资格，享有选举权和被选举权。\n\n依照法律被剥夺政治权利的人没有选举权和被选举权。\n\n精神病患者不能行使选举权利的，经选举委员会确认，不参加选举。\n\n## 第二章\u3000选举委员会\n\n第八条 人民解放军选举委员会的组成人员，由全国人民代表大会常务委员会批准。其他各级选举委员会的组成人员，由上一级选举委员会批准。\n\n下级选举委员会受上级选举委员会的领导。', 'context': '位于《中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法》全文之首，涵盖立法沿革、总则及选举委员会设立与领导体制，为后续各章选举程序、代表名额、选区划分、候选人提出、投票选举、监督罢免等具体规定确立根本依据与组织框架。', 'chunk_index': 0, 'char_count': 1071}
2026-05-13 08:59:30,475 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-13 08:59:30,475 - bm25_engine - DEBUG - Tokenizing text of length 1071
2026-05-13 08:59:30,475 - bm25_engine - DEBUG - Found 2 raw tokens
2026-05-13 08:59:30,476 - bm25_engine - DEBUG - After removing stop words: 2 tokens
2026-05-13 08:59:30,476 - bm25_engine - DEBUG - Document 20: 2 tokens, 2 unique terms
2026-05-13 08:59:30,476 - bm25_engine - DEBUG - Index statistics: 21 documents, 4 unique terms, 16 total terms
2026-05-13 08:59:30,476 - bm25_engine - INFO - Document 20 indexed successfully
2026-05-13 08:59:30,476 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=0.76
2026-05-13 08:59:30,476 - __main__ - INFO - Document indexed successfully with ID 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法_2021_04_29_chunk_0
INFO:     127.0.0.1:63342 - "POST /index HTTP/1.1" 200 OK
```
## 4242 retrieval-pipeline：python main.py
```
2026-05-13 08:53:07,188 - __main__ - INFO - Starting server on 0.0.0.0:4242
2026-05-13 08:53:07,188 - __main__ - INFO - Dense service: http://localhost:4240
2026-05-13 08:53:07,188 - __main__ - INFO - Sparse service: http://localhost:4241
INFO:     Started server process [14792]
INFO:     Waiting for application startup.
2026-05-13 08:53:07,226 - __main__ - INFO - Starting retrieval pipeline...
2026-05-13 08:53:07,227 - reranker - INFO - Initializing reranker with model: BAAI/bge-reranker-v2-m3
2026-05-13 08:53:07,227 - reranker - INFO - Device: cpu, FP16: False
2026-05-13 08:53:07,228 - reranker - INFO - Model already cached at C:\Users\admin\.cache\huggingface\hub\models--BAAI--bge-reranker-v2-m3
2026-05-13 08:53:07,228 - reranker - INFO - Loading reranker model into memory...
D:\python\Lib\site-packages\huggingface_hub\file_download.py:1142: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
  warnings.warn(
2026-05-13 08:53:14,334 - reranker - INFO - Reranker initialized successfully in 7.11s
2026-05-13 08:53:14,334 - retrieval_pipeline - INFO - Retrieval pipeline initialized
2026-05-13 08:53:14,334 - __main__ - INFO - Pipeline initialized successfully
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:4242 (Press CTRL+C to quit)
2026-05-13 08:54:22,479 - document_store - INFO - Cleared all documents from store
INFO:     127.0.0.1:60929 - "DELETE /clear HTTP/1.1" 200 OK
2026-05-13 08:54:32,189 - __main__ - INFO - Indexing document: 宪法_chunk_0
2026-05-13 08:54:32,191 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_0
2026-05-13 08:54:32,191 - retrieval_client - INFO - Indexing document 宪法_chunk_0 in parallel...
2026-05-13 08:54:32,526 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:54:36,976 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:63031 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:54:45,300 - __main__ - INFO - Indexing document: 宪法_chunk_1
2026-05-13 08:54:45,300 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_1
2026-05-13 08:54:45,301 - retrieval_client - INFO - Indexing document 宪法_chunk_1 in parallel...
2026-05-13 08:54:45,599 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:54:50,126 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:63070 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:01,101 - __main__ - INFO - Indexing document: 宪法_chunk_2
2026-05-13 08:55:01,101 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_2
2026-05-13 08:55:01,101 - retrieval_client - INFO - Indexing document 宪法_chunk_2 in parallel...
2026-05-13 08:55:01,401 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:55:06,520 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:60969 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:15,228 - __main__ - INFO - Indexing document: 宪法_chunk_3
2026-05-13 08:55:15,229 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_3
2026-05-13 08:55:15,229 - retrieval_client - INFO - Indexing document 宪法_chunk_3 in parallel...
2026-05-13 08:55:15,527 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:55:20,566 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:61030 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:30,368 - __main__ - INFO - Indexing document: 宪法_chunk_4
2026-05-13 08:55:30,368 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_4
2026-05-13 08:55:30,368 - retrieval_client - INFO - Indexing document 宪法_chunk_4 in parallel...
2026-05-13 08:55:30,670 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:55:35,389 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:61059 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:55:45,131 - __main__ - INFO - Indexing document: 宪法_chunk_5
2026-05-13 08:55:45,131 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_5
2026-05-13 08:55:45,131 - retrieval_client - INFO - Indexing document 宪法_chunk_5 in parallel...
2026-05-13 08:55:45,400 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:55:50,311 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:61088 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:01,410 - __main__ - INFO - Indexing document: 宪法_chunk_6
2026-05-13 08:56:01,410 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_6
2026-05-13 08:56:01,410 - retrieval_client - INFO - Indexing document 宪法_chunk_6 in parallel...
2026-05-13 08:56:01,690 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:56:07,055 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:49167 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:16,210 - __main__ - INFO - Indexing document: 宪法_chunk_7
2026-05-13 08:56:16,210 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_7
2026-05-13 08:56:16,210 - retrieval_client - INFO - Indexing document 宪法_chunk_7 in parallel...
2026-05-13 08:56:16,494 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:56:21,892 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:49198 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:32,571 - __main__ - INFO - Indexing document: 宪法_chunk_8
2026-05-13 08:56:32,571 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_8
2026-05-13 08:56:32,572 - retrieval_client - INFO - Indexing document 宪法_chunk_8 in parallel...
2026-05-13 08:56:32,873 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:56:37,347 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51203 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:46,038 - __main__ - INFO - Indexing document: 宪法_chunk_9
2026-05-13 08:56:46,039 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_9
2026-05-13 08:56:46,039 - retrieval_client - INFO - Indexing document 宪法_chunk_9 in parallel...
2026-05-13 08:56:46,314 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:56:51,747 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51216 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:56:59,237 - __main__ - INFO - Indexing document: 宪法_chunk_10
2026-05-13 08:56:59,237 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_10
2026-05-13 08:56:59,237 - retrieval_client - INFO - Indexing document 宪法_chunk_10 in parallel...
2026-05-13 08:56:59,522 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:57:04,444 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51230 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:13,481 - __main__ - INFO - Indexing document: 宪法_chunk_11
2026-05-13 08:57:13,481 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_11
2026-05-13 08:57:13,481 - retrieval_client - INFO - Indexing document 宪法_chunk_11 in parallel...
2026-05-13 08:57:13,784 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:57:18,200 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51252 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:26,832 - __main__ - INFO - Indexing document: 宪法_chunk_12
2026-05-13 08:57:26,832 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_12
2026-05-13 08:57:26,832 - retrieval_client - INFO - Indexing document 宪法_chunk_12 in parallel...
2026-05-13 08:57:27,104 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:57:32,830 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51272 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:43,392 - __main__ - INFO - Indexing document: 宪法_chunk_13
2026-05-13 08:57:43,392 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_13
2026-05-13 08:57:43,392 - retrieval_client - INFO - Indexing document 宪法_chunk_13 in parallel...
2026-05-13 08:57:43,680 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:57:49,313 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51302 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:57:57,607 - __main__ - INFO - Indexing document: 宪法_chunk_14
2026-05-13 08:57:57,607 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_14
2026-05-13 08:57:57,607 - retrieval_client - INFO - Indexing document 宪法_chunk_14 in parallel...
2026-05-13 08:57:57,898 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:58:03,059 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51316 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:14,472 - __main__ - INFO - Indexing document: 宪法_chunk_15
2026-05-13 08:58:14,472 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_15
2026-05-13 08:58:14,473 - retrieval_client - INFO - Indexing document 宪法_chunk_15 in parallel...
2026-05-13 08:58:14,746 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:58:20,540 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51330 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:28,183 - __main__ - INFO - Indexing document: 宪法_chunk_16
2026-05-13 08:58:28,183 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_16
2026-05-13 08:58:28,183 - retrieval_client - INFO - Indexing document 宪法_chunk_16 in parallel...
2026-05-13 08:58:28,491 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:58:33,835 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51363 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:42,388 - __main__ - INFO - Indexing document: 宪法_chunk_17
2026-05-13 08:58:42,388 - retrieval_pipeline - INFO - Indexing document 宪法_chunk_17
2026-05-13 08:58:42,388 - retrieval_client - INFO - Indexing document 宪法_chunk_17 in parallel...
2026-05-13 08:58:42,680 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:58:47,708 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:51385 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:58:56,148 - __main__ - INFO - Indexing document: 专属经济区和大陆架法_1998_06_26_chunk_0
2026-05-13 08:58:56,148 - retrieval_pipeline - INFO - Indexing document 专属经济区和大陆架法_1998_06_26_chunk_0
2026-05-13 08:58:56,148 - retrieval_client - INFO - Indexing document 专属经济区和大陆架法_1998_06_26_chunk_0 in parallel...
2026-05-13 08:58:56,432 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:59:02,460 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:60420 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:59:14,783 - __main__ - INFO - Indexing document: 专属经济区和大陆架法_1998_06_26_chunk_1
2026-05-13 08:59:14,783 - retrieval_pipeline - INFO - Indexing document 专属经济区和大陆架法_1998_06_26_chunk_1
2026-05-13 08:59:14,783 - retrieval_client - INFO - Indexing document 专属经济区和大陆架法_1998_06_26_chunk_1 in parallel...
2026-05-13 08:59:15,071 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:59:20,266 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:63321 - "POST /index HTTP/1.1" 200 OK
2026-05-13 08:59:30,194 - __main__ - INFO - Indexing document: 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法_2021_04_29_chunk_0
2026-05-13 08:59:30,194 - retrieval_pipeline - INFO - Indexing document 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法_2021_04_29_chunk_0
2026-05-13 08:59:30,194 - retrieval_client - INFO - Indexing document 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法_2021_04_29_chunk_0 in parallel...
2026-05-13 08:59:30,477 - httpx - INFO - HTTP Request: POST http://localhost:4241/index "HTTP/1.1 200 OK"
2026-05-13 08:59:35,137 - httpx - INFO - HTTP Request: POST http://localhost:4240/index "HTTP/1.1 200 OK"
INFO:     127.0.0.1:63337 - "POST /index HTTP/1.1" 200 OK
```
## contextual-retrieval：python index_local_laws_contextual.py
```
2026-05-13 08:54:20,420 - INFO - Using kimi (kimi-k2-0905-preview) for context generation
2026-05-13 08:54:20,421 - INFO - Initialized ContextualChunker (contextual=True)
2026-05-13 08:54:20,421 - INFO - Initialized contextual indexer for local laws in E:\ai&ai agent\github\ai-agent-book-projects\week3\agentic-rag\laws
2026-05-13 08:54:20,421 - INFO - Pipeline URL: http://localhost:4242
2026-05-13 08:54:20,421 - INFO - Contextual mode: True
2026-05-13 08:54:20,421 - INFO - Cleaning up existing indexes...
2026-05-13 08:54:22,481 - INFO - Cleared retrieval pipeline index
2026-05-13 08:54:22,482 - INFO - Cleanup complete
2026-05-13 08:54:22,482 - INFO - Found category: 1-宪法
2026-05-13 08:54:22,483 - INFO - Found category: 2-宪法相关法
2026-05-13 08:54:22,607 - INFO - Found category: 3-民法典
2026-05-13 08:54:22,608 - INFO - Found category: 3-民法商法
2026-05-13 08:54:22,609 - INFO - Found category: 4-行政法
2026-05-13 08:54:22,625 - INFO - Found category: 5-经济法
2026-05-13 08:54:22,627 - INFO - Found category: 6-社会法
2026-05-13 08:54:22,629 - INFO - Found category: 7-刑法
2026-05-13 08:54:22,629 - INFO - Found category: 8-诉讼与非诉讼程序法
2026-05-13 08:54:22,638 - INFO - Found 288 legal documents
2026-05-13 08:54:22,638 - INFO - Processing 288 documents...
2026-05-13 08:54:22,638 - INFO -
[1/288] Processing: 宪法
2026-05-13 08:54:22,639 - INFO -   Category: 1-宪法
2026-05-13 08:54:22,643 - INFO - Chunking 宪法 with contextual enhancement...
2026-05-13 08:54:22,644 - INFO - Starting chunking for document 宪法
2026-05-13 08:54:22,645 - INFO - Created 18 basic chunks
2026-05-13 08:54:22,645 - INFO - Generating context for chunk 1/18
2026-05-13 08:54:30,116 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:54:30,135 - INFO - Generated context in 7.49s: 宪法开篇：通过及历次修正日期＋历史背景与政权合法性总述，为全文纲领。
2026-05-13 08:54:37,081 - INFO -   → Indexed chunk 1 immediately
2026-05-13 08:54:37,081 - INFO - Generating context for chunk 2/18
2026-05-13 08:54:43,252 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:54:43,252 - INFO - Generated context in 6.17s: 宪法序言中关于国家根本任务、指导思想、统一大业、爱国统一战线与民族关系的集中表述
2026-05-13 08:54:50,498 - INFO -   → Indexed chunk 2 immediately
2026-05-13 08:54:50,498 - INFO - Generating context for chunk 3/18
2026-05-13 08:54:59,079 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:54:59,080 - INFO - Generated context in 8.58s: 该段位于宪法序言末尾与第一章“总纲”开头之间，概括了国家民族政策、对外政策及宪法地位，并紧接引出国家性质、政权组织形式与民族平等原则，是连接宪法序言与总纲的过渡性关键段落。
2026-05-13 08:55:06,525 - INFO -   → Indexed chunk 3 immediately
2026-05-13 08:55:06,525 - INFO - Generating context for chunk 4/18
2026-05-13 08:55:13,191 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:55:13,192 - INFO - Generated context in 6.67s: 总纲中关于民族区域自治、法治国家、基本经济制度及土地与自然资源的宪法条款。
2026-05-13 08:55:20,685 - INFO -   → Indexed chunk 4 immediately
2026-05-13 08:55:20,685 - INFO - Generating context for chunk 5/18
2026-05-13 08:55:28,318 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:55:28,319 - INFO - Generated context in 7.63s: 位于《宪法》第一章“总纲”第十条至第十九条，集中规定土地制度、多种所有制经济、财产保护、国家经济政策、教育文化方针等社会主义基本经济制度与社会发展原则。
2026-05-13 08:55:35,502 - INFO -   → Indexed chunk 5 immediately
2026-05-13 08:55:35,502 - INFO - Generating context for chunk 6/18
2026-05-13 08:55:43,122 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:55:43,122 - INFO - Generated context in 7.62s: 总纲中关于国家发展教育、科学、文化、卫生、体育、语言、人才、精神文明、计划生育、生态环保、国家机关原则、社会秩序、国防建设及行政区划的连续条款群。
2026-05-13 08:55:50,412 - INFO -   → Indexed chunk 6 immediately
2026-05-13 08:55:50,412 - INFO - Generating context for chunk 7/18
2026-05-13 08:55:59,371 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:55:59,372 - INFO - Generated context in 8.96s: 该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的过渡段落。
2026-05-13 08:56:07,060 - INFO -   → Indexed chunk 7 immediately
2026-05-13 08:56:07,060 - INFO - Generating context for chunk 8/18
2026-05-13 08:56:14,188 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:56:14,189 - INFO - Generated context in 7.13s: 第二章“公民的基本权利和义务”中段，集中列举公民在政治、劳动、休息、社会保障、教育、文化、性别平等、婚姻家庭及侨务等方面享有的基本权利与对应国家保障义务。
2026-05-13 08:56:21,931 - INFO -   → Indexed chunk 8 immediately
2026-05-13 08:56:21,932 - INFO - Generating context for chunk 9/18
2026-05-13 08:56:30,551 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:56:30,552 - INFO - Generated context in 8.62s: 该段条文位于《宪法》第二章“公民的基本权利和义务”末尾，紧接其后即进入第三章“国家机构”第一节“全国人民代表大会”，标志从基本权利义务向国家权力机关规定的过渡。
2026-05-13 08:56:37,351 - INFO -   → Indexed chunk 9 immediately
2026-05-13 08:56:37,352 - INFO - Generating context for chunk 10/18
2026-05-13 08:56:44,007 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:56:44,008 - INFO - Generated context in 6.66s: 位于《宪法》第三章“国家机构”第一节“全国人民代表大会”第六十二条至第六十七条，集中规定全国人大及其常委会的职权、人事选举与罢免、宪法修改程序及常委会组成与任期。
2026-05-13 08:56:51,760 - INFO -   → Indexed chunk 10 immediately
2026-05-13 08:56:51,760 - INFO - Progress: 10/18 chunks, avg time: 7.55s
2026-05-13 08:56:51,760 - INFO - Generating context for chunk 11/18
2026-05-13 08:56:57,209 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:56:57,210 - INFO - Generated context in 5.45s: 第六十七条 全国人民代表大会常务委员会行使下列职权：
2026-05-13 08:57:04,451 - INFO -   → Indexed chunk 11 immediately
2026-05-13 08:57:04,451 - INFO - Generating context for chunk 12/18
2026-05-13 08:57:11,431 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:57:11,432 - INFO - Generated context in 6.98s: 位于《宪法》第三章“国家机构”第一节“全国人民代表大会”末尾，衔接第二节“中华人民共和国主席”，规定全国人大及其常委会的组织运作、代表权利义务及与主席的职权交接。
2026-05-13 08:57:18,278 - INFO -   → Indexed chunk 12 immediately
2026-05-13 08:57:18,279 - INFO - Generating context for chunk 13/18
2026-05-13 08:57:24,807 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:57:24,807 - INFO - Generated context in 6.53s: 国家主席、副主席的职权与国务院的组成、任期及行政权——位于《宪法》第三章“国家机构”第二节与第三节之间，衔接元首制度与最高行政机关。
2026-05-13 08:57:32,846 - INFO -   → Indexed chunk 13 immediately
2026-05-13 08:57:32,846 - INFO - Generating context for chunk 14/18
2026-05-13 08:57:41,360 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:57:41,361 - INFO - Generated context in 8.52s: 该段位于《宪法》第三章“国家机构”第三节“国务院”末尾至第五节“地方各级人民代表大会和地方各级人民政府”开头，列举国务院第（八）至（十八）项职权、部委职责、审计署设置及其对全国人大负责的关系，并衔接过渡到中央军事委员会与地方人大、政府的组织规定。
2026-05-13 08:57:49,337 - INFO -   → Indexed chunk 14 immediately
2026-05-13 08:57:49,337 - INFO - Generating context for chunk 15/18
2026-05-13 08:57:55,576 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:57:55,577 - INFO - Generated context in 6.24s: 地方各级人民代表大会及其常务委员会的组织、选举、任期与职权规定，位于《宪法》第三章“国家机构”第五节“地方各级人民代表大会和地方各级人民政府”。
2026-05-13 08:58:03,085 - INFO -   → Indexed chunk 15 immediately
2026-05-13 08:58:03,085 - INFO - Generating context for chunk 16/18
2026-05-13 08:58:12,436 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:58:12,437 - INFO - Generated context in 9.35s: 地方国家机构设置与职权划分：在宪法“国家机构”章第五节“地方各级人民代表大会和地方各级人民政府”中，规定县级以上人大常委会组成人员不得兼任行政、监察、审判、检察机关职务，并列举常委会重大事项决定权、监督权及政府执行机关地位、任期、职权、审计设置与基层群众自治组织等内容。
2026-05-13 08:58:20,546 - INFO -   → Indexed chunk 16 immediately
2026-05-13 08:58:20,547 - INFO - Generating context for chunk 17/18
2026-05-13 08:58:26,159 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:58:26,160 - INFO - Generated context in 5.61s: 基层群众自治组织（居民/村民委员会）职责与民族区域自治制度衔接条款
2026-05-13 08:58:33,842 - INFO -   → Indexed chunk 17 immediately
2026-05-13 08:58:33,843 - INFO - Generating context for chunk 18/18
2026-05-13 08:58:40,358 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:58:40,359 - INFO - Generated context in 6.52s: 第三章“国家机构”第八节、第九节，分别规定国家的监察、审判与法律监督机关的组织、任期、职权及其与人大之间的负责关系。
2026-05-13 08:58:47,748 - INFO -   → Indexed chunk 18 immediately
2026-05-13 08:58:47,748 - INFO - Chunking completed in 265.10s
2026-05-13 08:58:47,748 - INFO - Statistics: {
  "total_chunks": 18,
  "contextual_chunks": 18,
  "total_context_tokens": 12166,
  "total_generation_time": 130.7198781967163,
  "cache_hits": 0,
  "cache_misses": 18
}
2026-05-13 08:58:47,748 - INFO -   ✓ Created and indexed 18 chunks (18 with context)
2026-05-13 08:58:47,753 - INFO -
[2/288] Processing: 专属经济区和大陆架法（1998-06-26）
2026-05-13 08:58:47,753 - INFO -   Category: 2-宪法相关法
2026-05-13 08:58:47,778 - INFO - Chunking 专属经济区和大陆架法（1998-06-26） with contextual enhancement...
2026-05-13 08:58:47,778 - INFO - Starting chunking for document 专属经济区和大陆架法_1998_06_26
2026-05-13 08:58:47,779 - INFO - Created 2 basic chunks
2026-05-13 08:58:47,779 - INFO - Generating context for chunk 1/2
2026-05-13 08:58:54,114 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:58:54,115 - INFO - Generated context in 6.34s: 本法开篇界定专属经济区与大陆架的法定范围及中国在其中的主权权利、管辖权，并确立对外国渔业、资源勘查、科研等活动的审批与管理框架，为后续条款奠定权利基础与适用范围。
2026-05-13 08:59:02,466 - INFO -   → Indexed chunk 1 immediately
2026-05-13 08:59:02,467 - INFO - Generating context for chunk 2/2
2026-05-13 08:59:12,740 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:59:12,740 - INFO - Generated context in 10.27s: 本段位于《中华人民共和国专属经济区和大陆架法》第六条至第十六条，集中规定了中国对专属经济区和大陆架生物资源（特别是溯河产卵种群）的主权利益、对外国勘查开发及科研活动的审批权、人工岛屿与设施的专属建造管辖权、海洋环保措施、航行与电缆管道自由、执法手段（登临、检查、逮捕、紧追权）以及历史性权利的保留，是对国家海洋权益具体行使和管控的核心条款群。
2026-05-13 08:59:20,277 - INFO -   → Indexed chunk 2 immediately
2026-05-13 08:59:20,277 - INFO - Chunking completed in 32.50s
2026-05-13 08:59:20,278 - INFO - Statistics: {
  "total_chunks": 20,
  "contextual_chunks": 20,
  "total_context_tokens": 12441,
  "total_generation_time": 147.32955765724182,
  "cache_hits": 0,
  "cache_misses": 20
}
2026-05-13 08:59:20,278 - INFO -   ✓ Created and indexed 2 chunks (2 with context)
2026-05-13 08:59:20,282 - INFO -
[3/288] Processing: 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法（2021-04-29）
2026-05-13 08:59:20,283 - INFO -   Category: 2-宪法相关法
2026-05-13 08:59:20,298 - INFO - Chunking 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法（2021-04-29） with contextual enhancement...
2026-05-13 08:59:20,299 - INFO - Starting chunking for document 中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法_2021_04_29
2026-05-13 08:59:20,299 - INFO - Created 6 basic chunks
2026-05-13 08:59:20,299 - INFO - Generating context for chunk 1/6
2026-05-13 08:59:28,154 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:59:28,155 - INFO - Generated context in 7.86s: 位于《中国人民解放军选举全国人民代表大会和县级以上地方各级人民代表大会代表的办法》全文之首，涵盖立法沿革、总则及选举委员会设立与领导体制，为后续各章选举程序、代表名额、选区划分、候选人提出、投票选举、监督罢免等具体规定确立根本依据与组织框架。
2026-05-13 08:59:35,143 - INFO -   → Indexed chunk 1 immediately
2026-05-13 08:59:35,143 - INFO - Generating context for chunk 2/6
2026-05-13 08:59:39,355 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 08:59:39,356 - INFO - Generated context in 4.21s: 第二章　选举委员会
```
## contextual-retrieval：main.py
```
2026-05-13 09:12:00,604 - INFO - Using model: kimi-k2-0905-preview
2026-05-13 09:12:00,605 - INFO - Initialized AgenticRAG with provider: kimi

============================================================
Agentic RAG System - Agentic Mode
Verbose: Enabled | Top-K: 3
============================================================
Type 'quit' or 'exit' to stop
Type 'clear' to clear conversation history
Type 'mode' to switch between agentic/non-agentic modes
============================================================


[USER] > 宪法第四条是什么？

[ASSISTANT (agentic)] > 2026-05-13 09:12:12,927 - INFO - Iteration 1/10
2026-05-13 09:12:19,062 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 09:12:19,079 - INFO - Executing tool: knowledge_base_search with args: {'query': '中华人民共和国宪法 第四条'}
2026-05-13 09:12:19,080 - INFO - Knowledge base search initiated - Type: KnowledgeBaseType.LOCAL, Query: '中华人民共和国宪法 第四条'
2026-05-13 09:12:19,080 - INFO - Searching local knowledge base for: 中华人民共和国宪法 第四条
2026-05-13 09:12:38,137 - INFO - Local search returned 3 results for query: 中华人民共和国宪法 第四条
2026-05-13 09:12:38,138 - INFO - Tool result: {
  "status": "success",
  "results": [
    {
      "doc_id": "宪法_chunk_7",
      "chunk_id": "宪法_chunk_7",
      "text": "第二章“公民的基本权利和义务”中段，集中列举公民在政治、劳动、休息、社会保障、教育、文化、性别平等、婚姻家庭及侨务等方面享有的基本权利与对应国家保障义务。\n\n第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。\n\n对于公民的申诉、控告或者检举，有关国家机关必须查清事实，负责处理。任何人不得压制和打击报复。\n\n由于国家机关和国家工作人员侵犯公民权利而受到损失的人，有依照法律规定取得赔偿的权利。\n\n第四十二条 中华人民共和国公民有劳动的权利和义务。\n\n国家通过各种途径，创造劳动就业条件，加强劳动保护，改善劳动条件，并在发展生产的基础上，提高劳动报酬和福利待遇。\n\n劳动是一切有劳动能力的公民的光荣职责。国有企业和城乡集体经济组织的劳动者都应当以国家主人翁的态度对待自己的劳动。国家提倡社会主义劳动竞赛，奖励劳动模范和先进工作者。国家提倡公民从事义务劳动。\n\n国家对就业前的公民进行必要的劳动就业训练。\n\n第四十三条 中华人民共和国劳动者有休息的权利。\n\n国家发展劳动者休息和休养的设施，规定职工的工作时间和休假制度。\n\n第四十四条 国家依照法律规定实行企业事业组织的职工和国家机关工作人员的退休制度。退休人员的生活受到国家和社会的保障。\n\n第四十五条 中华人民共和国公民在年老、疾病或者丧失劳动能力的情况下，有从国家和社会获得物质帮助的权利。国家发展为公民享受这些权利所需要的社会保险、社会救济和医疗卫生事业。\n\n国家和社会保障残废军人的生活，抚恤烈士家属，优待军人家属。\n\n国家和社会帮助安排盲、聋、哑和其他有残疾的公民的劳动、生活和教育。\n\n第四十六条 中华人民共和国公民有受教育的权利和义务。\n\n国家培养青年、少年、儿童在品德、智力、体质等方面全面发展。\n\n第四十七条 中华人民共和国公民有进行科学研究、文学艺术创作和其他文化活动的自由。国家对于从事教育、科学、技术、文学、艺术和其他文化事业的公民的有益于人民的创造性工作，给以鼓励和帮助。\n\n第四十八条 中华人民共和国妇女在政治的、经济的、文化的、社会的和家庭的生活等各方面享有同男子平等的权利。\n\n国家保护妇女的权利和利益，实行男女同工同酬，培养和选拔妇女干部。\n\n第四十九条 婚姻、家庭、母亲和儿童受国家的保护。\n\n夫妻双方有实行计划生育的义务。\n\n父母有抚养教育未成年子女的义务，成年子女有赡养扶助父母的义务。\n\n禁止破坏婚姻自由，禁止虐待老人、妇女和儿童。\n\n第五十条 中华人民共和国保护华侨的正当的权利和利益，保护归侨和侨眷的合法的权利和利益。",
      "score": 1.8442139625549316
    },
    {
      "doc_id": "宪法_chunk_6",
      "chunk_id": "宪法_chunk_6",
      "text": "该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的过渡段落。\n\n（三）县、自治县分为乡、民族乡、镇。\n\n直辖市和较大的市分为区、县。自治州分为县、自治县、市。\n\n自治区、自治州、自治县都是民族自治地方。\n\n第三十一条 国家在必要时得设立特别行政区。在特别行政区内实行的制度按照具体情况由全国人民代表大会以法律规定。\n\n第三十二条 中华人民共和国保护在中国境内的外国人的合法权利和利益，在中国境内的外国人必须遵守中华人民共和国的法律。\n\n中华人民共和国对于因为政治原因要求避难的外国人，可以给予受庇护的权利。\n\n## 第二章 公民的基本权利和义务\n\n第三十三条 凡具有中华人民共和国国籍的人都是中华人民共和国公民。\n\n中华人民共和国公民在法律面前一律平等。\n\n国家尊重和保障人权。\n\n任何公民享有宪法和法律规定的权利，同时必须履行宪法和法律规定的义务。\n\n第三十四条 中华人民共和国年满十八周岁的公民，不分民族、种族、性别、职业、家庭出身、宗教信仰、教育程度、财产状况、居住期限，都有选举权和被选举权；但是依照法律被剥夺政治权利的人除外。\n\n第三十五条 中华人民共和国公民有言论、出版、集会、结社、游行、示威的自由。\n\n第三十六条 中华人民共和国公民有宗教信仰自由。\n\n任何国家机关、社会团体和个人不得强制公民信仰宗教或者不信仰宗教，不得歧视信仰宗教的公民和不信仰宗教的公民。\n\n国家保护正常的宗教活动。任何人不得利用宗教进行破坏社会秩序、损害公民身体健康、妨碍国家教育制度的活动。\n\n宗教团体和宗教事务不受外国势力的支配。\n\n第三十七条 中华人民共和国公民的人身自由不受侵犯。\n\n任何公民，非经人民检察院批准或者决定或者人民法院决定，并由公安机关执行，不受逮捕。\n\n禁止非法拘禁和以其他方法非法剥夺或者限制公民的人身自由，禁止非法搜查公民的身体。\n\n第三十八条 中华人民共和国公民的人格尊严不受侵犯。禁止用任何方法对公民进行侮辱、诽谤和诬告陷害。\n\n第三十九条 中华人民共和国公民的住宅不受侵犯。禁止非法搜查或者非法侵入公民的住宅。\n\n第四十条 中华人民共和国公民的通信自由和通信秘密受法律的保护。除因国家安全或者追查刑事犯罪的需要，由公安机关或者检察机关依照法律规定的程序对通信进行检查外，任何组织或者个人不得以任何理由侵犯公民的通信自由和通信秘密。\n\n第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。",
      "score": 1.1311166286468506
    },
    {
      "doc_id": "宪法_chunk_0",
      "chunk_id": "宪法_chunk_0",
      "text": "宪法开篇：通过及历次修正日期＋历史背景与政权合法性总述，为全文纲领。\n\n# 中华人民共和国宪法\n\n1982年12月4日 第五届全国人民代表大会第五次会议通过\n\n1982年12月4日 全国人民代表大会公告公布施行\n\n1988年4月12日 第七届全国人民代表大会第一次会议通过的《中华人民共和国宪法修正案》\n\n1993年3月29日 第八届全国人民代表大会第一次会议通过的《中华人民共和国宪法修正案》\n\n1999年3月15日 第九届全国人民代表大会第二次会议通过的《中华人民共和国宪法修正案》\n\n2004年3月14日 第十届全国人民代表大会第二次会议通过的《中华人民共和国宪法修正案》\n\n2018年3月11日 第十三届全国人民代表大会第一次会议通过的《中华人民共和国宪法修正案》\n\n<!-- INFO END -->\n\n## 序言\n\n中国是世界上历史最悠久的国家之一。中国各族人民共同创造了光辉灿烂的文化，具有光荣的革命传统。\n\n一八四○年以后，封建的中国逐渐变成半殖民地、半封建的国家。中国人民为国家独立、民族解放和民主自由进行了前仆后继的英勇奋斗。\n\n二十世纪，中国发生了翻天覆地的伟大历史变革。\n\n一九一一年孙中山先生领导的辛亥革命，废除了封建帝制，创立了中华民国。但是，中国人民反对帝国主义和封建主义的历史任务还没有完成。\n\n一九四九年，以毛泽东主席为领袖的中国共产党领导中国各族人民，在经历了长期的艰难曲折的武装斗争和其他形式的斗争以后，终于推翻了帝国主义、封建主义和官僚资本主义的统治，取得了新民主主义革命的伟大胜利，建立了中华人民共和国。从此，中国人民掌握了国家的权力，成为国家的主人。\n\n<!-- FORCE BREAK -->\n\n中华人民共和国成立以后，我国社会逐步实现了由新民主主义到社会主义的过渡。生产资料私有制的社会主义改造已经完成，人剥削人的制度已经消灭，社会主义制度已经确立。工人阶级领导的、以工农联盟为基础的人民民主专政，实质上即无产阶级专政，得到巩固和发展。中国人民和中国人民解放军战胜了帝国主义、霸权主义的侵略、破坏和武装挑衅，维护了国家的独立和安全，增强了国防。经济建设取得了重大的成就，独立的、比较完整的社会主义工业体系已经基本形成，农业生产显著提高。教育、科学、文化等事业有了很大的发展，社会主义思想教育取得了明显的成效。广大人民的生活有了较大的改善。\n\n<!-- FORCE BREAK -->",
      "score": -0.7014836072921753
    }
  ],
  "total_found": 3
}
2026-05-13 09:12:38,138 - INFO - Iteration 2/10
2026-05-13 09:12:44,620 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 09:12:44,620 - INFO - Executing tool: knowledge_base_search with args: {'query': '宪法 第四条 具体条文内容'}
2026-05-13 09:12:44,621 - INFO - Knowledge base search initiated - Type: KnowledgeBaseType.LOCAL, Query: '宪法 第四条 具体条文内容'
2026-05-13 09:12:44,621 - INFO - Searching local knowledge base for: 宪法 第四条 具体条文内容
2026-05-13 09:13:01,648 - INFO - Local search returned 3 results for query: 宪法 第四条 具体条文内容
2026-05-13 09:13:01,648 - INFO - Tool result: {
  "status": "success",
  "results": [
    {
      "doc_id": "宪法_chunk_6",
      "chunk_id": "宪法_chunk_6",
      "text": "该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的过渡段落。\n\n（三）县、自治县分为乡、民族乡、镇。\n\n直辖市和较大的市分为区、县。自治州分为县、自治县、市。\n\n自治区、自治州、自治县都是民族自治地方。\n\n第三十一条 国家在必要时得设立特别行政区。在特别行政区内实行的制度按照具体情况由全国人民代表大会以法律规定。\n\n第三十二条 中华人民共和国保护在中国境内的外国人的合法权利和利益，在中国境内的外国人必须遵守中华人民共和国的法律。\n\n中华人民共和国对于因为政治原因要求避难的外国人，可以给予受庇护的权利。\n\n## 第二章 公民的基本权利和义务\n\n第三十三条 凡具有中华人民共和国国籍的人都是中华人民共和国公民。\n\n中华人民共和国公民在法律面前一律平等。\n\n国家尊重和保障人权。\n\n任何公民享有宪法和法律规定的权利，同时必须履行宪法和法律规定的义务。\n\n第三十四条 中华人民共和国年满十八周岁的公民，不分民族、种族、性别、职业、家庭出身、宗教信仰、教育程度、财产状况、居住期限，都有选举权和被选举权；但是依照法律被剥夺政治权利的人除外。\n\n第三十五条 中华人民共和国公民有言论、出版、集会、结社、游行、示威的自由。\n\n第三十六条 中华人民共和国公民有宗教信仰自由。\n\n任何国家机关、社会团体和个人不得强制公民信仰宗教或者不信仰宗教，不得歧视信仰宗教的公民和不信仰宗教的公民。\n\n国家保护正常的宗教活动。任何人不得利用宗教进行破坏社会秩序、损害公民身体健康、妨碍国家教育制度的活动。\n\n宗教团体和宗教事务不受外国势力的支配。\n\n第三十七条 中华人民共和国公民的人身自由不受侵犯。\n\n任何公民，非经人民检察院批准或者决定或者人民法院决定，并由公安机关执行，不受逮捕。\n\n禁止非法拘禁和以其他方法非法剥夺或者限制公民的人身自由，禁止非法搜查公民的身体。\n\n第三十八条 中华人民共和国公民的人格尊严不受侵犯。禁止用任何方法对公民进行侮辱、诽谤和诬告陷害。\n\n第三十九条 中华人民共和国公民的住宅不受侵犯。禁止非法搜查或者非法侵入公民的住宅。\n\n第四十条 中华人民共和国公民的通信自由和通信秘密受法律的保护。除因国家安全或者追查刑事犯罪的需要，由公安机关或者检察机关依照法律规定的程序对通信进行检查外，任何组织或者个人不得以任何理由侵犯公民的通信自由和通信秘密。\n\n第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。",
      "score": -0.6960959434509277
    },
    {
      "doc_id": "宪法_chunk_13",
      "chunk_id": "宪法_chunk_13",
      "text": "该段位于《宪法》第三章“国家机构”第三节“国务院”末尾至第五节“地方各级人民代表大会和地方各级人民政府”开头，列举国务院第（八）至（十八）项职权、部委职责、审计署设置及其对全国人大负责的关系，并衔接过渡到中央军事委员会与地方人大、政府的组织规定。\n\n（八）领导和管理民政、公安、司法行政等工作；\n\n（九）管理对外事务，同外国缔结条约和协定；\n\n（十）领导和管理国防建设事业；\n\n（十一）领导和管理民族事务，保障少数民族的平等权利和民族自治地方的自治权利；\n\n（十二）保护华侨的正当的权利和利益，保护归侨和侨眷的合法的权利和利益；\n\n（十三）改变或者撤销各部、各委员会发布的不适当的命令、指示和规章；\n\n（十四）改变或者撤销地方各级国家行政机关的不适当的决定和命令；\n\n（十五）批准省、自治区、直辖市的区域划分，批准自治州、县、自治县、市的建置和区域划分；\n\n（十六）依照法律规定决定省、自治区、直辖市的范围内部分地区进入紧急状态；\n\n（十七）审定行政机构的编制，依照法律规定任免、培训、考核和奖惩行政人员；\n\n（十八）全国人民代表大会和全国人民代表大会常务委员会授予的其他职权。\n\n第九十条 国务院各部部长、各委员会主任负责本部门的工作；召集和主持部务会议或者委员会会议、委务会议，讨论决定本部门工作的重大问题。\n\n各部、各委员会根据法律和国务院的行政法规、决定、命令，在本部门的权限内，发布命令、指示和规章。\n\n第九十一条 国务院设立审计机关，对国务院各部门和地方各级政府的财政收支，对国家的财政金融机构和企业事业组织的财务收支，进行审计监督。\n\n审计机关在国务院总理领导下，依照法律规定独立行使审计监督权，不受其他行政机关、社会团体和个人的干涉。\n\n第九十二条 国务院对全国人民代表大会负责并报告工作；在全国人民代表大会闭会期间，对全国人民代表大会常务委员会负责并报告工作。\n\n### 第四节 中央军事委员会\n\n第九十三条 中华人民共和国中央军事委员会领导全国武装力量。\n\n中央军事委员会由下列人员组成：\n\n主席，\n\n副主席若干人，\n\n委员若干人。\n\n中央军事委员会实行主席负责制。\n\n中央军事委员会每届任期同全国人民代表大会每届任期相同。\n\n第九十四条 中央军事委员会主席对全国人民代表大会和全国人民代表大会常务委员会负责。\n\n### 第五节 地方各级人民代表大会和地方各级人民政府\n\n第九十五条 省、直辖市、县、市、市辖区、乡、民族乡、镇设立人民代表大会和人民政府。\n\n地方各级人民代表大会和地方各级人民政府的组织由法律规定。\n\n自治区、自治州、自治县设立自治机关。自治机关的组织和工作根据宪法第三章第五节、第六节规定的基本原则由法律规定。\n\n第九十六条 地方各级人民代表大会是地方国家权力机关。\n\n县级以上的地方各级人民代表大会设立常务委员会。",
      "score": -1.3767120838165283
    },
    {
      "doc_id": "宪法_chunk_4",
      "chunk_id": "宪法_chunk_4",
      "text": "位于《宪法》第一章“总纲”第十条至第十九条，集中规定土地制度、多种所有制经济、财产保护、国家经济政策、教育文化方针等社会主义基本经济制度与社会发展原则。\n\n一切使用土地的组织和个人必须合理地利用土地。\n\n第十一条 在法律规定范围内的个体经济、私营经济等非公有制经济，是社会主义市场经济的重要组成部分。\n\n国家保护个体经济、私营经济等非公有制经济的合法的权利和利益。国家鼓励、支持和引导非公有制经济的发展，并对非公有制经济依法实行监督和管理。\n\n第十二条 社会主义的公共财产神圣不可侵犯。\n\n国家保护社会主义的公共财产。禁止任何组织或者个人用任何手段侵占或者破坏国家的和集体的财产。\n\n第十三条 公民的合法的私有财产不受侵犯。\n\n国家依照法律规定保护公民的私有财产权和继承权。\n\n国家为了公共利益的需要，可以依照法律规定对公民的私有财产实行征收或者征用并给予补偿。\n\n第十四条 国家通过提高劳动者的积极性和技术水平，推广先进的科学技术，完善经济管理体制和企业经营管理制度，实行各种形式的社会主义责任制，改进劳动组织，以不断提高劳动生产率和经济效益，发展社会生产力。\n\n国家厉行节约，反对浪费。\n\n国家合理安排积累和消费，兼顾国家、集体和个人的利益，在发展生产的基础上，逐步改善人民的物质生活和文化生活。\n\n国家建立健全同经济发展水平相适应的社会保障制度。\n\n第十五条 国家实行社会主义市场经济。\n\n国家加强经济立法，完善宏观调控。\n\n国家依法禁止任何组织或者个人扰乱社会经济秩序。\n\n第十六条 国有企业在法律规定的范围内有权自主经营。\n\n国有企业依照法律规定，通过职工代表大会和其他形式，实行民主管理。\n\n第十七条 集体经济组织在遵守有关法律的前提下，有独立进行经济活动的自主权。\n\n集体经济组织实行民主管理，依照法律规定选举和罢免管理人员，决定经营管理的重大问题。\n\n第十八条 中华人民共和国允许外国的企业和其他经济组织或者个人依照中华人民共和国法律的规定在中国投资，同中国的企业或者其他经济组织进行各种形式的经济合作。\n\n在中国境内的外国企业和其他外国经济组织以及中外合资经营的企业，都必须遵守中华人民共和国的法律。它们的合法的权利和利益受中华人民共和国法律的保护。\n\n第十九条 国家发展社会主义的教育事业，提高全国人民的科学文化水平。\n\n国家举办各种学校，普及初等义务教育，发展中等教育、职业教育和高等教育，并且发展学前教育。\n\n国家发展各种教育设施，扫除文盲，对工人、农民、国家工作人员和其他劳动者进行政治、文化、科学、技术、业务的教育，鼓励自学成才。\n\n国家鼓励集体经济组织、国家企业事业组织和其他社会力量依照法律规定举办各种教育事业。\n\n国家推广全国通用的普通话。",
      "score": -2.048053026199341
    }
  ],
  "total_found": 3
}
2026-05-13 09:13:01,649 - INFO - Iteration 3/10
2026-05-13 09:13:07,226 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 09:13:07,228 - INFO - Tool result: {
  "status": "success",
  "document": {
    "doc_id": "宪法_chunk_6",
    "content": "该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的过渡段落。\n\n（三）县、自治县分为乡、民族乡、镇。\n\n直辖市和较大的市分为区、县。自治州分为县、自治县、市。\n\n自治区、自治州、自治县都是民族自治地方。\n\n第三十一条 国家在必要时得设立特别行政区。在特别行政区内实行的制度按照具体情况由全国人民代表大会以法律规定。\n\n第三十二条 中华人民共和国保护在中国境内的外国人的合法权利和利益，在中国境内的外国人必须遵守中华人民共和国的法律。\n\n中华人民共和国对于因为政治原因要求避难的外国人，可以给予受庇护的权利。\n\n## 第二章 公民的基本权利和义务\n\n第三十三条 凡具有中华人民共和国国籍的人都是中华人民共和国公民。\n\n中华人民共和国公民在法律面前一律平等。\n\n国家尊重和保障人权。\n\n任何公民享有宪法和法律规定的权利，同时必须履行宪法和法律规定的义务。\n\n第三十四条 中华人民共和国年满十八周岁的公民，不分民族、种族、性别、职业、家庭出身、宗教信仰、教育程度、财产状况、居住期限，都有选举权和被选举权；但是依照法律被剥夺政治权利的人除外。\n\n第三十五条 中华人民共和国公民有言论、出版、集会、结社、游行、示威的自由。\n\n第三十六条 中华人民共和国公民有宗教信仰自由。\n\n任何国家机关、社会团体和个人不得强制公民信仰宗教或者不信仰宗教，不得歧视信仰宗教的公民和不信仰宗教的公民。\n\n国家保护正常的宗教活动。任何人不得利用宗教进行破坏社会秩序、损害公民身体健康、妨碍国家教育制度的活动。\n\n宗教团体和宗教事务不受外国势力的支配。\n\n第三十七条 中华人民共和国公民的人身自由不受侵犯。\n\n任何公民，非经人民检察院批准或者决定或者人民法院决定，并由公安机关执行，不受逮捕。\n\n禁止非法拘禁和以其他方法非法剥夺或者限制公民的人身自由，禁止非法搜查公民的身体。\n\n第三十八条 中华人民共和国公民的人格尊严不受侵犯。禁止用任何方法对公民进行侮辱、诽谤和诬告陷害。\n\n第三十九条 中华人民共和国公民的住宅不受侵犯。禁止非法搜查或者非法侵入公民的住宅。\n\n第四十条 中华人民共和国公民的通信自由和通信秘密受法律的保护。除因国家安全或者追查刑事犯罪的需要，由公安机关或者检察机关依照法律规定的程序对通信进行检查外，任何组织或者个人不得以任何理由侵犯公民的通信自由和通信秘密。\n\n第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。",
    "metadata": {
      "contextual": true,
      "original_char_count": 1054,
      "context_char_count": 105,
      "category": "1-宪法",
      "doc_title": "宪法",
      "original_text": "（三）县、自治县分为乡、民族乡、镇。\n\n直辖市和较大的市分为区、县。自治州分为县、自治县、市。\n\n自治区、自治州、自治县都是民族自治地方。\n\n第三十一条 国家在必要时得设立特别行政区。在特别行政区内实行的制度按照具体情况由全国人民代表大会以法律规定。\n\n第三十二条 中华人民共和国保护在中国境内的外国人的合法权利和利益，在中国境内的外国人必须遵守中华人民共和国的法律。\n\n中华人民共和国对于因为政治原因要求避难的外国人，可以给予受庇护的权利。\n\n## 第二章 公民的基本权利和义务\n\n第三十三条 凡具有中华人民共和国国籍的人都是中华人民共和国公民。\n\n中华人民共和国公民在法律面前一律平等。\n\n国家尊重和保障人权。\n\n任何公民享有宪法和法律规定的权利，同时必须履行宪法和法律规定的义务。\n\n第三十四条 中华人民共和国年满十八周岁的公民，不分民族、种族、性别、职业、家庭出身、宗教信仰、教育程度、财产状况、居住期限，都有选举权和被选举权；但是依照法律被剥夺政治权利的人除外。\n\n第三十五条 中华人民共和国公民有言论、出版、集会、结社、游行、示威的自由。\n\n第三十六条 中华人民共和国公民有宗教信仰自由。\n\n任何国家机关、社会团体和个人不得强制公民信仰宗教或者不信仰宗教，不得歧视信仰宗教的公民和不信仰宗教的公民。\n\n国家保护正常的宗教活动。任何人不得利用宗教进行破坏社会秩序、损害公民身体健康、妨碍国家教育制度的活动。\n\n宗教团体和宗教事务不受外国势力的支配。\n\n第三十七条 中华人民共和国公民的人身自由不受侵犯。\n\n任何公民，非经人民检察院批准或者决定或者人民法院决定，并由公安机关执行，不受逮捕。\n\n禁止非法拘禁和以其他方法非法剥夺或者限制公民的人身自由，禁止非法搜查公民的身体。\n\n第三十八条 中华人民共和国公民的人格尊严不受侵犯。禁止用任何方法对公民进行侮辱、诽谤和诬告陷害。\n\n第三十九条 中华人民共和国公民的住宅不受侵犯。禁止非法搜查或者非法侵入公民的住宅。\n\n第四十条 中华人民共和国公民的通信自由和通信秘密受法律的保护。除因国家安全或者追查刑事犯罪的需要，由公安机关或者检察机关依照法律规定的程序对通信进行检查外，任何组织或者个人不得以任何理由侵犯公民的通信自由和通信秘密。\n\n第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。",
      "context": "该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的过渡段落。",
      "chunk_index": 6,
      "char_count": 1161
    }
  }
}
2026-05-13 09:13:07,229 - INFO - Iteration 4/10
2026-05-13 09:13:14,329 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 09:13:14,329 - INFO - Executing tool: knowledge_base_search with args: {'query': '宪法 第一章 总纲 第一条 第二条 第三条 第四条'}
2026-05-13 09:13:14,330 - INFO - Knowledge base search initiated - Type: KnowledgeBaseType.LOCAL, Query: '宪法 第一章 总纲 第一条 第二条 第三条 第四条'
2026-05-13 09:13:14,330 - INFO - Searching local knowledge base for: 宪法 第一章 总纲 第一条 第二条 第三条 第四条
2026-05-13 09:13:31,327 - INFO - Local search returned 3 results for query: 宪法 第一章 总纲 第一条 第二条 第三条 第四条
2026-05-13 09:13:31,328 - INFO - Tool result: {
  "status": "success",
  "results": [
    {
      "doc_id": "宪法_chunk_4",
      "chunk_id": "宪法_chunk_4",
      "text": "位于《宪法》第一章“总纲”第十条至第十九条，集中规定土地制度、多种所有制经济、财产保护、国家经济政策、教育文化方针等社会主义基本经济制度与社会发展原则。\n\n一切使用土地的组织和个人必须合理地利用土地。\n\n第十一条 在法律规定范围内的个体经济、私营经济等非公有制经济，是社会主义市场经济的重要组成部分。\n\n国家保护个体经济、私营经济等非公有制经济的合法的权利和利益。国家鼓励、支持和引导非公有制经济的发展，并对非公有制经济依法实行监督和管理。\n\n第十二条 社会主义的公共财产神圣不可侵犯。\n\n国家保护社会主义的公共财产。禁止任何组织或者个人用任何手段侵占或者破坏国家的和集体的财产。\n\n第十三条 公民的合法的私有财产不受侵犯。\n\n国家依照法律规定保护公民的私有财产权和继承权。\n\n国家为了公共利益的需要，可以依照法律规定对公民的私有财产实行征收或者征用并给予补偿。\n\n第十四条 国家通过提高劳动者的积极性和技术水平，推广先进的科学技术，完善经济管理体制和企业经营管理制度，实行各种形式的社会主义责任制，改进劳动组织，以不断提高劳动生产率和经济效益，发展社会生产力。\n\n国家厉行节约，反对浪费。\n\n国家合理安排积累和消费，兼顾国家、集体和个人的利益，在发展生产的基础上，逐步改善人民的物质生活和文化生活。\n\n国家建立健全同经济发展水平相适应的社会保障制度。\n\n第十五条 国家实行社会主义市场经济。\n\n国家加强经济立法，完善宏观调控。\n\n国家依法禁止任何组织或者个人扰乱社会经济秩序。\n\n第十六条 国有企业在法律规定的范围内有权自主经营。\n\n国有企业依照法律规定，通过职工代表大会和其他形式，实行民主管理。\n\n第十七条 集体经济组织在遵守有关法律的前提下，有独立进行经济活动的自主权。\n\n集体经济组织实行民主管理，依照法律规定选举和罢免管理人员，决定经营管理的重大问题。\n\n第十八条 中华人民共和国允许外国的企业和其他经济组织或者个人依照中华人民共和国法律的规定在中国投资，同中国的企业或者其他经济组织进行各种形式的经济合作。\n\n在中国境内的外国企业和其他外国经济组织以及中外合资经营的企业，都必须遵守中华人民共和国的法律。它们的合法的权利和利益受中华人民共和国法律的保护。\n\n第十九条 国家发展社会主义的教育事业，提高全国人民的科学文化水平。\n\n国家举办各种学校，普及初等义务教育，发展中等教育、职业教育和高等教育，并且发展学前教育。\n\n国家发展各种教育设施，扫除文盲，对工人、农民、国家工作人员和其他劳动者进行政治、文化、科学、技术、业务的教育，鼓励自学成才。\n\n国家鼓励集体经济组织、国家企业事业组织和其他社会力量依照法律规定举办各种教育事业。\n\n国家推广全国通用的普通话。",
      "score": 2.24894118309021
    },
    {
      "doc_id": "宪法_chunk_6",
      "chunk_id": "宪法_chunk_6",
      "text": "该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的过渡段落。\n\n（三）县、自治县分为乡、民族乡、镇。\n\n直辖市和较大的市分为区、县。自治州分为县、自治县、市。\n\n自治区、自治州、自治县都是民族自治地方。\n\n第三十一条 国家在必要时得设立特别行政区。在特别行政区内实行的制度按照具体情况由全国人民代表大会以法律规定。\n\n第三十二条 中华人民共和国保护在中国境内的外国人的合法权利和利益，在中国境内的外国人必须遵守中华人民共和国的法律。\n\n中华人民共和国对于因为政治原因要求避难的外国人，可以给予受庇护的权利。\n\n## 第二章 公民的基本权利和义务\n\n第三十三条 凡具有中华人民共和国国籍的人都是中华人民共和国公民。\n\n中华人民共和国公民在法律面前一律平等。\n\n国家尊重和保障人权。\n\n任何公民享有宪法和法律规定的权利，同时必须履行宪法和法律规定的义务。\n\n第三十四条 中华人民共和国年满十八周岁的公民，不分民族、种族、性别、职业、家庭出身、宗教信仰、教育程度、财产状况、居住期限，都有选举权和被选举权；但是依照法律被剥夺政治权利的人除外。\n\n第三十五条 中华人民共和国公民有言论、出版、集会、结社、游行、示威的自由。\n\n第三十六条 中华人民共和国公民有宗教信仰自由。\n\n任何国家机关、社会团体和个人不得强制公民信仰宗教或者不信仰宗教，不得歧视信仰宗教的公民和不信仰宗教的公民。\n\n国家保护正常的宗教活动。任何人不得利用宗教进行破坏社会秩序、损害公民身体健康、妨碍国家教育制度的活动。\n\n宗教团体和宗教事务不受外国势力的支配。\n\n第三十七条 中华人民共和国公民的人身自由不受侵犯。\n\n任何公民，非经人民检察院批准或者决定或者人民法院决定，并由公安机关执行，不受逮捕。\n\n禁止非法拘禁和以其他方法非法剥夺或者限制公民的人身自由，禁止非法搜查公民的身体。\n\n第三十八条 中华人民共和国公民的人格尊严不受侵犯。禁止用任何方法对公民进行侮辱、诽谤和诬告陷害。\n\n第三十九条 中华人民共和国公民的住宅不受侵犯。禁止非法搜查或者非法侵入公民的住宅。\n\n第四十条 中华人民共和国公民的通信自由和通信秘密受法律的保护。除因国家安全或者追查刑事犯罪的需要，由公安机关或者检察机关依照法律规定的程序对通信进行检查外，任何组织或者个人不得以任何理由侵犯公民的通信自由和通信秘密。\n\n第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。",
      "score": 1.313538670539856
    },
    {
      "doc_id": "宪法_chunk_3",
      "chunk_id": "宪法_chunk_3",
      "text": "总纲中关于民族区域自治、法治国家、基本经济制度及土地与自然资源的宪法条款。\n\n国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。\n\n各少数民族聚居的地方实行区域自治，设立自治机关，行使自治权。各民族自治地方都是中华人民共和国不可分离的部分。\n\n各民族都有使用和发展自己的语言文字的自由，都有保持或者改革自己的风俗习惯的自由。\n\n第五条 中华人民共和国实行依法治国，建设社会主义法治国家。\n\n国家维护社会主义法制的统一和尊严。\n\n一切法律、行政法规和地方性法规都不得同宪法相抵触。\n\n一切国家机关和武装力量、各政党和各社会团体、各企业事业组织都必须遵守宪法和法律。一切违反宪法和法律的行为，必须予以追究。\n\n任何组织或者个人都不得有超越宪法和法律的特权。\n\n第六条 中华人民共和国的社会主义经济制度的基础是生产资料的社会主义公有制，即全民所有制和劳动群众集体所有制。社会主义公有制消灭人剥削人的制度，实行各尽所能、按劳分配的原则。\n\n国家在社会主义初级阶段，坚持公有制为主体、多种所有制经济共同发展的基本经济制度，坚持按劳分配为主体、多种分配方式并存的分配制度。\n\n第七条 国有经济，即社会主义全民所有制经济，是国民经济中的主导力量。国家保障国有经济的巩固和发展。\n\n第八条 农村集体经济组织实行家庭承包经营为基础、统分结合的双层经营体制。农村中的生产、供销、信用、消费等各种形式的合作经济，是社会主义劳动群众集体所有制经济。参加农村集体经济组织的劳动者，有权在法律规定的范围内经营自留地、自留山、家庭副业和饲养自留畜。\n\n城镇中的手工业、工业、建筑业、运输业、商业、服务业等行业的各种形式的合作经济，都是社会主义劳动群众集体所有制经济。\n\n国家保护城乡集体经济组织的合法的权利和利益，鼓励、指导和帮助集体经济的发展。\n\n第九条 矿藏、水流、森林、山岭、草原、荒地、滩涂等自然资源，都属于国家所有，即全民所有；由法律规定属于集体所有的森林和山岭、草原、荒地、滩涂除外。\n\n国家保障自然资源的合理利用，保护珍贵的动物和植物。禁止任何组织或者个人用任何手段侵占或者破坏自然资源。\n\n第十条 城市的土地属于国家所有。\n\n农村和城市郊区的土地，除由法律规定属于国家所有的以外，属于集体所有；宅基地和自留地、自留山，也属于集体所有。\n\n国家为了公共利益的需要，可以依照法律规定对土地实行征收或者征用并给予补偿。\n\n任何组织或者个人不得侵占、买卖或者以其他形式非法转让土地。土地的使用权可以依照法律的规定转让。\n\n一切使用土地的组织和个人必须合理地利用土地。",
      "score": 1.1622469425201416
    }
  ],
  "total_found": 3
}
2026-05-13 09:13:31,328 - INFO - Iteration 5/10
2026-05-13 09:13:38,633 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 09:13:38,634 - INFO - Tool result: {
  "status": "success",
  "document": {
    "doc_id": "宪法_chunk_3",
    "content": "总纲中关于民族区域自治、法治国家、基本经济制度及土地与自然资源的宪法条款。\n\n国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。\n\n各少数民族聚居的地方实行区域自治，设立自治机关，行使自治权。各民族自治地方都是中华人民共和国不可分离的部分。\n\n各民族都有使用和发展自己的语言文字的自由，都有保持或者改革自己的风俗习惯的自由。\n\n第五条 中华人民共和国实行依法治国，建设社会主义法治国家。\n\n国家维护社会主义法制的统一和尊严。\n\n一切法律、行政法规和地方性法规都不得同宪法相抵触。\n\n一切国家机关和武装力量、各政党和各社会团体、各企业事业组织都必须遵守宪法和法律。一切违反宪法和法律的行为，必须予以追究。\n\n任何组织或者个人都不得有超越宪法和法律的特权。\n\n第六条 中华人民共和国的社会主义经济制度的基础是生产资料的社会主义公有制，即全民所有制和劳动群众集体所有制。社会主义公有制消灭人剥削人的制度，实行各尽所能、按劳分配的原则。\n\n国家在社会主义初级阶段，坚持公有制为主体、多种所有制经济共同发展的基本经济制度，坚持按劳分配为主体、多种分配方式并存的分配制度。\n\n第七条 国有经济，即社会主义全民所有制经济，是国民经济中的主导力量。国家保障国有经济的巩固和发展。\n\n第八条 农村集体经济组织实行家庭承包经营为基础、统分结合的双层经营体制。农村中的生产、供销、信用、消费等各种形式的合作经济，是社会主义劳动群众集体所有制经济。参加农村集体经济组织的劳动者，有权在法律规定的范围内经营自留地、自留山、家庭副业和饲养自留畜。\n\n城镇中的手工业、工业、建筑业、运输业、商业、服务业等行业的各种形式的合作经济，都是社会主义劳动群众集体所有制经济。\n\n国家保护城乡集体经济组织的合法的权利和利益，鼓励、指导和帮助集体经济的发展。\n\n第九条 矿藏、水流、森林、山岭、草原、荒地、滩涂等自然资源，都属于国家所有，即全民所有；由法律规定属于集体所有的森林和山岭、草原、荒地、滩涂除外。\n\n国家保障自然资源的合理利用，保护珍贵的动物和植物。禁止任何组织或者个人用任何手段侵占或者破坏自然资源。\n\n第十条 城市的土地属于国家所有。\n\n农村和城市郊区的土地，除由法律规定属于国家所有的以外，属于集体所有；宅基地和自留地、自留山，也属于集体所有。\n\n国家为了公共利益的需要，可以依照法律规定对土地实行征收或者征用并给予补偿。\n\n任何组织或者个人不得侵占、买卖或者以其他形式非法转让土地。土地的使用权可以依照法律的规定转让。\n\n一切使用土地的组织和个人必须合理地利用土地。",
    "metadata": {
      "contextual": true,
      "original_char_count": 1044,
      "context_char_count": 37,
      "category": "1-宪法",
      "doc_title": "宪法",
      "original_text": "国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。\n\n各少数民族聚居的地方实行区域自治，设立自治机关，行使自治权。各民族自治地方都是中华人民共和国不可分离的部分。\n\n各民族都有使用和发展自己的语言文字的自由，都有保持或者改革自己的风俗习惯的自由。\n\n第五条 中华人民共和国实行依法治国，建设社会主义法治国家。\n\n国家维护社会主义法制的统一和尊严。\n\n一切法律、行政法规和地方性法规都不得同宪法相抵触。\n\n一切国家机关和武装力量、各政党和各社会团体、各企业事业组织都必须遵守宪法和法律。一切违反宪法和法律的行为，必须予以追究。\n\n任何组织或者个人都不得有超越宪法和法律的特权。\n\n第六条 中华人民共和国的社会主义经济制度的基础是生产资料的社会主义公有制，即全民所有制和劳动群众集体所有制。社会主义公有制消灭人剥削人的制度，实行各尽所能、按劳分配的原则。\n\n国家在社会主义初级阶段，坚持公有制为主体、多种所有制经济共同发展的基本经济制度，坚持按劳分配为主体、多种分配方式并存的分配制度。\n\n第七条 国有经济，即社会主义全民所有制经济，是国民经济中的主导力量。国家保障国有经济的巩固和发展。\n\n第八条 农村集体经济组织实行家庭承包经营为基础、统分结合的双层经营体制。农村中的生产、供销、信用、消费等各种形式的合作经济，是社会主义劳动群众集体所有制经济。参加农村集体经济组织的劳动者，有权在法律规定的范围内经营自留地、自留山、家庭副业和饲养自留畜。\n\n城镇中的手工业、工业、建筑业、运输业、商业、服务业等行业的各种形式的合作经济，都是社会主义劳动群众集体所有制经济。\n\n国家保护城乡集体经济组织的合法的权利和利益，鼓励、指导和帮助集体经济的发展。\n\n第九条 矿藏、水流、森林、山岭、草原、荒地、滩涂等自然资源，都属于国家所有，即全民所有；由法律规定属于集体所有的森林和山岭、草原、荒地、滩涂除外。\n\n国家保障自然资源的合理利用，保护珍贵的动物和植物。禁止任何组织或者个人用任何手段侵占或者破坏自然资源。\n\n第十条 城市的土地属于国家所有。\n\n农村和城市郊区的土地，除由法律规定属于国家所有的以外，属于集体所有；宅基地和自留地、自留山，也属于集体所有。\n\n国家为了公共利益的需要，可以依照法律规定对土地实行征收或者征用并给予补偿。\n\n任何组织或者个人不得侵占、买卖或者以其他形式非法转让土地。土地的使用权可以依照法律的规定转让。\n\n一切使用土地的组织和个人必须合理地利用土地。",
      "context": "总纲中关于民族区域自治、法治国家、基本经济制度及土地与自然资源的宪法条款。",
      "chunk_index": 3,
      "char_count": 1083
    }
  }
}
2026-05-13 09:13:38,634 - INFO - Iteration 6/10
2026-05-13 09:13:44,733 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 09:13:44,734 - INFO - Executing tool: knowledge_base_search with args: {'query': '宪法 民族政策 第四条 各少数民族'}
2026-05-13 09:13:44,734 - INFO - Knowledge base search initiated - Type: KnowledgeBaseType.LOCAL, Query: '宪法 民族政策 第四条 各少数民族'
2026-05-13 09:13:44,734 - INFO - Searching local knowledge base for: 宪法 民族政策 第四条 各少数民族
2026-05-13 09:13:59,827 - INFO - Local search returned 3 results for query: 宪法 民族政策 第四条 各少数民族
2026-05-13 09:13:59,828 - INFO - Tool result: {
  "status": "success",
  "results": [
    {
      "doc_id": "宪法_chunk_2",
      "chunk_id": "宪法_chunk_2",
      "text": "该段位于宪法序言末尾与第一章“总纲”开头之间，概括了国家民族政策、对外政策及宪法地位，并紧接引出国家性质、政权组织形式与民族平等原则，是连接宪法序言与总纲的过渡性关键段落。\n\n中华人民共和国是全国各族人民共同缔造的统一的多民族国家。平等团结互助和谐的社会主义民族关系已经确立，并将继续加强。在维护民族团结的斗争中，要反对大民族主义，主要是大汉族主义，也要反对地方民族主义。国家尽一切努力，促进全国各民族的共同繁荣。\n\n中国革命、建设、改革的成就是同世界人民的支持分不开的。中国的前途是同世界的前途紧密地联系在一起的。中国坚持独立自主的对外政策，坚持互相尊重主权和领土完整、互不侵犯、互不干涉内政、平等互利、和平共处的五项原则，坚持和平发展道路，坚持互利共赢开放战略，发展同各国的外交关系和经济、文化交流，推动构建人类命运共同体；坚持反对帝国主义、霸权主义、殖民主义，加强同世界各国人民的团结，支持被压迫民族和发展中国家争取和维护民族独立、发展民族经济的正义斗争，为维护世界和平和促进人类进步事业而努力。\n\n本宪法以法律的形式确认了中国各族人民奋斗的成果，规定了国家的根本制度和根本任务，是国家的根本法，具有最高的法律效力。全国各族人民、一切国家机关和武装力量、各政党和各社会团体、各企业事业组织，都必须以宪法为根本的活动准则，并且负有维护宪法尊严、保证宪法实施的职责。\n\n## 第一章 总纲\n\n第一条 中华人民共和国是工人阶级领导的、以工农联盟为基础的人民民主专政的社会主义国家。\n\n社会主义制度是中华人民共和国的根本制度。中国共产党领导是中国特色社会主义最本质的特征。禁止任何组织或者个人破坏社会主义制度。\n\n第二条 中华人民共和国的一切权力属于人民。\n\n人民行使国家权力的机关是全国人民代表大会和地方各级人民代表大会。\n\n人民依照法律规定，通过各种途径和形式，管理国家事务，管理经济和文化事业，管理社会事务。\n\n第三条 中华人民共和国的国家机构实行民主集中制的原则。\n\n全国人民代表大会和地方各级人民代表大会都由民主选举产生，对人民负责，受人民监督。\n\n国家行政机关、监察机关、审判机关、检察机关都由人民代表大会产生，对它负责，受它监督。\n\n中央和地方的国家机构职权的划分，遵循在中央的统一领导下，充分发挥地方的主动性、积极性的原则。\n\n第四条 中华人民共和国各民族一律平等。国家保障各少数民族的合法的权利和利益，维护和发展各民族的平等团结互助和谐关系。禁止对任何民族的歧视和压迫，禁止破坏民族团结和制造民族分裂的行为。\n\n国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。",
      "score": 3.248065710067749
    },
    {
      "doc_id": "宪法_chunk_3",
      "chunk_id": "宪法_chunk_3",
      "text": "总纲中关于民族区域自治、法治国家、基本经济制度及土地与自然资源的宪法条款。\n\n国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。\n\n各少数民族聚居的地方实行区域自治，设立自治机关，行使自治权。各民族自治地方都是中华人民共和国不可分离的部分。\n\n各民族都有使用和发展自己的语言文字的自由，都有保持或者改革自己的风俗习惯的自由。\n\n第五条 中华人民共和国实行依法治国，建设社会主义法治国家。\n\n国家维护社会主义法制的统一和尊严。\n\n一切法律、行政法规和地方性法规都不得同宪法相抵触。\n\n一切国家机关和武装力量、各政党和各社会团体、各企业事业组织都必须遵守宪法和法律。一切违反宪法和法律的行为，必须予以追究。\n\n任何组织或者个人都不得有超越宪法和法律的特权。\n\n第六条 中华人民共和国的社会主义经济制度的基础是生产资料的社会主义公有制，即全民所有制和劳动群众集体所有制。社会主义公有制消灭人剥削人的制度，实行各尽所能、按劳分配的原则。\n\n国家在社会主义初级阶段，坚持公有制为主体、多种所有制经济共同发展的基本经济制度，坚持按劳分配为主体、多种分配方式并存的分配制度。\n\n第七条 国有经济，即社会主义全民所有制经济，是国民经济中的主导力量。国家保障国有经济的巩固和发展。\n\n第八条 农村集体经济组织实行家庭承包经营为基础、统分结合的双层经营体制。农村中的生产、供销、信用、消费等各种形式的合作经济，是社会主义劳动群众集体所有制经济。参加农村集体经济组织的劳动者，有权在法律规定的范围内经营自留地、自留山、家庭副业和饲养自留畜。\n\n城镇中的手工业、工业、建筑业、运输业、商业、服务业等行业的各种形式的合作经济，都是社会主义劳动群众集体所有制经济。\n\n国家保护城乡集体经济组织的合法的权利和利益，鼓励、指导和帮助集体经济的发展。\n\n第九条 矿藏、水流、森林、山岭、草原、荒地、滩涂等自然资源，都属于国家所有，即全民所有；由法律规定属于集体所有的森林和山岭、草原、荒地、滩涂除外。\n\n国家保障自然资源的合理利用，保护珍贵的动物和植物。禁止任何组织或者个人用任何手段侵占或者破坏自然资源。\n\n第十条 城市的土地属于国家所有。\n\n农村和城市郊区的土地，除由法律规定属于国家所有的以外，属于集体所有；宅基地和自留地、自留山，也属于集体所有。\n\n国家为了公共利益的需要，可以依照法律规定对土地实行征收或者征用并给予补偿。\n\n任何组织或者个人不得侵占、买卖或者以其他形式非法转让土地。土地的使用权可以依照法律的规定转让。\n\n一切使用土地的组织和个人必须合理地利用土地。",
      "score": 0.44985875487327576
    },
    {
      "doc_id": "宪法_chunk_6",
      "chunk_id": "宪法_chunk_6",
      "text": "该段位于《宪法》“总纲”末尾与“公民基本权利和义务”开头，衔接行政区划、特别行政区、外国人地位规定后，转入列举公民平等权、选举权、言论宗教人身自由及监督权等核心权利，是连接国家结构规范与公民权利规范的过渡段落。\n\n（三）县、自治县分为乡、民族乡、镇。\n\n直辖市和较大的市分为区、县。自治州分为县、自治县、市。\n\n自治区、自治州、自治县都是民族自治地方。\n\n第三十一条 国家在必要时得设立特别行政区。在特别行政区内实行的制度按照具体情况由全国人民代表大会以法律规定。\n\n第三十二条 中华人民共和国保护在中国境内的外国人的合法权利和利益，在中国境内的外国人必须遵守中华人民共和国的法律。\n\n中华人民共和国对于因为政治原因要求避难的外国人，可以给予受庇护的权利。\n\n## 第二章 公民的基本权利和义务\n\n第三十三条 凡具有中华人民共和国国籍的人都是中华人民共和国公民。\n\n中华人民共和国公民在法律面前一律平等。\n\n国家尊重和保障人权。\n\n任何公民享有宪法和法律规定的权利，同时必须履行宪法和法律规定的义务。\n\n第三十四条 中华人民共和国年满十八周岁的公民，不分民族、种族、性别、职业、家庭出身、宗教信仰、教育程度、财产状况、居住期限，都有选举权和被选举权；但是依照法律被剥夺政治权利的人除外。\n\n第三十五条 中华人民共和国公民有言论、出版、集会、结社、游行、示威的自由。\n\n第三十六条 中华人民共和国公民有宗教信仰自由。\n\n任何国家机关、社会团体和个人不得强制公民信仰宗教或者不信仰宗教，不得歧视信仰宗教的公民和不信仰宗教的公民。\n\n国家保护正常的宗教活动。任何人不得利用宗教进行破坏社会秩序、损害公民身体健康、妨碍国家教育制度的活动。\n\n宗教团体和宗教事务不受外国势力的支配。\n\n第三十七条 中华人民共和国公民的人身自由不受侵犯。\n\n任何公民，非经人民检察院批准或者决定或者人民法院决定，并由公安机关执行，不受逮捕。\n\n禁止非法拘禁和以其他方法非法剥夺或者限制公民的人身自由，禁止非法搜查公民的身体。\n\n第三十八条 中华人民共和国公民的人格尊严不受侵犯。禁止用任何方法对公民进行侮辱、诽谤和诬告陷害。\n\n第三十九条 中华人民共和国公民的住宅不受侵犯。禁止非法搜查或者非法侵入公民的住宅。\n\n第四十条 中华人民共和国公民的通信自由和通信秘密受法律的保护。除因国家安全或者追查刑事犯罪的需要，由公安机关或者检察机关依照法律规定的程序对通信进行检查外，任何组织或者个人不得以任何理由侵犯公民的通信自由和通信秘密。\n\n第四十一条 中华人民共和国公民对于任何国家机关和国家工作人员，有提出批评和建议的权利；对于任何国家机关和国家工作人员的违法失职行为，有向有关国家机关提出申诉、控告或者检举的权利，但是不得捏造或者歪曲事实进行诬告陷害。",
      "score": -1.283142328262329
    }
  ],
  "total_found": 3
}
2026-05-13 09:13:59,828 - INFO - Iteration 7/10
2026-05-13 09:14:11,301 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-05-13 09:14:11,302 - INFO - Final response generated (length: 189 chars)
很好！我找到了宪法第四条的内容。根据搜索结果，宪法第四条规定：

**第四条 中华人民共和国各民族一律平等。国家保障各少数民族的合法的权利和利益，维护和发展各民族的平等团结互助和谐关系。禁止对任何民族的歧视和压迫，禁止破坏民族团结和制造民族分裂的行为。**

**国家根据各少数民族的特点和需要，帮助各少数民族地区加速经济和文化的发展。**

[Doc: 宪法_chunk_2]
```