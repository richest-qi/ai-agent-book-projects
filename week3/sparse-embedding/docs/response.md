>python quickstart.py

============================================================
 Educational Sparse Vector Search Engine - Quick Start
============================================================

This demo shows the core functionality of BM25 search.

Initializing search engine...
2026-05-09 11:05:06,534 - bm25_engine - INFO - InvertedIndex initialized
2026-05-09 11:05:06,534 - bm25_engine - INFO - SparseSearchEngine initialized

Indexing 10 documents...
----------------------------------------
2026-05-09 11:05:06,534 - bm25_engine - INFO - Indexing document with external ID '0' (internal ID 0)
2026-05-09 11:05:06,534 - bm25_engine - INFO - Adding document 0 to index
2026-05-09 11:05:06,534 - bm25_engine - DEBUG - Document text: Python is a versatile programming language widely used for web development, data science, machine le...
2026-05-09 11:05:06,534 - bm25_engine - DEBUG - Document metadata: {'title': 'Python Overview'}
2026-05-09 11:05:06,535 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,535 - bm25_engine - DEBUG - Tokenizing text of length 171
2026-05-09 11:05:06,538 - bm25_engine - DEBUG - Found 25 raw tokens
2026-05-09 11:05:06,538 - bm25_engine - DEBUG - After removing stop words: 22 tokens
2026-05-09 11:05:06,538 - bm25_engine - DEBUG - Document 0: 22 tokens, 21 unique terms
2026-05-09 11:05:06,538 - bm25_engine - DEBUG - Index statistics: 1 documents, 21 unique terms, 22 total terms
2026-05-09 11:05:06,538 - bm25_engine - INFO - Document 0 indexed successfully
2026-05-09 11:05:06,539 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=22.00
  [0] Python Overview
2026-05-09 11:05:06,539 - bm25_engine - INFO - Indexing document with external ID '1' (internal ID 1)
2026-05-09 11:05:06,539 - bm25_engine - INFO - Adding document 1 to index
2026-05-09 11:05:06,539 - bm25_engine - DEBUG - Document text: JavaScript powers the interactive web. It runs in browsers and on servers with Node.js. Modern JavaS...
2026-05-09 11:05:06,539 - bm25_engine - DEBUG - Document metadata: {'title': 'JavaScript Essentials'}
2026-05-09 11:05:06,539 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,540 - bm25_engine - DEBUG - Tokenizing text of length 177
2026-05-09 11:05:06,540 - bm25_engine - DEBUG - Found 26 raw tokens
2026-05-09 11:05:06,540 - bm25_engine - DEBUG - After removing stop words: 23 tokens
2026-05-09 11:05:06,540 - bm25_engine - DEBUG - Document 1: 23 tokens, 21 unique terms
2026-05-09 11:05:06,540 - bm25_engine - DEBUG - Index statistics: 2 documents, 40 unique terms, 45 total terms
2026-05-09 11:05:06,541 - bm25_engine - INFO - Document 1 indexed successfully
2026-05-09 11:05:06,541 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=22.50
  [1] JavaScript Essentials
2026-05-09 11:05:06,541 - bm25_engine - INFO - Indexing document with external ID '2' (internal ID 2)
2026-05-09 11:05:06,541 - bm25_engine - INFO - Adding document 2 to index
2026-05-09 11:05:06,541 - bm25_engine - DEBUG - Document text: Machine learning algorithms enable computers to learn from data. Popular algorithms include linear r...
2026-05-09 11:05:06,541 - bm25_engine - DEBUG - Document metadata: {'title': 'ML Algorithms'}
2026-05-09 11:05:06,541 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,541 - bm25_engine - DEBUG - Tokenizing text of length 172
2026-05-09 11:05:06,541 - bm25_engine - DEBUG - Found 22 raw tokens
2026-05-09 11:05:06,542 - bm25_engine - DEBUG - After removing stop words: 22 tokens
2026-05-09 11:05:06,542 - bm25_engine - DEBUG - Document 2: 22 tokens, 21 unique terms
2026-05-09 11:05:06,542 - bm25_engine - DEBUG - Index statistics: 3 documents, 57 unique terms, 67 total terms
2026-05-09 11:05:06,542 - bm25_engine - INFO - Document 2 indexed successfully
2026-05-09 11:05:06,542 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=22.33
  [2] ML Algorithms
