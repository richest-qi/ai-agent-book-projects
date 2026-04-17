- messages，调用大模型接口时，给大模型发送的消息。

```json
[{'role': 'system','content': 'You are a research assistant...', }, 
{'role': 'user','content': 'Please research and find the current affiliations of all OpenAI co-founders.'}, 
{'role': 'assistant','content': 'I'll help you research...',}, 
{'role': 'tool', 'content': 'OpenAI was founded on December 8, 2015.  
The original 11 co-founders are:

1. Sam Altman (still at OpenAI, CEO)  
2. Elon Musk (left)  
3. Ilya Sutskever (left May 2024)  
4. Greg Brockman (still at OpenAI, President)  
5. Trevor Blackwell  
6. Vicki Cheung  
7. Andrej Karpathy  
8. Durk Kingma  
9. John Schulman (still at OpenAI)  
10. Pamela Vagata  
11. Wojciech Zaremba

Only four of these founders remain with the company today: Sam Altman, Greg Brockman, John Schulman, and Wojciech Zaremba.'}]
```


```json
[{'content': 'You are a research assistant tasked with finding information about OpenAI co-founders.

Your task is to:
1. First, search for and identify ALL OpenAI co-founders
2. Then, search for EACH co-founder individually to find their CURRENT affiliations
3. Compile a comprehensive report with current status for each co-founder

Important instructions:
- Be thorough and systematic - search for each person individually
- Focus on CURRENT affiliations, not historical roles
- Include company names, positions, and any recent changes
- If someone left a position, note where they went
- When you have gathered all information, provide a FINAL ANSWER with a complete list

Available tools:
- search_web: Search the web for information
- fetch_webpage: Fetch specific webpage content

Start by searching for the complete list of OpenAI co-founders.

TODAY'S DATE: Friday, April 17, 2026', 'role': 'system'}, 
{'content': 'Please research and find the current affiliations of all OpenAI co-founders.', 'role': 'user'}, {'content': 'I'll help you research the current affiliations of all OpenAI co-founders. Let me start by searching for the complete list of OpenAI co-founders.', 'role': 'assistant', 'tool_calls': [{'function': {'arguments': '{"query": "OpenAI co-founders complete list founders original"}', 'name': 'search_web'}, 'id': 'search_web:0', 'type': 'function'}]}, 
{'content': 'OpenAI was founded on December 8, 2015.  
The original 11 co-founders are:

1. Sam Altman (still at OpenAI, CEO)  
2. Elon Musk (left)  
3. Ilya Sutskever (left May 2024)  
4. Greg Brockman (still at OpenAI, President)  
5. Trevor Blackwell  
6. Vicki Cheung  
7. Andrej Karpathy  
8. Durk Kingma  
9. John Schulman (still at OpenAI)  
10. Pamela Vagata  
11. Wojciech Zaremba

Only four of these founders remain with the company today: Sam Altman, Greg Brockman, John Schulman, and Wojciech Zaremba.', 'role': 'tool', 'tool_call_id': 'search_web:0'}]
```