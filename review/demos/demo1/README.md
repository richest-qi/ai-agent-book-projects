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

**方式三：OpenRouter（OpenAI 兼容）**

一个 API Key 通过 [OpenRouter](https://openrouter.ai) 调用 100+ 模型。仍用 `openai` 包，`base_url` 指到 OpenRouter，并在 `.env` 中设置 `OPENROUTER_API_KEY`：

```bash
python main_openrouter.py
```

**多轮对话（方舟 responses API，自动管理上下文）**

```bash
python main_multiturn.py
```

**内置联网搜索（Web Search）查实时信息（如天气）**

使用豆包内置 [联网搜索 Web Search](https://www.volcengine.com/docs/82379/1756990) 工具，通过 Responses API 获取实时公开网络信息（新闻、商品、天气等）：

```bash
python main_weather_websearch.py
```

> **若报错 `ToolNotOpen` / 404**：表示当前账号未开通「联网搜索」能力。需在火山引擎控制台开通 [内容插件](https://console.volcengine.com/common-buy/CC_content_plugin) 后再用；或改用 **Function Calling 自定义天气**（见下）。

**Function Calling 自定义天气（推荐，无需开通内容插件）**

在 Chat API 中注册 `get_weather` 工具，本地调用 [Open-Meteo](https://open-meteo.com/) 免费天气 API 获取实时数据，由豆包根据工具结果生成回复：

```bash
python main_weather_function_calling.py
```

**Function Calling 流程理解**（大模型 ↔ Agent 如何协作）：

1. **大模型决定要调工具**：看到用户问题（如「北京今天天气如何？」）后，大模型在**响应里**通过结构化的 `**tool_calls`** 表示要调用哪个函数、传什么参数（例如 `get_weather`、`{"city": "北京"}`），而不是用自然语言“告诉”谁去调。
2. **Agent 执行工具**：**Agent（本 demo 的代码）** 解析响应中的 `tool_calls`，在本地调用 `get_weather("北京")`，从 Open-Meteo 等接口拿到天气数据。
3. **把工具结果与对话再次发给大模型**：Agent 将「助手消息（含 tool_calls）」和「每条工具的执行结果」按约定格式追加进 **messages**（工具结果用 `role: "tool"` 并带上对应 `tool_call_id`），然后把**整段对话**（用户问题 + 助手带 tool_calls 的消息 + 天气结果）再次请求大模型。
4. **大模型给出最终回答**：大模型基于完整上下文（含天气数据）生成面向用户的最终回复（如天气概况 + 穿衣建议）；此轮通常不再带 `tool_calls`，`finish_reason` 为 `stop`，Agent 取 `content` 作为最终答案。

小结：**大模型负责“决定”调什么工具、传什么参数（通过 `tool_calls`）；Agent 负责真正执行工具、把结果回填进对话并再次请求；大模型根据新上下文给出最终回答。**

六种方式共用同一套依赖；方式一、二、四、五、六用 `ARK_API_KEY`，方式三用 `OPENROUTER_API_KEY`。成功时都会打印模型回复。

---

## 豆包：Responses API 与 Chat API 的区别

本 demo 里 **main.py** 用的是 **Chat API**（`client.chat.completions.create`），**main_multiturn.py** 用的是 **Responses API**（`client.responses.create`）。二者都是方舟/豆包提供的接口，但用法和适用场景不同。


| 维度          | Chat API                                                                            | Responses API                                                                                 |
| ----------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **调用方式**    | `client.chat.completions.create(model=..., messages=[...])`                         | `client.responses.create(model=..., input=..., previous_response_id=...)`                     |
| **上下文由谁维护** | **客户端**：每次请求都要传完整的 `messages`（历史对话 + 本轮输入）                                          | **服务端**：用 `previous_response_id` 关联上一轮，只传本轮 `input`，不必每次带完整历史                                 |
| **多轮对话**    | 自己把每轮的 assistant 回复和 tool 结果 append 到 `messages`，下次请求整段发出去                          | 服务端根据 `previous_response_id` 自动关联上下文，多轮只需不断传新 input + 上一轮 response.id                         |
| **工具调用**    | 需自己实现循环：收到 `tool_calls` → 本地执行工具 → 把结果以 `role: "tool"` 追加进 messages → 再次调用 Chat API | 支持服务端/内置工具与自动化流程，多轮与工具调用由 API 设计原生支持                                                          |
| **返回结构**    | OpenAI 风格：`response.choices[0].message`（含 `content`、`tool_calls` 等）                 | 方舟自有结构：`response.output`（列表，含 reasoning、message 等），`response.id` 用作下一轮 `previous_response_id` |
| **典型场景**    | 需要精细控制每条消息、或与 OpenAI 接口对齐（如 agent 自管上下文、自执行工具）                                      | 多轮对话、智能体式交互，希望少写上下文与工具循环代码时                                                                   |


**简要结论**：**Chat API** = 客户端管上下文、自己组 messages、自己处理 tool_calls 的「传统」用法；**Responses API** = 服务端管上下文、用 `previous_response_id` 串起多轮、适合多轮对话与内置工具的「新」用法。本仓库中 [week1/context](../../week1/context) 的 agent 用的是 Chat API 自管上下文 + 自执行工具；demo1 的 main_multiturn.py 演示的是 Responses API 的多轮用法。

---

### 区别概览


| 维度          | main.py（方舟 SDK）           | main_openai.py（OpenAI → 豆包）  | main_openrouter.py（OpenRouter） |
| ----------- | ------------------------- | ---------------------------- | ------------------------------ |
| **依赖**      | `volcenginesdkarkruntime` | `openai`                     | `openai`                       |
| **客户端**     | `Ark(...)`                | `OpenAI(base_url=豆包)`        | `OpenAI(base_url=OpenRouter)`  |
| **API Key** | ARK_API_KEY（豆包）           | ARK_API_KEY（豆包）              | OPENROUTER_API_KEY             |
| **模型范围**    | 仅豆包/方舟模型                  | 仅豆包模型                        | 100+ 厂商模型（按模型 ID 切换）           |
| **厂商能力**    | 可用方舟独有参数（如 thinking）      | 仅 OpenAI 兼容部分                | 统一成 OpenAI 形接口，部分高级能力可能被归一化    |
| **代码形态**    | 厂商专用                      | 通用 OpenAI 写法，换 base_url 即换厂商 | 同一套代码换 model 即换模型              |


- **main.py**：直接调豆包，和火山引擎文档、控制台一致，可用方舟特有参数（例如 `thinking` 配置）。
- **main_openai.py**：用「OpenAI 兼容接口」调豆包，不装方舟 SDK 也能调豆包，适合已有大量 `openai` 代码、只想多接一个豆包后端的项目。
- **main_openrouter.py**：不直接连某一家厂商，而是连 OpenRouter 网关，通过改 `model` 字符串（如 `openai/gpt-4o-mini`、`google/gemini-2.0-flash-exp:free`）切换模型，一个 Key 多模型。

### 实际 AI Agent 开发中怎么选

- **只接豆包、要深度用方舟能力**（思考链、特定参数）→ 用 **main.py 方式**（方舟 SDK）。
- **已有或打算统一用 OpenAI 接口**，且主要/只接豆包 → 用 **main_openai.py 方式**（`openai` + 豆包 base_url），少一个 SDK，代码风格统一。
- **要接多厂商、多模型，或希望少管多个 API Key** → 用 **main_openrouter.py 方式**（OpenRouter + `openai`），用一份调用逻辑、通过配置或环境变量切换 `model` 和 OPENROUTER_API_KEY。
- **做产品/框架、希望后端可插拔**：在代码里抽象一层「LLM 客户端」（例如统一成 `client.chat.completions.create(...)`），再按配置选不同的 `base_url` + `api_key`（或 OpenRouter），这样三种方式都可以作为后端实现之一接入。

---

## 方舟 responses.create 返回结构解析

使用方舟 **Responses API**（`client.responses.create`，多轮对话）时，返回的是方舟自定义的 **Response** 对象，与 OpenAI 的 `choices[0].message.content` 不同。下面说明其真实结构及如何取出「助手回复文本」。

### 顶层 Response 对象


| 字段                     | 含义                                                            |
| ---------------------- | ------------------------------------------------------------- |
| `id`                   | 本轮响应 ID，多轮续聊时下一轮请求需传 `previous_response_id=response.id`       |
| `output`               | **列表**，包含推理项和助手消息（见下）                                         |
| `status`               | 状态，如 `completed`                                              |
| `usage`                | 用量：`input_tokens`、`output_tokens`、`reasoning_tokens`（若为思考模型）等 |
| `previous_response_id` | 上一轮响应的 ID（首轮为 `None`）                                         |


### output 列表结构

`response.output` 是一个**列表**，按顺序包含两类元素：

1. **推理项**（可选）
  - 类型：`ResponseReasoningItem`，`type='reasoning'`  
  - 内容：模型内部思考过程（`summary[].text`），一般不直接展示给用户。
2. **助手消息**
  - 类型：`ResponseOutputMessage`，`type='message'`，`role='assistant'`  
  - **content**：列表，元素为 `ResponseOutputText(type='output_text', text='...')`  
  - 这里的 `**text`** 才是需要展示的助手回复正文。

### 结构关系简图

```text
Response
├── id                    # 本轮响应 ID（多轮时传给下一轮）
├── output: [             # 列表
│   ├── ResponseReasoningItem   # type='reasoning'，推理过程，可不展示
│   └── ResponseOutputMessage  # type='message'，助手消息
│         └── content: [
│               ResponseOutputText(text='助手回复的纯文本')
│             ]
├── usage                 #  token 用量
└── previous_response_id  # 上一轮 ID（首轮为 None）
```

```
Response(
    created_at = 1772421084,
    error = None,
    id = 'resp_021772421084318b786245abeed7e2e08a64d817f8b1331b56a7f',
    incomplete_details = None,
    max_output_tokens = 32768,
    model = 'doubao-seed-1-6-251015',
    object = 'response',
    output = [
        ResponseReasoningItem(
            id = 'rs_02177242108498800000000000000000000ffffac15bc7b2dbce5',
            summary = [Summary(text = '\n用户让讲个笑话，首先得选一个轻松有趣、容易理解的，别太复杂。最好贴近生活，有共鸣的那种。比如关于日常小糗事或者动物的？动物的笑话通常比较可爱，容易让人笑。\n\n比如，想到一个关于企鹅的笑话？或者关于程序员的？或者生活中的小误会？比如下面这个：\n\n有一天，我问我家猫：“你为什么总是盯着我看？” 猫说：“因为你长得像鱼啊！” 我：“可我不是鱼啊？” 猫：“没关系，我可以等你变成鱼。” \n\n或者另一个：程序员去买早餐，老板问：“要加蛋吗？” 程序员说：“加一个。” 老板又问：“还要加别的吗？” 程序员：“加一个蛋。” 老板：“……我是问你还要加别的吗？比如火腿？” 程序员：“哦，那加一个火腿和一个蛋。” 老板：“……” \n\n或者更简单的：为什么数学书总是很忧郁？因为它有太多的问题。 \n\n嗯，选哪个好呢？第一个猫的笑话比较温馨可爱，应该不错。或者再想想有没有更搞笑的？比如：\n\n有一次我去买奶茶，店员问我：“要几分糖？” 我说：“七分糖。” 店员：“好的，那请问你要大杯还是中杯？” 我：“七分杯。” 店员：“？？？” \n\n哈哈，这个也挺有趣的。或者选那个数学书的？或者企鹅的？比如：\n\n企鹅开车去南极，半路上车坏了，他下来检查，发现是发动机出问题了。于是他去附近的修理厂，修理工说：“你先回去等吧，我看看，明天再来取。” 第二天企鹅来取车，修理工说：“好了，修好了。” 企鹅问：“什么问题？” 修理工说：“没什么，就是冻住了。” 企鹅：“……” \n\n这个也可以。不过可能用户喜欢更生活化的。再选一个吧，比如：\n\n为什么老师总是喜欢用红笔批改作业？因为这样看起来像“开门红”，希望学生进步！ \n\n或者：小明问妈妈：“妈妈，为什么我不能玩手机？” 妈妈说：“因为手机会影响你的学习。” 小明：“那爸爸为什么可以玩？” 妈妈：“因为爸爸已经不用学习了。” 小明：“哦，那我也不想学习了！” 妈妈：“……” \n\n这个挺真实的，可能会引起共鸣。或者就用那个猫的笑话吧，比较可爱。确定了，就讲那个猫的笑话：\n\n有一天，我蹲下来跟我家猫对视，它一直盯着我看，我忍不住问：“你老盯着我干嘛呀？”  \n猫慢悠悠地甩了甩尾巴，说：“因为你长得像鱼啊。”  \n我愣了一下：“可我不是鱼啊！”  \n猫眨了眨眼：“没关系，我可以等你变成鱼。”  \n\n这个应该可以，轻松有趣，没有什么复杂的梗，容易理解。', type = 'summary_text')],
            type = 'reasoning',
            status = 'completed'),
        ResponseOutputMessage(
			   type = 'message', 
			   role = 'assistant',
            content = [ResponseOutputText(type = 'output_text', text = '有一天，我蹲下来跟我家猫对视，它一直盯着我看，我忍不住问：“你老盯着我干嘛呀？”  \n猫慢悠悠地甩了甩尾巴，说：“因为你长得像鱼啊。”  \n我愣了一下：“可我不是鱼啊！”  \n猫眨了眨眼：“没关系，我可以等你变成鱼。”  \n\n（猫：耐心是捕猎的第一要素，人类你不懂~） 😂', annotations = None)],
            status = 'completed',
            id = 'msg_02177242110573800000000000000000000ffffac15bc7ba248e4',
            partial = None)],
    previous_response_id = None,
    thinking = None,
    service_tier = 'default',
    status = 'completed',
    temperature = None,
    tools = None,
    top_p = None,
    usage = ResponseUsage(input_tokens = 41, input_tokens_details = InputTokensDetails(cached_tokens = 0), output_tokens = 801, output_tokens_details = OutputTokensDetails(reasoning_tokens = 701), total_tokens = 842, tool_usage = None, tool_usage_details = None),
    caching = ResponseCaching(type = 'disabled', prefix = None),
    text = None,
    instructions = None,
    store = True,
    expire_at = 1772680284,
    tool_choice = None,
    parallel_tool_calls = None,
    max_tool_calls = None,
    reasoning = None
)
```

### 如何取出助手回复文本

1. 遍历 `response.output`，找到 `type='message'` 的项。
2. 从该项的 `content` 列表中，取每个元素的 `text` 属性并拼接（通常只有一条），即得到助手回复的纯文本。

本仓库中 `main_multiturn.py` 里的 `get_reply_text(resp)` 即按上述逻辑实现，可直接复用或参考。

---

### 连接错误：WinError 10054 / ArkAPIConnectionError

表示**与豆包服务器的连接被中断**，多为网络环境导致，而非代码错误。可依次排查：

- **代理 / VPN**：关闭 VPN 或切换网络（如手机热点）后重试。
- **公司网络 / 防火墙**：出口可能拦截 `ark.cn-beijing.volces.com`，尝试换网络或放行该域名。
- **偶发**：多运行几次 `python main.py`。

可先在浏览器访问 [https://ark.cn-beijing.volces.com](https://ark.cn-beijing.volces.com) 确认本机能否连通。

### pip 安装方舟 SDK 报错

若出现 `Invalid requirement ... Expected package name at the start`，多半是 Windows 下用了**单引号**。请改用双引号：

```bash
pip install "volcengine-python-sdk[ark]"
```

---

## 文件说明


| 文件                                 | 说明                                                                      |
| ---------------------------------- | ----------------------------------------------------------------------- |
| `main.py`                          | 方舟 SDK：创建 Ark 客户端，发送一条对话并打印回复                                           |
| `main_openai.py`                   | OpenAI SDK 调豆包：用 `openai` 包 + 豆包 base_url，效果同 main.py                   |
| `main_openrouter.py`               | OpenRouter：用 `openai` 包 + OpenRouter base_url，可切换 100+ 模型               |
| `main_multiturn.py`                | 多轮对话：方舟 responses.create + previous_response_id，每轮输出清晰区分                |
| `main_weather_websearch.py`        | 内置 Web Search：Responses API + tools=[web_search]，查询北京今日天气等实时信息（需开通内容插件） |
| `main_weather_function_calling.py` | Function Calling：Chat API + 自定义 get_weather 工具（Open-Meteo），无需开通插件即可查天气  |
| `requirements.txt`                 | 依赖：方舟 SDK、python-dotenv、openai、requests                                 |
| `env.example`                      | 环境变量示例，复制为 `.env` 并填写 `ARK_API_KEY`                                     |
| `record.md`                        | 安装与排错记录（如 Windows 下 pip 引号问题）                                           |


