## System Hint简介
一个实际的场景：Agent需要通过打电话来处理用户的业务请求，System Prompt要求拨打每个商家的电话不能超过3次。但Agent怎么知道到底打了几次呢?    
虽然通话记录被保存了下来，但Agent需要花费额外的reasoning tokens去扫描上下文中的通话记录，重新统计和计算。    
如果我们在每个电话的工具调用结果中直接加入这个电话的重复呼叫次数，如"本次是第3次呼叫该客户"，模型就能立即发现已经达到限制，不再继续呼叫。   

- 将隐式状态显式化
- 将分散信息集中化
- 将原始数据提炼为可直接使用的知识  


在长上下文场景中，模型的注意力资源是有限的。随着上下文长度的增加，模型必须在更多候选内容之间分配注意力，这导致关键信息可能无法获得足够的注意力权重。特别是在复杂的Agent轨迹中，早期的任务目标和关键约束容易被后续大量的工具调用结果所淹没。模型会过度关注最近的上下文内容，而对位于上下文中部的信息产生"注意力衰减"现象。   
是的，这就导致了前文提到的：无线循环、状态遗忘、任务目标偏离等情况。   


System Hint，以结构化的元数据嵌入到上下文中。  
System Hint，可以作为一个特殊的用户信息或工具调用结果，追加在Agent执行轨迹的末尾，但不记录在Agent执行轨迹中。在每一轮推理开始前，System Hint为模型提供及时引导，确保其在复杂的任务执行中保持清晰的方向感和状态感知。  


### Cursor的理解

有两份"列表"：
1. 给大模型看的输入列表
2. 保存到`trajectory.json`的历史列表  

这句话的意思是：
- System Hint会被放入第1份列表的最后一条，让模型在本轮能看到。
- 但不会写进第2份列表，所以你回看`trajectory.json`看不到它。   

极简伪代码如下：  
```
history = load_trajectory_events()  # 持久化历史
hint = build_system_hint()          # 临时提示

# 调模型时
model_input = history + [hint]      # 追加在末尾（仅本轮）
resp = llm(model_input)

# 落盘时
save_trajectory(history + [resp])   # 不把 hint 写入
```  

一句话："追加"是给模型临时看的；"不记录"是不给日志永久存。     
更好理解的一句话是：System Hint参与计算，但不参与记忆。  

为什么要这么设计？    
因为这是一种“既要效果，又要干净日志”的折中设计，核心原因有4个：  
- 不污染长期记忆：System Hint常是动态信息（当前目录、工具状态、时间戳、重试建议）。这些不该变成"历史事实"。
- 保持轨迹可审计：`trajectory.json`只记录真正发生的user/assistant/tool事件，回放时更清晰，不会混入一堆运行噪音。
- 避免上下文膨胀：如果每轮都把hint写入历史，消息会越来越长，成本更好、性能更差，还容易分散模型注意力。
- 便于策略热更新：你随时改hint生成逻辑，比如新加"防循环提醒"，不需要旧轨迹。


### Claude的理解
1. 追加到执行轨迹末尾  
意味着它在运行时会被插入到Agent当前处理的上下文中，Agent能够"看到"并利用来影响下一步行为。  
2. 但不记录在执行轨迹中  
意味着它不会被持久化到Agent的历史记忆/轨迹存储里。下一轮执行时，这条信息就消失了，不会成为对话历史的一部分。  

#### 用一个具体类比类理解
想象Agent的执行轨迹是一条纸带：  
```
[用户输入] → [工具调用A] → [工具结果A] → [工具调用B] → ...
     ↑ 这些都会被永久记录在纸带上
     
System Hint：像一张"便利贴"，临时贴在纸带末尾，
             Agent当前能读到它，但它不会印在纸带上。
```
#### 为什么这样设计？
1. 能被Agent读到：可以在关键时刻注入外部信号，干扰Agent行为，如超时提醒、安全警告、资源限制
2. 不记录在轨迹中：不污染历史上下文，不影响后续的推理/回放/调试，保持轨迹的“纯洁性”。  

#### 典型使用场景
- 超时警告："你已执行15步，请尽快收敛给出最终答案"
- 安全熔断："检测到敏感操作，请停止并请求用户确认"
- 环境状态同步："外部系统状态已变更为X，请重新规划"
- 资源提示："Token预算剩余不足，请简化输出"

## System Hint实践
- timestamp，时间戳
- tool_call_counts，工具调用次数
- todo_list，todo列表
- detail_error，详细错误信息
- system_state，系统状态

### timestamp
在实现中，系统为每条用户消息和工具调用结果添加精确到秒的时间戳。那时间戳应该放在哪里?  
**不能放在系统提示词中，应该放在用户消息和工具响应中**。  
- `{role:"system",content:""}`,NO
- `{role:"user",content:""}`，YES
- `{role:"assistant",content:""}`，YES

