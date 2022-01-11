from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class StartKeyboard:
    register_btn = KeyboardButton("Зареєструватись ✍")
    view_card_btn = KeyboardButton("Переглянути карточку 🗂")
    order_book_btn = KeyboardButton("Замовити підручник 📚")
    play_games_btn = KeyboardButton("Грати в гру 🎲")
    search_books_btn = KeyboardButton("Знайти на Google Books 🔎")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(register_btn).row(view_card_btn)\
        .row(order_book_btn).row(play_games_btn).row(search_books_btn)


class LibraryBooksKeyboard:
    back_btn = KeyboardButton("⬅ Повернутися")
    random_btn = KeyboardButton("Випадкова книга 🎲")
    top_btn = KeyboardButton("Найпопулярніші книги 🏆")
    genre_button = KeyboardButton("Книги за жанром 👀")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(back_btn, random_btn)\
        .row(genre_button, top_btn)


class GenresKeyboard:
    back_btn = KeyboardButton("⬅ Назад до видів")
    drama = KeyboardButton("Драма")
    fantasy = KeyboardButton("Фантастика")
    comedy = KeyboardButton("Комедія")
    sport = KeyboardButton("Спорт")
    history = KeyboardButton("Історія")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(back_btn, drama).row(fantasy, comedy).row(sport, history)


class GoogleBooksKeyboard:
    back_btn = KeyboardButton("⬅ Повернутися")
    title_btn = KeyboardButton("Шукати за назвою 📔")
    author_btn = KeyboardButton("Шукати за автором 🙍")
    title_and_author_button = KeyboardButton("Шукати за автором і назвою 🙍📔")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(back_btn).row(title_btn, author_btn).row(title_and_author_button)


class CancelKeyboard:
    cancel_btn = KeyboardButton("Скасувати ❌")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(cancel_btn)


class SkipKeyboard:
    cancel_btn = KeyboardButton("Скасувати ❌")
    skip_btn = KeyboardButton("Пропустити ➡")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(cancel_btn, skip_btn)


class OrderBook:
    order_btn = types.InlineKeyboardButton(text="Замовити",
                                           callback_data="order_book")
    review_btn = types.InlineKeyboardButton(text="Відгук",
                                           callback_data="review_book")

    keyboard = types.InlineKeyboardMarkup(row_width=2)\
        .add(order_btn, review_btn)
