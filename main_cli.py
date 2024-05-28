import json
import requests

conversation_history = []
url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

def generate_response():
    user_prompt = input("Enter your prompt: ")
    conversation_history.append(user_prompt)
    full_prompt = "\n".join(conversation_history)

    data = {
        "model": "llama3",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        print(actual_response)
    else:
        print("Error:", response.status_code, response.text)

while True:
    generate_response()