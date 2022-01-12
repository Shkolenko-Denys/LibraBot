from aiogram.dispatcher.filters import Text

from db.LibraLibrary import libra_library
from dispatcher import dp


@dp.message_handler(Text(equals="Переглянути карточку 🗂"))
async def view_card(message):
    logs = libra_library.get_logs(message.from_user.id)
    result = ""
    for log in logs:
        book = libra_library.get_book(log[2])
        result += f"📕 <b>{book[2]}</b>\n" \
                  f"  Дата взяття: {log[3][:-7]}\n" \
                  f"  Дата повернення: {log[4][:-7]}\n"
        if log[5]:
            result += "  ✅ Повернено\n\n"
        else:
            result += "  ❌ Борг\n\n"
    await message.answer(result)
