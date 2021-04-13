from fastapi import APIRouter, Request

from bot.messages import send_raw_event

router = APIRouter()


@router.get("/")
async def index(req: Request):
    return {"error": "you should send events as POST"}

@router.post("/")
async def webhook_base(req: Request):
    doc = await req.json()
    await send_raw_event(chat_id=-445530430, event=doc)
    return {"result": "OK"}
