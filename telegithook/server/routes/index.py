from fastapi import APIRouter, Request

from ...bot.messages import send_message
from ..helpers import to_html
from ... import strings
from ...env import get

router = APIRouter()


@router.get("/")
async def index(req: Request):
    return {"error": "you should send events as POST"}


@router.post("/")
async def webhook_base(req: Request):
    json = await req.json()
    actions = strings.get("actions")

    for action in actions:
        if action in json:
            await send_message(get("CHAT_ID"), actions[action].format(_=json, __=to_html))
