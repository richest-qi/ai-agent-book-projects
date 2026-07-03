"""Configuration for local Ollama tool-calling demo."""

import os
from dotenv import load_dotenv

load_dotenv()

# Ollama
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:0.6b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")

# Inference
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
STREAM = os.getenv("STREAM", "true").lower() in ("1", "true", "yes")

# Fixed task (edit here or set TASK env var)
TASK = os.getenv(
    "TASK",
    "What's the current time and weather like in Vancouver right now?",
)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
