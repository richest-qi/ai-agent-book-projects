# week2-llm / sample1 — 极简本地 Ollama

对应 `week2/local_llm_serving/main.py` 里 **Sample 1** 的那道题，但**不**使用交互、`/samples`、`/sample`、流式与工具调用；运行一次脚本即可在终端看到「问题 + 模型原文回复」。

## Sample 1 问题

> What is the current time in Vancouver?

## 与 `main.py` 的差异

| 项目 | `local_llm_serving/main.py` | 本目录 `main.py` |
|------|-----------------------------|------------------|
| 交互 | 有 | 无，一次运行结束 |
| 工具 | 可调用 `get_current_time` 等 | **不**传 tools，纯 chat |
| 时间是否准确 | 可走工具得到真实时间 | 依赖模型知识，**可能不精确** |

若你需要和原 demo 一样「工具给出的温哥华当前时间」，请继续用 `week2/local_llm_serving/main.py` 的 `/sample 1`。

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
```
