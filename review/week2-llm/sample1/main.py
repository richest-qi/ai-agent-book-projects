"""
本机 Ollama + get_current_time 工具：模型推断 IANA，程序只执行工具。

运行: python main.py  或  python main.py --city Paris
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from typing import Any, Dict, List, Optional
from zoneinfo import ZoneInfo

import ollama

DEFAULT_CITY = "北京"

TOOLS: List[Dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": (
                "Get current local time on this machine for an IANA timezone. "
                "Map the user's place to the correct IANA id and pass it as timezone."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string",
                        "description": "IANA timezone, e.g. Asia/Shanghai, Europe/Paris.",
                    }
                },
                "required": ["timezone"],
            },
        },
    },
]


def get_current_time(timezone: str = "UTC") -> Dict[str, Any]:
    tz_key = (timezone or "UTC").strip()
    try:
        tz = ZoneInfo(tz_key)
    except Exception:
        now_utc = datetime.now(ZoneInfo("UTC"))
        return {
            "timezone": "UTC",
            "datetime": now_utc.strftime("%Y-%m-%d %H:%M:%S"),
            "day_of_week": now_utc.strftime("%A"),
            "utc_offset": now_utc.strftime("%z"),
            "note": f"invalid timezone {timezone!r}, used UTC",
        }
    now = datetime.now(tz)
    return {
        "timezone": tz_key,
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "day_of_week": now.strftime("%A"),
        "utc_offset": now.strftime("%z"),
    }


def _run_tool(name: str, raw_args: Any) -> str:
    if isinstance(raw_args, str):
        try:
            args = json.loads(raw_args) if raw_args.strip() else {}
        except json.JSONDecodeError:
            args = {}
    elif isinstance(raw_args, dict):
        args = raw_args
    else:
        args = {}
    if name != "get_current_time":
        return json.dumps({"error": f"unknown tool: {name}"})
    tz = str(args.get("timezone", "UTC"))
    return json.dumps(get_current_time(tz), ensure_ascii=False)


def chat_with_tools(
    client: ollama.Client,
    model: str,
    user_text: str,
    *,
    max_rounds: int = 6,
) -> tuple[str, List[Dict[str, Any]]]:
    messages: List[Dict[str, Any]] = [
        {
            "role": "system",
            "content": (
                "Answer in plain English. Use get_current_time with the right IANA timezone for the user's place."
            ),
        },
        {"role": "user", "content": user_text},
    ]
    for _ in range(max_rounds):
        r = client.chat(model=model, messages=messages, tools=TOOLS, options={"temperature": 0.7})
        msg = r.get("message") or {}
        content = (msg.get("content") or "").strip()
        tool_calls: Optional[List[Dict[str, Any]]] = msg.get("tool_calls")
        if not tool_calls:
            messages.append({"role": "assistant", "content": content or msg.get("content", "")})
            return content or "(empty)", messages
        messages.append({"role": "assistant", "content": content, "tool_calls": tool_calls})
        for tc in tool_calls:
            fn = (tc.get("function") or {})
            name, raw = fn.get("name"), fn.get("arguments")
            if name:
                messages.append({"role": "tool", "content": _run_tool(name, raw)})
    r = client.chat(model=model, messages=messages, tools=TOOLS, options={"temperature": 0.7})
    final = (r.get("message") or {}).get("content", "").strip()
    messages.append({"role": "assistant", "content": final})
    return final or "(empty)", messages


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="qwen3:0.6b")
    p.add_argument("--host", default="http://127.0.0.1:11434")
    p.add_argument("--verbose", action="store_true", help="打印对话与 tool JSON")
    p.add_argument("--city", default=None)
    args = p.parse_args()

    if args.city is not None:
        city = args.city.strip() or DEFAULT_CITY
    else:
        try:
            raw = input(f"城市（回车默认 {DEFAULT_CITY}）: ").strip()
        except EOFError:
            raw = ""
        city = raw or DEFAULT_CITY

    q = f"What is the current time in {city}?"
    client = ollama.Client(host=args.host)
    print(f"问题: {q}\n模型: {args.model}\n")

    answer, msgs = chat_with_tools(client, args.model, q)

    if args.verbose:
        for i, m in enumerate(msgs):
            print(f"[{i}] {m.get('role')}: {str(m)[:500]}{'...' if len(str(m)) > 500 else ''}")
        print()

    print(answer)


if __name__ == "__main__":
    main()
