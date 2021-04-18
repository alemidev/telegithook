from aiogram import Bot, Dispatcher
from ..env import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dispatcher = Dispatcher(bot)
