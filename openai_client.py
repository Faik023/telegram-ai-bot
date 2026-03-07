import os
from dotenv import load_dotenv
from openai import OpenAI

# Загружаем .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY не найден в .env файле")

# Создаём клиента
client = OpenAI(api_key=OPENAI_API_KEY)


def ask_openai(persona: str, user_message: str) -> str:
    print("Отправляем в OpenAI:")
    print("Persona:", persona)
    print("User message:", user_message)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content