from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from dispatcher import dp
import keyboards
from handlers.common import cancel
from db.LibraLibrary import libra_library


class UserRegister(StatesGroup):
    waiting_for_nickname = State()
    waiting_for_name = State()
    waiting_for_password = State()
    waiting_for_about_me = State()


@dp.message_handler(Text(equals=["Зареєструватись ✍", "/register"]))
async def register_start(message: types.Message):
    await message.answer("Придумайте унікальний нікнейм:",
                         reply_markup=keyboards.CancelKeyboard.keyboard)
    await UserRegister.waiting_for_nickname.set()


@dp.message_handler(state=UserRegister.waiting_for_nickname)
async def surname_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    if libra_library.find_nickname(message.text):
        await message.answer("Такий уже існує, придумайте інший:",
                             reply_markup=keyboards.CancelKeyboard.keyboard)
        await UserRegister.waiting_for_nickname.set()
    else:
        await state.update_data(nickname=message.text)
        await message.answer("Введіть ім'я:")
        await UserRegister.waiting_for_name.set()


@dp.message_handler(state=UserRegister.waiting_for_name)
async def name_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(name=message.text)
    await message.answer("Придумайте пароль:")
    await UserRegister.waiting_for_password.set()


@dp.message_handler(state=UserRegister.waiting_for_password)
async def name_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(password=message.text)
    await message.answer("Напишіть коротко про себе(необов'язково):",
                         reply_markup=keyboards.SkipKeyboard.keyboard)
    await UserRegister.waiting_for_about_me.set()


@dp.message_handler(state=UserRegister.waiting_for_about_me)
async def passport_number_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    if message.text == "Пропустити ➡":
        await state.update_data(about_me="None")
    else:
        await state.update_data(about_me=message.text)

    user_data = await state.get_data()
    libra_library.register(message.from_user.id,
                           user_data["nickname"], user_data["name"],
                           user_data["password"], user_data["about_me"])
    await message.answer("Реєстрація виконана успішно ✅",
                         reply_markup=keyboards.StartKeyboard.keyboard)
    await state.finish()
