## Response Context

============================================================
KV CACHE DEMONSTRATION - MODE SELECTION
============================================================

Select a mode to run:

  1. ✅ Correct Implementation - Optimal KV cache usage
  2. ❌ Dynamic System Prompt - Adds timestamps
  3. ❌ Shuffled Tools - Randomizes tool order
  4. ❌ Dynamic Profile - Updates user credits
  5. ❌ Sliding Window - Keeps only recent messages
  6. ❌ Text Format - Plain text instead of structured
  7. 📊 Compare All - Run all modes and compare

  0. Exit
------------------------------------------------------------

Enter your choice (0-7): 1

✓ Selected: ✅ Correct Implementation - Optimal KV cache usage
2026-03-30 13:39:10,719 - INFO - Running in mode: correct
2026-03-30 13:39:10,719 - INFO - Task: Please analyze and summarize all the projects in the week1 and week2 directories.
For each project:
1. Find all Python files
2. Read the main files and understand the functionality
3. Identify the key features and purpose
4. Provide a comprehensive summary

Start with week1 projects, then move to week2. Be thorough in your analysis.
2026-03-30 13:39:10,719 - INFO - ================================================================================
2026-03-30 13:39:10,771 - INFO - File tools initialized with root: E:\ai&ai agent\github\ai-agent-book-projects
2026-03-30 13:39:10,772 - INFO - Agent initialized with mode: correct, model: kimi-k2-0905-preview
2026-03-30 13:39:22,485 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant (Iteration 1):
----------------------------------------
I'll analyze the projects in the week1 and week2 directories systematically. Let me start by exploring the structure and finding all Python files.
----------------------------------------
2026-03-30 13:39:22,497 - INFO - Iteration 1 - TTFT: 11.725s, Tokens: prompt=462, completion=49, cached=462
2026-03-30 13:39:22,498 - INFO - Executing tool: find with args: {'pattern': '*.py', 'directory': 'week1'}
    ✓ find: Found 39 files
2026-03-30 13:39:27,099 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:39:27,099 - INFO - Iteration 2 - TTFT: 4.599s, Tokens: prompt=1003, completion=22, cached=256
2026-03-30 13:39:27,100 - INFO - Executing tool: find with args: {'pattern': '*.py', 'directory': 'week2'}
    ✓ find: Found 100 files
2026-03-30 13:39:38,275 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant (Iteration 3):
----------------------------------------
Now let me start analyzing the week1 projects. I'll begin by examining the main files in each project to understand their structure and purpose.
----------------------------------------
2026-03-30 13:39:38,276 - INFO - Iteration 3 - TTFT: 9.176s, Tokens: prompt=2785, completion=48, cached=768
2026-03-30 13:39:38,276 - INFO - Executing tool: read_file with args: {'file_path': 'week1/context/main.py'}
    ✓ read_file: Read 1056 lines
2026-03-30 13:39:43,161 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:39:43,162 - INFO - Iteration 4 - TTFT: 4.885s, Tokens: prompt=5264, completion=21, cached=2560
2026-03-30 13:39:43,163 - INFO - Executing tool: read_file with args: {'file_path': 'week1/context/agent.py'}
    ✓ read_file: Read 720 lines
2026-03-30 13:39:49,043 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:39:49,044 - INFO - Iteration 5 - TTFT: 5.879s, Tokens: prompt=7641, completion=25, cached=5120
2026-03-30 13:39:49,044 - INFO - Executing tool: read_file with args: {'file_path': 'week1/learning-from-experience/demo.py'}
    ✓ read_file: Read 209 lines
2026-03-30 13:39:54,478 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:39:54,479 - INFO - Iteration 6 - TTFT: 5.435s, Tokens: prompt=9584, completion=26, cached=7424
2026-03-30 13:39:54,479 - INFO - Executing tool: read_file with args: {'file_path': 'week1/learning-from-experience/game_environment.py'}
    ✓ read_file: Read 503 lines
2026-03-30 13:40:00,335 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:40:00,335 - INFO - Iteration 7 - TTFT: 5.853s, Tokens: prompt=12205, completion=22, cached=9472
2026-03-30 13:40:00,336 - INFO - Executing tool: read_file with args: {'file_path': 'week1/search-codegen/agent.py'}
    ✓ read_file: Read 363 lines
2026-03-30 13:40:06,747 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:40:06,748 - INFO - Iteration 8 - TTFT: 6.412s, Tokens: prompt=14715, completion=23, cached=12032
2026-03-30 13:40:06,748 - INFO - Executing tool: read_file with args: {'file_path': 'week1/web-search-agent/agent.py'}
    ✓ read_file: Read 245 lines
