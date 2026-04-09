## Tau-Bench 是什么？

**Tau-Bench 是一套「工具调用型 Agent」的评测框架**（来自 Sierra 等团队的开源/改编代码，你项目里是 `week2/prompt-engineering/tau_bench/`）。

它做的是几件事：

1. **造一个假的业务世界**  
   例如 **航空订票（airline）** 或 **零售（retail）**：有假数据库、假用户、假订单等。

2. **给 Agent 一堆「工具」**  
   例如查航班、下单、改订单……每个工具对应环境里的一个操作（你日志里那 14 个 function tools 就是这套 API）。

3. **用「任务」来考 Agent**  
   每个 task 里有一段 **给「模拟用户」的隐藏指令**（instruction），例如「我是某某用户，要订某天的机票、要几件行李、用某张卡付钱……」。  
   **模拟用户** 通常也是 **另一个 LLM**（`user_strategy=llm`），按指令和 Agent 多轮对话，但不会一次性把全部条件说完。

4. **用 reward 判对错**  
   对话结束后，环境会检查：**Agent 是否在规则允许的前提下，把数据库/状态改到和「标准答案」一致**。  
   常见是 **reward=1 成功，0 失败**（你 `results_ablation/*.json` 里的 `reward` 就是这个）。

所以：**Tau-Bench 不是「聊天好玩」**，而是 **「在固定规则 + 固定工具下，测 Agent 能不能可靠办完一件事」** 的基准。

---

## `run_ablation.py` 这个实验到底在讲什么？

这个目录在 README 里写得很明确：**在 Tau-Bench 上跑「提示工程消融」**——也就是 **故意把提示/说明变差**，看 **成功率（reward）和轨迹** 怎么掉。

`run_ablation.py` 会：

- 选环境（默认 `--env airline`）、选模型（默认 `openai/gpt-5` + OpenRouter）、跑一串 task；
- 可选三种「糟蹋提示」的方式（消融）：
  - **语气**（trump / casual）：改 system/wiki 里的表达风格；
  - **Wiki 随机化**：把规则顺序/结构打乱，模拟「员工手册写得一团糟」；
  - **去掉工具描述**：工具名还在，但说明变空，模拟「操作手册没写清楚」。

**baseline** 就是三种都不开，作为对照组。

所以整件事的叙事是：

> **同样的 Tau-Bench 任务、同样的工具**  
> **只改「提示/文档质量」**  
> → 看 Agent **还能不能稳定按政策办事、少犯错**。

这就是它和 Tau-Bench 的关系：**Tau-Bench 提供「考场」；`run_ablation.py` 用同一套考场，对比「好提示 vs 烂提示」**。

---

## `results_ablation` 里该看什么？

每个 JSON 大致会有：

- **`ablation_config`**：这次开了哪些消融；
- **`results`**：每个 `task_id` 的 **`reward`**、**`info`**（含任务说明、评测细节）、**`traj`**（完整对话/调用轨迹）。

你要快速懂「实验结论」，优先看：**不同消融下 `reward` 的平均值/成功率**，再需要时才翻 `traj` 看是错在工具参数、漏确认、还是违反 wiki 规则。



