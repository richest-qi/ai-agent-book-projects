"""
Minimal context-aware agent for the currency conversion demo.
Tools: convert_currency, calculate.
"""

import json
import logging
import math
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional

from openai import OpenAI

from config import Config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class ToolCall:
    tool_name: str
    arguments: Dict[str, Any]
    result: Optional[Any] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class AgentTrajectory:
    tool_calls: List[ToolCall] = field(default_factory=list)


class ToolRegistry:
    @staticmethod
    def convert_currency(amount: float, from_currency: str, to_currency: str) -> Dict[str, Any]:
        try:
            from_currency = (
                from_currency.replace("S$", "SGD").replace("$", "USD")
                if from_currency.startswith("S$")
                else from_currency
            )
            to_currency = (
                to_currency.replace("S$", "SGD").replace("$", "USD")
                if to_currency.startswith("S$")
                else to_currency
            )

            rates = Config.EXCHANGE_RATES
            if from_currency not in rates or to_currency not in rates:
                return {"error": f"Unsupported currency: {from_currency} or {to_currency}"}

            usd_amount = amount / rates[from_currency]
            converted_amount = usd_amount * rates[to_currency]
            return {
                "original_amount": amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "converted_amount": round(converted_amount, 2),
                "exchange_rate": round(rates[to_currency] / rates[from_currency], 4),
                "timestamp": datetime.now().isoformat(),
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def calculate(expression: str) -> Dict[str, Any]:
        try:
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            allowed_names.update({"abs": abs, "round": round, "min": min, "max": max})
            expression = expression.replace("^", "**")
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return {"expression": expression, "result": result, "type": type(result).__name__}
        except Exception as e:
            return {"error": str(e)}


class CurrencyAgent:
    def __init__(
        self,
        api_key: str,
        provider: str = "doubao",
        model: Optional[str] = None,
        verbose: bool = True,
    ):
        self.provider = provider.lower()
        self.verbose = verbose

        if self.provider == "siliconflow":
            self.client = OpenAI(api_key=api_key, base_url="https://api.siliconflow.cn/v1")
        elif self.provider == "doubao":
            self.client = OpenAI(api_key=api_key, base_url="https://ark.cn-beijing.volces.com/api/v3")
        elif self.provider in ("kimi", "moonshot"):
            self.client = OpenAI(api_key=api_key, base_url="https://api.moonshot.cn/v1")
        else:
            raise ValueError(f"Unsupported provider: {provider}")

        self.model = model or Config.get_default_model(self.provider)
        self.tools = ToolRegistry()
        self.trajectory = AgentTrajectory()
        self.conversation_history: List[Dict[str, Any]] = []
        self._init_system_prompt()

        logger.info(
            "Agent initialized: provider=%s, model=%s, verbose=%s",
            self.provider,
            self.model,
            self.verbose,
        )

    def _init_system_prompt(self):
        self.conversation_history = [
            {
                "role": "system",
                "content": (
                    "You are an intelligent assistant with access to tools.\n\n"
                    "Your task is to solve the given problems using the available tools. "
                    "Think step by step and use tools as needed.\n\n"
                    'Important: When you have gathered all necessary information and computed '
                    'the final answer, clearly state "FINAL ANSWER:" followed by your answer.'
                ),
            }
        ]

    def _get_tools_description(self) -> List[Dict[str, Any]]:
        return [
            {
                "type": "function",
                "function": {
                    "name": "convert_currency",
                    "description": "Convert an amount from one currency to another using current exchange rates",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "amount": {"type": "number", "description": "The amount to convert"},
                            "from_currency": {
                                "type": "string",
                                "description": "The source currency code (e.g., USD, EUR)",
                            },
                            "to_currency": {
                                "type": "string",
                                "description": "The target currency code (e.g., USD, EUR)",
                            },
                        },
                        "required": ["amount", "from_currency", "to_currency"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "calculate",
                    "description": "Evaluate a simple mathematical expression",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "The mathematical expression to evaluate",
                            }
                        },
                        "required": ["expression"],
                    },
                },
            },
        ]

    def _log_request_response(self, request_data: Dict[str, Any], response_data: Any, iteration: int):
        if not self.verbose:
            return
        print("\n" + "=" * 80)
        print(f"ITERATION {iteration} - REQUEST:")
        print("-" * 80)
        print(json.dumps(request_data, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print(f"ITERATION {iteration} - RESPONSE:")
        print("-" * 80)
        if hasattr(response_data, "model_dump"):
            response_dict = response_data.model_dump()
        elif hasattr(response_data, "dict"):
            response_dict = response_data.dict()
        else:
            response_dict = {"raw_response": str(response_data)}
        print(json.dumps(response_dict, indent=2, ensure_ascii=False))
        print("=" * 80 + "\n")

    def _execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        tool_map = {
            "convert_currency": self.tools.convert_currency,
            "calculate": self.tools.calculate,
        }
        if tool_name not in tool_map:
            return {"error": f"Unknown tool: {tool_name}"}
        return tool_map[tool_name](**arguments)

    def execute_task(self, task: str, max_iterations: int = None) -> Dict[str, Any]:
        max_iterations = max_iterations or Config.MAX_ITERATIONS
        self.conversation_history.append({"role": "user", "content": task})
        messages = self.conversation_history

        iteration = 0
        final_answer = None

        while iteration < max_iterations:
            iteration += 1
            logger.info("Iteration %s/%s", iteration, max_iterations)

            request_data = {
                "model": self.model,
                "messages": messages,
                "temperature": 0.3,
                "max_tokens": 8192,
                "tools": self._get_tools_description(),
                "tool_choice": "auto",
            }

            try:
                logger.info("Sending request to %s API", self.provider)
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    tools=self._get_tools_description(),
                    tool_choice="auto",
                    temperature=0.3,
                    max_tokens=8192,
                    timeout=180,
                )
                self._log_request_response(request_data, response, iteration)

                message = response.choices[0].message

                if message.content and "FINAL ANSWER:" in message.content:
                    final_answer = message.content.split("FINAL ANSWER:")[1].strip()
                    logger.info("Final answer found: %s", final_answer)
                    messages.append(message.model_dump())
                    break

                if message.tool_calls:
                    messages.append(message.model_dump())
                    for tool_call in message.tool_calls:
                        function_name = tool_call.function.name
                        function_args = json.loads(tool_call.function.arguments)
                        logger.info("Executing tool: %s with args: %s", function_name, function_args)
                        result = self._execute_tool(function_name, function_args)
                        self.trajectory.tool_calls.append(
                            ToolCall(
                                tool_name=function_name,
                                arguments=function_args,
                                result=result,
                            )
                        )
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": json.dumps(result),
                            }
                        )
                elif message.content:
                    messages.append(message.model_dump())

            except Exception as e:
                logger.error("Error during task execution: %s", e)
                return {
                    "error": str(e),
                    "trajectory": self.trajectory,
                    "iterations": iteration,
                    "success": False,
                }

        return {
            "final_answer": final_answer,
            "trajectory": self.trajectory,
            "iterations": iteration,
            "success": final_answer is not None,
        }