### tool_call_counts
`tool_call_counts`，记录工具被调用的次数。  
当模型看到某个工具已经被调用多次，比如超过3次，仍然失败时，它会主动改变策略，而不是机械地重试。  
在我们的实验中，当Agent尝试读取不存在的文件时，  
- 第一次失败后，它会检查路径
- 第二次失败后，它会列出目录内容  
- 第三次失败后，它会主动放弃并寻找替代方案

### todo_list
每个TODO项，包含
- 唯一标识符
- 内容描述
- 状态
    - pending
    - in_progress
    - completed
    - cancelled
- 时间戳  

系统提供了两个专门的工具：
- `rewrite_todo_list`，用于创建和重写待办事项
- `update_todo_list`，用于更新任务状态

当Agent接收到包含3个或者更多独立步骤的复杂任务时，**系统提示词中的规则会引导它立即创建TODO列表**，且这个列表不是静态的，而是动态的工作记忆。Agent在执行过程中会不断更新任务状态：
- 开始某项任务时，标记为`in_progress`
- 完成后，标记为`completed`
- 遇到障碍时，可能标记为`cancelled`，并添加新的替代任务  

TODO列表，起到了外部记忆的作用。    
每次迭代时，**TODO列表会作为系统状态的一部分出现在上下文的末尾**。

### detail_error
在我们的实现中，错误信息包含4个层次的内容：
- 问题概要：错误类型、基本描述
- 完整的参数信息：以JSON格式展示失败操作的所有输入参数
- 调用栈信息
- 修复建议。修复建议与错误类型相匹配，比如
    - `FileNotFoundError`，会建议
        - 验证文件路径是否存在
        - 检查当前工作目录
        - 使用绝对路径或创建文件
    - `PermissionError`，会建议
        - 检查文件权限
        - 尝试使用不同目录  
          
    这些建议不是硬编码的模板，而是根据具体错误上下文动态生成的。

### system_status
当前环境信息，包括当前时间、工作目录、操作系统类型、Shell环境和Python版本等。  
比如**当前工作目录**，
- 在上下文中明确显示当前工作目录，Agent能正确解析相对路径，避免找不到文件。
- 当Agent执行`cd`改变目录时，系统会自动更新内部的`current_directory`变量，确保后续操作在正确的上下文中执行。  

比如**操作系统和Shell环境**，
- 在Windows系统上使用`dir`命令，而不是`ls`
- 在Linux系统上使用`apt`，而在macOS上使用`brew`

## 上下文工程
System Prompt  
System Hint   
都属于**上下文工程**的范畴，都是在**上下文设计**这方面下功夫。



- System Prompt
```
You are an intelligent assistant with access to various tools for file operations, code execution, and system commands.

Your task is to complete the given objectives efficiently using the available tools. Think step by step and use tools as needed.

## TODO List Management Rules:
- For any complex task with 3+ distinct steps, immediately create a TODO list using `rewrite_todo_list`
- Break down the user's request into specific, actionable TODO items
- Update TODO items to 'in_progress' when starting work on them using `update_todo_status`
- Mark items as 'completed' immediately after finishing them
- Only have ONE item 'in_progress' at a time
- If you encounter errors or need to change approach, update relevant TODOs to 'cancelled' and add new ones
- Use the TODO list as your primary planning and tracking mechanism
- Reference TODO items by their ID when discussing progress

## Key Behaviors:
1. ALWAYS start complex tasks by creating a TODO list
2. Pay attention to timestamps to understand the timeline of events
3. Notice tool call numbers (e.g., "Tool call #3") to avoid repetitive loops - if you see high numbers, change strategy
4. Learn from detailed error messages to fix issues and adapt your approach
5. Be aware of your current directory and system environment shown in system state
6. When exploring projects, systematically read key files (README, main.py, agent.py) to understand structure

## Error Handling:
- Read error messages carefully - they contain specific information about what went wrong
- Use the suggestions provided in error messages to fix issues
- If a tool fails multiple times (check the call number), try a different approach
- Common fixes: check file paths, verify current directory, ensure proper permissions

Important: When you have completed all tasks, clearly state "FINAL ANSWER:" followed by a comprehensive summary of what was accomplished.
```
- User Prompt
```
[2026-04-14 10:33:54] Analyze and summarize the AI Agent projects in week1 and week2 directories. Create a comprehensive analysis file 'project_analysis_report.md' containing:

   - Overview of all the projects in week1 and week2 directories
   - What you have learned from the projects
```
- System State → User Prompt
```
Current Time: 2026-04-14 10:50:18
Current Directory: E:\ai&ai agent\github\ai-agent-book-projects\week2
System: Windows (10)
Shell Environment: Windows Command Prompt or PowerShell
Python Version: 3.11.4
```


