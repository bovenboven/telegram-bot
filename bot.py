import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.enums import ParseMode
import os

API_TOKEN = os.getenv("API_TOKEN", "your_telegram_bot_token_here")
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐️ Избранное", callback_data="favorites")],
        [InlineKeyboardButton(text="🔎 Поиск рецепта", callback_data="search")],
        [InlineKeyboardButton(text="🎲 Случайный рецепт", callback_data="random")]
    ])
    await message.answer("Привет! 👋🏻 Готов к кукингу? 🥗 Давай приступим!🙏🏻", reply_markup=keyboard)

@dp.callback_query(F.data == "favorites")
async def show_favorites(callback: CallbackQuery):
    await callback.message.answer("⭐️ Здесь будут избранные рецепты!")

@dp.callback_query(F.data == "search")
async def search_recipes(callback: CallbackQuery):
    await callback.message.answer("🔎 Выберите, как вы хотите искать рецепт:")

@dp.callback_query(F.data == "random")
async def random_recipe(callback: CallbackQuery):
    await callback.message.answer("🎲 Вот случайный рецепт!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
