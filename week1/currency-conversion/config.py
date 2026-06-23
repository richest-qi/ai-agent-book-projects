"""Configuration for the currency conversion demo."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")


class Config:
    ARK_API_KEY: str = os.getenv("ARK_API_KEY", "")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "doubao-seed-2-0-lite-260428")
    MAX_ITERATIONS: int = int(os.getenv("MAX_ITERATIONS", "10"))

    EXCHANGE_RATES = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 149.50,
    }

    @classmethod
    def validate(cls) -> bool:
        if cls.ARK_API_KEY:
            return True
        print("ERROR: ARK_API_KEY is not set. Copy env.example to .env and fill in your API key.")
        return False
