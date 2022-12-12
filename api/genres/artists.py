from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.models import Album, Artist

artists_router = APIRouter()


@artists_router.get("/artists/{artist_id}/albums")
async def get_artists(artist_id):
    album = Album.query().filter(Artist.id == artist_id).first()

    if not album:
        return HTTPException(status_code=404)

    return JSONResponse(content=album.as_dict)


@artists_router.get("/artists")
async def get_artist_by_song(song_id = None):
    album = Album.query().filter(Album.song_id == song_id).first()

    if not album:
        return HTTPException(status_code=404)

    artist = Artist.query().filter(Album.id == album.id).first()

    if not artist:
        return HTTPException(status_code=404)

    return JSONResponse(content=artist.as_dict)

