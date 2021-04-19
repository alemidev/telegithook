from aiogram import Bot
from aiogram import Dispatcher

from ..env import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dispatcher = Dispatcher(bot)
