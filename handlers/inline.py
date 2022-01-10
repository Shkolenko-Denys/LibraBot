from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dispatcher import dp
import requests

from config import KEY

URL = "https://www.googleapis.com/books/v1/volumes?"


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query

    parameters = {"q": text, "key": KEY, "maxResults": 20}
    books = requests.get(URL, params=parameters)
    book_json = books.json()

    if books.status_code == 200:
        articles = [types.InlineQueryResultArticle(
            id=book["id"],
            title=book["volumeInfo"]["title"],
            url=book["volumeInfo"]["canonicalVolumeLink"],
            thumb_url=book.get("volumeInfo").get("imageLinks", {}).
                get("smallThumbnail", "https://www.globaluniversityalliance.org/wp-content/uploads/2017/10/No-Cover-Image-01.png"),
            description=f'{"".join(book["volumeInfo"]["authors"])}\n'
                        f'{book.get("volumeInfo").get("publishedDate", "")}\n'
                        f'{book.get("volumeInfo").get("description", "Анотація відсутня")}',
            hide_url=True,

            input_message_content=types.InputTextMessageContent(
                message_text=f'{book["volumeInfo"]["title"]}\n'
                             f'{"".join(book["volumeInfo"]["authors"])}\n'
                             f'{book.get("volumeInfo").get("publishedDate", "")}\n\n'
                             f'{book.get("volumeInfo").get("description", "")}'
            ),


            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Посилання",
                                                                         url=book["volumeInfo"]["canonicalVolumeLink"]))

        ) for book in book_json["items"]]

        await query.answer(articles, cache_time=1, is_personal=True)