2026-03-30 13:40:14,504 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant (Iteration 9):
----------------------------------------
Now let me examine the week2 projects:
----------------------------------------
2026-03-30 13:40:14,505 - INFO - Iteration 9 - TTFT: 7.755s, Tokens: prompt=18680, completion=33, cached=14592
2026-03-30 13:40:14,505 - INFO - Executing tool: read_file with args: {'file_path': 'week2/attention_visualization/main.py'}
    ✓ read_file: Read 726 lines
2026-03-30 13:40:22,907 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:40:22,908 - INFO - Iteration 10 - TTFT: 8.402s, Tokens: prompt=21066, completion=23, cached=18432
2026-03-30 13:40:22,909 - INFO - Executing tool: read_file with args: {'file_path': 'week2/context-compression/main.py'}
    ✓ read_file: Read 195 lines
2026-03-30 13:40:30,723 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:40:30,724 - INFO - Iteration 11 - TTFT: 7.814s, Tokens: prompt=23123, completion=23, cached=20992
2026-03-30 13:40:30,724 - INFO - Executing tool: read_file with args: {'file_path': 'week2/kv-cache/main.py'}
    ✓ read_file: Read 369 lines
2026-03-30 13:40:39,270 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:40:39,271 - INFO - Iteration 12 - TTFT: 8.547s, Tokens: prompt=26234, completion=25, cached=23040
2026-03-30 13:40:39,271 - INFO - Executing tool: read_file with args: {'file_path': 'week2/local_llm_serving/main.py'}
    ✓ read_file: Read 650 lines
2026-03-30 13:40:43,208 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 429 Too Many Requests"
2026-03-30 13:40:43,209 - INFO - Retrying request to /chat/completions in 0.464743 seconds
2026-03-30 13:40:53,226 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:40:53,227 - INFO - Iteration 13 - TTFT: 13.955s, Tokens: prompt=28863, completion=25, cached=26112
2026-03-30 13:40:53,227 - INFO - Executing tool: read_file with args: {'file_path': 'week2/log-sanitization/main.py'}
    ✓ read_file: Read 181 lines
2026-03-30 13:41:01,961 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:41:01,961 - INFO - Iteration 14 - TTFT: 8.733s, Tokens: prompt=30554, completion=26, cached=28672
2026-03-30 13:41:01,962 - INFO - Executing tool: read_file with args: {'file_path': 'week2/prompt-engineering/run_ablation.py'}
    ✓ read_file: Read 365 lines
2026-03-30 13:45:34,366 - INFO - Retrying request to /chat/completions in 0.388070 seconds
2026-03-30 13:45:46,513 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant (Iteration 15):
----------------------------------------
Now let me examine a few more key files to get a complete picture:
----------------------------------------
2026-03-30 13:45:46,515 - INFO - Iteration 15 - TTFT: 284.551s, Tokens: prompt=33277, completion=36, cached=33277
2026-03-30 13:45:46,515 - INFO - Executing tool: read_file with args: {'file_path': 'week1/context/config.py'}
    ✓ read_file: Read 177 lines
2026-03-30 13:45:52,602 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant (Iteration 16):
----------------------------------------
Now let me check some additional key files to understand the structure better:
----------------------------------------
2026-03-30 13:45:52,604 - INFO - Iteration 16 - TTFT: 6.087s, Tokens: prompt=34973, completion=34, cached=33024
2026-03-30 13:45:52,604 - INFO - Executing tool: find with args: {'pattern': 'README*', 'directory': '.'}
    ✓ find: Found 79 files
2026-03-30 13:45:58,419 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:45:58,420 - INFO - Iteration 17 - TTFT: 5.688s, Tokens: prompt=36228, completion=21, cached=34816
2026-03-30 13:45:58,420 - INFO - Executing tool: read_file with args: {'file_path': 'week1/context/README.md'}
    ✓ read_file: Read 368 lines
2026-03-30 13:46:07,199 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant (Iteration 18):
----------------------------------------
Now let me check a few more README files to understand the projects better:
----------------------------------------
2026-03-30 13:46:07,200 - INFO - Iteration 18 - TTFT: 8.780s, Tokens: prompt=38845, completion=39, cached=36096
2026-03-30 13:46:07,200 - INFO - Executing tool: read_file with args: {'file_path': 'week2/attention_visualization/README.md'}
    ✓ read_file: Read 237 lines
