# Groq & Llama3 Chatbot Application

This project uses the Groq Cloud API and Llama3 to build a chatbot application. It includes two main scripts: `main.py` and `main_cli.py`.

## Tech Stack

- [GroqCloud](https://console.groq.com/login) for the Groq Cloud API.
- [Llama3](https://llama.meta.com/llama3/) for the language model. Download llama3 from the website. Use "ollama run llama3" on 
your terminal to run the model.
- Python v3.9.13

## main.py

`main.py` is a script that runs a chatbot in a web-based interface. It uses Django to handle HTTP requests and responses. When a user sends a message to the chatbot, the script sends the message to the Groq Cloud API, which uses Llama3 to generate a response. The response is then sent back to the user.

## main_cli.py

`main_cli.py` is a script that runs a chatbot in the command line. It uses Python's built-in `input()` function to get user input and print functions to display the chatbot's responses. Like `main.py`, it uses the Groq Cloud API and Llama3 to generate responses.

## Setup Instructions

### Update .env file

Update the `.env` file with your `GROQ_API_KEY`.

### Setup a virtual environment

Run the following command to create a new virtual environment:

```bash
python3 -m venv env
