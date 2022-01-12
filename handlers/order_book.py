import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from db.LibraLibrary import libra_library
from dispatcher import dp, bot
import keyboards
from handlers.common import cancel


@dp.message_handler(Text(equals="Замовити книгу 📚"))
async def order_book(message):
    await message.answer("👇 Обирайте вид 👇",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="⬅ Назад до видів"))
async def back(message):
    await message.answer("👇 Обирайте вид 👇",
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="Найпопулярніші книги 🏆"))
async def top_books(message):
    top_books = libra_library.get_top5_books()
    result = "🏆 Top 5:\n"
    for book in top_books:
        result += f"📕 {book[1]} ({book[2]}, {book[3]}, {book[4]}) /book{book[0]}\n"
    await message.answer(result,
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(Text(equals="За жанром 👀"))
async def by_genre(message):
    await message.answer("👇 Обирайте жанр 👇",
                         reply_markup=keyboards.GenresKeyboard.keyboard)


@dp.message_handler(lambda message: message.text in libra_library.get_genres())
async def genre_books(message):
    books = libra_library.get_by_genre(message.text)
    result = f"🧩 {message.text}:\n"
    for book in books:
        result += f"📕 {book[1]} ({book[2]}, {book[3]}) /book{book[0]}\n"
    await message.answer(result,
                         reply_markup=keyboards.LibraryBooksKeyboard.keyboard)


@dp.message_handler(Text(startswith="/book"))
async def view_book(message):
    book_id = int(message.text[5:])
    book = libra_library.get_book(book_id)
    description = f"ISBN: {book[1]}\n" \
                  f"Title: {book[2]}\n" \
                  f"Summary: {book[10]}\n"

    order_btn = types.InlineKeyboardButton(text="Замовити 🎒",
                                           callback_data=f"order{book_id}")
    review_btn = types.InlineKeyboardButton(text="Відгук ✍",
                                            callback_data=f"review{book_id}")
    keyboard = types.InlineKeyboardMarkup(row_width=2) \
        .add(order_btn, review_btn)

    await bot.send_photo(message.from_user.id, book[7],
                         caption=description,
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="Випадкова книга 🎲"))
async def random_book(message):
    count = libra_library.count_books()
    message.text = f"/book{random.randint(1, count)}"
    await view_book(message)


@dp.callback_query_handler(lambda call: call.data.startswith("order"))
async def order_book(call: types.CallbackQuery):
    await call.answer(cache_time=10)
    book_id = int(call.data[5:])
    book = libra_library.get_book(book_id)
    libra_library.order_book(call.from_user.id, book_id)
    await call.message.answer(
        f"Успішне замовлення ✅\n"
        f"Книга: {book[2]}\n"
        f"Рік: {book[8]}\n"
        f"Повернути до {libra_library.get_log(call.from_user.id, book_id)[4][:-16]}"
    )


class UserReview(StatesGroup):
    waiting_for_review = State()


@dp.callback_query_handler(lambda call: call.data.startswith("review"))
async def review_book(call: types.CallbackQuery):
    await call.answer(cache_time=10)
    book_id = int(call.data[6:])

    await call.message.answer("Відгук ✍️",
                              reply_markup=keyboards.CancelKeyboard.keyboard)
    await UserReview.waiting_for_review.set()

    @dp.message_handler(state=UserReview.waiting_for_review)
    async def review_input(message: types.Message, state: FSMContext):
        if message.text == "Скасувати ❌":
            await cancel(message, state)
            return

        await state.update_data(review=message.text)
        user_data = await state.get_data()
        libra_library.comment(message.from_user.id, book_id,
                              user_data["review"])
        await message.answer("Відгук додано успішно ✅",
                             reply_markup=keyboards.StartKeyboard.keyboard)
        await state.finish()