```json
[{'content': 'You are an intelligent...', 'role': 'system'},
{'content': '[2026-04-14 10:33:54] Analyze and summarize...', 'role': 'user'}, 
{'content': '=== SYSTEM STATE ===', 'role': 'user'}]
```

```json
[{'content': 'You are an intelligent assistant...', 'role': 'system'}, 
{'content': '[2026-04-15 09:40:28] Analyze and summarize...', 'role': 'user'}, 
{'annotations': None, 'audio': None, 'content': 'I'll analyze and summarize the AI Agent projects in both week1 and week2 directories. Let me start by creating a TODO list to organize this comprehensive analysis.', 'function_call': None, 'refusal': None, 'role': 'assistant', 'tool_calls': [{'function': {'arguments': '{"items": ["Explore week1 directory structure and identify all projects", "Read and analyze each project in week1 directory", "Explore week2 directory structure and identify all projects", "Read and analyze each project in week2 directory", "Synthesize learnings from both weeks' projects", "Create comprehensive project_analysis_report.md file"]}', 'name': 'rewrite_todo_list'}, 'id': 'rewrite_todo_list:0', 'index': 0, 'type': 'function'}]}]
```

```json
[{'content': 'You are an intelligent assistant...', 'role': 'system'}, 
{'content': '[2026-04-15 09:40:28] Analyze and summarize...', 'role': 'user'}, 
{'annotations': None, 'audio': None, 'content': 'I'll analyze and summarize the AI Agent projects in both week1 and week2 directories. Let me start by creating a TODO list to organize this comprehensive analysis.', 'function_call': None, 'refusal': None, 'role': 'assistant', 'tool_calls': [{'function': {'arguments': '{"items": ["Explore week1 directory structure and identify all projects", "Read and analyze each project in week1 directory", "Explore week2 directory structure and identify all projects", "Read and analyze each project in week2 directory", "Synthesize learnings from both weeks' projects", "Create comprehensive project_analysis_report.md file"]}', 'name': 'rewrite_todo_list'}, 'id': 'rewrite_todo_list:0', 'index': 0, 'type': 'function'}]}, 
{'content': '[2026-04-15 10:12:06] [Tool call #1 for 'rewrite_todo_list']
{"success": true, "kept_items": 0, "new_items": 6, "total_items": 6}', 'role': 'tool', 'tool_call_id': 'rewrite_todo_list:0'}]
```

```json
[{'content': 'You are an intelligent assistant...', 'role': 'system'}, 
{'content': '[2026-04-15 09:40:28] Analyze and summarize...', 'role': 'user'}, 
{'annotations': None, 'audio': None, 'content': 'I'll analyze and summarize the AI Agent projects in both week1 and week2 directories. Let me start by creating a TODO list to organize this comprehensive analysis.', 'function_call': None, 'refusal': None, 'role': 'assistant', 'tool_calls': [{'function': {'arguments': '{"items": ["Explore week1 directory structure and identify all projects", "Read and analyze each project in week1 directory", "Explore week2 directory structure and identify all projects", "Read and analyze each project in week2 directory", "Synthesize learnings from both weeks' projects", "Create comprehensive project_analysis_report.md file"]}', 'name': 'rewrite_todo_list'}, 'id': 'rewrite_todo_list:0', 'index': 0, 'type': 'function'}]}, 
{'content': '[2026-04-15 10:12:06] [Tool call #1 for 'rewrite_todo_list']
{"success": true, "kept_items": 0, "new_items": 6, "total_items": 6}', 'role': 'tool', 'tool_call_id': 'rewrite_todo_list:0'}, 
{'content': '=== SYSTEM STATE ===
Current Time: 2026-04-15 10:33:16
Current Directory: E:\ai&ai agent\github\ai-agent-book-projects\week2
System: Windows (10)
Shell Environment: Windows Command Prompt or PowerShell
Python Version: 3.11.4

=== CURRENT TASKS ===
TODO List:
  [7] ⏳ Explore week1 directory structure and identify all projects (pending)
  [8] ⏳ Read and analyze each project in week1 directory (pending)
  [9] ⏳ Explore week2 directory structure and identify all projects (pending)
  [10] ⏳ Read and analyze each project in week2 directory (pending)
  [11] ⏳ Synthesize learnings from both weeks' projects (pending)
  [12] ⏳ Create comprehensive project_analysis_report.md file (pending)
', 'role': 'user'}]
```

