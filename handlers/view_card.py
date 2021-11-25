from aiogram.dispatcher.filters import Text

from dispatcher import dp


@dp.message_handler(Text(equals="Переглянути карточку 🗂"))
async def view_card(message):
    await message.answer("Тут відображається карточка")
