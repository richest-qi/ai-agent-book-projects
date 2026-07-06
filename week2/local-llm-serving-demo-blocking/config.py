"""Configuration for Ollama tool-calling demo (Mode C: API non-stream / blocking)."""

import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:0.6b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
# 本项目用于调试学习：默认打印每次阻塞响应分解；设 0 关闭
DEBUG_RESPONSE = os.getenv("DEBUG_RESPONSE", "true").lower() in ("1", "true", "yes")

TASK = os.getenv(
    "TASK",
    "What's the current time and weather like in Vancouver right now?",
)
