"""GPT-5 agent via OpenRouter — aligned with week1/search-codegen/agent.py."""

import json
import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Literal, Optional

import requests

from config import Config

logger = logging.getLogger(__name__)


class ToolType(Enum):
    """Enum for GPT-5 native tool types."""

    WEB_SEARCH = "web_search"
    CODE_INTERPRETER = "code_interpreter"


@dataclass
class ToolResult:
    """Container for tool execution results."""

    tool_type: ToolType
    success: bool
    result: Any
    error: Optional[str] = None


class GPT5NativeAgent:
    """
    GPT-5 Agent with Native Tool Support

    Uses GPT-5's native web_search and code_interpreter capabilities through OpenRouter.
    See week1/search-codegen/NOTE.md for how OpenRouter maps these to plugins at request time.
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

    def _build_openrouter_request(
        self,
        messages: List[Dict[str, Any]],
        use_tools: bool = True,
        reasoning_effort: str = "low",
        stream: bool = False,
    ) -> Dict[str, Any]:
        request: Dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": stream,
        }

        if use_tools:
            # OpenRouter 转发到 OpenAI 时仍走 Chat Completions 接口，不接受 type: "web_search"/"code_interpreter"，
            # 会报 400（即使 provider 已是 OpenAI）。改用 OpenRouter 的 plugins 启用联网，所有 provider 均支持。
            # 见 https://openrouter.ai/docs/guides/features/plugins/web-search
            request["plugins"] = [
                {"id": "web", "max_results": Config.WEB_SEARCH_MAX_RESULTS}
            ]

        request["reasoning"] = {
            "effort": reasoning_effort,
            "generate_summary": False,
        }
        request["background"] = False

        return request

    def process_request(
        self,
        user_request: str,
        use_tools: bool = True,
        tool_choice: Literal["auto", "none", "required"] = "auto",
        temperature: float = 0.3,
        max_tokens: Optional[int] = None,
        reasoning_effort: str = "medium",
    ) -> Dict[str, Any]:
        if not self.conversation_history:
            self.conversation_history.append({
                "role": "system",
                "content": self.system_prompt,
            })

        self.conversation_history.append({
            "role": "user",
            "content": user_request,
        })

        logger.info("Processing request: %s...", user_request[:100])
        logger.info("Using OpenRouter format with reasoning effort: %s", reasoning_effort)

        try:
            request_body = self._build_openrouter_request(
                messages=self.conversation_history,
                use_tools=use_tools,
                reasoning_effort=reasoning_effort,
                stream=False,
            )

            if temperature is not None:
                request_body["temperature"] = temperature
            if max_tokens:
                request_body["max_tokens"] = max_tokens

            logger.info("Request body: %s", json.dumps(request_body, indent=2))

            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}",
                },
                json=request_body,
                timeout=600,
            )

            logger.info("Response status: %s", response.status_code)

            if response.status_code != 200:
                error_msg = f"API error (status {response.status_code}): {response.text}"
                logger.error(error_msg)
                return {
                    "success": False,
                    "error": error_msg,
                    "response": None,
                    "tool_calls": [],
                    "usage": {},
                }

            response_data = response.json()

            if "usage" in response_data:
                usage = response_data["usage"]
                logger.info(
                    "GPT-5 OpenRouter Usage - Input: %s tokens "
                    "(cached: %s), Output: %s tokens "
                    "(reasoning: %s), Total: %s",
                    usage.get("input_tokens", usage.get("prompt_tokens", 0)),
                    usage.get("input_tokens_details", {}).get("cached_tokens", 0),
                    usage.get("output_tokens", usage.get("completion_tokens", 0)),
                    usage.get("output_tokens_details", {}).get("reasoning_tokens", 0),
                    usage.get("total_tokens", 0),
                )

            message_content = None
            finish_reason = None
            if response_data.get("choices"):
                choice = response_data["choices"][0]
                finish_reason = choice.get("finish_reason")
                message = choice.get("message", {})
                message_content = message.get("content") or ""

                if message_content:
                    self.conversation_history.append({
                        "role": "assistant",
                        "content": message_content,
                    })
                elif finish_reason == "length":
                    message_content = (
                        "响应因达到 max_tokens 上限被截断（推理阶段耗尽了配额）。"
                        "请在 .env 中增大 DEFAULT_MAX_TOKENS 后重试。"
                    )
                    logger.warning("Empty content with finish_reason=length; increase max_tokens")

            success = bool(message_content and finish_reason != "length")
            return {
                "success": success,
                "response": message_content or "No response generated",
                "tool_calls": [],  # GPT-5 handles tools internally
                "usage": response_data.get("usage", {}),
                "model": self.model,
                "finish_reason": finish_reason,
            }

        except Exception as e:
            logger.error("Error processing request: %s", e)
            return {
                "success": False,
                "error": str(e),
                "response": None,
                "tool_calls": [],
                "usage": {},
            }