2026-05-09 11:05:06,542 - bm25_engine - INFO - Indexing document with external ID '3' (internal ID 3)
2026-05-09 11:05:06,542 - bm25_engine - INFO - Adding document 3 to index
2026-05-09 11:05:06,542 - bm25_engine - DEBUG - Document text: Web development involves HTML for structure, CSS for styling, and JavaScript for interactivity. Mode...
2026-05-09 11:05:06,542 - bm25_engine - DEBUG - Document metadata: {'title': 'Web Development'}
2026-05-09 11:05:06,542 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,542 - bm25_engine - DEBUG - Tokenizing text of length 173
2026-05-09 11:05:06,543 - bm25_engine - DEBUG - Found 23 raw tokens
2026-05-09 11:05:06,543 - bm25_engine - DEBUG - After removing stop words: 23 tokens
2026-05-09 11:05:06,543 - bm25_engine - DEBUG - Document 3: 23 tokens, 20 unique terms
2026-05-09 11:05:06,543 - bm25_engine - DEBUG - Index statistics: 4 documents, 70 unique terms, 90 total terms
2026-05-09 11:05:06,543 - bm25_engine - INFO - Document 3 indexed successfully
2026-05-09 11:05:06,543 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=22.50
  [3] Web Development
2026-05-09 11:05:06,543 - bm25_engine - INFO - Indexing document with external ID '4' (internal ID 4)
2026-05-09 11:05:06,543 - bm25_engine - INFO - Adding document 4 to index
2026-05-09 11:05:06,543 - bm25_engine - DEBUG - Document text: Data structures organize information efficiently. Arrays provide fast access, linked lists enable dy...
2026-05-09 11:05:06,543 - bm25_engine - DEBUG - Document metadata: {'title': 'Data Structures'}
2026-05-09 11:05:06,543 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,544 - bm25_engine - DEBUG - Tokenizing text of length 191
2026-05-09 11:05:06,544 - bm25_engine - DEBUG - Found 24 raw tokens
2026-05-09 11:05:06,544 - bm25_engine - DEBUG - After removing stop words: 24 tokens
2026-05-09 11:05:06,544 - bm25_engine - DEBUG - Document 4: 24 tokens, 23 unique terms
2026-05-09 11:05:06,544 - bm25_engine - DEBUG - Index statistics: 5 documents, 88 unique terms, 114 total terms
2026-05-09 11:05:06,544 - bm25_engine - INFO - Document 4 indexed successfully
2026-05-09 11:05:06,544 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=22.80
  [4] Data Structures
2026-05-09 11:05:06,544 - bm25_engine - INFO - Indexing document with external ID '5' (internal ID 5)
2026-05-09 11:05:06,544 - bm25_engine - INFO - Adding document 5 to index
2026-05-09 11:05:06,544 - bm25_engine - DEBUG - Document text: Databases store and manage data persistently. SQL databases like PostgreSQL use structured tables, w...
2026-05-09 11:05:06,544 - bm25_engine - DEBUG - Document metadata: {'title': 'Database Systems'}
2026-05-09 11:05:06,544 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,544 - bm25_engine - DEBUG - Tokenizing text of length 159
2026-05-09 11:05:06,545 - bm25_engine - DEBUG - Found 21 raw tokens
2026-05-09 11:05:06,545 - bm25_engine - DEBUG - After removing stop words: 21 tokens
2026-05-09 11:05:06,545 - bm25_engine - DEBUG - Document 5: 21 tokens, 17 unique terms
2026-05-09 11:05:06,545 - bm25_engine - DEBUG - Index statistics: 6 documents, 101 unique terms, 135 total terms
2026-05-09 11:05:06,545 - bm25_engine - INFO - Document 5 indexed successfully
2026-05-09 11:05:06,545 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=22.50
  [5] Database Systems
2026-05-09 11:05:06,545 - bm25_engine - INFO - Indexing document with external ID '6' (internal ID 6)
2026-05-09 11:05:06,545 - bm25_engine - INFO - Adding document 6 to index
2026-05-09 11:05:06,545 - bm25_engine - DEBUG - Document text: Cloud computing provides scalable infrastructure on demand. AWS, Google Cloud, and Azure offer servi...
2026-05-09 11:05:06,545 - bm25_engine - DEBUG - Document metadata: {'title': 'Cloud Computing'}
2026-05-09 11:05:06,545 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,545 - bm25_engine - DEBUG - Tokenizing text of length 159
2026-05-09 11:05:06,545 - bm25_engine - DEBUG - Found 21 raw tokens
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - After removing stop words: 20 tokens
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - Document 6: 20 tokens, 18 unique terms
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - Index statistics: 7 documents, 114 unique terms, 155 total terms
2026-05-09 11:05:06,546 - bm25_engine - INFO - Document 6 indexed successfully
2026-05-09 11:05:06,546 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=22.14
  [6] Cloud Computing
