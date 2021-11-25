from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import keyboards


async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Привіт ✌\nВикористовуй клавіатуру внизу, щоб виконувати команди 👇\n",
        reply_markup=keyboards.StartKeyboard.keyboard)


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Скасовано",
                         reply_markup=keyboards.StartKeyboard.keyboard)


async def back_to_start_menu(message):
    await message.answer(message, "👇 Окей, що далі? 👇",
                         reply_markup=keyboards.StartKeyboard.keyboard)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start", state="*")
    dp.register_message_handler(cancel, Text(equals="Скасувати ❌"), state="*")
    dp.register_message_handler(back_to_start_menu,
                                Text(equals="⬅ Повернутися"), state="*")
