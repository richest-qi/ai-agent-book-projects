"""GPT-5 agent via OpenRouter — web search plugin + reasoning."""

import json
import logging
from typing import Any, Dict, List, Optional

import requests

from config import Config

logger = logging.getLogger(__name__)


class GPT5NativeAgent:
    """OpenRouter GPT-5 agent with web search plugin."""

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
        return """You are an advanced AI assistant with web search and reasoning capabilities.

Guidelines:
- Use web search when you need factual or geographic data
- Use code or calculations when distances or comparisons are required
- Show your analysis and reasoning process clearly
- Cite sources when possible and synthesize a definitive answer"""

    def _build_openrouter_request(
        self,
        messages: List[Dict[str, Any]],
        use_tools: bool,
        reasoning_effort: str,
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
        }

        if use_tools:
            # OpenRouter web search plugin (see search-codegen NOTE.md)
            request["plugins"] = [
                {"id": "web", "max_results": Config.WEB_SEARCH_MAX_RESULTS}
            ]

        return request

    def process_request(
        self,
        user_request: str,
        use_tools: bool = True,
        temperature: float = 0.3,
        max_tokens: Optional[int] = None,
        reasoning_effort: str = "medium",
    ) -> Dict[str, Any]:
        if not self.conversation_history:
            self.conversation_history.append({"role": "system", "content": self.system_prompt})

        self.conversation_history.append({"role": "user", "content": user_request})

        logger.info("Processing request: %s...", user_request[:80])
        logger.info("Reasoning effort: %s", reasoning_effort)

        try:
            request_body = self._build_openrouter_request(
                messages=self.conversation_history,
                use_tools=use_tools,
                reasoning_effort=reasoning_effort,
            )
            request_body["temperature"] = temperature
            if max_tokens:
                request_body["max_tokens"] = max_tokens

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
                return {"success": False, "error": error_msg, "response": None, "usage": {}}

            response_data = response.json()

            if "usage" in response_data:
                usage = response_data["usage"]
                logger.info(
                    "Tokens - input: %s, output: %s, total: %s",
                    usage.get("prompt_tokens", usage.get("input_tokens", 0)),
                    usage.get("completion_tokens", usage.get("output_tokens", 0)),
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
                    self.conversation_history.append(
                        {"role": "assistant", "content": message_content}
                    )
                elif finish_reason == "length":
                    message_content = (
                        "响应因达到 max_tokens 上限被截断（推理阶段耗尽了配额）。"
                        "请在 .env 中增大 DEFAULT_MAX_TOKENS 后重试。"
                    )
                    logger.warning("Empty content with finish_reason=length; increase max_tokens")

            return {
                "success": bool(message_content and finish_reason != "length"),
                "response": message_content or "No response generated",
                "usage": response_data.get("usage", {}),
                "model": self.model,
                "finish_reason": finish_reason,
            }

        except Exception as e:
            logger.error("Error processing request: %s", e)
            return {"success": False, "error": str(e), "response": None, "usage": {}}
