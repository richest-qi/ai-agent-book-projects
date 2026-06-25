#!/usr/bin/env python3
"""Run fixed web search task. Config from .env only."""

import logging
import sys

from agent import WebSearchAgent
from config import Config

logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s",
)

TASK = "2024年诺贝尔物理学奖获得者是谁？"


def main():
    if not Config.validate():
        sys.exit(1)

    logging.info("Model: %s", Config.DEFAULT_MODEL)
    logging.info("Question: %s", TASK)

    agent = WebSearchAgent(
        api_key=Config.MOONSHOT_API_KEY,
        base_url=Config.KIMI_BASE_URL,
    )
    answer = agent.search_and_answer(TASK, max_iterations=Config.MAX_SEARCH_ITERATIONS)

    print("\n" + "=" * 50)
    print("ANSWER")
    print("=" * 50)
    print(answer)
    print("=" * 50)

    failed = answer.startswith("搜索过程中出现错误") or answer.startswith("抱歉")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
