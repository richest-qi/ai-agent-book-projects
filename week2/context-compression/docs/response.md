======================================================================
CONTEXT COMPRESSION RESEARCH AGENT - INTERACTIVE DEMO
======================================================================

This demo allows you to test different compression strategies
for researching OpenAI co-founders' current affiliations.

Available Compression Strategies:
1. No Compression (expected to fail with large contexts)
2. Non-Context-Aware: Individual Summaries (summarize each page, then concatenate)
3. Non-Context-Aware: Combined Summary (concatenate all pages, then summarize once)
4. Context-Aware Summarization
5. Context-Aware with Citations
6. Windowed Context (only compress when approaching context limit)

Select strategy (1-6): 1

Selected: no_compression
Streaming output: ENABLED

Initializing agent...
2026-04-16 15:09:22,710 - INFO - compression_strategies - Context compressor initialized with strategy: no_compression, streaming: True
2026-04-16 15:09:22,711 - INFO - agent - Agent initialized with compression strategy: no_compression

Starting research task...
Task: Find current affiliations of all OpenAI co-founders

----------------------------------------------------------------------

============================================================
Starting research with no_compression strategy
============================================================

📍 Iteration 1/50
📊 Cumulative Token Usage - Prompt: 0, Completion: 0, Total: 0
2026-04-16 15:09:27,508 - INFO - httpx - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant: I'll help you research the current affiliations of all OpenAI co-founders. Let me start by searching for the complete list of OpenAI co-founders.

2026-04-16 15:09:30,699 - INFO - agent - 🔢 Kimi API Token Usage - Prompt: 334, Completion: 55, Total: 389

🤖 Assistant: I'll help you research the current affiliations of all OpenAI co-founders. Let me start by searching for the complete list of OpenAI co-founders.

🔧 Executing: search_web
   Args: {'query': 'OpenAI co-founders complete list founders'}
2026-04-16 15:09:30,700 - INFO - web_tools - Searching web for: OpenAI co-founders complete list founders
2026-04-16 15:09:32,893 - INFO - web_tools - Fetching webpage: https://www.reddit.com/r/OpenAI/comments/1m80e9g/the_11_cofounders_of_openai_in_2025/
2026-04-16 15:09:34,796 - INFO - web_tools - Fetching webpage: https://en.wikipedia.org/wiki/OpenAI
2026-04-16 15:09:38,417 - INFO - web_tools - Fetching webpage: https://techcrunch.com/2026/02/20/the-openai-mafia-15-of-the-most-notable-startups-founded-by-alumni/
2026-04-16 15:09:40,774 - INFO - web_tools - Fetching webpage: https://observer.com/2024/07/openai-founders-career/
2026-04-16 15:09:43,097 - INFO - web_tools - Fetching webpage: https://www.lxahub.com/stories/the-history-of-openai
   📄 Result size: 125,597 characters

📍 Iteration 2/50
📊 Cumulative Token Usage - Prompt: 334, Completion: 55, Total: 389
2026-04-16 15:09:53,424 - INFO - httpx - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant: Based on the search results, I can see that OpenAI was founded in 2015 with 11 co-founders. From the Wikipedia page, I can identify the complete list of co-founders. Let me now search for each individual co-founder to find their current affiliations.

2026-04-16 15:09:57,148 - INFO - agent - 🔢 Kimi API Token Usage - Prompt: 33164, Completion: 82, Total: 33246

🤖 Assistant: Based on the search results, I can see that OpenAI was founded in 2015 with 11 co-founders. From the Wikipedia page, I can identify the complete list of co-founders. Let me now search for each individual co-founder to find their current affiliations.

🔧 Executing: search_web
   Args: {'query': 'Sam Altman current position OpenAI 2026'}
