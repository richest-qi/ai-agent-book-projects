"""
使用 Function Calling 自定义 get_weather 工具，在 Chat API 中查询天气。
不依赖豆包内置 Web Search，无需开通内容插件。
运行: python main_weather_function_calling.py
"""
import json
import os
import sys
from dotenv import load_dotenv
from volcenginesdkarkruntime import Ark
import requests

load_dotenv()

api_key = os.getenv("ARK_API_KEY")
if not api_key:
    print("错误: 请设置 ARK_API_KEY（.env 或环境变量）")
    sys.exit(1)

client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=api_key,
)

MODEL = "doubao-seed-1-6-251015"

# 城市名 -> (纬度, 经度)，用于 Open-Meteo 免费 API（无需 key）
CITY_COORDS = {
    "北京": (39.9042, 116.4074),
    "上海": (31.2304, 121.4737),
    "广州": (23.1291, 113.2644),
    "深圳": (22.5431, 114.0579),
    "杭州": (30.2741, 120.1551),
    "成都": (30.5728, 104.0668),
    "西安": (34.3416, 108.9398),
    "南京": (32.0603, 118.7969),
    "武汉": (30.5928, 114.3055),
    "重庆": (29.4316, 106.9123),
}

# WMO 天气代码 -> 简短描述（常见）
WEATHER_DESC = {
    0: "晴",
    1: "大部晴",
    2: "少云",
    3: "多云",
    45: "雾",
    48: "雾",
    51: "毛毛雨",
    53: "毛毛雨",
    55: "毛毛雨",
    61: "小雨",
    63: "中雨",
    65: "大雨",
    71: "小雪",
    73: "中雪",
    75: "大雪",
    80: "阵雨",
    81: "阵雨",
    82: "强阵雨",
    95: "雷暴",
    96: "雷暴伴小冰雹",
    99: "雷暴伴大冰雹",
}


def get_weather(city: str) -> str:
    """
    查询指定城市当前天气（使用 Open-Meteo 免费 API，无需 key）。
    """
    city = (city or "").strip() or "北京"
    if city not in CITY_COORDS:
        return json.dumps({
            "error": f"暂不支持城市「{city}」。支持: " + "、".join(CITY_COORDS.keys()),
            "city": city,
        }, ensure_ascii=False)

    lat, lon = CITY_COORDS[city]
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
        "&timezone=Asia/Shanghai"
    )
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        return json.dumps({"error": f"请求天气接口失败: {e}", "city": city}, ensure_ascii=False)

    cur = data.get("current") or {}
    code = cur.get("weather_code", 0)
    desc = WEATHER_DESC.get(code, f"天气代码{code}")
    return json.dumps({
        "city": city,
        "temperature_2m": cur.get("temperature_2m"),
        "relative_humidity_2m": cur.get("relative_humidity_2m"),
        "weather_code": code,
        "weather_desc": desc,
        "wind_speed_10m": cur.get("wind_speed_10m"),
        "time": cur.get("time"),
    }, ensure_ascii=False)


# Chat API 使用的工具定义（OpenAI 兼容格式）
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市当前的天气情况，包括温度、湿度、天气现象、风速等。用于回答用户关于某地天气、穿衣建议等问题。",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如：北京、上海、广州、深圳、杭州、成都、西安、南京、武汉、重庆",
                    },
                },
                "required": ["city"],
            },
        },
    },
]


def assistant_message_to_dict(msg):
    """将 SDK 返回的 assistant message 转为可再次请求的 dict（含 tool_calls）。"""
    if hasattr(msg, "model_dump"):
        d = msg.model_dump()
    elif hasattr(msg, "dict"):
        d = msg.dict()
    else:
        d = dict(msg)
    # 部分 SDK 返回的 tool_calls 是对象列表，需转为 dict
    if "tool_calls" in d and d["tool_calls"]:
        out = []
        for tc in d["tool_calls"]:
            if hasattr(tc, "model_dump"):
                out.append(tc.model_dump())
            elif hasattr(tc, "dict"):
                out.append(tc.dict())
            elif isinstance(tc, dict):
                out.append(tc)
            else:
                out.append({"id": getattr(tc, "id", ""), "type": "function", "function": {"name": getattr(tc.function, "name", ""), "arguments": getattr(tc.function, "arguments", "{}")}})
        d["tool_calls"] = out
    return d


def run_weather_chat(user_query: str) -> None:
    messages = [{"role": "user", "content": user_query}]
    max_rounds = 10

    for _ in range(max_rounds):
        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )
        choice = resp.choices[0]
        msg = choice.message
        finish_reason = getattr(choice, "finish_reason", None) or "stop"

        if finish_reason == "stop" and not (getattr(msg, "tool_calls", None) or []):
            text = getattr(msg, "content", None) or ""
            if text:
                print("助手:", text.strip())
            return

        if getattr(msg, "tool_calls", None):
            assistant_msg = assistant_message_to_dict(msg)
            messages.append(assistant_msg)
            for tc in msg.tool_calls:
                name = tc.function.name
                try:
                    args = json.loads(tc.function.arguments)
                except Exception:
                    args = {}
                result = get_weather(args.get("city", "北京"))
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result,
                })
            continue

        # 无 tool_calls 且有 content
        text = getattr(msg, "content", None) or ""
        if text:
            print("助手:", text.strip())
            return

    print("助手: 达到最大轮数，未得到最终回复。")


if __name__ == "__main__":
    user_query = "北京今天的具体天气情况如何？适合穿什么衣服？"
    print("用户:", user_query)
    print("-" * 50)
    run_weather_chat(user_query)
