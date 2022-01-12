from contextlib import suppress

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified

from db.LibraLibrary import libra_library
from dispatcher import dp
import keyboards


user_data = {}
answer = True


async def update_num_text(message: types.Message, score: int, question: str):
    with suppress(MessageNotModified):
        await message.edit_text(f"📊 Рейтинг: <b>{score}</b>\n"
                                f"❔ Питання: {question[0]}",
                                reply_markup=keyboards.GameKeyboard.keyboard)


@dp.message_handler(Text(equals=["Грати в гру 🎲", "/game"]))
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    question = libra_library.get_question()
    global answer
    answer = question[1]
    await message.answer(f"📊 Рейтинг: <b>0</b>\n"
                         f"❔ Питання: {question[0]}",
                         reply_markup=keyboards.GameKeyboard.keyboard)


@dp.callback_query_handler(Text(startswith="game_"))
async def callbacks_num(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    action = call.data.split("_")[1]

    question = libra_library.get_question()
    global answer

    if action == "true":
        if answer:
            user_data[call.from_user.id] = user_value + 3
        else:
            user_data[call.from_user.id] = user_value - 1
        answer = question[1]
        await update_num_text(call.message, user_data[call.from_user.id],
                              question)
    elif action == "false":
        if answer:
            user_data[call.from_user.id] = user_value - 1
        else:
            user_data[call.from_user.id] = user_value + 3
        answer = question[1]
        await update_num_text(call.message, user_data[call.from_user.id],
                              question)
    elif action == "finish":
        await call.message.edit_text(f"⭐️ Результат: <b>{user_value}</b>")

    await call.answer()
