# `get_env` 与环境构造说明（baseline 视角）

对应代码：

- `week2/prompt-engineering/run_ablation.py`
- `week2/prompt-engineering/tau_bench/envs/__init__.py`
- `week2/prompt-engineering/tau_bench/envs/airline/env.py`
- `week2/prompt-engineering/tau_bench/envs/base.py`

---

## 1. 这段 `get_env` 在做什么？

`run_ablation.py` 在开始处会调用：

```python
env = get_env(
    config.env,
    user_strategy=config.user_strategy,
    user_model=config.user_model,
    user_provider=config.user_model_provider,
    task_split=config.task_split,
)
```

它不是“只读配置”，而是在构造一个 **可执行的业务评测环境对象**，后续 Agent 的每一步都要通过这个环境来推进。

---

## 2. 为什么要构造环境？

因为这个实验测的不是普通聊天，而是：

**在固定业务规则 + 固定工具 + 固定任务下，Agent 能否正确完成操作并拿到 reward。**

环境至少要提供这些要素：

1. **任务集（tasks）**：每个任务包含隐藏 instruction 与目标动作。
2. **业务数据（data）**：如航班、预订、用户资料等，工具会读写这些数据。
3. **规则与手册（wiki/rules）**：作为 Agent 的行为约束与知识边界。
4. **工具集合（tools）**：Agent 通过工具调用与环境交互，而非直接改数据。
5. **用户侧模拟器（user simulation）**：用于生成顾客首句与后续回复。

没有这层环境，就无法做可重复、可量化的任务评测。

---

## 3. baseline 下 `get_env` 具体走了哪条路径？

### 3.1 路由到 airline 环境

`get_env` 根据 `env_name` 分发：

- `retail` → `MockRetailDomainEnv`
- `airline` → `MockAirlineDomainEnv`

baseline 默认是 `airline`，因此会构造 `MockAirlineDomainEnv`。

### 3.2 `MockAirlineDomainEnv` 装载哪些资源

在 `airline/env.py` 中：

- `task_split="test"` 时加载 `tasks_test.py` 的 `TASKS`
- `data_load_func=load_data`
- `tools=ALL_TOOLS`
- `wiki=WIKI`
- `rules=RULES`

其中来源分别是：

- `tasks_test.py`：任务脚本（含 `instruction` 与目标动作）
- `data/__init__.py`：从 `flights.json`、`reservations.json`、`users.json` 读数据
- `tools/__init__.py`：`ALL_TOOLS`（如 `SearchDirectFlight`、`BookReservation` 等）
- `wiki.py`：读取 `wiki.md` 为长文本 `WIKI`
- `rules.py`：当前 airline 里是 `RULES = []`（规则主要体现在 wiki）

---

## 4. `Env` 对象内部最终长什么样？

`Env.__init__` 会把上面资源变成运行时能力：

- `self.data`：当前业务数据（由 `data_load_func()` 载入）
- `self.tools_map` / `self.tools_info`：工具可执行映射 + 供模型使用的工具 schema
- `self.tasks` / `self.task`：任务集合与当前任务
- `self.wiki` / `self.rules`：策略文本与规则
- `self.user`：由 `load_user(...)` 创建的用户模拟器（受 `user_strategy` 控制）

因此 `run_ablation.py` 紧接着可以直接拿：

- `modified_wiki = env.wiki`
- `modified_tools_info = env.tools_info`

在 baseline 下这两者不做改动，直接交给 `AblationAgent`。

---

## 5. 环境在一轮交互中的职责（最关键）

### `reset(task_index)`

- 重置数据与动作轨迹
- 选定当前任务
- 调用 `self.user.reset(instruction=task.instruction)` 生成用户首句
- 返回 `observation`（Agent 收到的第一条用户消息）

### `step(action)`

- 若 `action.name == "respond"`：把 Agent 文本交给用户模拟器，得到下一句用户回复
- 若是工具名：执行对应工具，返回工具输出
- 判断是否结束（如用户回复含 `###STOP###` 或终止工具）
- 结束时计算 `reward`（比对执行结果是否满足任务目标）

