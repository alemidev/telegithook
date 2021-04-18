import io
import json
import logging
from typing import Union

from . import bot
from .connections import CONNECTIONS

logger = logging.getLogger()

async def dispatch(repository:str, message:Union[str,None]=None, data:Union[dict,None]=None):
    for chat_id in CONNECTIONS.get(repository):
        try:
            if data:
                doc = io.BytesIO(json.dumps(data, indent=2).encode('utf-8'))
                doc.name = 'event.json'
                await bot.send_document(chat_id=chat_id, document=doc, caption=message)
            elif message:
                await bot.send_message(chat_id=chat_id, text=message, disable_web_page_preview=True)
        except:
            logger.exception(f"Error dispatching event to {chat_id}")

