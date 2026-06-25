"""Kimi Web Search Agent — uses Moonshot built-in $web_search tool."""

import json
import logging
from typing import Any, Dict, List

from openai import OpenAI
from openai.types.chat.chat_completion import Choice

from config import Config

logger = logging.getLogger(__name__)


def search_impl(arguments: Dict[str, Any]) -> Any:
    """Return arguments as-is; Kimi executes $web_search on the server side."""
    return arguments


class WebSearchAgent:
    """Web Search Agent using Kimi API built-in $web_search."""

    def __init__(self, api_key: str, base_url: str = "https://api.moonshot.cn/v1"):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = Config.DEFAULT_MODEL
        self.conversation_history: List[Dict[str, Any]] = []
        self.temperature = 1.0  # kimi-k2.5 only supports temperature=1

    def _get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "type": "builtin_function",
                "function": {"name": "$web_search"},
            }
        ]

    def _get_system_prompt(self) -> str:
        return """你是 Kimi，一个智能搜索助手。

请按照以下步骤处理：
1. 分析用户问题，识别关键信息需求
2. 使用 $web_search 工具搜索相关信息
3. 如果需要更多信息，可以多次调用搜索工具
4. 综合所有信息，生成准确、全面的答案

注意：
- 搜索时使用精准的关键词
- 优先获取最新、最权威的信息
- 答案要结构清晰，有理有据
"""

    def _assistant_message_to_dict(self, message) -> Dict[str, Any]:
        """Convert SDK assistant message to dict, preserving builtin_function type."""
        msg: Dict[str, Any] = {"role": "assistant", "content": message.content}
        if message.tool_calls:
            msg["tool_calls"] = [
                {
                    "id": tool_call.id,
                    "type": tool_call.type,
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
                for tool_call in message.tool_calls
            ]
        return msg

    def _chat(self, messages: List[Dict[str, Any]]) -> Choice:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            tools=self._get_tools(),
        )
        return completion.choices[0]

    def _ensure_system_prompt(self) -> None:
        if not self.conversation_history:
            self.conversation_history.append(
                {"role": "system", "content": self._get_system_prompt()}
            )

    def _run_until_answer(self, max_iterations: int) -> str:
        logger.info("开始调用 Kimi 搜索工具...")

        try:
            finish_reason = None
            iteration = 0

            while (finish_reason is None or finish_reason == "tool_calls") and iteration < max_iterations:
                iteration += 1
                logger.info("迭代 %s/%s", iteration, max_iterations)

                choice = self._chat(self.conversation_history)
                finish_reason = choice.finish_reason

                if finish_reason == "tool_calls":
                    logger.info("模型请求调用 %s 个工具", len(choice.message.tool_calls))
                    self.conversation_history.append(self._assistant_message_to_dict(choice.message))

                    for tool_call in choice.message.tool_calls:
                        tool_call_name = tool_call.function.name
                        tool_call_arguments = json.loads(tool_call.function.arguments)
                        logger.info("执行工具: %s, 参数: %s", tool_call_name, tool_call_arguments)

                        if tool_call_name == "$web_search":
                            tool_result = search_impl(tool_call_arguments)
                        else:
                            tool_result = f"Error: unable to find tool by name '{tool_call_name}'"

                        self.conversation_history.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": tool_call_name,
                            "content": json.dumps(tool_result, ensure_ascii=False),
                        })
                elif choice.message.content:
                    answer = choice.message.content
                    logger.info("成功生成答案")
                    self.conversation_history.append({"role": "assistant", "content": answer})
                    return answer

            if iteration >= max_iterations:
                logger.warning("达到最大迭代次数 %s", max_iterations)
                return "抱歉，搜索过程超过了最大迭代次数，请稍后重试。"

            return "抱歉，我无法获取足够的信息来回答您的问题。"

        except Exception as e:
            logger.error("搜索过程中出现错误: %s", e)
            return f"搜索过程中出现错误: {str(e)}"

    def chat(self, user_message: str, max_iterations: int | None = None) -> str:
        """Append a user turn and run the agent loop (multi-turn)."""
        if max_iterations is None:
            max_iterations = Config.MAX_SEARCH_ITERATIONS

        self._ensure_system_prompt()
        self.conversation_history.append({"role": "user", "content": user_message})
        return self._run_until_answer(max_iterations)

    def reset(self) -> None:
        """Clear conversation history for a new session."""
        self.conversation_history = []
