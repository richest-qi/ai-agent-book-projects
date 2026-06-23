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

可选参数：

```bash
python main.py --provider doubao
python main.py --model doubao-seed-2-0-lite-260428
python main.py --quiet          # 不打印完整 request/response JSON
```

## 与 week1/context 的区别

| | `week1/context` | 本工程 |
|---|---|---|
| 入口 | 交互式 REPL | `python main.py` 直接跑完 |
| 任务 | 5 个 sample + 消融实验 | 仅货币换算任务 |
| 工具 | PDF、code_interpreter 等 | `convert_currency`、`calculate` |
| 依赖 | 较多 | 仅 `openai`、`python-dotenv` |

代码为独立副本，修改 `week1/context` 不会影响本目录。
