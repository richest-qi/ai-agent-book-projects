## 评估环境的基本组成
- 数据集
- 环境状态
- 工具接口
- 评估指标
- 执行协议 

## 工具调用型评估环境
verifiers https://github.com/PrimeIntellect-ai/verifiers
Environments Hub https://app.primeintellect.ai/dashboard/environments?ex_sort=most_stars
- terminal-bench
- tau2-bench  week2\prompt-engineering\tau_bench\envs\airline


## 人机调用型评估环境

## 仿真环境的构建    

aworld https://github.com/inclusionAI/AWorld

## 数据集的设计  
下载GAIA、AndroidWorld、SWE-Bench Verified、τ²-bench、Terminal-Bench、OSWorld-Verified这几个数据集的官方版本。    
每个数据集都提供了标准化的任务描述文件与测试用例。  
每个数据集中挑选至少一个代表性任务，人工尝试完成这个任务。任务完成后，将自己的执行结果与数据集提供的标准答案对比，并分析差异的来源。  


数据集设计需要：     
- 任务描述的精确性设计    
- 任务复杂度的层次化设计     
    - easy
    - medium
    - hard   
- 可验证性与客观性的保障     
- 防止数据泄露     



android world 
- https://google-research.github.io/android_world/
- https://google-research.github.io/android_world/task_list.html     

OSWorld
- https://os-world.github.io/    

SWE-Bench
- https://www.swebench.com/
- swe-bench https://www.swebench.com/original.html
- dataset https://huggingface.co/datasets/SWE-bench/SWE-bench     


Arena AI  https://arena.ai/leaderboard/agent
配对比较      

LangSmith  Ship great agents faster with LangSmith       

LangSmith负责：
- Agent到底干了什么?
- 为什么回答错了？
- 哪个Prompt出了问题？
- 哪个工具调用失败了？
- 花了多少token？
- 耗时多久？    

本质是:Agent出了问题怎么查？   

Agent上线后最难的不是搭Agent，而是定位Agent为什么错。  


benchmark报告     


https://github.com/jingyaogong/minimind-v    


SFT，学知识，记忆知识；RL，学能力。
先掌握SFT基础，再做RL。如果直接RL，学东西很慢。  
先用小模型训练，再用大模型训练。   
如果直接在大模型上训练，成本很高。   

如果不SFT，直接RL呢？   


AdaptThink：让推理模型学会何时思考   
- 需要思考的时候去推理    
- 不需要思考的时候直接回答问题   
  

当模型没有推理能力时，如何让模型可以凑出24点 —— SFT + RL训练，让大模型具备推理能力。  


