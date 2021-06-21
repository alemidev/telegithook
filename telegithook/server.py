import logging

from fastapi import FastAPI, APIRouter, Request

from .events import EVENTS
from .bot.updates import dispatch
from .env import DEBUG


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
        repo = data["repository"]["full_name"]

        count = 0
        text = ''  # TODO fancier message/string builder
        for event in EVENTS:
            if event.isPresent(data):
                text += event(data).parse()
                count += 1
        # await dispatch(repo, data=data)
        # logging.info("normal wale se aaya hoon")
        if text:
            await dispatch(repo, message=text)
        elif DEBUG:
            # logging.info("debug wale se aaya hoon")
            await dispatch(repo, data=data)
        return {'ok': True, 'result': f'{count} events processed'}
    except Exception as e:
        logger.exception("Failed to process payload")
        if DEBUG and 'repo' in locals(): # gross but will do for now
            await dispatch(repo, data=data)
        return {'ok': False, 'result': str(e)}


app.include_router(router)
