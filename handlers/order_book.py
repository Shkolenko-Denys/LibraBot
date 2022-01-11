from aiogram import types

from db.LibraLibrary import libra_library
from dispatcher import dp, bot
import keyboards

genres = ('ddf', 'sdsf', 'dfdf', 'qwqwq')


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
    top_books = libra_library.get_top5_books()
    result = "🏆 Top 5:\n"
    for book in top_books:
        result += f"📕 {book[1]} ({book[2]}, {book[3]}, {book[4]}) /book{book[0]}\n"
    await message.answer(result,
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(lambda message: message.text == "Книги за жанром 👀")
async def by_genre(message):
    await message.answer("👇 Обирайте жанр 👇",
                         reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(lambda message: message.text in genres)
async def genre_books(message):
    await message.answer("Тут будуть якісь книги",
                         reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(lambda message: message.text.startswith("/book"))
async def view_book(message):
    book = libra_library.get_book(int(message.text[5:]))
    description = f"ISBN: {book[1]}\n" \
                  f"Title: {book[2]}\n" \
                  f"Summary: {book[10]}\n"
    await bot.send_photo(message.from_user.id, book[7],
                         caption=description,
                         reply_markup=keyboards.OrderBook.keyboard)


@dp.callback_query_handler(text="order_book")
async def order_book(call: types.CallbackQuery):
    await call.message.answer("Успішно!")


@dp.callback_query_handler(text="review_book")
async def order_book(call: types.CallbackQuery):
    await call.message.answer("Успішно теж!")