#!/usr/bin/env python3
"""Minimal generator/yield demo — same example as README.md."""


def demo():
    print("  [agent] 开始")
    yield {"type": "tool_call", "name": "get_time"}
    print("  [agent] 执行工具中...")
    yield {"type": "tool_result", "data": "19:32"}
    print("  [agent] 结束")


if __name__ == "__main__":
    print("[main] 准备循环\n")
    for chunk in demo():
        print(f"[main] 收到: {chunk}")
    print("\n[main] 全部结束")
