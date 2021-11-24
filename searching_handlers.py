from dispatcher import dp, bot
import keyboards


@dp.message_handler(lambda message:
                    message.text == "Search books with Google Books")
async def register(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="👇 Choose mode 👇",
        reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Search by title")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="Search by title func",
        reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Search by author")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="Search by author func",
        reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(lambda message:
                    message.text == "Search by title and author")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="Search by title and author func",
        reply_markup=keyboards.GoogleBooksKeyboard.keyboard)
