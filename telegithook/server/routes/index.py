from fastapi import APIRouter, Request

from ...bot.messages import send_message, send_raw_event
from ..helpers import to_html
from ...events import EVENTS
from ...env import get

router = APIRouter()


@router.get("/")
async def _():
    return {}


@router.post("/")
async def webhook_base(req: Request):
    json = await req.json()

    text = ""  # TODO fancier message/string builder
    for event in EVENTS:
        if event.isPresent(json):
            text += event(json).parse()
    await send_message(get("CHAT_ID"), text)

    # still send this for debug purposes
    await send_raw_event(get("CHAT_ID"), json)
