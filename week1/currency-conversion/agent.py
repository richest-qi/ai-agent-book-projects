"""
Currency conversion agent (Doubao / Volcengine Ark).
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

logger = logging.getLogger(__name__)


@dataclass
class ToolCall:
    tool_name: str
    arguments: Dict[str, Any]
    result: Optional[Any] = None


@dataclass
class AgentTrajectory:
    tool_calls: List[ToolCall] = field(default_factory=list)


def convert_currency(amount: float, from_currency: str, to_currency: str) -> Dict[str, Any]:
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


def calculate(expression: str) -> Dict[str, Any]:
    try:
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names.update({"abs": abs, "round": round, "min": min, "max": max})
        expression = expression.replace("^", "**")
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return {"expression": expression, "result": result, "type": type(result).__name__}
    except Exception as e:
        return {"error": str(e)}


TOOL_HANDLERS = {
    "convert_currency": convert_currency,
    "calculate": calculate,
}

TOOLS_SCHEMA = [
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

SYSTEM_PROMPT = (
    "You are an intelligent assistant with access to tools.\n\n"
    "Your task is to solve the given problems using the available tools. "
    "Think step by step and use tools as needed.\n\n"
    'Important: When you have gathered all necessary information and computed '
    'the final answer, clearly state "FINAL ANSWER:" followed by your answer.'
)


class CurrencyAgent:
    def __init__(self, api_key: str, model: Optional[str] = None):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://ark.cn-beijing.volces.com/api/v3",
        )
        self.model = model or Config.MODEL_NAME
        self.trajectory = AgentTrajectory()
        self.conversation_history: List[Dict[str, Any]] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        logger.info("Agent initialized: model=%s", self.model)

    def _log_request_response(self, request_data: Dict[str, Any], response_data: Any, iteration: int):
        print("\n" + "=" * 80)
        print(f"ITERATION {iteration} - REQUEST:")
        print("-" * 80)
        print(json.dumps(request_data, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print(f"ITERATION {iteration} - RESPONSE:")
        print("-" * 80)
        response_dict = (
            response_data.model_dump()
            if hasattr(response_data, "model_dump")
            else response_data.dict()
        )
        print(json.dumps(response_dict, indent=2, ensure_ascii=False))
        print("=" * 80 + "\n")

    def execute_task(self, task: str) -> Dict[str, Any]:
        self.conversation_history.append({"role": "user", "content": task})
        messages = self.conversation_history

        iteration = 0
        final_answer = None

        while iteration < Config.MAX_ITERATIONS:
            iteration += 1
            logger.info("Iteration %s/%s", iteration, Config.MAX_ITERATIONS)

            request_data = {
                "model": self.model,
                "messages": messages,
                "temperature": 0.3,
                "max_tokens": 8192,
                "tools": TOOLS_SCHEMA,
                "tool_choice": "auto",
            }

            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    tools=TOOLS_SCHEMA,
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
                        name = tool_call.function.name
                        args = json.loads(tool_call.function.arguments)
                        logger.info("Executing tool: %s with args: %s", name, args)
                        handler = TOOL_HANDLERS.get(name)
                        result = handler(**args) if handler else {"error": f"Unknown tool: {name}"}
                        self.trajectory.tool_calls.append(
                            ToolCall(tool_name=name, arguments=args, result=result)
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
