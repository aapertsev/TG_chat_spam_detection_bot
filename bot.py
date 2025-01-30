import logging
import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

# 🔹 Укажите токен вашего бота
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# 🔹 URL API для проверки спама
SPAM_API_URL = "http://localhost:5000/predict"

# 🔹 Настройка логирования
logging.basicConfig(level=logging.INFO)

# 🔹 Инициализация бота и диспетчера
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# ✅ Обработчик команды /start
@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("👋 Привет! Я антиспам-бот. Отправьте мне сообщение, и я проверю его.")

# ✅ Обработчик всех входящих сообщений
@dp.message()
async def check_message(message: Message):
    text = message.text

    if not text:
        return  # Игнорируем сообщения без текста (например, стикеры)

    try:
        # 🔹 Отправляем запрос в API
        response = requests.post(SPAM_API_URL, json={"text": text})

        if response.status_code == 200:
            result = response.json()
            if result["spam"]:  # Если сообщение — спам
                await message.delete()
                await message.answer(f"⚠️ Сообщение удалено (спам, уверенность {result['confidence']})")
        else:
            await message.answer("⚠️ Ошибка анализа спама.")

    except Exception as e:
        logging.error(f"Ошибка при обращении к API: {e}")
        await message.answer("⚠️ Внутренняя ошибка сервера.")

# ✅ Функция запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())  # 🔥 Новый способ запуска бота в aiogram 3.x
