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

## 与 `week2/local_llm_serving` 的差异

| 项目 | local_llm_serving | 本目录 |
|------|-------------------|--------|
| 入口 | 交互式 main | 单次问答 |
| 工具 | `tools.py` | 本文件内 `get_current_time` |
