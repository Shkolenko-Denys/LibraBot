from dispatcher import dp, bot
import keyboards
import genres


@dp.message_handler(commands=["start"])
async def send_welcome(message,
                       message_text="Hey ✌\nUse the keyboard below "
                                    "to invoke commands.\n"):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text=message_text,
                           reply_markup=keyboards.StartKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == f"⬅ Back")
async def back_to_start_keyboard(message):
    await send_welcome(message, "👇 Ok, choose what to do 👇")


@dp.message_handler(lambda message: message.text == "Login")
async def login(message):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text="Login func",
                           parse_mode="markdown")


@dp.message_handler(lambda message: message.text == "Register")
async def register(message):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text="Register func",
                           parse_mode="markdown")


@dp.message_handler(lambda message: message.text == "View your library card")
async def view_card(message):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text="View your library card func",
                           parse_mode="markdown")


@dp.message_handler(lambda message: message.text == "Order a book")
async def order_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="👇 Choose mode 👇",
        reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "⬅ Back to modes")
async def order_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="👇 Ok, choose mode 👇",
        reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Random book")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="Random book",
        reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Top books")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="Top books",
        reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Books by genre")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text="👇 Choose genre 👇",
                           reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(lambda message: message.text in genres.GENRES)
async def register(message):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text="Some books",
                           reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Play games")
async def register(message):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text="Game",
                           reply_markup=keyboards.StartKeyboard.keyboard)
