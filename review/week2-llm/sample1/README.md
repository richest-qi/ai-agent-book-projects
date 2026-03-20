# week2-llm / sample1 — 极简本地 Ollama

对应 `week2/local_llm_serving/main.py` 里 **Sample 1** 题型（查询某城市实时时间），但**不**使用 `local_llm_serving` 的交互菜单、`/samples`、`/sample`、流式。运行后会**提示输入城市**（或用 `--city`），再打印「问题 + 模型回复」。

**工具**：在 `main.py` 内**自行实现** `get_current_time`（`datetime.now` + IANA `ZoneInfo`），**不引用** `week2/local_llm_serving/tools.py`。模型通过 Ollama 的 `tools` 调用该函数，结果以 `role: tool` 回传后再生成最终回答。

## 问题形式

根据你输入的城市生成英文提问；**直接回车**默认城市为 **北京**（中国），例如：

> What is the current time in 北京?

也可用中文等地名。**城市 → IANA 时区由模型在 tool call 里自行决定**；程序只负责执行 `get_current_time(timezone)`，**不维护**客户端城市映射表。若模型较弱，可能出现错配或胡写，可换更大模型或自行加回映射/API（本示例刻意保持「仅 model + 工具」）。

若模型把 **tool JSON** 当正文输出，脚本会 **无 tools 再追问一轮** 生成自然语言，否则回退为工具 JSON 的可读摘要。

## 与 `local_llm_serving/main.py` 的差异

| 项目 | `local_llm_serving/main.py` | 本目录 `main.py` |
|------|-----------------------------|------------------|
| 交互 | 完整聊天 + sample 命令 | 仅询问城市名一次，查完即退出 |
| 工具实现 | `tools.py` 中 `ToolRegistry` | **本文件内**独立实现的 `get_current_time` |
| 城市→IANA | （同上，由模型在 tool 里填） | **无**客户端穷举表；仅 **model + `get_current_time(timezone)`** |
| 时间来源 | 本地 Python 执行工具 | 同上（以模型传入的 `timezone` 为准） |

调试工具链可加 `--verbose`，会打印每轮 tool 调用与返回 JSON。

## 运行

```bash
cd review/week2-llm/sample1
pip install -r requirements.txt
# 确保 Ollama 已启动，且已拉取模型
python main.py
```

可选参数：

```bash
python main.py --model qwen3:0.6b --host http://127.0.0.1:11434
python main.py --city "New York"          # 非交互指定城市
python main.py --verbose                   # 打印 tool 调用与返回 JSON
```
