# Currency Conversion Demo

从 `week1/context` 抽取的**独立精简工程**，直接运行货币换算示例（Sample 1），无需交互式输入。

## 任务

将 $1000 USD 转换为 EUR、GBP、JPY，并计算三者换算结果的平均值。

## 运行

```bash
cd week1/currency-conversion
pip install -r requirements.txt
cp env.example .env   # 填入 ARK_API_KEY 等
python main.py
```

所有配置在 `.env` 中设置（`ARK_API_KEY`、`MODEL_NAME`），见 `env.example`。

## 豆包 API 地址说明

火山方舟文档中的 Chat API 完整地址为：

```text
https://ark.cn-beijing.volces.com/api/v3/chat/completions
```

本工程使用 OpenAI 兼容 SDK（`openai` 包），`agent.py` 中配置的是 **API 根路径** `base_url`，而不是完整 endpoint：

```python
OpenAI(
    api_key=api_key,
    base_url="https://ark.cn-beijing.volces.com/api/v3",  # 不含 /chat/completions
)
```

调用 `client.chat.completions.create(...)` 时，SDK 会自动拼接路径：

```text
base_url + /chat/completions
= https://ark.cn-beijing.volces.com/api/v3/chat/completions
```

因此 `base_url` 与文档中的完整 URL **并不矛盾**，写法是正确的。

常见误配：

| 写法 | 结果 |
|------|------|
| `base_url=".../api/v3"` + `chat.completions.create()` | 正确 |
| `base_url=".../api/v3/chat/completions"` | 错误，SDK 会再拼 `/chat/completions`，导致 404 |
| `base_url="https://ark.cn-beijing.volces.com"` | 错误，缺少 `/api/v3` 前缀 |

## 与 week1/context 的区别

| | `week1/context` | 本工程 |
|---|---|---|
| 入口 | 交互式 REPL | `python main.py` 直接跑完 |
| 任务 | 5 个 sample + 消融实验 | 仅货币换算任务 |
| 工具 | PDF、code_interpreter 等 | `convert_currency`、`calculate` |
| 依赖 | 较多 | 仅 `openai`、`python-dotenv` |

代码为独立副本，修改 `week1/context` 不会影响本目录。
