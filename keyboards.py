from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class StartKeyboard:
    login_btn = KeyboardButton("Login")
    register_btn = KeyboardButton("Register")
    view_card_btn = KeyboardButton("View your library card")
    order_book_btn = KeyboardButton("Order a book")
    play_games_btn = KeyboardButton("Play games")
    search_books_btn = KeyboardButton("Search books with Google Books")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(login_btn).row(register_btn).row(view_card_btn)\
        .row(order_book_btn).row(play_games_btn).row(search_books_btn)


class LibraryBooksKeyboard:
    random_btn = KeyboardButton("Random book")
    back_btn = KeyboardButton("⬅ Back")

    top_btn = KeyboardButton("Top books")
    genre_button = KeyboardButton("Books by genre")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(back_btn, random_btn)\
        .row(genre_button, top_btn)


class GenresKeyboard:
    back_btn = KeyboardButton("⬅ Back to modes")
    drama = KeyboardButton("Drama")
    fantasy = KeyboardButton("Fantasy")
    comedy = KeyboardButton("Comedy")
    sport = KeyboardButton("Sport")
    history = KeyboardButton("History")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(back_btn, drama).row(fantasy, comedy).row(sport, history)


class GoogleBooksKeyboard:
    title_btn = KeyboardButton("Search by title")
    back_btn = KeyboardButton("⬅ Back")

    author_btn = KeyboardButton("Search by author")
    title_and_author_button = KeyboardButton("Search by title and author")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(back_btn).row(title_btn, author_btn).row(title_and_author_button)
