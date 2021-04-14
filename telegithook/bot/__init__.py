from aiogram import Bot
from ..env import get

bot = Bot(get('BOT_TOKEN'), parse_mode='HTML')
