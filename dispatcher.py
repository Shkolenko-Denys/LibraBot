import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
from handlers.common import register_handlers_common
from handlers.login import register_handlers_login
from handlers.register import register_handlers_register

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not config.TOKEN:
    exit("No token provided")

# init
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


register_handlers_common(dp)
register_handlers_login(dp)
register_handlers_register(dp)
