"""
week2 / local_llm_serving 的 Sample 1 极简版：
不经过 interactive main、不启用工具调用，只把问题发给本机 Ollama 并打印回复。

前置: 本机已安装 Ollama 并已 ollama pull qwen3:0.6b（或与 --model 一致的模型）
运行: python main.py
"""
from __future__ import annotations

import argparse

import ollama

# 与 week2/local_llm_serving/main.py 中 get_sample_tasks() 的第一条一致
SAMPLE1_QUESTION = "What is the current time in Vancouver?"


def main() -> None:
    parser = argparse.ArgumentParser(description="极简本地 Ollama 调用（Sample 1 问题）")
    parser.add_argument(
        "--model",
        default="qwen3:0.6b",
        help="Ollama 模型名（默认与 local_llm_serving 一致）",
    )
    parser.add_argument(
        "--host",
        default="http://127.0.0.1:11434",
        help="Ollama 服务地址",
    )
    args = parser.parse_args()

    client = ollama.Client(host=args.host)

    print("Sample 1（与 week2/local_llm_serving 中 /sample 1 同一道题）")
    print("-" * 60)
    print(f"问题: {SAMPLE1_QUESTION}")
    print("-" * 60)
    print(f"模型: {args.model}  |  服务: {args.host}")
    print()

    response = client.chat(
        model=args.model,
        messages=[{"role": "user", "content": SAMPLE1_QUESTION}],
        # 不传 tools：纯对话，不走 get_current_time 等工具
    )
    text = (response.get("message") or {}).get("content", "").strip()
    print("回复:")
    print(text)


if __name__ == "__main__":
    main()
