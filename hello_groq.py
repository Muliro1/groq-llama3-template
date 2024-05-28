import os
import requests
import json
import gradio as gr

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

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
def generate_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.environ.get("GROQ_API_KEY")}'
    }


    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": "write a one verse poem"}],
        "stream": False,
        "prompt":prompt
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['choices'][0]['message']['content']
        print(actual_response)
    else:
        print(response.status_code)

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=3, label="Input"),
    outputs=gr.Textbox(label="Output"),
    title="GPT-3 Chatbot",
    description="This is a GPT-3 chatbot that generates responses to user prompts."
)

#print(chat_completion.choices[0].message.content)
iface.launch(share=True)