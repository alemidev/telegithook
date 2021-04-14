from fastapi import APIRouter, Request

from ...bot.messages import send_message
from ..helpers import to_html
from ...actions import actions
from ...env import get

router = APIRouter()


@router.post("/")
async def webhook_base(req: Request):
    json = await req.json()

    for action in actions:
        print()
        if action in json:
            await send_message(get("CHAT_ID"), actions[action].format(r=json, html=to_html))
