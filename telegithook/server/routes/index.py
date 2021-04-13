from fastapi import APIRouter, Request

from messages import send_raw_event

router = APIRouter()


@router.get("/")
async def index(req: Request):
    doc = await req.json()
    await send_raw_event(-445530430, doc)
    return {"result": "OK"}
