#!/usr/bin/env python3

# -- coding: utf-8 --
import subprocess
import time
from sglang.utils import wait_for_server, print_highlight, terminate_process

def test_image_api():

    # 调用接口的 curl 命令，发送问题“这张图片里有什么？”
    curl_command = f"""
    curl -s http://localhost:30005/v1/chat/completions \\
    -d '{{
        "model": "Qwen/Qwen2.5-VL-3B-Instruct",
        "messages": [
        {{
            "role": "user",
            "content": [
            {{
                "type": "text",
                "text": "这张图片里有什么？"
            }},
            {{
                "type": "image_url",
                "image_url": {{
                "url": "https://raw.githubusercontent.com/sgl-project/sglang/refs/heads/main/test/lang/example_image.png"
                }}
            }}
            ]
        }}
        ],
        "max_tokens": 300
    }}'
    """

    # 记录调用前时间
    start_time = time.time()

    # 发送请求并获取响应
    response = subprocess.check_output(curl_command, shell=True).decode()

    # 记录调用后时间，并计算延迟
    end_time = time.time()
    latency = end_time - start_time

    # 对响应进行简单处理，统计响应中的单词数，进而计算吞吐量（每秒单词数）
    response_words = response.split()
    response_word_count = len(response_words)
    throughput = response_word_count / latency if latency > 0 else 0

    # 打印响应及性能指标
    print("响应结果:")
    print_highlight(response)
    print("性能指标:")
    print(f"延迟: {latency:.3f} 秒")
    print(f"响应单词数: {response_word_count} 个")
    print(f"吞吐量: {throughput:.2f} 个单词/秒")

if __name__ == "__main__":
    test_image_api()
