from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import keyboards
from dispatcher import dp


@dp.message_handler(commands="start")
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Привіт ✌\nВикористовуй клавіатуру внизу, щоб виконувати команди 👇\n",
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
