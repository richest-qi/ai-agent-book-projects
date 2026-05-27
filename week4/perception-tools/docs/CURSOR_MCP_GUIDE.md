# 在 Cursor 中使用 Perception Tools（模式 B）

本文说明如何在 Cursor 里通过 MCP 使用 `perception-tools`，并以「查伦敦天气」为例演示完整流程。

---

## 先理解：在哪里提问、在哪里回复

`python src/main.py` 启动的是 **MCP 服务端**，使用 **stdio** 与客户端通信，**不是聊天窗口**。

```
你（自然语言）  →  Cursor Chat / Agent  →  LLM 选择工具
                              ↓
                    MCP 客户端调用 perception-tools
                              ↓
                    src/main.py 执行 weather / webpage_reader 等
                              ↓
                    结果返回 LLM  →  你在对话里看到最终回复
```

| 位置 | 作用 |
|------|------|
| 运行 `python main.py` 的终端 | 仅服务进程日志；**不要在这里输入「查天气」** |
| **Cursor 聊天 / Agent** | **在这里用自然语言提问并看回复** |

日常推荐：**只配置 MCP，由 Cursor 自动拉起 `main.py`**，不必手动先开终端跑 `main.py`。

---

## 前置条件

1. 已在项目目录安装依赖（建议使用独立虚拟环境）：

```bash
cd week4/perception-tools
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. 天气等公开数据工具 **无需 API Key**（Open-Meteo 等）。

---

## 第一步：配置 Cursor MCP

### 方式 A：Cursor 设置界面

1. 打开 **Cursor Settings → MCP**。
2. 添加 Server，或编辑用户级 MCP 配置文件。

### 方式 B：直接编辑 `mcp.json`

在用户配置中增加（路径按本机修改）：

```json
{
  "mcpServers": {
    "perception-tools": {
      "command": "E:/ai&ai agent/github/ai-agent-book-projects/week4/perception-tools/.venv/Scripts/python.exe",
      "args": [
        "E:/ai&ai agent/github/ai-agent-book-projects/week4/perception-tools/src/main.py"
      ],
      "cwd": "E:/ai&ai agent/github/ai-agent-book-projects/week4/perception-tools/src"
    }
  }
}
```

说明：

- `command`：已安装 `requirements.txt` 的 **Python 解释器**（优先用 `.venv`）。
- `args`：`main.py` 的绝对路径。
- `cwd`：设为 `src`，与 `main.py` 内模块 import 方式一致。
- 路径含空格时，JSON 里可用 `/` 写法。

保存后 **重启 Cursor**，或在 MCP 面板确认 `perception-tools` 为已连接。

---

## 第二步：在 Cursor 里提问

1. 打开 **Chat** 或 **Agent**（Agent 更易自动调用 MCP 工具）。
2. 确认当前会话可使用 MCP（部分模式需在设置中启用对应 MCP Server）。
3. 用自然语言提问，例如：

   - `查一下伦敦现在的天气`
   - `用 weather 工具查 London 天气`

4. 观察对话中是否出现 **工具调用**（如 `weather`），以及 LLM 汇总后的文字回复。

### 背后发生了什么

1. LLM 读取 MCP 暴露的工具列表（`src/main.py` 中 `@mcp.tool` 注册的工具名与描述）。
2. 对「查伦敦天气」，通常会选用 **`weather`**（内部调用 `get_weather`）。
3. Cursor 通过 stdio 把请求发给 `main.py`，执行后返回 JSON。
4. LLM 将结果整理成自然语言展示给你。

对应实现：

- MCP 工具名：`weather`（`src/main.py`）
- 实现函数：`get_weather`（`src/public_data_tools.py`）

---

## 示例：查伦敦天气

### 模式 B（Cursor + MCP，推荐）

**你怎么问（在 Cursor 聊天里）：**

```text
查伦敦天气
```

**期望现象：**

- 对话中出现工具调用，例如 `weather`，参数类似 `location: "London"`。
- 最终回复包含气温、天气状况、湿度等（由 LLM 根据工具结果生成）。

**工具返回的数据结构示例**（`get_weather` / Open-Meteo，查询时间：2026-05-27）：

```json
{
  "success": true,
  "message": {
    "location": "London",
    "country": "United Kingdom",
    "temperature": 19.1,
    "feels_like": 17.9,
    "humidity": 65,
    "description": "Clear sky",
    "wind_speed": 14.0,
    "units": "metric",
    "provider": "Open-Meteo"
  }
}
```

**可读的汇总示例（LLM 通常会写成类似这样）：**

> 伦敦当前约 **19.1°C**，体感 **17.9°C**，**晴**（Clear sky），湿度 **65%**，风速约 **14 km/h**。

实际数值会随查询时间变化；以工具实时返回为准。

---

### 模式 A（对比：不用 Cursor，本地脚本验证）

若仅验证工具是否可用，可在终端直接跑实现函数（不经过 LLM）：

```bash
cd week4/perception-tools/src
python -c "import asyncio, json; from public_data_tools import get_weather; r=asyncio.run(get_weather('London')); print(json.loads(r.text))"
```

或在项目根目录：

```bash
python quickstart.py
```

其中 Test 4 即为天气查询。模式 A **不会**在 Cursor 对话里回复，结果打印在终端。

---

## 模式 A 与模式 B 对照

| 项目 | 模式 A | 模式 B（Cursor） |
|------|--------|------------------|
| 入口 | `quickstart.py` 或命令行 `get_weather` | Cursor Chat / Agent |
| 谁决定调哪个工具 | 代码写死 | **LLM** |
| 是否需要 MCP 配置 | 否 | **是** |
| 回复出现在哪 | 终端 | **Cursor 对话窗口** |
| 是否需手跑 `python main.py` | 否 | 通常否（Cursor 自动拉起） |

---

## 常见问题

### 1. 跑了 `python main.py` 但不知道在哪提问

在 **Cursor 聊天**里提问，不要在 `main.py` 的终端里输入。可关闭手动启动的进程，避免与 Cursor 拉起的实例冲突。

### 2. MCP 未连接 / 没有工具调用

- 检查 `mcp.json` 中 `command`、`args`、`cwd` 路径是否正确。
- 确认该 Python 环境已 `pip install -r requirements.txt`。
- 重启 Cursor，查看 MCP 面板中 `perception-tools` 状态。

### 3. 对话里没有调用 `weather`

- 改用 **Agent** 模式，或明确说「使用 perception-tools 的 weather 查 London」。
- 确认当前会话已启用该 MCP Server。

### 4. 与模式 A 文档的关系

- 模式 A 跑通记录与工具定义说明：见 [notes.md](./notes.md)
- PyCharm 调试 `quickstart.py`：见 [PYCHARM_DEBUG_QUICKSTART.md](./PYCHARM_DEBUG_QUICKSTART.md)

---

## 其他可尝试的自然语言示例

在 Cursor 中配置好 MCP 后，还可以尝试：

| 你说的话 | 可能调用的 MCP 工具 |
|----------|---------------------|
| 查伦敦天气 | `weather` |
| 100 美元等于多少欧元 | `currency_converter` |
| 搜一下维基百科里的人工智能 | `wikipedia_search` |
| 总结这个网页 https://www.example.com | `webpage_reader` |

更多工具名见 `src/main.py` 中 `@mcp.tool` 注册列表。
