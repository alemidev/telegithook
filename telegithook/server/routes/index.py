from fastapi import APIRouter, Request

from bot.messages import send_raw_event
from env import get

router = APIRouter()


@router.get("/")
async def index(req: Request):
    return {"error": "you should send events as POST"}

@router.post("/")
async def webhook_base(req: Request):
    doc = await req.json()
    await send_raw_event(chat_id=get("DEBUG_CHAT_ID"), event=doc)
    return {"result": "OK"}
