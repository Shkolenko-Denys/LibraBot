from dispatcher import dp
import keyboards
import genres


@dp.message_handler(lambda message: message.text == "Замовити підручник 📚")
async def order_book(message):
    await message.answer("👇 Обирайте вид 👇",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "⬅ Назад до видів")
async def back(message):
    await message.answer("👇 Добре, обирайте вид 👇",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Випадкова книга 🎲")
async def random_book(message):
    await message.answer("Тут буде випадкова книга",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Найпопулярніші книги 🏆")
async def top_books(message):
    await message.answer("Тут будуть популярні книги",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Книги за жанром 👀")
async def by_genre(message):
    await message.answer("👇 Обирайте жанр 👇",
                         reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(lambda message: message.text in genres.GENRES)
async def genre_books(message):
    await message.answer("Тут будуть якісь книги",
                         reply_markup=keyboards.GenresKeyboard.keyboard)
