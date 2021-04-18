import logging

from fastapi import FastAPI, APIRouter, Request

from .events import EVENTS
from .bot import send_message, send_raw_event
from .env import CHAT_ID, DEBUG


app = FastAPI()
router = APIRouter()

logger = logging.getLogger()


@router.get('/')
async def index(req: Request):
    return {'ok': False,
            'result': 'GET endpoint does nothing, send payloads to POST endpoint'}


@router.post('/')
async def webhook_base(req: Request):
    try:
        data = await req.json()

        count = 0
        text = ''  # TODO fancier message/string builder
        for event in EVENTS:
            if event.isPresent(data):
                text += event(data).parse()
                count += 1
        if text:
            await send_message(CHAT_ID, text)
        elif DEBUG:
            await send_raw_event(CHAT_ID, data)
        return {'ok': True, 'result': f'{count} events processed'}
    except Exception as e:
        logger.exception("Failed to process payload")
        if DEBUG:
            await send_raw_event(CHAT_ID, data)
        return {'ok': False, 'result': str(e)}


app.include_router(router)
