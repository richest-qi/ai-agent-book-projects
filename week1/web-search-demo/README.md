# Web Search Demo

从 `week1/web-search-agent` 抽取的**独立精简工程**，固定问题、无命令行交互，直接运行联网搜索示例。

## 任务

回答：**2024年诺贝尔物理学奖获得者是谁？**

## 运行

```bash
cd week1/web-search-demo
pip install -r requirements.txt
cp env.example .env   # 填入 MOONSHOT_API_KEY
python main.py
```

配置见 `env.example`（`MOONSHOT_API_KEY`、`DEFAULT_MODEL` 等）。

## 与 web-search-agent 的区别

| 项目 | 说明 |
|------|------|
| `web-search-agent` | 完整版，支持交互式问答、示例脚本 |
| `web-search-demo` | 精简版，固定单题，`python main.py` 直接跑 |

## 技术要点

- 使用 Kimi 内置工具 `$web_search`（`type: builtin_function`）
- 默认模型 `kimi-k2.5`（`kimi-k2-0905-preview` 已下线）
- `temperature` 固定为 `1`（kimi-k2.5 要求）
- assistant 消息以普通 `dict` 回传，避免 OpenAI SDK 对 `builtin_function` 的 Pydantic 警告

官方文档：[Use Web Search](https://platform.moonshot.cn/docs/guide/use-web-search)
