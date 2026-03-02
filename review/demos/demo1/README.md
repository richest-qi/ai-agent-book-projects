# Demo1：豆包对话最小示例

使用火山引擎**方舟（Ark）SDK**调用豆包模型，完成一次简单对话（例如「你是谁？」）。适合快速验证环境与 API Key 是否可用。

---

## 前置条件

- Python 3.8+
- 豆包 API Key（[火山引擎控制台](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey) 创建）

---

## 安装依赖

```bash
pip install -r requirements.txt
```

**Windows 下若单独安装方舟 SDK**：请使用双引号，不要用单引号，否则会报 `Invalid requirement`：

```bash
pip install "volcengine-python-sdk[ark]"
```

---

## 配置 API Key

二选一即可：

1. **推荐：使用 .env 文件**  
   复制 `env.example` 为 `.env`，将 `ARK_API_KEY=你的密钥` 改为你的真实密钥。勿将 `.env` 提交到 Git。

2. **使用环境变量**  
   - Windows CMD: `set ARK_API_KEY=你的密钥`  
   - PowerShell: `$env:ARK_API_KEY="你的密钥"`  
   - Linux/macOS: `export ARK_API_KEY=你的密钥`

程序会先读同目录下的 `.env`，没有再使用系统环境变量。  
- `main.py` / `main_openai.py` 使用 **ARK_API_KEY**（豆包）。  
- `main_openrouter.py` 使用 **OPENROUTER_API_KEY**（在 [OpenRouter](https://openrouter.ai/keys) 获取）。

---

## 运行

**方式一：方舟 SDK（默认）**

```bash
python main.py
```

**方式二：OpenAI SDK 调豆包**

豆包提供 OpenAI 兼容接口，可用 `openai` 包调用，仅需把 `base_url` 指到豆包：

```bash
python main_openai.py
```

**方式三：OpenRouter SDK（OpenAI 兼容）**

一个 API Key 通过 [OpenRouter](https://openrouter.ai) 调用 100+ 模型（OpenAI、Google、Anthropic 等）。仍用 `openai` 包，`base_url` 指到 OpenRouter，并在 `.env` 中设置 `OPENROUTER_API_KEY`：

```bash
python main_openrouter.py
```

三种方式共用同一套依赖（`requirements.txt`）；方式一、二用 `ARK_API_KEY`，方式三用 `OPENROUTER_API_KEY`。成功时都会打印模型回复。

---

## 三种调用方式对比与选择

### 区别概览

| 维度 | main.py（方舟 SDK） | main_openai.py（OpenAI → 豆包） | main_openrouter.py（OpenRouter） |
|------|---------------------|----------------------------------|----------------------------------|
| **依赖** | `volcenginesdkarkruntime` | `openai` | `openai` |
| **客户端** | `Ark(...)` | `OpenAI(base_url=豆包)` | `OpenAI(base_url=OpenRouter)` |
| **API Key** | ARK_API_KEY（豆包） | ARK_API_KEY（豆包） | OPENROUTER_API_KEY |
| **模型范围** | 仅豆包/方舟模型 | 仅豆包模型 | 100+ 厂商模型（按模型 ID 切换） |
| **厂商能力** | 可用方舟独有参数（如 thinking） | 仅 OpenAI 兼容部分 | 统一成 OpenAI 形接口，部分高级能力可能被归一化 |
| **代码形态** | 厂商专用 | 通用 OpenAI 写法，换 base_url 即换厂商 | 同一套代码换 model 即换模型 |

- **main.py**：直接调豆包，和火山引擎文档、控制台一致，可用方舟特有参数（例如 `thinking` 配置）。
- **main_openai.py**：用「OpenAI 兼容接口」调豆包，不装方舟 SDK 也能调豆包，适合已有大量 `openai` 代码、只想多接一个豆包后端的项目。
- **main_openrouter.py**：不直接连某一家厂商，而是连 OpenRouter 网关，通过改 `model` 字符串（如 `openai/gpt-4o-mini`、`google/gemini-2.0-flash-exp:free`）切换模型，一个 Key 多模型。

### 实际 AI Agent 开发中怎么选

- **只接豆包、要深度用方舟能力**（思考链、特定参数）→ 用 **main.py 方式**（方舟 SDK）。
- **已有或打算统一用 OpenAI 接口**，且主要/只接豆包 → 用 **main_openai.py 方式**（`openai` + 豆包 base_url），少一个 SDK，代码风格统一。
- **要接多厂商、多模型，或希望少管多个 API Key** → 用 **main_openrouter.py 方式**（OpenRouter + `openai`），用一份调用逻辑、通过配置或环境变量切换 `model` 和 OPENROUTER_API_KEY。
- **做产品/框架、希望后端可插拔**：在代码里抽象一层「LLM 客户端」（例如统一成 `client.chat.completions.create(...)`），再按配置选不同的 `base_url` + `api_key`（或 OpenRouter），这样三种方式都可以作为后端实现之一接入。

---

## 常见问题

### 连接错误：WinError 10054 / ArkAPIConnectionError

表示**与豆包服务器的连接被中断**，多为网络环境导致，而非代码错误。可依次排查：

- **代理 / VPN**：关闭 VPN 或切换网络（如手机热点）后重试。
- **公司网络 / 防火墙**：出口可能拦截 `ark.cn-beijing.volces.com`，尝试换网络或放行该域名。
- **偶发**：多运行几次 `python main.py`。

可先在浏览器访问 https://ark.cn-beijing.volces.com 确认本机能否连通。

### pip 安装方舟 SDK 报错

若出现 `Invalid requirement ... Expected package name at the start`，多半是 Windows 下用了**单引号**。请改用双引号：

```bash
pip install "volcengine-python-sdk[ark]"
```

---

## 文件说明

| 文件 | 说明 |
|------|------|
| `main.py` | 方舟 SDK：创建 Ark 客户端，发送一条对话并打印回复 |
| `main_openai.py` | OpenAI SDK 调豆包：用 `openai` 包 + 豆包 base_url，效果同 main.py |
| `main_openrouter.py` | OpenRouter：用 `openai` 包 + OpenRouter base_url，可切换 100+ 模型 |
| `requirements.txt` | 依赖：方舟 SDK、python-dotenv、openai |
| `env.example` | 环境变量示例，复制为 `.env` 并填写 `ARK_API_KEY` |
| `record.md` | 安装与排错记录（如 Windows 下 pip 引号问题） |
