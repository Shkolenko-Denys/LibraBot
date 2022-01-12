from aiogram import types
from aiogram.dispatcher.filters import Text

from db.LibraLibrary import libra_library
from dispatcher import dp, bot
import keyboards

genres = ('ddf', 'sdsf', 'dfdf', 'qwqwq')


@dp.message_handler(Text(equals="Замовити підручник 📚"))
async def order_book(message):
    await message.answer("👇 Обирайте вид 👇",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="⬅ Назад до видів"))
async def back(message):
    await message.answer("👇 Добре, обирайте вид 👇",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="Випадкова книга 🎲"))
async def random_book(message):
    await message.answer("Тут буде випадкова книга",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="Найпопулярніші книги 🏆"))
async def top_books(message):
    top_books = libra_library.get_top5_books()
    result = "🏆 Top 5:\n"
    for book in top_books:
        result += f"📕 {book[1]} ({book[2]}, {book[3]}, {book[4]}) /book{book[0]}\n"
    await message.answer(result,
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="Книги за жанром 👀"))
async def by_genre(message):
    await message.answer("👇 Обирайте жанр 👇",
                         reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(lambda message: message.text in genres)
async def genre_books(message):
    await message.answer("Тут будуть якісь книги",
                         reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(Text(startswith="/book"))
async def view_book(message):
    book_id = int(message.text[5:])
    book = libra_library.get_book(book_id)
    description = f"ISBN: {book[1]}\n" \
                  f"Title: {book[2]}\n" \
                  f"Summary: {book[10]}\n"

    order_btn = types.InlineKeyboardButton(text="Замовити",
                                           callback_data=f"order{book_id}")
    review_btn = types.InlineKeyboardButton(text="Відгук",
                                            callback_data=f"review{book_id}")
    keyboard = types.InlineKeyboardMarkup(row_width=2) \
        .add(order_btn, review_btn)

    await bot.send_photo(message.from_user.id, book[7],
                         caption=description,
                         reply_markup=keyboard)


@dp.callback_query_handler(lambda call: call.data.startswith("order"))
async def order_book(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    book_id = int(call.data[5:])
    book = libra_library.get_book(book_id)
    libra_library.order_book(call.from_user.id, book_id)
    await call.message.answer(f"Успішне замовлення книги {book[2]}")


@dp.callback_query_handler(lambda call: call.data.startswith("review"))
async def order_book(call: types.CallbackQuery):
    await call.message.answer("Успішно теж!")