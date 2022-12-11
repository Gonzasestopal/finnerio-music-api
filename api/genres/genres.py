from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.models import Genre

genres_router = APIRouter()


@genres_router.get("/genres")
async def list_all_genres():
    genres = [genre.as_dict for genre in Genre.query().all()]
    return JSONResponse(content=genres)
