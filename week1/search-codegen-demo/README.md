# Search Codegen Demo

从 `week1/search-codegen` 抽取的**独立精简工程**，固定问题、无命令行交互，直接运行 OpenRouter + GPT-5 联网推理示例。

## 任务

> 东盟 10 国首都之间，距离最近的两个首都是？给出你的详细分析推理过程。

## 运行

```bash
cd week1/search-codegen-demo
pip install -r requirements.txt
cp env.example .env   # 填入 OPENROUTER_API_KEY
python main.py
```

配置见 `env.example`（`OPENROUTER_API_KEY`、`MODEL_NAME`、`REASONING_EFFORT` 等）。

## 与 search-codegen 的区别

| 项目 | 说明 |
|------|------|
| `search-codegen` | 完整版，交互式 CLI、`argparse`、测试脚本 |
| `search-codegen-demo` | 精简版，固定单题，`python main.py` 直接跑 |

## 技术要点

- **API**：OpenRouter `POST /chat/completions`
- **联网**：OpenRouter `plugins: [{ "id": "web" }]`（非 Kimi 的 `$web_search`）
- **推理**：`reasoning.effort` 默认 **`medium`**（可通过 `REASONING_EFFORT` 覆盖）
- **Token 上限**：`DEFAULT_MAX_TOKENS` 默认 `16000`（medium 推理 + 联网任务较耗 token，4000 可能截断）
- **模型**：默认 `openai/gpt-5-2025-08-07`

更多背景见 `week1/search-codegen/NOTE.md`（OpenRouter 与 GPT-5 原生工具格式的差异）。
