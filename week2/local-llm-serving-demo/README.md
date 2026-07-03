# Local LLM Serving Demo

基于本地 **Ollama** 的工具调用单次任务 demo，从 [`../local_llm_serving`](../local_llm_serving) 复制核心代码，**完全独立**，不依赖父目录。

与父项目的交互模式不同：运行 `python main.py` 即执行固定任务，无需 CMD 输入。

## 前置条件

1. 安装 [Ollama](https://ollama.com)
2. 启动服务并拉取默认模型：

```cmd
ollama serve
ollama pull qwen3:0.6b
```

### Ollama 常用命令

`<model>` 为模型名，本项目默认 `qwen3:0.6b`。

| 命令 | 作用 |
|------|------|
| `ollama list` | 查看已安装模型 |
| `ollama pull <model>` | 下载模型 |
| `ollama run <model>` | 交互测试（`/bye` 退出） |
| `ollama stop <model>` | 从内存卸载模型，释放显存（不删磁盘文件） |
| `ollama rm <model>` | 删除本机模型文件 |

### Windows 服务管理

| 命令 | 作用 |
|------|------|
| `tasklist \| findstr ollama` | 查看 Ollama 进程，最后一列为 PID |
| `taskkill /F /PID <pid>` | 结束指定进程（如 `taskkill /F /PID 6012`） |
| `ollama serve` | 重新启动 Ollama 服务 |

## 快速开始

```bash
cd week2/local-llm-serving-demo
pip install -r requirements.txt
python main.py
```

默认任务（温哥华当前时间与天气）：

> What's the current time and weather like in Vancouver right now?

## 配置

复制 `env.example` 为 `.env`，或在 `config.py` 中修改：

| 变量 | 说明 | 默认 |
|------|------|------|
| `OLLAMA_MODEL` | Ollama 模型名 | `qwen3:0.6b` |
| `TASK` | 固定任务文本 | 温哥华时间+天气 |
| `STREAM` | 是否流式输出 | `true` |
| `DEFAULT_TEMPERATURE` | 采样温度 | `0.7` |

## 可用工具

与父项目相同，由 `tools.py` 注册：

- `get_current_temperature` — Open-Meteo 天气
- `get_current_time` — 时区时间
- `convert_currency` — 货币换算
- `code_interpreter` — Python 代码执行

## 与 `local_llm_serving` 的关系

| | `local_llm_serving` | 本项目 |
|--|---------------------|--------|
| 入口 | 交互模式 `/sample 3` | `python main.py` 直接跑 |
| 后端 | vLLM / Ollama 自动选择 | 仅 Ollama |
| 代码 | 完整工程 | 复制 `tools.py`、`ollama_native.py`，独立维护 |

## 文件结构

```
local-llm-serving-demo/
├── main.py           # 非交互入口
├── config.py         # 模型与固定任务
├── ollama_native.py  # Ollama 工具调用 Agent
├── tools.py          # 工具注册与实现
├── requirements.txt
└── env.example
```
