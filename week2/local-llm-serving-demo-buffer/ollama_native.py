"""
Mode B: Ollama chat(stream=True) — token stream buffered in memory;
main.py prints the full answer once (no yield / no print-per-token).
"""

import json
import logging
import re
from typing import Any, Dict, List

import ollama
from config import DEBUG_CHUNKS
from tools import ToolRegistry

logger = logging.getLogger(__name__)


def _get_field(obj: Any, key: str, default: Any = None) -> Any:
    """Read a field from dict or Ollama/Pydantic response object."""
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _format_tool_call_debug(tool_call: Any, index: int) -> str:
    """One-line summary of a tool_call for debug printing."""
    tc_id = _get_field(tool_call, "id")
    function = _get_field(tool_call, "function", {})
    name = _get_field(function, "name") or _get_field(tool_call, "tool_name")
    args = _get_field(function, "arguments")
    if args is None:
        args = _get_field(tool_call, "arguments")

    if isinstance(args, dict):
        args_str = json.dumps(args, ensure_ascii=False)
    elif isinstance(args, str) and args:
        args_str = args if len(args) <= 120 else args[:120] + "..."
    elif args:
        args_str = repr(args)
    else:
        args_str = "(参数尚未完整)"

    parts = [f"[{index}]"]
    if tc_id:
        parts.append(f"id={tc_id!r}")
    parts.append(f"name={name!r}")
    parts.append(f"arguments={args_str}")
    return " ".join(parts)


def _debug_print_tool_calls(chunk_tool_calls: Any) -> None:
    calls = list(chunk_tool_calls)
    print(f"[chunk] content 空，但有 tool_calls ({len(calls)})")
    for i, tc in enumerate(calls, 1):
        print(f"         {_format_tool_call_debug(tc, i)}")


def _merge_tool_calls(accumulated: List[Any], incoming: Any) -> List[Any]:
    """Merge tool_calls across streaming chunks (Ollama may send one tool per chunk)."""
    if not incoming:
        return accumulated
    result = list(accumulated)
    for new_tc in incoming:
        new_fn = _get_field(new_tc, "function", {})
        new_name = _get_field(new_fn, "name")
        replaced = False
        for i, existing in enumerate(result):
            ex_fn = _get_field(existing, "function", {})
            if _get_field(ex_fn, "name") == new_name:
                result[i] = new_tc
                replaced = True
                break
        if not replaced:
            result.append(new_tc)
    return result


def _print_tool_execution(name: str, args: Dict[str, Any], result: str) -> None:
    print(f"  → {name}: {args}")
    print(f"    ✓ {result}")


class OllamaNativeAgent:
    """Agent: API stream=True, display buffered."""

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
        logger.info("Mode B: Ollama API stream=True, output buffered until complete")
        if DEBUG_CHUNKS:
            logger.info("DEBUG_CHUNKS=1: printing each stream chunk")

        for iteration in range(1, max_iterations + 1):
            logger.info("Iteration %s/%s", iteration, max_iterations)

            stream_response = self.client.chat(
                model=self.model,
                messages=self.conversation_history,
                tools=tools,
                options={"temperature": temperature},
                stream=True,
            )

            collected: List[str] = []
            tool_calls: List[Dict[str, Any]] = []

            for chunk in stream_response:
                message_chunk = _get_field(chunk, "message")
                piece = _get_field(message_chunk, "content", "") or ""
                chunk_tool_calls = _get_field(message_chunk, "tool_calls")
                if DEBUG_CHUNKS:
                    if piece:
                        print(f"[chunk content] {piece!r}")
                    elif chunk_tool_calls:
                        _debug_print_tool_calls(chunk_tool_calls)
                    elif _get_field(chunk, "done"):
                        print("[chunk] 结束包 done=true")
                    else:
                        thinking = _get_field(message_chunk, "thinking")
                        tool_name = _get_field(message_chunk, "tool_name")
                        if thinking:
                            print(f"[chunk] content 空，thinking 片段: {thinking!r}")
                        elif tool_name:
                            print(f"[chunk] content 空，tool_name: {tool_name!r}")
                        else:
                            print("[chunk] content 空，等待模型下一 token")
                if piece:
                    collected.append(piece)
                if chunk_tool_calls:
                    tool_calls = _merge_tool_calls(tool_calls, chunk_tool_calls)

            if tool_calls:
                logger.info("Model requested %s tool call(s)", len(tool_calls))
                self.conversation_history.append({
                    "role": "assistant",
                    "content": "".join(collected),
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

            answer = self._clean_content("".join(collected))
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
