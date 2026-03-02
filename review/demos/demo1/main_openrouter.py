"""
使用 OpenAI SDK 通过 OpenRouter 调用任意支持的模型。
OpenRouter 统一接口：一个 API Key 可调 100+ 模型（OpenAI、Google、Anthropic 等）。
运行: python main_openrouter.py
依赖: pip install -r requirements.txt
配置: .env 中设置 OPENROUTER_API_KEY（https://openrouter.ai/keys）
"""
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("错误: 请设置 OPENROUTER_API_KEY（.env 或环境变量）")
    print("  获取: https://openrouter.ai/keys")
    sys.exit(1)

# OpenRouter 提供 OpenAI 兼容接口，仅改 base_url
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

# 模型 ID 格式为 厂商/模型名，见 https://openrouter.ai/models
completion = client.chat.completions.create(
    model="openai/gpt-4o-mini",  # 可改为 google/gemini-2.0-flash-exp:free 等
    messages=[{"role": "user", "content": "你是谁，请详细介绍下你自己?"}],
)
print(completion.choices[0].message.content)
