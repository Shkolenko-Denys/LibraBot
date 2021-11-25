from phonenumbers import is_possible_number, parse, NumberParseException
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import keyboards
from LibraLibrary import libra_library
from handlers.common import cancel
from dispatcher import dp


class UserLogin(StatesGroup):
    waiting_for_phone_number = State()
    waiting_for_password = State()


@dp.message_handler(Text(equals="Увійти 🧑‍💻"))
async def login_start(message: types.Message):
    await message.answer("Введіть номер телефону 📞:",
                         reply_markup=keyboards.CancelKeyboard.keyboard)
    await UserLogin.waiting_for_phone_number.set()


@dp.message_handler(state=UserLogin.waiting_for_phone_number)
async def phone_number_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    try:
        phone_number = parse(message.text)
    except NumberParseException:
        await message.answer("Введений рядок не відповідає номеру телефона 😔\n"
                             "Спробуйте ще раз")
        return

    if not is_possible_number(phone_number):
        await message.answer("Некоректний номер телефону 😔\nСпробуйте ще раз")
        return

    if not libra_library.find_phone_number(message.text):
        await message.answer("Цей номер телефону не зареєстрований в "
                             "бібліотеці. Спробуйте ще раз або поверніться "
                             "і зареєструйтесь 🙂")
        return

    await state.update_data(phone_number=message.text)
    await message.answer("Введіть пароль 🔑:")
    await UserLogin.waiting_for_password.set()


@dp.message_handler(state=UserLogin.waiting_for_password)
async def password_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    user_data = await state.get_data()
    if libra_library.login(user_data["phone_number"], message.text):
        await message.answer("Вхід виконано успішно ✅",
                             reply_markup=keyboards.StartKeyboard.keyboard)
    else:
        await message.answer(
            "Пароль не вірний 🤔 Спробуйте ще раз",
            reply_markup=keyboards.StartKeyboard.keyboard)
    await state.finish()
