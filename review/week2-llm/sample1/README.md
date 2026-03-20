# week2-llm / sample1

本机 **Ollama** + **`get_current_time` 工具**：模型根据用户说的城市选择 IANA 时区并调用工具，程序只负责执行工具并多轮对话直到模型给出文本回复。

- 无客户端城市映射表、无二次追问修复 JSON、无 verbose 轨迹打印（刻意保持简单）。

## 运行

```bash
cd review/week2-llm/sample1
pip install -r requirements.txt
python main.py
python main.py --city Paris
python main.py --model qwen3:0.6b --host http://127.0.0.1:11434
```

默认城市：直接回车为 **北京**。

## 切换模型对比

该脚本支持通过命令行参数切换 Ollama 模型（用于对比不同模型的稳定性）。

```bash
# 小模型
python main.py --city 东京 --model qwen3:0.6b

# 更大模型（你已下载）
python main.py --city 东京 --model qwen3:8b

# 也可以不指定 --city，直接回车默认查 北京
python main.py --model qwen3:0.6b
python main.py --model qwen3:8b
```

## 与 `week2/local_llm_serving` 的差异

| 项目 | local_llm_serving | 本目录 |
|------|-------------------|--------|
| 入口 | 交互式 main | 单次问答 |
| 工具 | `tools.py` | 本文件内 `get_current_time` |

---

## 小模型的现象与分析（为何「东京」可能错、巴黎可能对）

在默认 **`qwen3:0.6b`** 等较小模型下，可以观察到：

| 用户输入 | 可能出现的现象 |
|----------|----------------|
| **巴黎** | 回答里时间与 `Europe/Paris` 一致的情况较多，整体较像样。 |
| **东京 / Tokyo** | 文案里出现 **`Asia/Shanghai`**、`+0800`，或把偏移与 **Eastern** 等混写——与日本标准时（一般为 **`Asia/Tokyo`、UTC+9**）不符。 |

### 核心结论

- **墙上几点钟**完全由模型在 tool call 里传入的 **`timezone`（IANA）** 决定；`get_current_time` 只是用本机时钟在 `ZoneInfo(timezone)` 下计算，**不会替你纠正「东京该用哪个区」**。
- 若模型传了 `Asia/Shanghai`，工具返回的就是**中国东八区**的时间；这不算「算错」，而是 **模型把东京错配成了中国时区**。
- 最终自然语言里还可能 **张冠李戴**（例如偏移 +0800 又写 Eastern），属于 **小模型复述/概念混乱**，与工具 JSON 是否自洽都未必一致。

### 为何会这样（在本示例「无城市映射、无校验」的前提下）

1. **模型太小**：在 `tools` 里填对 IANA 这种细粒度决策容易不稳定。  
2. **中英与日区语境**：问题里常出现中文地名 + 英文问句，小模型容易把「东亚」糊成一块，误用 `Asia/Shanghai`。  
3. **架构取舍**：刻意不做客户端城市→IANA 表、不做二次校验，就等于接受 **「地理上是否正确」完全押在模型一层**——小模型这一层往往**不牢**。

### 可以怎么想

- 这是 **能力边界** 而非偶然单点 bug：在「纯模型 + 小模型 + 无映射」下，东京类问题**本来就可能错**。  
- 若要稳定：**换更大、tool calling 更可靠的模型**，或在产品里增加 **映射 / 地理 API / 参数校验**（与本目录「极简 demo」目标不同）。

**一句话**：**对的时钟 ≠ 对的地理**；中间隔着模型选 IANA 与组织语言两层，小模型这两层都不可靠时，就会出现「东京却用上海时区」这类输出。

---

## 实验补充：东京类输入在不同模型下的表现

在「本目录仅 model + `get_current_time(timezone)`（无客户端城市→IANA 映射）」的前提下，复现到以下现象：

### 输入 `Tokyo` / `Toyko` / `Tyoko`

| 模型 | 输入 | 输出（节选） | 结论 |
|------|------|--------------|------|
| `qwen3:0.6b` | `Tokyo` | `Asia/Shanghai`、`+0800` | 错（日本东京应为 `Asia/Tokyo`、`+0900`） |
| `qwen3:0.6b` | `Toyko` | `Asia/Shanghai` | 错 |
| `qwen3:8b` | `Tyoko` | `Asia/Tokyo`、`+0900` | 对 |
| `qwen3:8b` | `Toyko` | `Asia/Tokyo`、`+0900` | 对（但响应更慢） |

### 观察

- `qwen3:8b` 相对更可能在「拼写变体（Toyko/Tyoko）」时把 IANA 选对（`Asia/Tokyo`）。
- `qwen3:0.6b` 在 `Tokyo` 与 `Toyko` 上都稳定落到 `Asia/Shanghai`，基本无法正确映射到日本时区。
- 模型越大（`8b`）响应越慢，这是可接受的权衡。
