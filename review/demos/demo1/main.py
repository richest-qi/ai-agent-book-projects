import os
import sys
# Install SDK: pip install -r requirements.txt
from volcenginesdkarkruntime import Ark

# 从环境变量读取 API Key，避免硬编码（运行前设置 ARK_API_KEY）
# 获取地址：https://console.volcengine.com/ark/region:ark+cn-beijing/apikey
api_key = os.getenv("ARK_API_KEY")
if not api_key:
    print("错误: 请设置环境变量 ARK_API_KEY")
    print("  Windows CMD: set ARK_API_KEY=你的密钥")
    print("  PowerShell:  $env:ARK_API_KEY=\"你的密钥\"")
    print("  Linux/macOS: export ARK_API_KEY=你的密钥")
    sys.exit(1)

client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=api_key,
)

completion = client.chat.completions.create(
    # Replace with Model ID
    model = "doubao-seed-1-6-251015",
    messages=[
        {"role": "user", "content": "你是谁?"},
    ],
    # thinking={"type": "disabled"}, #  Manually disable deep thinking
)
print(completion.choices[0].message.content)