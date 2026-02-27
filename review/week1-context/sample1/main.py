"""
Main entry point for Sample 1 only (Currency Conversion Task).
Run: python main.py
API Key: 优先使用环境变量或 --api-key；未设置时使用下方 DEFAULT_ARK_API_KEY。
"""

import os
import sys
import argparse
import logging

# Load .env before reading env vars
import config  # noqa: F401

from agent import ContextAwareAgent, ContextMode

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# 在代码中设置默认 API Key，无需 set ARK_API_KEY（可被环境变量或 --api-key 覆盖）
DEFAULT_ARK_API_KEY = "8a1a765d-9904-4a05-875a-7afc9f31c9a1"

# Sample 1: Currency Conversion Task (from week1/context get_sample_tasks()[0])
SAMPLE_1_TASK = """Convert $1000 USD to EUR, GBP, and JPY. 
Then calculate the average value across all three converted currencies."""


def main():
    parser = argparse.ArgumentParser(description="Run Sample 1 - Currency Conversion Task")
    parser.add_argument(
        "--provider",
        choices=["siliconflow", "doubao", "kimi", "moonshot"],
        default="doubao",
        help="LLM provider (default: doubao)",
    )
    parser.add_argument(
        "--model",
        type=str,
        help="Model name (optional, uses provider default)",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="API key (or set ARK_API_KEY / SILICONFLOW_API_KEY / MOONSHOT_API_KEY)",
    )
    args = parser.parse_args()

    if args.api_key:
        api_key = args.api_key
    elif args.provider == "doubao":
        api_key = os.getenv("ARK_API_KEY") or DEFAULT_ARK_API_KEY
        if not api_key:
            logger.error("Set ARK_API_KEY or use --api-key")
            sys.exit(1)
    elif args.provider == "siliconflow":
        api_key = os.getenv("SILICONFLOW_API_KEY")
        if not api_key:
            logger.error("Set SILICONFLOW_API_KEY or use --api-key")
            sys.exit(1)
    elif args.provider in ["kimi", "moonshot"]:
        api_key = os.getenv("MOONSHOT_API_KEY")
        if not api_key:
            logger.error("Set MOONSHOT_API_KEY or use --api-key")
            sys.exit(1)
    else:
        logger.error(f"Unknown provider: {args.provider}")
        sys.exit(1)

    logger.info("Running Sample 1: Currency Conversion Task")
    logger.info("Task: %s", SAMPLE_1_TASK.strip())

    agent = ContextAwareAgent(
        api_key,
        ContextMode.FULL,
        provider=args.provider,
        model=args.model,
    )
    result = agent.execute_task(SAMPLE_1_TASK)

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


if __name__ == "__main__":
    main()
