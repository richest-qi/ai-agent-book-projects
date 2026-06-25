"""Configuration for the web search chat app."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")


class Config:
    MOONSHOT_API_KEY: str = os.getenv("MOONSHOT_API_KEY", "")
    if not MOONSHOT_API_KEY:
        MOONSHOT_API_KEY = os.getenv("KIMI_API_KEY", "")

    KIMI_BASE_URL: str = os.getenv("KIMI_BASE_URL", "https://api.moonshot.cn/v1")
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "kimi-k2.5")
    MAX_SEARCH_ITERATIONS: int = int(os.getenv("MAX_SEARCH_ITERATIONS", "5"))

    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls) -> bool:
        if cls.MOONSHOT_API_KEY:
            return True
        print("ERROR: MOONSHOT_API_KEY is not set. Copy env.example to .env and fill in your API key.")
        return False
