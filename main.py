#!/usr/bin/env python3

import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

conversation_history = []

def generate_response(prompt):
    """
    Generate a response to a given prompt using the GROQ server.

    This function takes a single string prompt as an argument, appends it
    to the conversation history, and then sends the full prompt to
    the GROQ server. The server's response is then appended to the
    conversation history and returned.

    :param prompt: The user's prompt
    :return: The server's response
    """
    conversation_history.append(prompt)

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
        return (actual_response + "running locally on CEO_254")
    else:
        print("Error:", response.status_code, response.text)
        return None

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)
print("Starting server...")

iface.launch(share=True)
