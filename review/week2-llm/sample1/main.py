"""
本机 Ollama + get_current_time 工具：模型推断城市对应 IANA，程序只执行工具。

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


def build_question(city: str) -> str:
    name = (city or "").strip() or DEFAULT_CITY
    return f"What is the current time in {name}?"


def get_current_time(timezone: str = "UTC") -> Dict[str, Any]:
    tz_key = (timezone or "UTC").strip()
    try:
        tz = ZoneInfo(tz_key)
    except Exception:
        now = datetime.now(ZoneInfo("UTC"))
        return {
            "timezone": "UTC",
            "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "day_of_week": now.strftime("%A"),
            "utc_offset": now.strftime("%z"),
            "note": f"invalid timezone {timezone!r}, used UTC",
        }
    now = datetime.now(tz)
    return {
        "timezone": tz_key,
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "day_of_week": now.strftime("%A"),
        "utc_offset": now.strftime("%z"),
    }


TOOLS: List[Dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": (
                "Get current local time on the user's machine for an IANA timezone. "
                "Map the user's place to the correct zone, then call this tool."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string",
                        "description": "IANA id, e.g. Asia/Shanghai, Europe/Paris",
                    }
                },
                "required": ["timezone"],
            },
        },
    }
]


def _parse_args(raw: Any) -> Dict[str, Any]:
    if isinstance(raw, str):
        try:
            return json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            return {}
    return dict(raw) if isinstance(raw, dict) else {}


def _exec_tool(name: str, raw_args: Any) -> str:
    if name != "get_current_time":
        return json.dumps({"error": f"unknown tool: {name}"})
    args = _parse_args(raw_args)
    return json.dumps(get_current_time(str(args.get("timezone", "UTC"))), ensure_ascii=False)


def chat_with_tools(client: ollama.Client, model: str, user: str, *, rounds: int = 6) -> str:
    system = (
        "Answer in plain English. For local time, call get_current_time with the right IANA timezone."
    )
    messages: List[Dict[str, Any]] = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    for _ in range(rounds):
        r = client.chat(model=model, messages=messages, tools=TOOLS, options={"temperature": 0.7})
        msg = r.get("message") or {}
        text = (msg.get("content") or "").strip()
        calls: Optional[List[Dict[str, Any]]] = msg.get("tool_calls")
        if not calls:
            messages.append({"role": "assistant", "content": text or msg.get("content", "")})
            return text or "(empty)"

        messages.append({"role": "assistant", "content": text, "tool_calls": calls})
        for tc in calls:
            fn = tc.get("function") or {}
            tname, targs = fn.get("name"), fn.get("arguments")
            if tname:
                messages.append({"role": "tool", "content": _exec_tool(tname, targs)})

    r = client.chat(model=model, messages=messages, tools=TOOLS, options={"temperature": 0.7})
    out = (r.get("message") or {}).get("content", "").strip()
    messages.append({"role": "assistant", "content": out})
    return out or "(empty)"


def main() -> None:
    p = argparse.ArgumentParser(description="Ollama + get_current_time")
    p.add_argument("--model", default="qwen3:0.6b")
    p.add_argument("--host", default="http://127.0.0.1:11434")
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

    q = build_question(city)
    client = ollama.Client(host=args.host)
    print(f"城市: {city}\n问题: {q}\n模型: {args.model}\n")
    print(chat_with_tools(client, args.model, q))


if __name__ == "__main__":
    main()
