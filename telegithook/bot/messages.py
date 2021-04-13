from . import bot


async def send_message(chat_id: int, message: str):
    await bot.send_message(chat_id, message)
