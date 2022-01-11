from aiogram import executor

from dispatcher import dp, flask_thread
import handlers


if __name__ == '__main__':
    flask_thread.start()
    executor.start_polling(dp, skip_updates=True)
