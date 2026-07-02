#!/usr/bin/env python3
"""Run fixed ASEAN capitals distance task. Config from .env only."""

import logging
import sys

from agent import GPT5NativeAgent
from config import Config

logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s",
)

TASK = "东盟 10 国首都之间，距离最近的两个首都是？给出你的详细分析推理过程。"


def main():
    if not Config.validate():
        sys.exit(1)

    logging.info("Model: %s", Config.MODEL_NAME)
    logging.info("Reasoning effort: %s", Config.REASONING_EFFORT)
    logging.info("Task: %s", TASK)

    agent = GPT5NativeAgent(
        api_key=Config.OPENROUTER_API_KEY,
        base_url=Config.OPENROUTER_BASE_URL,
        model=Config.MODEL_NAME,
    )

    result = agent.process_request(
        TASK,
        use_tools=True,
        temperature=Config.DEFAULT_TEMPERATURE,
        max_tokens=Config.DEFAULT_MAX_TOKENS,
        reasoning_effort=Config.REASONING_EFFORT,
    )

    print("\n" + "=" * 50)
    print("RESULT")
    print("=" * 50)

    if result["success"]:
        print(result["response"])
        usage = result.get("usage") or {}
        total = usage.get("total_tokens")
        if total:
            print("\n" + "-" * 50)
            print(f"Tokens used: {total}")
    else:
        print("Error:", result.get("error", "Unknown error"))

    print("=" * 50)
    sys.exit(0 if result.get("success") else 1)


if __name__ == "__main__":
    main()
