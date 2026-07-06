"""
Mode C: Ollama chat(stream=False) — full response per request;
main.py prints the full answer once (like web-search-demo).
"""

import json
import logging
import re
from typing import Any, Dict, List

import ollama
from config import DEBUG_RESPONSE
from tools import ToolRegistry

logger = logging.getLogger(__name__)


def _get_field(obj: Any, key: str, default: Any = None) -> Any:
    """Read a field from dict or Ollama/Pydantic response object."""
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _serialize_for_debug(obj: Any) -> Any:
    """Convert Ollama/Pydantic response to JSON-serializable dict."""
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, (list, tuple)):
        return [_serialize_for_debug(item) for item in obj]
    return obj


def _debug_print_blocking_response(iteration: int, response: Any) -> None:
    """Print raw blocking API response as returned by Ollama (DEBUG_RESPONSE=1)."""
    print(f"\n[response] iteration={iteration}")
    print(json.dumps(_serialize_for_debug(response), ensure_ascii=False, indent=2))
    print()


def _print_tool_execution(name: str, args: Dict[str, Any], result: str) -> None:
    print(f"  → {name}: {args}")
    print(f"    ✓ {result}")


class OllamaNativeAgent:
    """Agent: API stream=False, blocking responses."""

    def __init__(self, model: str = "qwen3:0.6b"):
        self.model = model
        self.client = ollama.Client()
        self.tool_registry = ToolRegistry()
        self.conversation_history: List[Dict[str, Any]] = []
        self.client.list()
        logger.info("Connected to Ollama with model: %s", model)

    def _convert_tools(self) -> List[Dict]:
        return self.tool_registry.get_tool_schemas()

    def _get_system_prompt(self) -> str:
        return (
            "You are an assistant with function-calling tools. "
            "Use get_current_time and get_current_temperature for real-time "
            "time and weather. Never guess."
        )

    def _parse_tool_args(self, tool_args: Any) -> Dict[str, Any]:
        if isinstance(tool_args, dict):
            return tool_args
        if isinstance(tool_args, str):
            try:
                return json.loads(tool_args)
            except json.JSONDecodeError:
                logger.error("Failed to parse tool arguments: %s", tool_args)
        return {}

    def _clean_content(self, content: str) -> str:
        return re.sub(
            r"<think>.*?</think>",
            "",
            content or "",
            flags=re.DOTALL,
        ).strip()

    def execute_task(
        self,
        task: str,
        use_tools: bool = True,
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """Run task; return final answer and tool records (no generator)."""
        self.conversation_history = [
            {"role": "system", "content": self._get_system_prompt()},
            {"role": "user", "content": task},
        ]
        tool_records: List[Dict[str, Any]] = []
        tools = self._convert_tools() if use_tools else None
        max_iterations = 10

        logger.info("Task: %s", task)
        logger.info("Mode C: Ollama API stream=False, blocking response")
        if DEBUG_RESPONSE:
            logger.info("DEBUG_RESPONSE=1: printing full response breakdown")

        for iteration in range(1, max_iterations + 1):
            logger.info("Iteration %s/%s", iteration, max_iterations)

            response = self.client.chat(
                model=self.model,
                messages=self.conversation_history,
                tools=tools,
                options={"temperature": temperature},
                stream=False,
            )

            message = _get_field(response, "message")
            tool_calls = _get_field(message, "tool_calls") or []

            if DEBUG_RESPONSE:
                _debug_print_blocking_response(iteration, response)

            if tool_calls:
                logger.info("Model requested %s tool call(s)", len(tool_calls))
                self.conversation_history.append({
                    "role": "assistant",
                    "content": _get_field(message, "content", "") or "",
                    "tool_calls": tool_calls,
                })
                print("🔧 Tool Calls:")
                for tool_call in tool_calls:
                    function = _get_field(tool_call, "function", {})
                    name = _get_field(function, "name")
                    args = self._parse_tool_args(_get_field(function, "arguments"))
                    logger.info("Executing tool: %s with args: %s", name, args)
                    result = self.tool_registry.execute_tool(name, args)
                    _print_tool_execution(name, args, result)
                    tool_records.append({
                        "name": name,
                        "arguments": args,
                        "result": result,
                    })
                    self.conversation_history.append({
                        "role": "tool",
                        "content": result,
                    })
                continue

            answer = self._clean_content(_get_field(message, "content", "") or "")
            self.conversation_history.append({
                "role": "assistant",
                "content": answer,
            })
            return {
                "success": True,
                "answer": answer,
                "tool_records": tool_records,
                "iterations": iteration,
            }

        return {
            "success": False,
            "answer": "Error: Maximum iterations reached",
            "tool_records": tool_records,
            "iterations": max_iterations,
        }
