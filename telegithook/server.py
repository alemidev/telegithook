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
        headers = req.headers
        event = headers["X-GitHub-Event"]
        repo = data["repository"]["full_name"]
        await dispatch(repo, message=EVENTS[event](data).parse())
        return {'ok': True, 'result': f'1 event processed'}
    except Exception as e:
        logger.exception("Failed to process payload")
        logger.error(str(data)) # TODO remove later
        if DEBUG and 'repo' in locals(): # gross but will do for now
            await dispatch(repo, data=data)
        return {'ok': False, 'result': str(e)}


app.include_router(router)
