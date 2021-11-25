from aiogram.dispatcher.filters import Text

from dispatcher import dp
import keyboards


@dp.message_handler(Text(equals="Знайти на Google Books 🔎"))
async def search_start(message):
    await message.answer("👇 Оберіть режим 👇",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="Шукати за назвою 📔"))
async def search_topic(message):
    await message.answer("Шукаємо за назвою...",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="Шукати за автором 🙍"))
async def search_author(message):
    await message.answer("Шукаємо за автором...",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="Шукати за автором і назвою 🙍📔"))
async def search_topic_author(message):
    await message.answer("Шукаємо за автором і назвою...",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)