这就是 “Agent ↔ 环境（用户/工具）↔ Agent” 的闭环。

---

## 6. 为什么 `run_ablation.py` 里会 `get_env` 两次？

在 `run_ablation.py` 中有两处调用：

1. **第一次（函数前半段）**  
   ```python
   env = get_env(...)
   ```
   这是构造一个**模板环境（母环境）**，主要用于：
   - 读取 `env.wiki`、`env.tools_info`（给 `AblationAgent`）
   - 获取 `len(env.tasks)`（用于计算任务范围）
   - 做一次性的实验配置准备

2. **第二次（`_run(idx)` 内）**  
   ```python
   isolated_env = get_env(..., task_index=idx)
   ```
   这是为每个任务创建**独立环境实例**，用于真正执行该 task。

这样设计的原因：

- **状态隔离**：每个任务从干净数据开始，互不污染。
- **并发安全**：`max_concurrency > 1` 时，每个线程各有环境实例。
- **评测公平**：避免前一任务改过的数据影响后一任务的 reward。

所以两次 `get_env` 不是重复，而是“**模板准备**”和“**任务执行隔离**”这两种不同职责。

---

## 7. 一句话总结

`get_env(...)` 的作用是：**把任务、数据、工具、wiki、用户模拟器打包成一个可执行考场**。  
baseline 只是“消融项不开”，并不意味着没有环境；恰恰相反，环境是整个实验能成立的基础。

---

## 8. 这些环境到底是“给谁”的？

结论：`Env` 不是只给 Agent，也不是只给用户模拟器，而是给 **整个交互系统** 的共享运行时容器。

- **给 Agent 用**：Agent 每步通过 `env.step(action)` 与外部世界交互，读取工具输出/用户回复，不能直接改底层数据。
- **给用户模拟器用**：`Env` 内部持有 `self.user = load_user(...)`。`reset` 与 `respond` 分支会调用用户模拟器生成首句/下一句。
- **环境自己还做**：工具执行、状态维护、终止判断、reward 计算（裁判职责）。

可以把它类比成：

- Agent = 前台客服
- 用户模拟器 = 来电顾客（真人或 LLM）
- Env = 航司后台系统 + 规则中心 + 评分裁判

三者共同组成可评测闭环，缺一不可。

---

## 9. 4 对象调用顺序图（baseline，更具体）

先固定对象名：

- `A` = `run_ablation.py`（调度器）
- `B` = `AblationAgent`（客服侧 Agent）
- `C` = `isolated_env`（共享业务世界 / 裁判）
- `D` = `user.py` 用户模拟器（顾客侧）

```text
A: run_ablation.py
  -> C0 = get_env(...)                          # 模板环境：读取 wiki/tools/tasks 元信息
  -> B = AblationAgent(wiki=C0.wiki, tools=C0.tools_info)
  -> for each idx:
       -> C = get_env(..., task_index=idx)      # 每个任务单独环境（状态隔离）
       -> B.solve(C)

B: AblationAgent.solve(C)
  -> C.reset(task_index=idx)
       -> D.reset(instruction=task.instruction) # 由用户模拟器生成首句
       <- observation(用户首句)
  -> messages = [system=wiki, user=observation]
  -> loop:
       -> Agent LLM(messages + tools)           # 产出 next_message/action
       -> C.step(action)
            -> if action == respond:
                 D.step(agent_text)             # 用户模拟器回一句
               else:
                 tool.invoke(data, **kwargs)    # 工具执行并读写环境数据
            -> done/reward 判断（环境负责）
       <- observation(用户回复或工具输出)
       -> B 将 observation 追加回 messages，进入下一步
  -> done 时返回 SolveResult(reward, traj, info)
```

关键点：**B 不直接调用 D，也不直接改数据；都通过 C（环境）中转与裁判。**

---

## 10. 相关文档

- `docs/run_ablation-parse_args.md`：`run_ablation.py` 参数与双角色说明
- `docs/ablation_agent实现说明.md`：`AblationAgent` 的 `solve` 循环、`messages` 维护与 `verbose` 日志
- `docs/tau_bench-user-py说明.md`：用户模拟器（`user.py`）详解
