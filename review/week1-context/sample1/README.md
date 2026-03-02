# Sample 1：货币换算任务

从 `week1/context` 抽取的**仅运行第一个样例**的最小代码副本。运行本目录下的 `main.py` 即执行「Currency Conversion Task」：将 1000 USD 转换为 EUR、GBP、JPY 并计算三者平均值。

## 运行方式

1. 安装依赖：`pip install -r requirements.txt`
2. API Key：代码中已内置默认豆包 API Key，可直接运行。若需使用自己的 key，可任选其一：
   - 环境变量：`set ARK_API_KEY=你的密钥`（Windows CMD）或 `export ARK_API_KEY=...`（Linux/macOS）
   - 命令行参数：`python main.py --api-key 你的密钥`
3. 执行：`python main.py`

可选参数：`--provider doubao`（默认）、`--model 模型名`、`--api-key 密钥`。

## 文件说明

- `main.py`：入口，仅执行 sample 1 任务并打印结果
- `agent.py`：Context-Aware Agent 与工具（货币换算、计算器、PDF、code_interpreter）
- `config.py`：配置与 .env 加载
- `requirements.txt`：依赖列表


```
E:\ai&ai agent\github\ai-agent-book-projects\week1\context>set ARK_API_KEY=8a1a765d-9904-4a05-875a-7afc9f31c9a1
```

火山引擎→产品→豆包大模型→官方文档
- 快速入门：https://www.volcengine.com/docs/82379/1399008?lang=zh
- 文本生成：https://www.volcengine.com/docs/82379/1399009?lang=zh