2026-05-09 11:05:06,546 - bm25_engine - INFO - Indexing document with external ID '7' (internal ID 7)
2026-05-09 11:05:06,546 - bm25_engine - INFO - Adding document 7 to index
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - Document text: Software testing ensures code quality. Unit tests verify individual functions, integration tests che...
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - Document metadata: {'title': 'Software Testing'}
2026-05-09 11:05:06,546 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - Tokenizing text of length 174
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - Found 21 raw tokens
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - After removing stop words: 21 tokens
2026-05-09 11:05:06,546 - bm25_engine - DEBUG - Document 7: 21 tokens, 19 unique terms
2026-05-09 11:05:06,547 - bm25_engine - DEBUG - Index statistics: 8 documents, 131 unique terms, 176 total terms
2026-05-09 11:05:06,547 - bm25_engine - INFO - Document 7 indexed successfully
2026-05-09 11:05:06,547 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=22.00
  [7] Software Testing
2026-05-09 11:05:06,547 - bm25_engine - INFO - Indexing document with external ID '8' (internal ID 8)
2026-05-09 11:05:06,547 - bm25_engine - INFO - Adding document 8 to index
2026-05-09 11:05:06,547 - bm25_engine - DEBUG - Document text: Version control systems track code changes over time. Git is the most popular system, enabling colla...
2026-05-09 11:05:06,547 - bm25_engine - DEBUG - Document metadata: {'title': 'Version Control'}
2026-05-09 11:05:06,547 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,547 - bm25_engine - DEBUG - Tokenizing text of length 154
2026-05-09 11:05:06,547 - bm25_engine - DEBUG - Found 22 raw tokens
2026-05-09 11:05:06,547 - bm25_engine - DEBUG - After removing stop words: 19 tokens
2026-05-09 11:05:06,547 - bm25_engine - DEBUG - Document 8: 19 tokens, 19 unique terms
2026-05-09 11:05:06,547 - bm25_engine - DEBUG - Index statistics: 9 documents, 147 unique terms, 195 total terms
2026-05-09 11:05:06,547 - bm25_engine - INFO - Document 8 indexed successfully
2026-05-09 11:05:06,547 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=21.67
  [8] Version Control
2026-05-09 11:05:06,548 - bm25_engine - INFO - Indexing document with external ID '9' (internal ID 9)
2026-05-09 11:05:06,548 - bm25_engine - INFO - Adding document 9 to index
2026-05-09 11:05:06,548 - bm25_engine - DEBUG - Document text: APIs (Application Programming Interfaces) enable communication between software systems. REST APIs u...
2026-05-09 11:05:06,548 - bm25_engine - DEBUG - Document metadata: {'title': 'APIs and Integration'}
2026-05-09 11:05:06,548 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,548 - bm25_engine - DEBUG - Tokenizing text of length 163
2026-05-09 11:05:06,549 - bm25_engine - DEBUG - Found 20 raw tokens
2026-05-09 11:05:06,549 - bm25_engine - DEBUG - After removing stop words: 20 tokens
2026-05-09 11:05:06,549 - bm25_engine - DEBUG - Document 9: 20 tokens, 19 unique terms
2026-05-09 11:05:06,549 - bm25_engine - DEBUG - Index statistics: 10 documents, 157 unique terms, 215 total terms
2026-05-09 11:05:06,549 - bm25_engine - INFO - Document 9 indexed successfully
2026-05-09 11:05:06,549 - bm25_engine - INFO - BM25 initialized with k1=1.5, b=0.75, avgdl=21.50
  [9] APIs and Integration

✓ Indexed 10 documents successfully!

Index Statistics:
  • Total documents: 10
  • Unique terms: 157
  • Average document length: 21.5 terms

============================================================
 Demonstration Searches
============================================================

