from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.models import Genre, Artist

genres_router = APIRouter()


@genres_router.get("/genres")
async def list_all_genres():
    genres = [genre.as_dict for genre in Genre.query().all()]
    return JSONResponse(content=genres)

@genres_router.get("/genres/{genre_id}/artists")
async def get_artists_by_genre(genre_id):
    artists = Artist.query().join(Genre, Artist.genre_id == Genre.id).filter(Genre.id == genre_id).all()

    if not artists:
        return HTTPException(status_code=404)

    artists = [artist.as_dict for artist in artists]

    return JSONResponse(content=artists)
