import logging
import threading

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app import app
import config


# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not config.TOKEN:
    exit("No token provided")

# init
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


class FlaskThread(threading.Thread):
    """Second thread for Flask."""
    def run(self) -> None:
        app.run(host='0.0.0.0')


flask_thread = FlaskThread()
flask_thread.daemon = True
