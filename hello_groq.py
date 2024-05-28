import os
import requests
import json

from groq import Groq

from dotenv import load_dotenv

load_dotenv()
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.environ.get("GROQ_API_KEY")}'
}


data = {
    "model": "llama3-8b-8192",
    "messages": [{"role": "user", "content": "write a one verse poem"}],
    "stream": False
}

response = requests.post(url, data=json.dumps(data), headers=headers)
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        },
        {
            "role": "user",
            "content": "What is the meaning of life?",}
    ],
    model="llama3-8b-8192",
)
if response.status_code == 200:
    response_text = response.text
    data = json.loads(response_text)
    actual_response = data['choices'][0]['message']['content']
    print(actual_response)
else:
    print(response.status_code)

#print(chat_completion.choices[0].message.content)