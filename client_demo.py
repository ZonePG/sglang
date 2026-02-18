import requests
import json

messages = [{"role": "user", "content": "What is the capital of France?"}]

response = requests.post(
    "http://localhost:30000/v1/chat/completions",
    json={
        "messages": messages,
        "sampling_params": {"temperature": 0.0, "max_new_tokens": 32},
        "stream": True,
    },
    stream=True,
)

for line in response.iter_lines(decode_unicode=True):
    if not line or not line.startswith("data: "):
        continue
    data = line[6:]
    if data.strip() == "[DONE]":
        break
    try:
        obj = json.loads(data)
    except json.JSONDecodeError:
        continue
    choice = obj["choices"][0]
    if not choice:
        continue
    delta = choice.get("delta", {})
    content = delta.get("content", "")
    if content:
        print(content, end="", flush=True)
print()
