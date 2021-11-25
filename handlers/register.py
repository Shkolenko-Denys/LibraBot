from phonenumbers import is_possible_number, parse, NumberParseException
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import keyboards
from LibraLibrary import libra_library
from handlers.common import cancel


class UserRegister(StatesGroup):
    waiting_for_surname = State()
    waiting_for_name = State()
    waiting_for_patronymic = State()
    waiting_for_birthday = State()
    waiting_for_phone_number = State()
    waiting_for_email = State()
    waiting_for_telegram_username = State()
    waiting_for_address = State()
    waiting_for_passport_number = State()


async def register_start(message: types.Message):
    await message.answer("Введіть прізвище:",
                         reply_markup=keyboards.CancelKeyboard.keyboard)
    await UserRegister.waiting_for_surname.set()


async def surname_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(surname=message.text)
    await message.answer("Введіть ім'я:")
    await UserRegister.waiting_for_name.set()


async def name_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(name=message.text)
    await message.answer("Введіть по батькові:")
    await UserRegister.waiting_for_patronymic.set()


async def patronymic_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(patronymic=message.text)
    await message.answer("Введіть дату народження:")
    await UserRegister.waiting_for_birthday.set()


async def birthday_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(birthday=message.text)
    await message.answer("Введіть номер телефону:")
    await UserRegister.waiting_for_phone_number.set()


# this func is duplicated. This will be fixed
async def phone_number_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    try:
        phone_number = parse(message.text)
    except NumberParseException:
        await message.answer(
            "Введений рядок не відповідає номеру телефона 😔\n"
            "Спробуйте ще раз")
        return

    if not is_possible_number(phone_number):
        await message.answer("Некоректний номер телефону 😔\nСпробуйте ще раз")
        return

    if libra_library.find_phone_number(message.text):
        await message.answer("Цей номер телефону вже зареєстрований в "
                             "бібліотеці. Спробуйте ще раз або поверніться "
                             "і увійдіть 🙂")
        return

    await state.update_data(phone_number=message.text)
    await message.answer("Введіть email:")
    await UserRegister.waiting_for_email.set()


async def email_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(email=message.text)
    await message.answer("Введіть username в телеграм:")
    await UserRegister.waiting_for_telegram_username.set()


async def telegram_username_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(telegram_username=message.text)
    await message.answer("Введіть адресу проживання:")
    await UserRegister.waiting_for_address.set()


async def address_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(address=message.text)
    await message.answer("Введіть номер паспорта:")
    await UserRegister.waiting_for_passport_number.set()


async def passport_number_input(message: types.Message, state: FSMContext):
    if message.text == "Скасувати ❌":
        await cancel(message, state)
        return

    await state.update_data(passport_number=message.text)
    user_data = await state.get_data()
    if libra_library.register(user_data["surname"], user_data["name"],
                              user_data["patronymic"], user_data["birthday"],
                              user_data["phone_number"], user_data["email"],
                              user_data["telegram_username"],
                              user_data["address"],
                              user_data["passport_number"]):
        await message.answer("Реєстрація виконана успішно ✅",
                             reply_markup=keyboards.StartKeyboard.keyboard)
    else:
        await message.answer(
            "Щось пішло не так 🤔 Спробуйте ще раз",
            reply_markup=keyboards.StartKeyboard.keyboard)
    await state.finish()


def register_handlers_register(dp: Dispatcher):
    dp.register_message_handler(
        register_start, Text(equals="Зареєструватись ✍"), state="*")
    dp.register_message_handler(
        surname_input, state=UserRegister.waiting_for_surname)
    dp.register_message_handler(
        name_input, state=UserRegister.waiting_for_name)
    dp.register_message_handler(
        patronymic_input, state=UserRegister.waiting_for_patronymic)
    dp.register_message_handler(
        birthday_input, state=UserRegister.waiting_for_birthday)
    dp.register_message_handler(
        phone_number_input, state=UserRegister.waiting_for_phone_number)
    dp.register_message_handler(
        email_input, state=UserRegister.waiting_for_email)
    dp.register_message_handler(
        telegram_username_input,
        state=UserRegister.waiting_for_telegram_username)
    dp.register_message_handler(
        address_input, state=UserRegister.waiting_for_address)
    dp.register_message_handler(
        passport_number_input, state=UserRegister.waiting_for_passport_number)
