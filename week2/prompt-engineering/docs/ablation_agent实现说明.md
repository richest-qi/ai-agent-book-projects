# AblationAgent 实现说明

本文梳理 `week2/prompt-engineering/ablation_agent.py` 中 **`AblationAgent`** 的职责与执行流程，便于对照 `run_ablation.py` 日志与 baseline 行为。

---

## 1. 文件角色

- **路径**：`week2/prompt-engineering/ablation_agent.py`
- **基类**：`tau_bench.agents.base.Agent`
- **定位**：在 Tau-Bench 的 **`ToolCallingAgent`** 思路上实现同一套 **「多轮 chat + 工具调用 + `env.step`」** 循环；额外提供 **`verbose` 全量日志**、**累计 API 费用**，以及对 **`gpt-5`** 的 **`reasoning_effort`** 传参。

`AblationAgent` **不实现消融逻辑本身**：语气/wiki/工具描述等变更由 **`run_ablation.py`** 在创建 Agent **之前**改好 `wiki` / `tools_info`，再传入构造函数。

---

## 2. 构造参数

| 参数 | 含义 |
|------|------|
| `tools_info` | 供模型使用的工具 schema 列表（OpenAI-style function definitions），与 `litellm.completion(..., tools=...)` 一致。 |
| `wiki` | 系统策略长文本，作为第一条 **`role: system`** 的 `content`。 |
| `model` | 模型名（如 `openai/gpt-5`）。 |
| `provider` | LiteLLM 的 `custom_llm_provider`（如 `openrouter`）。 |
| `temperature` | 采样温度。 |
| `verbose` | 为 `True` 时打印任务头、每步 API 请求/响应、环境回传与任务小结。 |

---

## 3. `solve` 总流程

```
env.reset(task_index)
  → observation = 用户模拟器首句
  → messages = [system=wiki, user=observation]

重复最多 max_num_steps（默认 30）次：
  completion(messages, tools=tools_info, ...)
  → next_message = assistant 消息（纯文本 和/或 tool_calls）
  → action = message_to_action(next_message)
  → env_response = env.step(action)
  → 按 action 类型把本轮内容 extend 进 messages
  → 若 env_response.done 则 break

return SolveResult(reward, info, messages, total_cost)
```

**核心状态**是列表 **`messages`**：每一轮发给模型的上下文就是当前完整的 `messages`；Agent **只在本文件内维护这一条 transcript**，不依赖环境替你存历史。

---

## 4. 启动阶段

1. **`env.reset(task_index)`**  
   - 得到 **`observation`**（第一条对用户模型可见的「用户」话）及 **`info`**。  
2. 初始化 **`messages`**：  
   - `{"role": "system", "content": self.wiki}`  
   - `{"role": "user", "content": obs}`  

---

## 5. 单轮循环（每一步）

### 5.1 调用模型

- 使用 **`litellm.completion`**，主要参数：  
  `messages`、`model`、`custom_llm_provider=self.provider`、`tools=self.tools_info`、`temperature`。  
- 当 **`"gpt-5" in self.model`** 时，增加  
  `extra_body={"reasoning_effort": "low"}`，用于压低 reasoning token 消耗。  
- 从返回中取 **`res.choices[0].message.model_dump()`** 作为 **`next_message`**（字典形式的 assistant 消息）。  
- 若存在 **`res._hidden_params["response_cost"]`**，累加到 **`total_cost`**。

### 5.2 转为协议动作

- **`message_to_action(next_message)`** 定义在 `tau_bench/agents/tool_calling_agent.py`：  
  - 若存在非空 **`tool_calls`** → **`Action(name=函数名, kwargs=json.loads(参数))`**  
  - 否则 → **`Action(name=RESPOND_ACTION_NAME, kwargs={"content": 正文})`**（对用户说话）。  

`RESPOND_ACTION_NAME` 即字符串 **`"respond"`**（与 `tau_bench.types` 一致）。

### 5.3 推进环境

- **`env.step(action)`** 返回 **`observation`**（字符串：工具输出或模拟用户下一句）、**`done`**、**`reward`**、**`info`**（与已有 `info` 做 dict merge）。

### 5.4 维护 `messages`（与日志里的 role 对应）

| `action.name` | 追加内容 |
|---------------|----------|
| **非 `respond`（工具）** | ① 将 **`next_message["tool_calls"]` 截断为仅第一项**（与 wiki「一次一个工具调用」一致）；② 追加该条 **`assistant`**；③ 追加 **`role: tool`**，含 `tool_call_id`、`name`、`content=env_response.observation`。 |
| **`respond`** | ① 追加 **`assistant`**（`content` 为对用户说的话）；② 追加 **`role: user`**，`content=env_response.observation`（模拟用户回复）。 |

