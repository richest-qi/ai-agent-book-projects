"""GPT-5 agent via OpenRouter — multi-turn loop with trajectory recording."""

import json
import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Literal, Optional

import requests

from config import Config

logger = logging.getLogger(__name__)


@dataclass
class ToolCall:
    """One explicit tool invocation (function calling)."""

    tool_name: str
    arguments: Dict[str, Any]
    result: Optional[Any] = None


@dataclass
class IterationRecord:
    """One Chat API round-trip."""

    iteration: int
    request: Dict[str, Any]
    response: Dict[str, Any]


@dataclass
class AgentTrajectory:
    iterations: List[IterationRecord] = field(default_factory=list)
    tool_calls: List[ToolCall] = field(default_factory=list)


# Custom function tools (empty: no run_python / local code execution).
# Add handlers here when needed; keys must match TOOLS_SCHEMA function names.
TOOL_HANDLERS: Dict[str, Callable[..., Any]] = {}

TOOLS_SCHEMA: List[Dict[str, Any]] = []


class GPT5NativeAgent:
    """
    OpenRouter GPT-5 agent.

    - Web search: OpenRouter plugins.web (internal; usually no tool_calls in response)
    - Explicit tools: TOOLS_SCHEMA + TOOL_HANDLERS (if configured)
    - code_interpreter: not available on OpenRouter (see search-codegen/NOTE.md)
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://openrouter.ai/api/v1",
        model: str = "openai/gpt-5-2025-08-07",
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.trajectory = AgentTrajectory()
        self.conversation_history: List[Dict[str, Any]] = []
        self.system_prompt = self._create_system_prompt()

    def _create_system_prompt(self) -> str:
        return """You are an advanced AI assistant powered by GPT-5 with native tool capabilities.

You have access to two powerful native tools:

1. **web_search**: Use this to search the internet for real-time information, current events, 
   documentation, or any information not in your training data.
   
2. **code_interpreter**: Use this to execute Python code, perform calculations, data analysis,
   generate visualizations, or solve computational problems.

Guidelines:
- Analyze the user's request carefully to determine which tools to use
- You can use multiple tools in sequence or combination to provide comprehensive answers
- When using code_interpreter, write clear, well-commented code
- When using web_search, search for authoritative and recent sources
- Always synthesize information from tools into clear, actionable responses
- Be proactive in using tools when they would enhance your answer quality

