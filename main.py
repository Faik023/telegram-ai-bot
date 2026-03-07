import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from openai_client import ask_openai

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 🔹 Хранилище персон (user_id -> persona)
user_personas = {}


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Я живой.\n"
        "Ты можешь изменить мою личность командой:\n"
        "/setpersona Текст личности"
    )


# 🔹 Команда изменения личности
@dp.message(lambda message: message.text and message.text.startswith("/setpersona"))
async def set_persona_handler(message: Message):
    user_id = message.from_user.id

    # Получаем текст после команды
    new_persona = message.text.replace("/setpersona", "").strip()

    if not new_persona:
        await message.answer(
            "Напиши личность после команды.\n"
            "Пример:\n"
            "/setpersona Ты философ 60 лет"
        )
        return

    user_personas[user_id] = new_persona

    await message.answer("Личность обновлена.")


# 🔹 Основной AI-обработчик
@dp.message()
async def chat_handler(message: Message):
    if not message.text:
        return

    print("Получено сообщение:", message.text)

    user_id = message.from_user.id

    # Берём персональную личность или дефолтную
    persona = user_personas.get(
        user_id,
        "Ты спокойный, немного ироничный мужчина 45 лет. Отвечай коротко."
    )

    try:
        reply = ask_openai(persona, message.text)
        await message.answer(reply)
    except Exception as e:
        await message.answer("Ошибка при обращении к AI.")
        print("Ошибка:", e)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())