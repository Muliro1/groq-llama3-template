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

conversation_history = []
def generate_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.environ.get("GROQ_API_KEY")}'
    }
    conversation_history.append(prompt)
    full_prompt = "\n".join(conversation_history)


    data = {
        "model": "llama3-8b-8192",
        "stream": False,
        "messages": conversation_history
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['choices'][0]['message']['content']
        conversation_history.append(actual_response)
        return actual_response
    else:
        print(response.text)

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=3, label="Input"),
    outputs="text",
    title="GPT-3 Chatbot",
    description="This is a GPT-3 chatbot that generates responses to user prompts."
)

#print(chat_completion.choices[0].message.content)
iface.launch(share=True)