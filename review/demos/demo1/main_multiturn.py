"""
多轮对话示例：方舟 SDK 的 responses.create 自动管理上下文，
通过 previous_response_id 持续追踪和记忆之前的对话内容。
运行: python main_multiturn.py
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

MODEL = "doubao-seed-1-6-251015"


def get_reply_text(resp):
    """从方舟 responses.create 返回的 Response 中取出助手回复文本。
    结构：resp.output 为列表，含 reasoning 项和 type='message' 的 ResponseOutputMessage，
    其 content 为 [ResponseOutputText(text='...')]。
    """
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


# ---------- 第 1 轮 ----------
user_1 = "Hi，帮我讲个笑话。"
print("\n" + "=" * 50)
print("第 1 轮")
print("=" * 50)
print("用户:", user_1)
print("-" * 50)

response = client.responses.create(model=MODEL, input=user_1)
reply_1 = get_reply_text(response)
print("助手:", reply_1)

# ---------- 第 2 轮（带上轮上下文） ----------
user_2 = "这个笑话的笑点在哪？"
print("\n" + "=" * 50)
print("第 2 轮")
print("=" * 50)
print("用户:", user_2)
print("-" * 50)

second_response = client.responses.create(
    model=MODEL,
    previous_response_id=response.id,
    input=[{"role": "user", "content": user_2}],
)
reply_2 = get_reply_text(second_response)
print("助手:", reply_2)

print("\n" + "=" * 50)
print("多轮对话结束")
print("=" * 50)
