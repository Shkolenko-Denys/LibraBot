from aiogram import types
from dispatcher import dp
import requests

from config import KEY

URL_VOLUMES = "https://www.googleapis.com/books/v1/volumes?"


@dp.message_handler(commands=['title'])
async def search_topic(message: types.Message):
    query_text = message.text.split(' ', 1)[1]
    query = "intitle:" + query_text
    parameters = {"q": query, "key": KEY, "maxResults": 10}
    book = requests.get(URL_VOLUMES, params=parameters)
    book_json = book.json()

    if book.status_code == 200:
        answer = ""
        if not book_json["totalItems"]:
            answer = "Не знайдено книг з такою назвою"
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
        await message.answer("Помилка")


@dp.message_handler(commands=['author'])
async def search_author(message):
    query_text = message.text.split(' ', 1)[1]
    query = "inauthor:" + query_text
    parameters = {"q": query, "key": KEY, "maxResults": 10}
    book = requests.get(URL_VOLUMES, params=parameters)
    book_json = book.json()

    if book.status_code == 200:
        answer = ""
        if not book_json["totalItems"]:
            answer = "Не знайдено книг з таким автором"
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
        await message.answer("Помилка")


@dp.message_handler(commands=['at'])
async def search_topic_author(message):
    query_text = message.text.split(' ', 1)[1]
    query = query_text
    parameters = {"q": query, "key": KEY, "maxResults": 10}
    book = requests.get(URL_VOLUMES, params=parameters)
    book_json = book.json()

    if book.status_code == 200:
        answer = ""
        if not book_json["totalItems"]:
            answer = "За запитом книг не знайдено"
        try:
            for book in book_json["items"]:
                try:
                    answer += f'\u2022 <a href="{book["volumeInfo"]["canonicalVolumeLink"]}">' \
                              f'{book["volumeInfo"]["title"]}</a>' \
                              + '\n  ' + book["volumeInfo"]["publishedDate"] + '\n'
                # if publishedDate do not exist
                except KeyError:
                    answer += f'\u2022 <a href="{book["volumeInfo"]["canonicalVolumeLink"]}">' \
                              f'{book["volumeInfo"]["title"]}</a> \n'
            await message.answer(answer, parse_mode="HTML", disable_web_page_preview=True)
        except KeyError:
            await message.answer(answer, parse_mode="HTML", disable_web_page_preview=True)
    else:
        await message.answer("Помилка")