2026-04-16 15:09:57,149 - INFO - web_tools - Searching web for: Sam Altman current position OpenAI 2026
2026-04-16 15:09:59,005 - INFO - web_tools - Fetching webpage: https://fortune.com/2026/03/21/openai-double-headcount-this-year-sam-altman-anthropic-google/
2026-04-16 15:10:01,320 - INFO - web_tools - Fetching webpage: https://en.wikipedia.org/wiki/Sam_Altman
2026-04-16 15:10:03,904 - INFO - web_tools - Fetching webpage: https://www.forbes.com/sites/richardnieva/2026/02/03/sam-altman-explains-the-future/
2026-04-16 15:10:05,281 - ERROR - web_tools - Error fetching webpage https://www.forbes.com/sites/richardnieva/2026/02/03/sam-altman-explains-the-future/: 403 Client Error: Forbidden for url: https://www.forbes.com/sites/richardnieva/2026/02/03/sam-altman-explains-the-future/
2026-04-16 15:10:05,783 - INFO - web_tools - Fetching webpage: https://www.linkedin.com/pulse/enterprise-top-openai-priority-2026-sam-altman-tells-nyc-kantrowitz-9rarc
2026-04-16 15:10:08,645 - INFO - web_tools - Fetching webpage: https://www.youtube.com/watch?v=fsvpUQDdC8Q
2026-04-16 15:10:12,262 - ERROR - web_tools - Error fetching webpage https://www.youtube.com/watch?v=fsvpUQDdC8Q: 429 Client Error: Too Many Requests for url: https://www.google.com/sorry/index?continue=https://www.youtube.com/watch%3Fv%3DfsvpUQDdC8Q&q=EhAqCbrBdqAamAAAAAAD_wBDGNGWgs8GIjC--bwkaEt5qH5zmINTMvygQgDMccfnI8VaUglkSyPCYj_LBvESYKlsyskgfXX3l3UyAnJSWgFD
   📄 Result size: 92,005 characters

📍 Iteration 3/50
📊 Cumulative Token Usage - Prompt: 33,498, Completion: 137, Total: 33,635
2026-04-16 15:10:22,960 - INFO - httpx - HTTP Request: POST https://api.moonshot.cn/v1/chat/completions "HTTP/1.1 200 OK"

🤖 Assistant: Now let me search for the other co-founders. Let me start with Greg Brockman:

2026-04-16 15:10:24,559 - INFO - agent - 🔢 Kimi API Token Usage - Prompt: 59488, Completion: 44, Total: 59532

🤖 Assistant: Now let me search for the other co-founders. Let me start with Greg Brockman:

🔧 Executing: search_web
   Args: {'query': 'Greg Brockman current position OpenAI 2026'}
2026-04-16 15:10:24,560 - INFO - web_tools - Searching web for: Greg Brockman current position OpenAI 2026
2026-04-16 15:10:26,813 - INFO - web_tools - Fetching webpage: https://www.reddit.com/r/singularity/comments/1q107i2/openai_cofounder_greg_brockman_on_2026_enterprise/
2026-04-16 15:10:28,831 - INFO - web_tools - Fetching webpage: https://cryptobriefing.com/greg-brockman-agi-will-emerge-in-the-next-few-years-openai-is-shifting-to-real-world-applications-and-robotics-will-transform-with-ai-integration-big-technology/
2026-04-16 15:10:31,788 - INFO - web_tools - Fetching webpage: https://www.linkedin.com/in/thegdb
2026-04-16 15:10:34,424 - INFO - web_tools - Fetching webpage: https://pmwcintl.com/speaker/greg-brockman-222_openai_2026sv/
2026-04-16 15:10:36,815 - INFO - web_tools - Fetching webpage: https://www.instagram.com/popular/greg-brockman-current-role-openai-2026/
   📄 Result size: 73,137 characters

📍 Iteration 4/50
📊 Cumulative Token Usage - Prompt: 92,986, Completion: 181, Total: 93,167


Demo interrupted by user

Try another strategy? (y/n): n

Thank you for using the demo!