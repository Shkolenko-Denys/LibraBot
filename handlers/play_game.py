from dispatcher import dp
import keyboards


@dp.message_handler(lambda message: message.text == "Грати в гру 🎲")
async def game(message):
    await message.answer("Game", reply_markup=keyboards.StartKeyboard.keyboard)
