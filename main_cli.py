#!/usr/bin/env python3

import json
import requests

conversation_history = []
url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

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
    conversation_history.append(user_prompt)
    # Create a full prompt by joining the conversation history with newline characters
    full_prompt = "\n".join(conversation_history)

    # Create a data object to send to the server
    data = {
        "model": "llama3",
        "stream": False,
        "prompt": full_prompt,
    }

    # Send the request to the server
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response status code
    if response.status_code == 200:
        # Parse the response text
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        # Add the server's response to the conversation history
        conversation_history.append(actual_response)
        print(actual_response)
        return actual_response
    else:
        # Print an error if the response status code is not 200
        print("Error:", response.status_code, response.text)
        return "Error"
if __name__ == "__main__":
    while True:
        response = generate_response()
        if response is None:
            break