### 5.5 baseline 下 `messages` 的“时间线”示例（更具体）

下面用一个最小示意，展示 `messages` 如何随步骤增长（与 `response4.md` 的结构一致）：

#### Step 0：`reset` 后（还没调过模型）

```python
messages = [
  {"role": "system", "content": wiki_text},
  {"role": "user", "content": first_user_utterance_from_env_reset},
]
```

此时第一次 `completion(...)` 看到的上下文只有这两条。

#### Step 1：模型选择“调用工具”（例如 `get_user_details`）

1) 模型返回 `next_message`（`role=assistant`，且有 `tool_calls`）  
2) `message_to_action` 转成 `Action(name="get_user_details", kwargs=...)`  
3) `env.step(action)` 执行工具，得到工具输出字符串 `tool_obs`  
4) Agent 追加两条到 `messages`：

```python
messages += [
  next_message,  # assistant + tool_calls
  {
    "role": "tool",
    "tool_call_id": next_message["tool_calls"][0]["id"],
    "name": next_message["tool_calls"][0]["function"]["name"],
    "content": tool_obs,
  },
]
```

下一轮模型会同时看到：之前用户说了什么、自己调用了哪个工具、工具返回了什么。

#### Step 2：模型选择“回复用户”（`respond`）

1) 模型返回 `next_message`（`role=assistant`，纯文本，无 `tool_calls`）  
2) `message_to_action` 转成 `Action(name="respond", kwargs={"content": ...})`  
3) `env.step(action)` 把这段话交给用户模拟器，得到用户下一句 `user_obs`  
4) Agent 追加两条到 `messages`：

```python
messages += [
  next_message,  # assistant text reply
  {"role": "user", "content": user_obs},
]
```

下一轮模型会看到自己上次回复 + 用户刚刚补充的信息（比如时间偏好、支付方式等）。

#### 一个关键不变量

- `messages` 始终满足 chat 协议顺序：  
  - 工具分支：`... -> assistant(tool_calls) -> tool`  
  - 对话分支：`... -> assistant(content) -> user`
- `tool` 角色永远和上一条 `assistant.tool_calls[0]` 对齐（通过 `tool_call_id` 绑定）。
- Agent 每轮只会保留并执行第一个 tool call，避免一轮多工具导致环境状态和日志对不齐。

### 5.6 终止

- 若 **`env_response.done`**：根据 **`reward`** 打成功/结束日志，`break`。  
- 若步数用尽仍未 `done`，循环正常结束，**`reward` 保持最后一轮的值**。

---

## 6. 返回值 `SolveResult`

| 字段 | 含义 |
|------|------|
| `reward` | 环境给出的最终奖励（Tau-Bench 中成功常为 `1.0`）。 |
| `info` | 自 `reset` 起与环境多次 `step` 合并后的信息字典。 |
| `messages` | 完整对话 transcript（含 `system` / `user` / `assistant` / `tool`）。 |
| `total_cost` | 本任务 LiteLLM 汇报的 API 费用累加（若无则为 0）。 |

---

## 7. `verbose` 与实验日志

`verbose=True`（默认）时，每一步会大致打印：

- 当前步序号、**API CALL #n**、**SENDING k messages**（会把每条 message 的 role、正文、`tool_calls` / `tool_call_id` 打出）；  
- 本次请求温度、工具 definition 全文；  
- 模型返回正文与 tool_calls；  
- **Environment Response**：`action.name`、工具输出或用户回复、`reward`、`done`；  
- 任务结束时的 **TASK SUMMARY**（最终 reward、步数、总费用、`messages` 条数）。

你在 `response4.md` / `response5.md` 里看到的格式即来源于此。

---

## 8. 与 `ToolCallingAgent` 的差异（便于对照源码）

| 项目 | `ToolCallingAgent` | `AblationAgent` |
|------|-------------------|-----------------|
| 日志 | 无详细打印 | `verbose` 控制全量 trace |
| `gpt-5` | 无特殊参数 | `reasoning_effort: low` |
| 费用 | 累加 `response_cost` | 同左，且打印 summary |
| 核心循环 | `completion` → `message_to_action` → `step` → 更新 `messages` | **相同** |

因此 **baseline 行为**可视为：**同一套消息协议 + 同一套 `message_to_action` / `env.step` 契约**，仅观测与费用统计更友好。

---

## 9. 相关文档

- `docs/get_env与环境构造说明.md`：`env.reset` / `env.step`、用户模拟器与工具谁负责什么。  
- `docs/run_ablation-parse_args.md`：如何拼装 `RunConfig`、如何把修改后的 `wiki` / `tools_info` 交给 `AblationAgent`。  
- `tau_bench/agents/tool_calling_agent.py`：`message_to_action` 的精确分支条件。