🔍 Query: 'machine learning algorithms'
----------------------------------------
2026-05-09 11:05:06,552 - bm25_engine - INFO - Executing search query: 'machine learning algorithms'
2026-05-09 11:05:06,552 - bm25_engine - INFO - Searching for: 'machine learning algorithms'
2026-05-09 11:05:06,552 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,552 - bm25_engine - DEBUG - Tokenizing text of length 27
2026-05-09 11:05:06,552 - bm25_engine - DEBUG - Found 3 raw tokens
2026-05-09 11:05:06,552 - bm25_engine - DEBUG - After removing stop words: 3 tokens
2026-05-09 11:05:06,553 - bm25_engine - INFO - Query terms after processing: ['machine', 'learning', 'algorithms']
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - Term 'machine' appears in 3 documents
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - Term 'learning' appears in 3 documents
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - Term 'algorithms' appears in 1 documents
2026-05-09 11:05:06,553 - bm25_engine - INFO - Found 3 candidate documents
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - IDF for 'machine': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - Term 'machine' in doc 0: tf=1, dl=22, score=1.1333
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - IDF for 'learning': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - Term 'learning' in doc 0: tf=1, dl=22, score=1.1333
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - Document 0 total score: 2.2665
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - Term contributions: {'machine': 1.1332724760651118, 'learning': 1.1332724760651118, 'algorithms': 0}
2026-05-09 11:05:06,553 - bm25_engine - DEBUG - IDF for 'machine': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Term 'machine' in doc 2: tf=1, dl=22, score=1.1333
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - IDF for 'learning': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Term 'learning' in doc 2: tf=1, dl=22, score=1.1333
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - IDF for 'algorithms': N=10, df=1, idf=1.9924
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Term 'algorithms' in doc 2: tf=2, dl=22, score=2.8252
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Document 2 total score: 5.0918
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Term contributions: {'machine': 1.1332724760651118, 'learning': 1.1332724760651118, 'algorithms': 2.8252101263537956}
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - IDF for 'machine': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Term 'machine' in doc 6: tf=1, dl=20, score=1.1822
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - IDF for 'learning': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Term 'learning' in doc 6: tf=1, dl=20, score=1.1822
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Document 6 total score: 2.3645
2026-05-09 11:05:06,554 - bm25_engine - DEBUG - Term contributions: {'machine': 1.182249437815825, 'learning': 1.182249437815825, 'algorithms': 0}
2026-05-09 11:05:06,554 - bm25_engine - INFO - Returning top 3 results
2026-05-09 11:05:06,554 - bm25_engine - INFO - Rank 1: Document 2 (score: 5.0918)
2026-05-09 11:05:06,554 - bm25_engine - INFO - Rank 2: Document 6 (score: 2.3645)
2026-05-09 11:05:06,555 - bm25_engine - INFO - Rank 3: Document 0 (score: 2.2665)

  #1 ML Algorithms (Score: 5.092)
     Matched terms: machine, learning, algorithms
     Preview: Machine learning algorithms enable computers to learn from data. Popular algorithms include linear r...

  #2 Cloud Computing (Score: 2.364)
     Matched terms: machine, learning
     Preview: Cloud computing provides scalable infrastructure on demand. AWS, Google Cloud, and Azure offer servi...

  #3 Python Overview (Score: 2.267)
     Matched terms: machine, learning
     Preview: Python is a versatile programming language widely used for web development, data science, machine le...

