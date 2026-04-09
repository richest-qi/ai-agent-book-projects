# `run_ablation.py` — `parse_args()` 说明

对应源码：`week2/prompt-engineering/run_ablation.py` 中 `parse_args()`（约第 38–159 行）。

---

## Agent 与用户模拟（双角色）

一次运行里存在 **两个由大模型驱动的交互方**，参数上分别对应 `--model` / `--model-provider` 与 `--user-model` / `--user-model-provider`：

| 角色 | 作用 | 相关参数 |
|------|------|----------|
| **Agent（客服 / 系统侧）** | 读业务规则（如 wiki）、看对话历史；决定 **回复用户** 或 **调用环境工具**（订座、查航班等）。 | `--model`、`--model-provider`、`--agent-strategy`、`--temperature` 等主要作用于 Agent。 |
| **用户（模拟用户）** | 在默认 `--user-strategy llm` 下由 **另一个 LLM** 扮演：按任务中的隐藏说明（instruction）与对话策略，与 Agent **多轮对话**，通常 **逐步透露需求**，而不是一次性说清全部条件。 | `--user-model`、`--user-model-provider`、`--user-strategy`。 |

因此常见情况是 **两个 LLM 在对话**：可以都叫同一个模型名（例如默认都是 `openai/gpt-5`），但 **系统提示与职责不同**。若 `user-strategy` 不是基于 LLM 的策略，则「用户」端可能由人机输入或其它逻辑提供，而非模型模拟。

---

## 参数一览

### 基础与任务调度

| 参数 | 类型 | 默认 | 说明 |
|------|------|------|------|
| `--num-trials` | int | `1` | 整批任务重复跑几轮。 |
| `--env` | str | `airline` | 环境：`retail` \| `airline`。 |
| `--model` | str | `openai/gpt-5` | Agent 使用的模型名。 |
| `--model-provider` | str | `None` | Agent 的推理后端；见下文「解析后补全」。可选值见 `provider_list`（与源码中列表一致）。 |
| `--user-model` | str | `openai/gpt-5` | 用户模拟器使用的模型名。 |
| `--user-model-provider` | str | `None` | 用户模拟器后端；见下文「解析后补全」。可选值同上。 |
| `--agent-strategy` | str | `tool-calling` | `tool-calling` \| `act` \| `react` \| `few-shot`。 |
| `--temperature` | float | `1.0` | 动作模型采样温度（注释：gpt-5 兼容）。 |
| `--task-split` | str | `test` | `train` \| `test` \| `dev`。 |
| `--start-index` | int | `0` | 任务起始索引（与 `--end-index` 连用）。 |
| `--end-index` | int | `-1` | 任务结束索引；`-1` 表示跑到末尾（由调用方换算）。 |
| `--task-ids` | int… | 无 | 仅运行指定的若干 task id（可变长列表）。 |
| `--log-dir` | str | `results_ablation` | 结果输出目录。 |
| `--max-concurrency` | int | `1` | 最大并发数。 |
| `--seed` | int | `10` | 随机种子。 |
| `--shuffle` | int | `0` | 非 0 时打乱任务顺序。 |
| `--user-strategy` | str | `llm` | 用户策略；取值为 `UserStrategy` 枚举的各 `value`。 |
| `--few-shot-displays-path` | str | 无 | few-shot 策略可选资源路径。 |

`--model-provider` / `--user-model-provider` 的合法取值（源码中的 `provider_list`）：

`openai`、`anthropic`、`azure`、`bedrock`、`cohere`、`gemini`、`groq`、`mistral`、`ollama`、`openrouter`、`replicate`、`together_ai`、`vertex_ai`、`huggingface`。

### 消融实验

| 参数 | 类型 | 默认 | 说明 |
|------|------|------|------|
| `--tone-style` | str | `default` | `default` \| `trump` \| `casual`。 |
| `--randomize-wiki` | flag | 关闭 | 置位则打乱 wiki 规则顺序。 |
| `--remove-tool-descriptions` | flag | 关闭 | 置位则移除工具与参数描述。 |
| `--ablation-name` | str | `""` | 自定义消融实验名称。 |
| `--no-verbose` | flag | 关闭 | 置位则关闭详细输出；**不置位时 verbose 为开**。 |

---

## 解析 `parse_args()` 之后的补全逻辑

1. **`args.verbose`**：`args.verbose = not args.no_verbose`  
   默认 **verbose 开启**，仅当传入 `--no-verbose` 时为 `False`。

2. **`args.model_provider`**：若命令行未指定 `--model-provider`（仍为 `None`）  
   - `args.model == "openai/gpt-5"` → `args.model_provider = "openrouter"`  
   - 否则 → `args.model_provider = "openai"`

3. **`args.user_model_provider`**：若未指定 `--user-model-provider`  
   - `args.user_model == "openai/gpt-5"` → `args.user_model_provider = "openrouter"`  
   - 否则 → `args.user_model_provider = "openai"`

最后 **`return args`**，供 `main()` → `run_with_ablation(args)` 使用。
