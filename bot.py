from aiogram import Bot, Dispatcher, types, executor
from func import transliterate
import os

API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.get_mention(as_html=True)}"
                         f" lotin-krill tarjimon botiga xush kelibsiz. Botdan foydalanish uchun biror matn yuboring")

@dp.message_handler(regexp=r'[a-zA-Z]')
async def latin(message: types.Message):
    await message.answer(transliterate(message.text, "cyrillic"))

@dp.message_handler(regexp=r'[а-яА-Я]')
async def krill(message: types.Message):
    await message.answer(transliterate(message.text, "latin"))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)