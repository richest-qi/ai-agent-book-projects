"""Configuration for the search-codegen demo."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")


class Config:
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    OPENROUTER_BASE_URL: str = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "openai/gpt-5-2025-08-07")

    DEFAULT_TEMPERATURE: float = float(os.getenv("DEFAULT_TEMPERATURE", "0.3"))
    DEFAULT_MAX_TOKENS: int = int(os.getenv("DEFAULT_MAX_TOKENS", "16000"))
    REASONING_EFFORT: str = os.getenv("REASONING_EFFORT", "low")
    WEB_SEARCH_MAX_RESULTS: int = int(os.getenv("WEB_SEARCH_MAX_RESULTS", "5"))

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls) -> bool:
        if cls.OPENROUTER_API_KEY:
            return True
        print("ERROR: OPENROUTER_API_KEY is not set. Copy env.example to .env and fill in your API key.")
        return False
