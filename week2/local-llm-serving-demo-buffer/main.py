#!/usr/bin/env python3
"""Mode B: Ollama API stream=True, buffer tokens, print answer once."""

import logging
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

import ollama

from config import DEFAULT_TEMPERATURE, LOG_LEVEL, OLLAMA_MODEL, TASK
from ollama_native import OllamaNativeAgent

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def init_agent() -> OllamaNativeAgent:
    client = ollama.Client()
    models_response = client.list()
    available_models = []
    if hasattr(models_response, "models"):
        available_models = [m.model for m in models_response.models]

    if not available_models:
        logger.error("No Ollama models installed. Run: ollama pull qwen3:0.6b")
        sys.exit(1)

    model = OLLAMA_MODEL
    if model not in available_models:
        logger.warning("Model %s not found, using %s", model, available_models[0])
        model = available_models[0]

    logger.info("Using Ollama model: %s", model)
    return OllamaNativeAgent(model=model)


def main() -> int:
    print("=" * 60)
    print("Local LLM Demo — Mode B (stream buffer)")
    print("API: stream=True  |  UI: print once after buffer")
    print("=" * 60)
    print("\n⚙️  Initializing agent...")

    try:
        agent = init_agent()
    except Exception as e:
        logger.error("Failed to connect to Ollama: %s", e)
        print("\nPlease start Ollama first: ollama serve")
        return 1

    print("✅ Agent ready!")
    print("\n" + "=" * 60)
    print("TASK EXECUTION")
    print("=" * 60)
    print(f"\n📋 Task: {TASK}")
    print("-" * 60)
    print("\n⏳ Processing (buffering API stream, no per-token print)...\n")

    try:
        result = agent.execute_task(TASK, temperature=DEFAULT_TEMPERATURE)
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted")
        return 130
    except Exception as e:
        logger.exception("Task failed")
        print(f"\n❌ Error: {e}")
        return 1

    print("\n🤖 Assistant:")
    print("-" * 40)
    print(result["answer"])
    print("-" * 40)
    print(f"\nIterations: {result.get('iterations', '?')}")

    return 0 if result.get("success") else 1


if __name__ == "__main__":
    sys.exit(main())
