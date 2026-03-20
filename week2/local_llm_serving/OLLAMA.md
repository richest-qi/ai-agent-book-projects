# Ollama 使用说明

本文档汇总本项目中与 [Ollama](https://ollama.com/) 相关的内容：安装、常用命令、如何查看本机安装路径，以及在本项目中的用法。

---

## 什么是 Ollama

Ollama 是在本机运行大语言模型的工具，支持 macOS、Windows、Linux。本项目在**无 NVIDIA GPU** 或 **macOS** 环境下会优先使用 Ollama 作为推理后端，与 vLLM（有 GPU 时）二选一。

- 官网：<https://ollama.com/>
- 文档：<https://ollama.com/docs>

---

## 安装

### Windows

1. 从官网下载安装程序：<https://ollama.com/download/windows>
2. 运行 `OllamaSetup.exe` 完成安装（可自选安装目录，例如 `D:\ollama`）
3. 安装完成后可从系统托盘启动，或在终端运行 `ollama serve`

### macOS

```bash
brew install ollama
# 启动服务（可在单独终端）
ollama serve
```

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
# 启动
systemctl start ollama
# 或前台运行
ollama serve
```

---

## 查看本机 Ollama 安装路径

### Windows

在 **PowerShell** 或 **CMD** 中执行：

```powershell
where ollama
```

或在 PowerShell 中：

```powershell
(Get-Command ollama).Source
```

输出即为 `ollama.exe` 的完整路径，其所在目录即为安装路径（例如 `D:\ollama`）。

### macOS / Linux

在终端执行：

```bash
which ollama
```

---

## 常用命令

| 命令 | 说明 |
|------|------|
| `ollama serve` | 启动本地服务（默认 http://localhost:11434） |
| `ollama list` | 列出已拉取的模型 |
| `ollama pull <模型名>` | 拉取模型，例如 `ollama pull qwen3:0.6b` |
| `ollama run <模型名>` | 在命令行中与模型对话 |
| `ollama stop <模型名>` | 从内存中卸载模型 |

本项目默认使用的模型为 **qwen3:0.6b**，若未安装可执行：

```bash
ollama pull qwen3:0.6b
```

---

## 在本项目中的使用

- **自动选择**：运行 `python main.py` 时，若无可用 GPU（或为 macOS），会自动使用 Ollama 后端。
- **强制使用 Ollama**：`python main.py --backend ollama`
- **依赖**：`pip install ollama`（见 `requirements.txt`）
- **实现**：Ollama 相关逻辑在 `ollama_native.py`，主入口在 `main.py` 中的 `_init_ollama()`。

若提示 “Ollama not found” 或连接失败，请先确认：

1. 已安装 Ollama（见上方安装说明）
2. 服务已启动（系统托盘或 `ollama serve`）
3. 已拉取模型：`ollama pull qwen3:0.6b`

更多说明见项目根目录 [README.md](README.md)。
