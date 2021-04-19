from aiogram.types import Message

from . import bot
from . import dispatcher
from .connections import CONNECTIONS


@dispatcher.message_handler(text_startswith=['track'])
async def track_new_repo(message: Message):
    args = message.text.replace('track ', '').split()
    repo = args[0]
    if len(text) > 1:
        chat_id = int(args[1])
    else:
        chat_id = message.chat.id
    CONNECTIONS.add(repo, chat_id)
