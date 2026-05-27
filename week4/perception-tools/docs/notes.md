1. 安装依赖：`pip install -r requirements.txt`
2. 导入module：`python test_imports.py`
3. 跑起来：`python quickstart.py`   

响应结果如下：
```bash
================================================================================
PERCEPTION TOOLS MCP SERVER - QUICKSTART
================================================================================

📝 Test 1: Web Search
--------------------------------------------------------------------------------
INFO:root:🔍 Searching for: 'Python programming'
INFO:root:✅ Found 0 results in 1.93s
✅ Found 0 results

📝 Test 2: Wikipedia Search
--------------------------------------------------------------------------------
INFO:root:📚 Searching Wikipedia for: Artificial Intelligence
INFO:root:✅ Found Wikipedia article: Artificial intelligence
✅ Article: Artificial intelligence
Summary: Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and dec...

📝 Test 3: Currency Conversion
--------------------------------------------------------------------------------
INFO:root:💱 Converting 100 USD to EUR
INFO:root:✅ 100 USD = 85.90 EUR
✅ 100 USD = 85.90 EUR

📝 Test 4: Weather Information
--------------------------------------------------------------------------------
INFO:root:🌤️ Getting weather for: London
INFO:root:✅ Weather: 26.9°C - Clear sky
✅ London: 26.9°C - Clear sky

📝 Test 5: Web Page Reading
--------------------------------------------------------------------------------
INFO:root:📄 Reading webpage: https://www.example.com
INFO:root:✅ Successfully extracted webpage content
✅ Page: Example Domain
Text length: 139 characters

📝 Test 6: File Operations (Reading this script)
--------------------------------------------------------------------------------
INFO:root:📖 Reading file: E:\ai&ai agent\github\ai-agent-book-projects\week4\perception-tools\quickstart.py
INFO:root:✅ Successfully read file (500 characters)
✅ Read 4326 bytes from quickstart.py

================================================================================
QUICKSTART COMPLETE
================================================================================

ℹ️  Note: Some tests may fail if API keys are not configured.
   Check env.example and configure your .env file for full functionality.

```

## 模式A：直接运行 `quickstart.py`（已跑通）

这是纯脚本方式，不涉及 MCP 通信，也不需要 LLM。

### 启动命令

在 `week4/perception-tools` 目录下运行：

```bash
python quickstart.py
```

### 工具定义与调用链

- 工具“实现”定义在 `src/` 下的函数里：
  - `search_tools.py`：`search_web`
  - `public_data_tools.py`：`search_wikipedia`、`convert_currency`、`get_weather`
  - `multimodal_tools.py`：`read_webpage`
  - `filesystem_tools.py`：`read_file`（以及 `grep_search` 等）
- `quickstart.py` 通过 `sys.path.insert(.../src)` 直接 `import` 这些函数，然后用 `await xxx(...)` 调用。

因此你看到的输出（Web Search/Wikipedia/Weather/网页读取/文件读取）都来自这些 `src/*.py` 的实现函数被直接执行。

---

## 模式B：启动 MCP Server + 让 LLM 调用工具（LLM 决定调哪个工具）

模式B会启动 `src/main.py` 作为 MCP Server（stdio 传输），客户端（如 Cursor Agent / Claude Desktop）连接后，由 LLM 根据用户意图选择要调用的 MCP 工具。

### 启动 MCP Server

在 `week4/perception-tools` 目录下运行：

```bash
python src/main.py
```

### 工具定义位置（MCP 侧）

- MCP 工具名及参数在 `src/main.py` 中用 `@mcp.tool(...)` 注册。
- `src/main.py` 里的 MCP 工具通常只是“薄封装”，内部会继续调用 `src/` 里的实现函数。

例如（对应关系）：

- `web_search` → 调用 `search_web`（在 `src/search_tools.py`）
- `weather` → 调用 `get_weather`（在 `src/public_data_tools.py`）
- `webpage_reader` → 调用 `read_webpage`（在 `src/multimodal_tools.py`）
- `file_reader` → 调用 `read_file`（在 `src/filesystem_tools.py`）

### 工具是如何被“调用到”的

当你在 MCP 客户端里说类似“查一下伦敦天气/总结这个网页”等问题时：

1. LLM 读取 MCP Server 暴露的工具清单（`@mcp.tool` 的描述与参数类型）。
2. LLM 推断需要哪个工具，并组织参数。
3. MCP 客户端把“工具调用请求”发给 `src/main.py`。
4. `src/main.py` 执行对应实现函数，然后把标准化的结果返回给 LLM。
5. LLM 再把结果组织成最终回答。

因此：**模式B里“调哪个工具”是 LLM 决策**；而模式A里“调哪个工具”是脚本写死的。

Cursor 配置步骤与「查伦敦天气」示例见：[CURSOR_MCP_GUIDE.md](./CURSOR_MCP_GUIDE.md)。