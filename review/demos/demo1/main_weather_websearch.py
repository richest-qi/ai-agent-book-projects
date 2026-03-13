"""
使用豆包内置「联网搜索 Web Search」工具查询实时信息（如天气）。
基于火山方舟 Responses API，参见：https://www.volcengine.com/docs/82379/1756990
运行: python main_weather_websearch.py
"""
import os
import sys
from dotenv import load_dotenv
from volcenginesdkarkruntime import Ark

load_dotenv()

api_key = os.getenv("ARK_API_KEY")
if not api_key:
    print("错误: 请设置 ARK_API_KEY（.env 或环境变量）")
    sys.exit(1)

client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=api_key,
)

# 文档示例使用该模型；部分能力可能依赖模型版本
MODEL = "doubao-seed-1-6-250615"

# 内置联网搜索工具，可为大模型提供实时公开网络信息（新闻、商品、天气等）
tools = [{"type": "web_search", "max_keyword": 2}]


def get_reply_text(resp):
    """从 responses.create 返回的 Response 中取出助手回复文本。"""
    if not getattr(resp, "output", None):
        return str(resp)
    for item in resp.output:
        if getattr(item, "type", None) != "message":
            continue
        content = getattr(item, "content", None) or []
        for c in content:
            if hasattr(c, "text") and c.text:
                return c.text
    return str(resp)


# 未开通 Web Search 时方舟会返回 404 ToolNotOpen
WEB_SEARCH_ACTIVATE_URL = "https://console.volcengine.com/common-buy/CC_content_plugin"

if __name__ == "__main__":
    user_query = "北京今天的具体天气情况如何？适合穿什么衣服？"
    print("用户:", user_query)
    print("-" * 50)

    try:
        response = client.responses.create(
            model=MODEL,
            input=[{"role": "user", "content": user_query}],
            tools=tools,
        )
        reply = get_reply_text(response)
        print("助手:", reply)
    except Exception as e:
        err_msg = str(e)
        if "ToolNotOpen" in err_msg or ("404" in err_msg and "web search" in err_msg.lower()):
            print("当前账号未开通豆包内置「联网搜索 Web Search」能力。")
            print()
            print("解决方式：")
            print("  1. 在火山引擎控制台开通「内容插件」：")
            print(f"     {WEB_SEARCH_ACTIVATE_URL}")
            print("  2. 或使用 Function Calling 自定义天气接口（不依赖 Web Search）：")
            print("     在 Chat API 中注册 get_weather 等工具并自行请求天气 API。")
            sys.exit(1)
        raise
