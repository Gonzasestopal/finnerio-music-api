from fastapi import APIRouter, Response

genres_router = APIRouter()


@genres_router.get("/genres")
async def home():
    return Response(status_code=200)
