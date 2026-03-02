import os
import sys
# Install SDK: pip install -r requirements.txt
from dotenv import load_dotenv
from volcenginesdkarkruntime import Ark

# 优先从同目录 .env 加载，再回退到系统环境变量
load_dotenv()

# 获取地址：https://console.volcengine.com/ark/region:ark+cn-beijing/apikey
api_key = os.getenv("ARK_API_KEY")
if not api_key:
    print("错误: 请设置 ARK_API_KEY")
    print("  方式一：在同目录创建 .env 文件，内容为 ARK_API_KEY=你的密钥")
    print("  方式二：设置环境变量")
    print("    Windows CMD: set ARK_API_KEY=你的密钥")
    print("    PowerShell:  $env:ARK_API_KEY=\"你的密钥\"")
    print("    Linux/macOS: export ARK_API_KEY=你的密钥")
    sys.exit(1)

client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=api_key,
)

completion = client.chat.completions.create(
    # Replace with Model ID
    model = "doubao-seed-1-6-251015",
    messages=[
        {"role": "user", "content": "讲个笑话"},
    ],
    # thinking={"type": "disabled"}, #  Manually disable deep thinking
)
print(completion.choices[0].message.content)