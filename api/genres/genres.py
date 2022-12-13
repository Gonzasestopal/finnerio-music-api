from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.models import Genre, Artist, Subgenre

genres_router = APIRouter()


@genres_router.get("/genres")
async def list_all_genres():
    genres_with_subgenres = []
    for genre in Genre.query().all():
        subgenres = Subgenre.query().join(Genre, Genre.id == Subgenre.genre_id).filter(Genre.id == genre.id)
        genre_info = genre.as_dict
        genre_info['subgenres'] = [subgenre.as_dict for subgenre in subgenres]
        genres_with_subgenres.append(genre_info)

    return JSONResponse(content=genres_with_subgenres)

@genres_router.get("/genres/{genre_id}/artists")
async def get_artists_by_genre(genre_id):
    artists = Artist.query().join(Genre, Artist.genre_id == Genre.id).filter(Genre.id == genre_id).all()

    if not artists:
        raise HTTPException(status_code=404)

    artists = [artist.as_dict for artist in artists]

    return JSONResponse(content=artists)
