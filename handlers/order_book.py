from dispatcher import dp, bot
import keyboards
import genres


@dp.message_handler(lambda message: message.text == "Замовити підручник 📚")
async def order_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="👇 Обирайте вид 👇",
        reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "⬅ Назад до видів")
async def order_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="👇 Добре, обирайте вид 👇",
        reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Випадкова книга 🎲")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="Random book",
        reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Найпопулярніші книги 🏆")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(
        chat_id=chat_id, text="Top books",
        reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Книги за жанром 👀")
async def random_book(message):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text="👇 Обирайте жанр 👇",
                           reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(lambda message: message.text in genres.GENRES)
async def register(message):
    chat_id = message.from_user.id

    await bot.send_message(chat_id=chat_id, text="Some books",
                           reply_markup=keyboards.GenresKeyboard.keyboard)
