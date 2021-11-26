from aiogram.dispatcher.filters import Text
from aiogram import types

from dispatcher import dp
import keyboards
import requests
from config import KEY
URL_VOLUMES = "https://www.googleapis.com/books/v1/volumes?"


@dp.message_handler(Text(equals="Знайти на Google Books 🔎"))
async def search_start(message):
    await message.answer("👇 Оберіть режим 👇",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)


@dp.message_handler(commands=['title'])
async def search_topic(message: types.Message):
    query_text = message.text.split(' ', 1)[1]
    await message.answer(query_text)
    query = "intitle:" + query_text
    parameters = {"q": query, "key": KEY, "maxResults": 10}
    book = requests.get(URL_VOLUMES, params=parameters)
    book_json = book.json()

    if book.status_code == 200:
        answer = ""
        if not book_json["totalItems"]:
            answer = "No books with such title"
        try:
            for book in book_json["items"]:
                try:
                    answer += f'\u2022 <a href="{book["volumeInfo"]["canonicalVolumeLink"]}">' \
                              f'{book["volumeInfo"]["title"]}</a>'\
                              + '\n  ' + book["volumeInfo"]["publishedDate"] + '\n'
                # if publishedDate do not exist
                except KeyError:
                    answer += f'\u2022 <a href="{book["volumeInfo"]["canonicalVolumeLink"]}">' \
                              f'{book["volumeInfo"]["title"]}</a> \n'
            await message.answer(answer, parse_mode="HTML", disable_web_page_preview=True)
        except KeyError:
            await message.answer(answer, parse_mode="HTML", disable_web_page_preview=True)
    else:
        await message.answer("Error")


@dp.message_handler(commands=['author'])
async def search_author(message):
    query_text = message.text.split(' ', 1)[1]
    await message.answer(query_text)
    query = "inauthor:" + query_text
    parameters = {"q": query, "key": KEY, "maxResults": 10}
    book = requests.get(URL_VOLUMES, params=parameters)
    book_json = book.json()

    if book.status_code == 200:
        answer = ""
        if not book_json["totalItems"]:
            answer = "That author doesn't have any books"
        try:
            for book in book_json["items"]:
                try:
                    answer += f'\u2022 <a href="{book["volumeInfo"]["canonicalVolumeLink"]}">' \
                              f'{book["volumeInfo"]["title"]}</a>'\
                              + '\n  ' + book["volumeInfo"]["publishedDate"] + '\n'
                # if publishedDate do not exist
                except KeyError:
                    answer += f'\u2022 <a href="{book["volumeInfo"]["canonicalVolumeLink"]}">' \
                              f'{book["volumeInfo"]["title"]}</a> \n'
            await message.answer(answer, parse_mode="HTML", disable_web_page_preview=True)
        except KeyError:
            await message.answer(answer, parse_mode="HTML", disable_web_page_preview=True)
    else:
        await message.answer("Error")


@dp.message_handler(commands=['at'])
async def search_topic_author(message):
    await message.answer("Шукаємо за автором і назвою...",
                         reply_markup=keyboards.GoogleBooksKeyboard.keyboard)
