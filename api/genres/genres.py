from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.models import Genre

genres_router = APIRouter()


@genres_router.get("/genres")
async def list_all_genres():
    genres = [genre.as_dict for genre in Genre.query().all()]
    return JSONResponse(content=genres)

@genres_router.get("/genres/{genre_id}")
async def get_genre(genre_id):
    genre = Genre.query().filter(Genre.id == genre_id).first()

    if not genre:
        return HTTPException(status_code=404)

    return JSONResponse(content=genre.as_dict)
