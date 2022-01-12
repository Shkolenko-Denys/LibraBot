from aiogram.dispatcher.filters import Text

from db.LibraLibrary import libra_library
from dispatcher import dp


@dp.message_handler(Text(equals="Переглянути карточку 🗂"))
async def view_card(message):
    logs = libra_library.get_logs(message.from_user.id)
    result = ""
    for log in logs:
        book = libra_library.get_book(log[2])
        result += f"📕 {book[2]} -- {log[3]}, {log[4]}"
        if log[5]:
            result += " ✅Повернено\n"
        else:
            result += " ❌Борг\n"
    await message.answer(result)
