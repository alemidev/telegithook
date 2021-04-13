from aiogram import Bot
from ..env import get

bot = Bot(get("TOKEN"), parse_mode="HTML")