Remember: These are native tools built into your capabilities, use them naturally as part of your reasoning process."""

    def _build_request_body(
        self,
        messages: List[Dict[str, Any]],
        use_tools: bool,
        reasoning_effort: str,
        temperature: float,
        max_tokens: int,
        tool_choice: str,
    ) -> Dict[str, Any]:
        request: Dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "reasoning": {
                "effort": reasoning_effort,
                "generate_summary": False,
            },
            "background": False,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        if use_tools:
            if TOOLS_SCHEMA:
                request["tools"] = TOOLS_SCHEMA
                request["tool_choice"] = tool_choice
            request["plugins"] = [
                {"id": "web", "max_results": Config.WEB_SEARCH_MAX_RESULTS}
            ]

        return request

    def _log_request_response(
        self, request_data: Dict[str, Any], response_data: Dict[str, Any], iteration: int
    ) -> None:
        print("\n" + "=" * 80)
        print(f"ITERATION {iteration} - REQUEST:")
        print("-" * 80)
        print(json.dumps(request_data, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print(f"ITERATION {iteration} - RESPONSE:")
        print("-" * 80)
        print(json.dumps(response_data, indent=2, ensure_ascii=False))
        print("=" * 80 + "\n")

    def _call_api(self, request_body: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            json=request_body,
            timeout=600,
        )
        if response.status_code != 200:
            raise RuntimeError(f"API error (status {response.status_code}): {response.text}")
        return response.json()

    def _execute_tool_call(self, tool_call: Dict[str, Any]) -> Any:
        name = tool_call["function"]["name"]
        args = json.loads(tool_call["function"]["arguments"])
        handler = TOOL_HANDLERS.get(name)
        if handler:
            return handler(**args)
        return {
            "error": f"No local handler for tool '{name}'. "
            "Native tools via OpenRouter plugins are not returned as tool_calls."
        }

    def execute_task(
        self,
        task: str,
        use_tools: bool = True,
        tool_choice: Literal["auto", "none", "required"] = "auto",
        temperature: float = 0.3,
        max_tokens: Optional[int] = None,
        reasoning_effort: str = "low",
    ) -> Dict[str, Any]:
        """Multi-turn agent loop; record each request/response and tool results in messages."""
        self.conversation_history = [{"role": "system", "content": self.system_prompt}]
        self.trajectory = AgentTrajectory()
        self.conversation_history.append({"role": "user", "content": task})
        messages = self.conversation_history

        iteration = 0
        final_answer: Optional[str] = None
        last_usage: Dict[str, Any] = {}
        max_tokens = max_tokens or Config.DEFAULT_MAX_TOKENS

        while iteration < Config.MAX_ITERATIONS:
            iteration += 1
            logger.info("Iteration %s/%s", iteration, Config.MAX_ITERATIONS)

            request_body = self._build_request_body(
                messages=messages,
                use_tools=use_tools,
                reasoning_effort=reasoning_effort,
                temperature=temperature,
                max_tokens=max_tokens,
                tool_choice=tool_choice if use_tools else "none",
            )

            try:
                response_data = self._call_api(request_body)
                self.trajectory.iterations.append(
                    IterationRecord(iteration=iteration, request=request_body, response=response_data)
                )
                self._log_request_response(request_body, response_data, iteration)

                last_usage = response_data.get("usage", {})
                choice = response_data["choices"][0]
                message = choice.get("message", {})
                finish_reason = choice.get("finish_reason")
                content = message.get("content") or ""
                tool_calls = message.get("tool_calls") or []

                if tool_calls:
                    messages.append(message)
                    for tool_call in tool_calls:
                        name = tool_call["function"]["name"]
                        args = json.loads(tool_call["function"]["arguments"])
                        logger.info("Tool call: %s", name)
                        result = self._execute_tool_call(tool_call)
                        self.trajectory.tool_calls.append(
                            ToolCall(tool_name=name, arguments=args, result=result)
                        )
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call["id"],
                            "content": json.dumps(result, ensure_ascii=False),
                        })
                    continue

                if content:
                    messages.append(message)
                    final_answer = content
                    if finish_reason in ("stop", "end_turn", None):
                        break
                    continue

                if finish_reason == "length":
                    return {
                        "success": False,
                        "error": "Response truncated (max_tokens). Increase DEFAULT_MAX_TOKENS.",
                        "final_answer": None,
                        "trajectory": self.trajectory,
                        "iterations": iteration,
                        "messages": messages,
                        "usage": last_usage,
                    }

                break

            except Exception as e:
                logger.error("Error during task execution: %s", e)
                return {
                    "success": False,
                    "error": str(e),
                    "final_answer": None,
                    "trajectory": self.trajectory,
                    "iterations": iteration,
                    "messages": messages,
                    "usage": last_usage,
                }

        return {
            "success": final_answer is not None,
            "final_answer": final_answer,
            "trajectory": self.trajectory,
            "iterations": iteration,
            "messages": messages,
            "usage": last_usage,
        }

    def process_request(self, user_request: str, **kwargs) -> Dict[str, Any]:
        result = self.execute_task(user_request, **kwargs)
        return {
            "success": result.get("success", False),
            "response": result.get("final_answer") or result.get("error"),
            "tool_calls": result["trajectory"].tool_calls,
            "usage": result.get("usage", {}),
            "trajectory": result.get("trajectory"),
            "iterations": result.get("iterations", 0),
            "messages": result.get("messages", []),
        }
