import io
import json

from aiogram import Bot
from .env import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode='HTML')


async def send_message(chat_id: int, message: str):
    await bot.send_message(
        chat_id=chat_id,
        text=message,
        disable_web_page_preview=True
    )


async def send_raw_event(chat_id: int, event: dict, caption: str = ''):
    doc = io.BytesIO(json.dumps(event, indent=2).encode('utf-8'))
    doc.name = 'event.json'
    await bot.send_document(chat_id=chat_id, document=doc, caption=caption)

