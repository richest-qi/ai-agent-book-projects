"""
使用 OpenAI SDK 调用豆包（豆包提供 OpenAI 兼容接口）。
运行: python main_openai.py
依赖: pip install -r requirements.txt（含 openai、python-dotenv）
"""
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("ARK_API_KEY")
if not api_key:
    print("错误: 请设置 ARK_API_KEY（.env 或环境变量）")
    sys.exit(1)

# 使用 OpenAI 客户端，仅将 base_url 指向豆包
client = OpenAI(
    api_key=api_key,
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

completion = client.chat.completions.create(
    model="doubao-seed-1-6-251015",
    messages=[{"role": "user", "content": "你是谁?"}],
)
print(completion.choices[0].message.content)
