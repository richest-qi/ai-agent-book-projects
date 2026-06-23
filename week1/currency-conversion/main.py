#!/usr/bin/env python3
"""Run currency conversion task. Config from .env only."""

import logging
import sys

from agent import CurrencyAgent
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

TASK = """Convert $1000 USD to EUR, GBP, and JPY. 
Then calculate the average value across all three converted currencies."""


def main():
    if not Config.validate():
        sys.exit(1)

    logging.info("Model: %s", Config.MODEL_NAME)
    logging.info("Task: %s", TASK.strip())

    result = CurrencyAgent(Config.ARK_API_KEY).execute_task(TASK)

    print("\n" + "=" * 50)
    print("RESULT")
    print("=" * 50)
    print("Success:", result.get("success", False))
    print("Iterations:", result.get("iterations", 0))
    print("Tool calls:", len(result["trajectory"].tool_calls))
    if result.get("final_answer"):
        print("\nAnswer:")
        print(result["final_answer"])
    if result.get("error"):
        print("\nError:", result["error"])
    print("=" * 50)

    sys.exit(0 if result.get("success") else 1)


if __name__ == "__main__":
    main()
