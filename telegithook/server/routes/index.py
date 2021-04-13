from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
async def index(req: Request):
    return "Ciao, cîhan!"
