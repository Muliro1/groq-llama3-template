#!/usr/bin/env python3

import json
import requests
import os
import requests
import json
import gradio as gr

from groq import Groq

from dotenv import load_dotenv

load_dotenv()


conversation_history = []
url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
def generate_response():
    """
    Generate a response to a given prompt using the GROQ server.

    This function takes a single string prompt as an argument, appends it
    to the conversation history, and then sends the full prompt to
    the GROQ server. The server's response is then appended to the
    conversation history and returned.

    :return: The server's response
    """
    # Get the user's prompt
    user_prompt = input(">>>  (type s or S to stop):")
    if user_prompt == 's' or user_prompt == 'S':
        print("Goodbye!")
        return None
    # Add the user's prompt to the conversation history
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_prompt,}
    ],
    model="llama3-8b-8192",
)
    conversation_history.append(user_prompt)
    # Create a full prompt by joining the conversation history with newline characters
    full_prompt = "\n".join(conversation_history)

    # Create a data object to send to the server
    data = {
        "model": "llama3",
        "stream": False,
        "prompt": full_prompt,
    }
    #print(full_prompt)
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content

    # Send the request to the server

if __name__ == "__main__":
    while True:
        response = generate_response()
        if response is None:
            break

