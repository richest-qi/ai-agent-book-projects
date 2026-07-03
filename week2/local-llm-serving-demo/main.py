#!/usr/bin/env python3
"""Run a fixed tool-calling task via local Ollama. No interactive input."""

import logging
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

import ollama

from config import DEFAULT_TEMPERATURE, LOG_LEVEL, OLLAMA_MODEL, STREAM, TASK
from ollama_native import OllamaNativeAgent

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def init_agent() -> OllamaNativeAgent:
    """Connect to Ollama and pick an available model."""
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


def run_task(agent: OllamaNativeAgent, task: str, stream: bool = True) -> int:
    """Execute one task with the same streaming output as local_llm_serving."""
    print("\n" + "=" * 60)
    print("TASK EXECUTION")
    print("=" * 60)
    print(f"\n📋 Task: {task}")
    print("-" * 60)

    try:
        if stream:
            print("\n⏳ Processing (streaming)...\n")

            thinking_shown = False
            tools_shown = False
            response_started = False
            last_chunk_type = None

            for chunk in agent.execute_task(
                task, stream=True, temperature=DEFAULT_TEMPERATURE
            ):
                chunk_type = chunk.get("type")
                content = chunk.get("content", "")

                if chunk_type == "thinking":
                    if not thinking_shown:
                        print("🧠 Thinking: ", end="", flush=True)
                        thinking_shown = True
                    print(f"\033[90m{content}\033[0m", end="", flush=True)

                elif chunk_type == "tool_call":
                    if not tools_shown:
                        print("\n\n🔧 Tool Calls:")
                        tools_shown = True
                    print(
                        f"  → {content.get('name', 'unknown')}: "
                        f"{content.get('arguments', {})}"
                    )
                    response_started = False

                elif chunk_type == "tool_result":
                    print(f"    ✓ {content}")
                    response_started = False

                elif chunk_type == "content":
                    if not response_started:
                        if last_chunk_type in ("tool_result", "tool_call"):
                            print("\n🤖 Assistant: ", end="", flush=True)
                        elif thinking_shown or tools_shown:
                            print("\n\n🤖 Assistant: ", end="", flush=True)
                        else:
                            print("🤖 Assistant: ", end="", flush=True)
                        response_started = True
                    print(content, end="", flush=True)

                elif chunk_type == "error":
                    print(f"\n❌ Error: {content}")
                    return 1

                last_chunk_type = chunk_type

            print("\n" + "-" * 40)
            return 0

        print("\n⏳ Processing...")
        response = agent.execute_task(
            task, stream=False, temperature=DEFAULT_TEMPERATURE
        )
        print("\n✅ Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)
        return 0

    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted")
        return 130
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logger.exception("Task execution failed")
        return 1


def main() -> int:
    print("=" * 60)
    print("🚀 Local LLM Tool Calling Demo (Ollama)")
    print("=" * 60)
    print("\n⚙️  Initializing agent...")

    try:
        agent = init_agent()
    except Exception as e:
        logger.error("Failed to connect to Ollama: %s", e)
        print("\nPlease start Ollama first:")
        print("  ollama serve")
        return 1

    print("✅ Agent ready!")
    return run_task(agent, TASK, stream=STREAM)


if __name__ == "__main__":
    sys.exit(main())
