#!/usr/bin/env python3
"""
Currency Conversion Task — non-interactive entry point.

Run: python main.py

Executes sample 1 from week1/context without interactive prompts.
"""

import argparse
import logging
import sys

from agent import CurrencyAgent
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

CURRENCY_CONVERSION_TASK = """Convert $1000 USD to EUR, GBP, and JPY. 
Then calculate the average value across all three converted currencies."""


def main():
    parser = argparse.ArgumentParser(
        description="Run Currency Conversion Task (week1/context sample 1)"
    )
    parser.add_argument(
        "--provider",
        choices=["siliconflow", "doubao", "kimi", "moonshot"],
        default=Config.LLM_PROVIDER,
        help="LLM provider (default: from .env LLM_PROVIDER)",
    )
    parser.add_argument("--model", type=str, help="Model name (default: from .env or provider default)")
    parser.add_argument("--api-key", type=str, help="API key override")
    parser.add_argument("--quiet", action="store_true", help="Hide full request/response JSON logs")
    args = parser.parse_args()

    api_key = args.api_key or Config.get_api_key(args.provider)
    if not api_key:
        Config.validate(args.provider)
        sys.exit(1)

    model = args.model or Config.get_default_model(args.provider)

    logger.info("Provider: %s, model: %s", args.provider, model)
    logger.info("Task: %s", CURRENCY_CONVERSION_TASK.strip())

    agent = CurrencyAgent(
        api_key=api_key,
        provider=args.provider,
        model=model,
        verbose=not args.quiet,
    )
    result = agent.execute_task(CURRENCY_CONVERSION_TASK)

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
