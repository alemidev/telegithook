import io
import json
from typing import Union

from . import bot
from .connections import CONNECTIONS

async def dispatch(repository:str, message:Union[str,None]=None, data=Union[dict,None]=None):
    for chat_id in CONNECTIONS.get(repository):
        if data:
            doc = io.BytesIO(json.dumps(data, indent=2).encode('utf-8'))
            doc.name = 'event.json'
            await bot.send_document(chat_id=chat_id, document=doc, caption=message)
        elif message:
            await bot.send_message(chat_id=chat_id, text=message, disable_web_page_preview=True)

