from fastapi import APIRouter, Request

from ...bot.messages import send_message, send_raw_event
from ...events import EVENTS
from ...env import CHAT_ID

router = APIRouter()


@router.get('/')
async def index(req: Request):
    return {'ok': True, 'result': True}


@router.post('/')
async def webhook_base(req: Request):
    try:
        json = await req.json()

        text = ''  # TODO fancier message/string builder
        for event in EVENTS:
            if event.isPresent(json):
                text += event(json).parse()
        if text:
            await send_message(CHAT_ID, text)

            # still send this for debug purposes
            await send_raw_event(CHAT_ID, json)
        return {'ok': True, 'result': True}
    except Exception as e:
        result = f'{type(e).__name__}: {e}'
        print('Error', result)
        return {'ok': False, 'result': result}