🔍 Query: 'web development JavaScript'
----------------------------------------
2026-05-09 11:05:06,555 - bm25_engine - INFO - Executing search query: 'web development JavaScript'
2026-05-09 11:05:06,555 - bm25_engine - INFO - Searching for: 'web development JavaScript'
2026-05-09 11:05:06,555 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,555 - bm25_engine - DEBUG - Tokenizing text of length 26
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - Found 3 raw tokens
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - After removing stop words: 3 tokens
2026-05-09 11:05:06,556 - bm25_engine - INFO - Query terms after processing: ['web', 'development', 'JavaScript']
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - Term 'web' appears in 3 documents
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - Term 'development' appears in 2 documents
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - Term 'JavaScript' appears in 2 documents
2026-05-09 11:05:06,556 - bm25_engine - INFO - Found 3 candidate documents
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - IDF for 'web': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - Term 'web' in doc 0: tf=1, dl=22, score=1.1333
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - IDF for 'development': N=10, df=2, idf=1.4816
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - Term 'development' in doc 0: tf=1, dl=22, score=1.4663
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - Document 0 total score: 2.5995
2026-05-09 11:05:06,556 - bm25_engine - DEBUG - Term contributions: {'web': 1.1332724760651118, 'development': 1.4662599599480153, 'JavaScript': 0}
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - IDF for 'web': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Term 'web' in doc 1: tf=1, dl=23, score=1.1103
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - IDF for 'JavaScript': N=10, df=2, idf=1.4816
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Term 'JavaScript' in doc 1: tf=2, dl=23, score=2.0702
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Document 1 total score: 3.1804
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Term contributions: {'web': 1.1102748384448504, 'development': 0, 'JavaScript': 2.0701541920305853}
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - IDF for 'web': N=10, df=3, idf=1.1451
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Term 'web' in doc 3: tf=1, dl=23, score=1.1103
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - IDF for 'development': N=10, df=2, idf=1.4816
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Term 'development' in doc 3: tf=1, dl=23, score=1.4365
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - IDF for 'JavaScript': N=10, df=2, idf=1.4816
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Term 'JavaScript' in doc 3: tf=1, dl=23, score=1.4365
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Document 3 total score: 3.9833
2026-05-09 11:05:06,557 - bm25_engine - DEBUG - Term contributions: {'web': 1.1102748384448504, 'development': 1.4365049663977738, 'JavaScript': 1.4365049663977738}
2026-05-09 11:05:06,557 - bm25_engine - INFO - Returning top 3 results
2026-05-09 11:05:06,557 - bm25_engine - INFO - Rank 1: Document 3 (score: 3.9833)
2026-05-09 11:05:06,558 - bm25_engine - INFO - Rank 2: Document 1 (score: 3.1804)
2026-05-09 11:05:06,558 - bm25_engine - INFO - Rank 3: Document 0 (score: 2.5995)

  #1 Web Development (Score: 3.983)
     Matched terms: web, development, JavaScript
     Preview: Web development involves HTML for structure, CSS for styling, and JavaScript for interactivity. Mode...

  #2 JavaScript Essentials (Score: 3.180)
     Matched terms: web, JavaScript
     Preview: JavaScript powers the interactive web. It runs in browsers and on servers with Node.js. Modern JavaS...

  #3 Python Overview (Score: 2.600)
     Matched terms: web, development
     Preview: Python is a versatile programming language widely used for web development, data science, machine le...

🔍 Query: 'database SQL NoSQL'
----------------------------------------
2026-05-09 11:05:06,558 - bm25_engine - INFO - Executing search query: 'database SQL NoSQL'
2026-05-09 11:05:06,558 - bm25_engine - INFO - Searching for: 'database SQL NoSQL'
2026-05-09 11:05:06,558 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,558 - bm25_engine - DEBUG - Tokenizing text of length 18
2026-05-09 11:05:06,558 - bm25_engine - DEBUG - Found 3 raw tokens
2026-05-09 11:05:06,558 - bm25_engine - DEBUG - After removing stop words: 3 tokens
2026-05-09 11:05:06,558 - bm25_engine - INFO - Query terms after processing: ['database', 'SQL', 'NoSQL']
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - Term 'database' appears in 0 documents
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - Term 'SQL' appears in 1 documents
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - Term 'NoSQL' appears in 1 documents
2026-05-09 11:05:06,559 - bm25_engine - INFO - Found 1 candidate documents
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - IDF for 'SQL': N=10, df=1, idf=1.9924
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - Term 'SQL' in doc 5: tf=1, dl=21, score=2.0135
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - IDF for 'NoSQL': N=10, df=1, idf=1.9924
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - Term 'NoSQL' in doc 5: tf=1, dl=21, score=2.0135
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - Document 5 total score: 4.0270
2026-05-09 11:05:06,559 - bm25_engine - DEBUG - Term contributions: {'database': 0, 'SQL': 2.013501694046507, 'NoSQL': 2.013501694046507}
2026-05-09 11:05:06,559 - bm25_engine - INFO - Returning top 1 results
2026-05-09 11:05:06,559 - bm25_engine - INFO - Rank 1: Document 5 (score: 4.0270)

  #1 Database Systems (Score: 4.027)
     Matched terms: SQL, NoSQL
     Preview: Databases store and manage data persistently. SQL databases like PostgreSQL use structured tables, w...

