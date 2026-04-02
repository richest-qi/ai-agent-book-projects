当模型处理一个token时，注意力机制需要计算这个token和所有之前的token之间的注意力分数。  
这个计算过程涉及三个关键矩阵：
- 查询矩阵（Query）
- 键矩阵（Key）
- 值矩阵（Value）

当模型生成第一个token时，它需要计算整个输入序列的K、V矩阵。  
当模型生成第二个token时，输入序列中原有部分的K、V矩阵与之前完全相同，只有新生成的token需要计算新的键值对。  
如果我们缓存之前的计算结果，就可以避免重新计算，因此就有了KV Cache。  
正确利用KV Cache机制是降低成本和延迟的关键。    

KV Cache失效会带来两个直接的负面影响：
- 成本显著增加。当缓存失效时，模型需要重新处理整个上下文，这意味着以前已经处理过的token需要再次计费。
- TTFT大幅增加。TTFT，Time to first token，首个token生成时间。TTFT是衡量用户体验的关键指标，它决定了用户提交请求后等待多久才能看到第一个响应。当KV Cache失效时，模型必须重新处理整个上下文才能开始生成新的响应。


- `Dynamic System Prompt`：每轮 system prompt 都带新时间戳，前缀文本变了。
- `Shuffled Tools`：工具定义顺序被打乱，请求结构变了。
- `Dynamic Profile`：每轮多一条变化的用户资料消息，前缀变了。
- `Sliding Window`：历史消息集合每轮不同，前缀截断/滑动了。
- `Text Format`：把原本结构化消息重新拼成纯文本，格式变了。

而 `agent.py` 里最核心的对照点是：

- `correct` 模式：首轮构造一次 `messages`，后续持续追加，尽量保持稳定前缀。
- 其它模式：每轮重新 `_format_messages()`，更容易让前缀发生变化。

**KV Cache复用依赖"稳定的请求前缀"；只要system prompt、tools、history、message format这些前缀部分频繁变化，缓存命中就会显著下降。**

可以把"请求前缀"理解成：**本轮生成前，模型已经看到的那一大段token**。  
只要这段token和上一轮不一致，KV Cache复用就会变差。

## KV Cache机制

**Transformer模型原理上通常都有"KV Cache"这个机制**，这是自回归生成时常见的推理优化，用来避免重复计算前面token的key/value。  
Transformer模型通常都有KV Cache机制。但不是所有基于Transformer的模型服务都对外提供可观测、可利用的KV Cache复用能力。  

开发者能不能在多轮请求里"吃到这个红利"，要看服务商是否支持：  
- 前缀缓存
- 跨请求复用
- `cache_tokens`之类可观测指标
- 稳定路由/会话策略

## 设计原则与最佳实践

### 保持上下文的稳定性是首要原则

保持上下文的稳定性是首要原则。系统提示词、工具定义、基础配置等元素应该在整个会话期间保持不变。如果确实需要动态信息，应该将其作为新的用户消息追加，而不是修改已有的上下文。这种追加式的设计不仅符合KV Cache的前缀特性，也更符合对话的自然流程。  

```json
{
    "messages":[
        {
            "role":"system",
            "content":"You are a helpful AI assistant with access to file system tools.
                    You can read files, find files by pattern, and search for text within files.
                    Use the ReAct pattern: Reason about what to do, then Act using tools, and Observe the results.

                    When asked to analyze or summarize code projects, be thorough:
                    1. First use 'find' to discover the structure
                    2. Then read key files to understand the content
                    3. Use 'grep' to search for specific patterns if needed
                    4. Once you have gathered sufficient information, provide your response

                    Always think step by step and use tools to gather information. When you have enough information to answer the user's question, simply provide your response without calling any tools.

                    CURRENT TIME: 2026-04-01 09:05:39.033622"
        },
        {
            "role":"user",
            "content":"Please analyze and summarize all the projects in the week1 and week2 directories.
                    For each project:
                    1. Find all Python files
                    2. Read the main files and understand the functionality
                    3. Identify the key features and purpose
                    4. Provide a comprehensive summary

                    Start with week1 projects, then move to week2. Be thorough in your analysis."
        }
    ]
}
```

核心原则是：
- **不要改已有前缀里的固定部分**，例如`system prompt`、工具定义、基础规则。
- 如果确实有"每轮都会变"的信息，比如时间戳、余额、状态、进度，**更适合追加新的消息**，而不是改写系统提示词。   

上述的做法不理想，因为它把时间戳塞进了`system`消息里，而`system prompt`本应该尽量保持稳定。  


所以更符合"保持前缀稳定"原则的做法通常是：
- `system`保持不变
- 时间戳作为**后续新增消息**附加进去  

就像这样
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful AI assistant with access to file system tools..."
    },
    {
      "role": "user",
      "content": "Please analyze and summarize all the projects in the week1 and week2 directories..."
    },
    {
      "role": "user",
      "content": "Current time: 2026-04-01 09:05:39.033622"
    }
  ]
}
```
不过这里要补一个更精确的点：  
**把时间戳放进新的`user`消息里，比放进`system prompt`更好，但它仍然会影响缓存复用。**  

因为还是新增了`token`，请求前缀还是变了。只是：  
- **修改`system prompt`**：破坏了最前面、最基础、最应稳定的前缀，影响更大
- **追加新的`user`消息**：是正常多轮对话里的自然增长，通常比"改system"更合理

所以最准确的说法是：  
1. **是的，时间戳不应该放在动态变化的`system prompt`里**
2. **如果必须传给模型，追加新消息更合理**
3. **但只要时间戳每轮都变，它仍然会带来一定缓存影响，只是比改 `system`更符合实践**

### 尊重模型的训练格式同样重要

使用标准的消息格式和工具调用接口，不仅能够充分利用模型的能力，还能确保KV Cache的有效性。模型提供商往往投入大量资源优化了这些标准接口的性能，偏离这些标准往往得不偿失。

### 在管理对话历史时，应该采用完整保留而非选择性删除的策略

尽量保留完整的对话历史，虽然这可能导致上下文变长，但现代模型的上下文窗口已经足够大（通常达到128K甚至更多），而且KV Cache机制使得上下文的处理成本主要集中在新增部分。相比之下，试图"智能地"压缩历史往往会破坏缓存并降低Agent的推理能力。  

通过遵循这些原则，我们可以构建既高效又可靠的Agent系统，充分发挥现代大语言模型基础设施的性能优势。