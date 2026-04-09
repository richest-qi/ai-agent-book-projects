# `tau_bench/envs/user.py` 说明

对应源码：`week2/prompt-engineering/tau_bench/envs/user.py`。

本文件实现 **用户模拟器（User Simulation）**：在评测里代替真实用户，与 **Agent（客服）** 进行多轮对话。

---

## 解决什么问题？

环境中的 **Agent** 只能通过 **工具调用** 与 **`respond`（对用户说话）** 与外界交互。评测需要有人 **扮演顾客**：提出需求、回答追问、在任务完成时结束对话。`user.py` 定义「这一侧由谁来做」以及如何做。

---

## 抽象接口：`BaseUserSimulationEnv`

所有用户模拟实现都需支持：

| 方法 | 含义 |
|------|------|
| `reset(instruction)` | 新任务开始。`instruction` 为任务中的隐藏剧本（顾客人设与目标）。返回 **顾客第一句要说的话**（字符串），通常作为 `env.reset()` 里 Agent 看到的 `observation`。 |
| `step(content)` | Agent 通过 `respond` 说了一句 `content`。返回 **顾客下一句** 回复。 |
| `get_total_cost()` | 用户侧若调用 LLM，可累计费用（供环境 `info.user_cost` 等使用）。 |

**调用时机**：`reset` 在 `Env.reset` 里调用一次；`step` 仅在 Agent 动作名为 **`respond`**（对用户说话）时，由 `Env.step` 调用。**工具调用**不会进入用户模拟器。

---

## `user-strategy`（`--user-strategy`）各选项说明

命令行参数与源码枚举 `UserStrategy` 一一对应。工厂函数 **`load_user(user_strategy, model, provider)`** 根据策略实例化下表中的类（定义在 `user.py`）。

| 策略值 | 实现类 | 是否需要 `model` / `provider` | 行为要点 |
|--------|--------|-------------------------------|----------|
| **`llm`**（默认） | `LLMUserSimulationEnv` | 需要 | 用 `litellm.completion` 调用 **用户模型**。内部维护自己的 `messages`：`system` 里拼接 `instruction` 与扮演规则（一次只说必要信息、instruction 里没写的不能编造、自然对话等）。**首句**：在 `reset` 里构造初始对话后调用模型生成 **一句用户话**。**后续**：`step` 把 Agent 的 `respond` 文本追加进对话，再调模型生成下一句。任务目标达成时要求输出单独一行 **`###STOP###`**，环境据此结束对话。 |
| **`human`** | `HumanUserSimulationEnv` | 不需要 | 终端 **`input()`**：真人读 `instruction` 或 Agent 的话并打字回复。`get_total_cost` 恒为 0。适合调试轨迹或不需要用户模型费用时。 |
| **`react`** | `ReactUserSimulationEnv` | 需要 | 在用户侧也采用 **ReAct 式输出**：模型被要求先写 **Thought**，再写 **User Response**；代码 **`parse_response`** 只把 **User Response** 那一段（或遇 `###STOP###` 则原样返回）交给环境。比纯 `llm` 多一层结构化，便于约束「内心戏」与「说出口的一句」分离。 |
| **`verify`** | `VerifyUserSimulationEnv` | 需要 | 在 `LLMUserSimulationEnv` 思路上增加 **`verify(model, provider, message, messages)`**：生成内容校验不通过时 **最多重试**（默认 `max_attempts=3`），通过才把该轮回复交给环境，用于抑制用户侧胡编、格式错误或脱离 instruction。 |
| **`reflection`** | `ReflectionUserSimulationEnv` | 需要 | 在验证/反思链路上更进一步：会结合 **`reflect`** 等对生成结果做反思与修正（见 `user.py` 中该类完整逻辑），多轮用户模型调用，**成本与延迟通常更高**，换更稳的用户行为。 |

### 公共约束（LLM 类策略通常都遵守）

- **Instruction** 来自当前 `Task`，**不**直接等价于 Agent `messages` 里用户的第一条 visible 文本；用户模型在 **自己的** `system` 里看到完整 instruction。
- 多轮对话中应 **逐步披露** 信息，而不是第一段就把剧本全文背给 Agent。
- 结束符 **`###STOP###`**：出现在用户模拟器返回的字符串中时，`Env.step` 会把 **`done`** 置为真并进入奖励计算（与 `base.py` 中逻辑一致）。

### 与 `agent-strategy` 的关系

- **`user-strategy`** 只决定 **顾客** 如何生成话术（真人 / 普通 LLM / ReAct 用户 / 带校验或反思的用户）。
- **`agent-strategy`**（`tool-calling` / `act` / `react` / `few-shot`）决定 **客服 Agent** 如何用工具、如何格式化行动；二者 **正交**。
- 在 **`run_ablation.py`** 中，解题主体固定为 **`AblationAgent`**，**`--user-strategy` 仍会改变** `load_user` 行为；若需对比多种 **Agent** 策略，应使用 **`tau_bench/run.py`** 或包内 `run(config)` 路径（通过 `agent_factory` 切换）。

---

## 实现类与工厂（速查）

| 类名 | 与策略值对应 |
|------|----------------|
| `HumanUserSimulationEnv` | `human` |
| `LLMUserSimulationEnv` | `llm` |
| `ReactUserSimulationEnv` | `react` |
| `VerifyUserSimulationEnv` | `verify` |
| `ReflectionUserSimulationEnv` | `reflection` |

**`load_user`**：在 `tau_bench/envs/base.py` 里 `Env.__init__` 时调用；除 `human` 外，其余策略若 `model` 或 `provider` 为 `None` 会 **`ValueError`**。

---

## 与 `AblationAgent` 的分工（便于对照）

- **`AblationAgent`（`ablation_agent.py`）**  
  维护 **客服 Agent** 侧的 `messages`，调用 **Agent 模型**，决定调用工具或 `respond`。

- **`user.py` 中的模拟器**  
  只在环境执行 **`respond`** 时被调用（以及 `reset` 时生成首句）。维护 **顾客** 自己的对话状态，调用 **用户模型**（若策略为 LLM 系），产出下一屏「用户话术」。

因此同一套评测里可以存在 **两个 LLM**：一个在 Agent 侧，一个在用户模拟侧；二者使用 **不同的 `messages` 与系统提示**，不要混为一份上下文。

---

## 延伸阅读

- 环境如何把 `respond` 交给用户模拟：`tau_bench/envs/base.py` 中 `Env.step` 对 `RESPOND_ACTION_NAME` 的分支。
- 命令行相关参数说明：`docs/run_ablation-parse_args.md` 中的 `--user-model`、`--user-model-provider`、`--user-strategy`。
- Agent 侧 `agent-strategy` 差异（与本文件互补）：`tau_bench/run.py` 中的 `agent_factory`。
