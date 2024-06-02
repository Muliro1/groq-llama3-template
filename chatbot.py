#!/usr/bin/env python3

import numpy as np
import llama
import groq

model = llama.LLM('sentence-transformer-base')

groq_model = groq.GroqModel()

def process_input(prompt):
    # Tokenize the input
    tokens = [t for t in prompt.split() if t]

    # Encode the input as a tensor
    tensor = [model.encode([t], return_tensors='pt')[0] for t in tokens]

    # Use Groq to generate a response
    response = groq_model.generate(tensor, num_beams=4, max_length=20)

    # Decode the response
    response = ''.join(response)

    return response

def run_chatbot():
    while True:
        # Read user input
        prompt = input('> ')

        # Process the input
        response = process_input(prompt)

        # Print the response
        print(response)

if __name__ == '__main__':
    run_chatbot()