- conversation_history
```json
[{'content': 'You are an intelligent assistant...', 'role': 'system'}, 
{'content': '[2026-04-16 09:05:59] Analyze and summarize...', 'role': 'user'}, {'annotations': None, 'audio': None, 'content': 'I'll analyze the AI Agent projects in both week1 and week2 directories and create a comprehensive analysis report. Let me start by exploring the project structure and understanding what's in each directory.', 'function_call': None, 'refusal': None, 'role': 'assistant', 'tool_calls': [{'function': {'arguments': '{"items": ["Explore week1 directory structure and identify projects", "Analyze each project in week1 directory", "Explore week2 directory structure and identify projects", "Analyze each project in week2 directory", "Document key learnings from both weeks", "Create comprehensive project_analysis_report.md file"]}', 'name': 'rewrite_todo_list'}, 'id': 'rewrite_todo_list:0', 'index': 0, 'type': 'function'}]}, 
{'content': '[2026-04-16 09:11:51] [Tool call #1 for 'rewrite_todo_list']
{"success": true, "kept_items": 0, "new_items": 6, "total_items": 6}', 'role': 'tool', 'tool_call_id': 'rewrite_todo_list:0'},
 {'annotations': None, 'audio': None, 'content': 'Let me start by exploring the week1 directory structure to identify the projects there.', 'function_call': None, 'refusal': None, 'role': 'assistant', 'tool_calls': [{'function': {'arguments': '{"updates": [{"id": 1, "status": "in_progress"}]}', 'name': 'update_todo_status'}, 'id': 'update_todo_status:1', 'index': 0, 'type': 'function'}]}]
```

```json
[{'content': 'You are an intelligent assistant...', 'role': 'system'}, 
{'content': '[2026-04-16 09:05:59] Analyze and summarize...', 'role': 'user'}, {'content': 'I'll analyze...', 'role': 'assistant'}, 
{'content': '[2026-04-16 09:11:51] [Tool call #1 for 'rewrite_todo_list']', 'role': 'tool'},
 {'content': 'Let me start by exploring the week1 ...', 'role': 'assistant'}]
```

- conversation_history
```json
[{'content': 'You are an intelligent assistant...', 'role': 'system'}, 
{'content': '[2026-04-16 09:05:59] Analyze and summarize...', 'role': 'user'}, {'content': 'I'll analyze...', 'role': 'assistant'}, 
{'content': '[2026-04-16 09:11:51] [Tool call #1 for 'rewrite_todo_list']', 'role': 'tool'}, 
{'content': 'Let me start..., 'role': 'assistant'}, 
{'content': '[2026-04-16 09:30:21] [Tool call #1 for 'update_todo_status']
'role': 'tool'}]
```

```json
[{'content': 'You are an intelligent assistant...', 'role': 'system'},
 {'content': '[2026-04-16 09:05:59] Analyze and summarize ...', 'role': 'user'}, {'content': 'I'll analyze...', 'role': 'assistant'}, 
 {'content': '[2026-04-16 09:11:51] [Tool call #1 for 'rewrite_todo_list']', 'role': 'tool'}, 
 {'content': 'Let me start...', 'role': 'assistant'}, 
 {'content': '[2026-04-16 09:30:21] [Tool call #1 for 'update_todo_status']', 'role': 'tool'}, 
 {'content': 'I can see I'm currently in the week2 directory. Let me first ...''role': 'assistant'}, 
 {'content': '[2026-04-16 09:51:34] [Tool call #1 for 'execute_command']', 'role': 'tool'}]
```

- message_to_send
```json
[{'content': 'You are an intelligent...', 'role': 'system'}, 
{'content': '[2026-04-16 09:05:59] Analyze and summarize...', 'role': 'user'}, {'content': 'I'll analyze...','role': 'assistant'}, 
{'content': '[2026-04-16 09:11:51] [Tool call #1 for 'rewrite_todo_list']', 'role': 'tool'}, 
{'content': 'Let me start...', 'role': 'assistant'},
{'content': '[2026-04-16 09:30:21] [Tool call #1 for 'update_todo_status']', 'role': 'tool', }, 
{'content': '=== SYSTEM STATE ===
Current Time: 2026-04-16 09:34:41
Current Directory: E:\ai&ai agent\github\ai-agent-book-projects\week2
System: Windows (10)
Shell Environment: Windows Command Prompt or PowerShell
Python Version: 3.11.4

=== CURRENT TASKS ===
TODO List:
  [1] 🔄 Explore week1 directory structure and identify projects (in_progress)
  [2] ⏳ Analyze each project in week1 directory (pending)
  [3] ⏳ Explore week2 directory structure and identify projects (pending)
  [4] ⏳ Analyze each project in week2 directory (pending)
  [5] ⏳ Document key learnings from both weeks (pending)
  [6] ⏳ Create comprehensive project_analysis_report.md file (pending)
', 'role': 'user'}]
```