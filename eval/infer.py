import subprocess
from sglang.utils import wait_for_server, print_highlight, terminate_process
curl_command = f"""
curl -s http://127.0.0.1:30005/v1/chat/completions \\
  -d '{{
    "model": "Qwen/Qwen2.5-VL-3B-Instruct",
    "messages": [
      {{
        "role": "user",
        "content": [
          {{
            "type": "text",
            "text": "What’s in this image?"
          }},
          {{
            "type": "image_url",
            "image_url": {{
              "url": "https://github.com/sgl-project/sglang/blob/main/test/lang/example_image.png?raw=true"
            }}
          }}
        ]
      }}
    ],
    "max_tokens": 300
  }}'
"""

response = subprocess.check_output(curl_command, shell=True).decode()
print_highlight(response)