2026-03-30 13:46:15,506 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"
2026-03-30 13:46:15,508 - INFO - Iteration 19 - TTFT: 8.306s, Tokens: prompt=40864, completion=23, cached=38656
2026-03-30 13:46:15,508 - INFO - Executing tool: read_file with args: {'file_path': 'week2/context-compression/README.md'}
    ✓ read_file: Read 264 lines
2026-03-30 13:46:29,505 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant (Iteration 20):
----------------------------------------
Based on my comprehensive analysis of the week1 and week2 projects, I can now provide a detailed summary. Let me examine a few more key files to ensure completeness:
----------------------------------------
2026-03-30 13:46:29,506 - INFO - Iteration 20 - TTFT: 13.998s, Tokens: prompt=43146, completion=60, cached=40704
2026-03-30 13:46:29,506 - INFO - Executing tool: find with args: {'pattern': '*.py', 'directory': 'week2/prompt-engineering'}
    ✓ find: Found 100 files
2026-03-30 13:51:01,662 - INFO - Retrying request to /chat/completions in 0.413646 seconds
2026-03-30 13:51:09,388 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 429 Too Many Requests"
2026-03-30 13:51:09,389 - INFO - Retrying request to /chat/completions in 0.791498 seconds
2026-03-30 13:51:14,766 - INFO - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 429 Too Many Requests"
2026-03-30 13:51:14,766 - ERROR - Error in iteration 21: Error code: 429 - {'error': {'message': 'The engine is currently overloaded, please try again later', 'type': 'engine_overloaded_error'}}

================================================================================
EXECUTION RESULTS - Mode: correct
================================================================================

📊 Performance Metrics:
  • Time to First Token (TTFT): 11.725 seconds
  • TTFT per iteration:
      Iteration 1: 11.725s
      Iteration 2: 4.599s
      Iteration 3: 9.176s
      Iteration 4: 4.885s
      Iteration 5: 5.879s
      Iteration 6: 5.435s
      Iteration 7: 5.853s
      Iteration 8: 6.412s
      Iteration 9: 7.755s
      Iteration 10: 8.402s
      Iteration 11: 7.814s
      Iteration 12: 8.547s
      Iteration 13: 13.955s
      Iteration 14: 8.733s
      Iteration 15: 284.551s
      Iteration 16: 6.087s
      Iteration 17: 5.688s
      Iteration 18: 8.780s
      Iteration 19: 8.306s
      Iteration 20: 13.998s
  • TTFT Analysis:
      First iteration: 11.725s
      Last iteration: 13.998s
      Average (after first): 22.361s
      Improvement: -19.4%
  • Total Execution Time: 723.995 seconds
  • Iterations: 21
  • Tool Calls: 20

🔄 Cache Statistics:
  • Cached Tokens: 386,507
  • Cache Hits: 20
  • Cache Misses: 0
  • Cache Hit Rate: 100.0%

💰 Token Usage:
  • Prompt Tokens: 429,512
  • Completion Tokens: 604
  • Total Tokens: 430,116
  • Cache Ratio: 90.0% of prompt tokens cached

🔧 Tool Calls Summary:
  • find: 4 calls
  • read_file: 16 calls

## 响应内容分析
**KV Cache是服务端能力。**  
这个例子中，KV Cache，是由Kimi（Moonshot）服务端做的缓存复用。  
这份代码做了两件事：
1. 通过"请求消息构造方式"来决定服务端能不能命中缓存
2. 从响应里的`useage.cached_tokens / cache_hits`看出是否命中  

这个例子说明了两件事：
- KV Cache在"正确实现"模式下确实被有效复用了。
- 第 1 轮 TTFT = 11.725s，到了第 2 轮 TTFT 掉到 4.599s，说明后续请求开始享受到缓存带来的加速（至少相对首轮更快）。
- 在`correct`模式下，第一次迭代构造messages，之后的每一轮迭代**不重建/不改写整体上下文结构**，而是持续追加，从而让后端能继续复用之前的KV缓存。而其他错误模式会在每轮迭代重建messsages，导致缓存失效，无法复用。  
```python
# agent.py
    if self.mode == KVCacheMode.CORRECT:
        # Correct mode: Build messages once, then keep using same list
        if iteration == 1:
            messages = self._format_messages(original_task)
    else:
        # Incorrect modes: Recreate messages from history each iteration
        # This forces cache invalidation due to context changes
        messages = self._format_messages(original_task)
```
- 外部服务（Moonshot/Kimi）限流/过载（429）会让整体跑不完，并让TTFT出现巨大异常
- `Iteration 15 - TTFT: 284.551s`，这一轮发生了**网络/队列/429重试延迟**这种外部因素，把"平均FFFT"严重拉坏。


