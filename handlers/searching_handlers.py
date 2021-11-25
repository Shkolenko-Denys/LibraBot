from dispatcher import dp
import keyboards


@dp.message_handler(lambda message:
                    message.text == "Знайти на Google Books 🔎")
async def register(message):
    await message.answer("👇 Оберіть режим 👇",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Шукати за назвою 📔")
async def random_book(message):
    await message.answer("Search by title func",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Шукати за автором 🙍")
async def random_book(message):
    await message.answer("Search by author func",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(lambda message:
                    message.text == "Шукати за автором і назвою 🙍📔")
async def random_book(message):
    await message.answer("Search by title and author func",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)
