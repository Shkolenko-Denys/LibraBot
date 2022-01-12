from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import keyboards
from dispatcher import dp
from db.LibraLibrary import libra_library


@dp.message_handler(commands="start")
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    name = libra_library.get_user_name(message.from_user.id)
    if name:
        await message.answer(
            f"Привіт, {name} ✌\n"
            f"Якщо потрібна допомога, тисни /help\n"
            f"Використовуй клавіатуру внизу, щоб виконувати команди 👇\n",
            reply_markup=keyboards.StartKeyboard.keyboard)
    else:
        await message.answer(
            f"Привіт ✌\n"
            f"Ти ще не зареєстрований, тисни /register\n"
            f"Якщо потрібна допомога, тисни /help\n",
            reply_markup=keyboards.StartKeyboard.keyboard)


@dp.message_handler(Text(equals="Скасувати ❌"))
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Скасовано",
                         reply_markup=keyboards.StartKeyboard.keyboard)


@dp.message_handler(Text(equals="⬅ Повернутися"))
async def back_to_start_menu(message):
    await message.answer(message, "👇 Окей, що далі? 👇",
                         reply_markup=keyboards.StartKeyboard.keyboard)


@dp.message_handler(commands="help")
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Для роботи доступні такі команди:\n"
                         "/register -- для реєстрації\n"
                         "/game -- для гри\n",
                         reply_markup=keyboards.StartKeyboard.keyboard)
