"""Configuration for the currency conversion demo."""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")


class Config:
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "doubao").lower()

    SILICONFLOW_API_KEY: str = os.getenv("SILICONFLOW_API_KEY", "")
    ARK_API_KEY: str = os.getenv("ARK_API_KEY", "")
    MOONSHOT_API_KEY: str = os.getenv("MOONSHOT_API_KEY", "")

    MODEL_NAME: str = os.getenv("MODEL_NAME", "")
    MAX_ITERATIONS: int = int(os.getenv("MAX_ITERATIONS", "10"))

    EXCHANGE_RATES = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 149.50,
        "CNY": 7.24,
        "CAD": 1.36,
        "AUD": 1.53,
        "CHF": 0.88,
        "INR": 83.12,
        "SGD": 1.34,
    }

    @classmethod
    def get_api_key(cls, provider: str = None) -> str:
        provider = (provider or cls.LLM_PROVIDER).lower()
        if provider == "siliconflow":
            return cls.SILICONFLOW_API_KEY
        if provider == "doubao":
            return cls.ARK_API_KEY
        if provider in ("kimi", "moonshot"):
            return cls.MOONSHOT_API_KEY
        return ""

    @classmethod
    def get_default_model(cls, provider: str = None) -> str:
        provider = (provider or cls.LLM_PROVIDER).lower()
        if cls.MODEL_NAME:
            return cls.MODEL_NAME
        if provider == "siliconflow":
            return "Qwen/Qwen3-235B-A22B-Thinking-2507"
        if provider == "doubao":
            return "doubao-seed-2-0-lite-260428"
        if provider in ("kimi", "moonshot"):
            return "kimi-k2-0905-preview"
        return ""

    @classmethod
    def validate(cls, provider: str = None) -> bool:
        provider = provider or cls.LLM_PROVIDER
        if cls.get_api_key(provider):
            return True
        key_names = {
            "siliconflow": "SILICONFLOW_API_KEY",
            "doubao": "ARK_API_KEY",
            "kimi": "MOONSHOT_API_KEY",
            "moonshot": "MOONSHOT_API_KEY",
        }
        env_var = key_names.get(provider.lower(), "API_KEY")
        print(f"ERROR: {env_var} is not set. Copy env.example to .env and fill in your API key.")
        return False
