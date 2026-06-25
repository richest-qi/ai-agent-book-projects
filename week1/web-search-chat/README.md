# Web Search Chat

从 `week1/web-search-demo` 延伸的**联网搜索聊天 Web 应用**，使用 **FastAPI（后端 API）+ 原生 HTML/CSS/JS（前端页面）**，体验类似 ChatGPT / Kimi 的对话界面。

## 功能

- 网页聊天：用户在输入框提问，Agent 联网搜索后返回答案
- 多轮对话：同一会话内可追问，服务端维护 `conversation_history`
- 新对话：点击「新对话」清空会话

## 架构

```text
浏览器 (static/index.html + app.js)
    │  POST /api/chat  { session_id, message }
    ▼
FastAPI (main.py)
    │  按 session_id 查找 WebSearchAgent
    ▼
agent.py  →  Kimi API + $web_search
```

| 文件 | 职责 |
|------|------|
| `main.py` | FastAPI 路由、会话管理、静态资源 |
| `agent.py` | Kimi 联网搜索 Agent 逻辑 |
| `config.py` | `.env` 配置 |
| `static/` | 前端页面与样式 |

## 运行

```bash
cd week1/web-search-chat
pip install -r requirements.txt
cp env.example .env   # 填入 MOONSHOT_API_KEY
python main.py
```

浏览器打开：<http://127.0.0.1:8000>

API 文档（FastAPI 自动生成）：<http://127.0.0.1:8000/docs>

## 环境变量

见 `env.example`。常用项：

| 变量 | 说明 | 默认 |
|------|------|------|
| `MOONSHOT_API_KEY` | Kimi API Key | 必填 |
| `DEFAULT_MODEL` | 模型 | `kimi-k2.5` |
| `HOST` / `PORT` | 服务地址 | `127.0.0.1:8000` |

## 与 sibling 项目对比

| 项目 | 交互 |
|------|------|
| `web-search-demo` | 命令行，固定问题 |
| `web-search-agent` | 命令行，交互输入 |
| `web-search-chat` | **Web 聊天界面** |

## 说明

- 会话保存在服务端内存中，重启服务后会话丢失（教学 demo 足够）
- 默认模型 `kimi-k2.5`，`temperature` 固定为 `1`
- 官方文档：[Use Web Search](https://platform.moonshot.cn/docs/guide/use-web-search)
