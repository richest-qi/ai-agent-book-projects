"""Configuration for Ollama tool-calling demo (Mode C: API non-stream / blocking)."""

import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:0.6b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEBUG_RESPONSE = os.getenv("DEBUG_RESPONSE", "false").lower() in ("1", "true", "yes")

TASK = os.getenv(
    "TASK",
    "What's the current time and weather like in Vancouver right now?",
)
