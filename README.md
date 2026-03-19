![Python](https://img.shields.io/badge/python-3.10-blue)
![Telegram Bot](https://img.shields.io/badge/telegram-bot-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)

# Telegram AI Persona Bot#

AI-powered Telegram bot built with Python and OpenAI API.

## Demo

Example conversation with the bot:

User:
/ask What is Python?

Bot:
Python is a popular programming language used for automation, web development, AI, and more.

User:
/ask Explain artificial intelligence in simple words

Bot:
Artificial Intelligence (AI) is when computers are designed to think and learn in ways similar to humans.
## Features

- Telegram bot using aiogram
- AI responses via OpenAI API
- Custom persona prompt
- Runs 24/7 on VPS (Ubuntu)
- Automatic restart via systemd

## Tech Stack

- Python
- aiogram
- OpenAI API
- python-dotenv
- Ubuntu VPS

## Quick Start

Clone repository

git clone https://github.com/Faik023/telegram-ai-bot.git

Go to project folder

cd telegram-ai-bot

Install dependencies

pip install -r requirements.txt

## Setup

1. Install dependencies

pip install -r requirements.txt

2. Create .env file

BOT_TOKEN=your_bot_token  
OPENAI_API_KEY=your_openai_api_key

3. Run bot

python main.py