🔍 Query: 'cloud computing AWS'
----------------------------------------
2026-05-09 11:05:06,559 - bm25_engine - INFO - Executing search query: 'cloud computing AWS'
2026-05-09 11:05:06,560 - bm25_engine - INFO - Searching for: 'cloud computing AWS'
2026-05-09 11:05:06,560 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - Tokenizing text of length 19
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - Found 3 raw tokens
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - After removing stop words: 3 tokens
2026-05-09 11:05:06,560 - bm25_engine - INFO - Query terms after processing: ['cloud', 'computing', 'AWS']
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - Term 'cloud' appears in 1 documents
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - Term 'computing' appears in 1 documents
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - Term 'AWS' appears in 1 documents
2026-05-09 11:05:06,560 - bm25_engine - INFO - Found 1 candidate documents
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - IDF for 'cloud': N=10, df=1, idf=1.9924
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - Term 'cloud' in doc 6: tf=2, dl=20, score=2.9116
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - IDF for 'computing': N=10, df=1, idf=1.9924
2026-05-09 11:05:06,560 - bm25_engine - DEBUG - Term 'computing' in doc 6: tf=1, dl=20, score=2.0570
2026-05-09 11:05:06,561 - bm25_engine - DEBUG - IDF for 'AWS': N=10, df=1, idf=1.9924
2026-05-09 11:05:06,561 - bm25_engine - DEBUG - Term 'AWS' in doc 6: tf=1, dl=20, score=2.0570
2026-05-09 11:05:06,561 - bm25_engine - DEBUG - Document 6 total score: 7.0256
2026-05-09 11:05:06,561 - bm25_engine - DEBUG - Term contributions: {'cloud': 2.9116226705753223, 'computing': 2.0570107342539945, 'AWS': 2.0570107342539945}
2026-05-09 11:05:06,561 - bm25_engine - INFO - Returning top 1 results
2026-05-09 11:05:06,561 - bm25_engine - INFO - Rank 1: Document 6 (score: 7.0256)

  #1 Cloud Computing (Score: 7.026)
     Matched terms: cloud, computing, AWS
     Preview: Cloud computing provides scalable infrastructure on demand. AWS, Google Cloud, and Azure offer servi...

🔍 Query: 'Python programming'
----------------------------------------
2026-05-09 11:05:06,561 - bm25_engine - INFO - Executing search query: 'Python programming'
2026-05-09 11:05:06,561 - bm25_engine - INFO - Searching for: 'Python programming'
2026-05-09 11:05:06,561 - bm25_engine - INFO - TextProcessor initialized with 61 stop words
2026-05-09 11:05:06,561 - bm25_engine - DEBUG - Tokenizing text of length 18
2026-05-09 11:05:06,561 - bm25_engine - DEBUG - Found 2 raw tokens
2026-05-09 11:05:06,561 - bm25_engine - DEBUG - After removing stop words: 2 tokens
2026-05-09 11:05:06,561 - bm25_engine - INFO - Query terms after processing: ['python', 'programming']
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Term 'python' appears in 1 documents
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Term 'programming' appears in 2 documents
2026-05-09 11:05:06,562 - bm25_engine - INFO - Found 2 candidate documents
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - IDF for 'python': N=10, df=1, idf=1.9924
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Term 'python' in doc 0: tf=1, dl=22, score=1.9718
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - IDF for 'programming': N=10, df=2, idf=1.4816
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Term 'programming' in doc 0: tf=1, dl=22, score=1.4663
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Document 0 total score: 3.4381
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Term contributions: {'python': 1.9717950996934144, 'programming': 1.4662599599480153}
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - IDF for 'programming': N=10, df=2, idf=1.4816
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Term 'programming' in doc 9: tf=1, dl=20, score=1.5296
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Document 9 total score: 1.5296
2026-05-09 11:05:06,562 - bm25_engine - DEBUG - Term contributions: {'python': 0, 'programming': 1.5296277373287221}
2026-05-09 11:05:06,562 - bm25_engine - INFO - Returning top 2 results
2026-05-09 11:05:06,562 - bm25_engine - INFO - Rank 1: Document 0 (score: 3.4381)
2026-05-09 11:05:06,562 - bm25_engine - INFO - Rank 2: Document 9 (score: 1.5296)

  #1 Python Overview (Score: 3.438)
     Matched terms: python, programming
     Preview: Python is a versatile programming language widely used for web development, data science, machine le...

  #2 APIs and Integration (Score: 1.530)
     Matched terms: programming
     Preview: APIs (Application Programming Interfaces) enable communication between software systems. REST APIs u...

============================================================
 Interactive Search
============================================================

Now you can try your own searches!
Type 'quit' to exit, 'stats' for statistics, or enter a search query.

Enter search query: