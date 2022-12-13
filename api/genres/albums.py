from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.models import  Song, Album

albums_router = APIRouter()


@albums_router.get("/albums/{album_id}")
async def get_songs_by_album(album_id):
    songs = Song.query().join(Album, Album.id == Song.album_id).filter(Song.album_id == album_id).all()

    if not songs:
        return HTTPException(status_code=404)

    songs = [song.as_dict for song in songs]

    return JSONResponse(content=songs)


@albums_router.get("/albums")
async def get_albums():
    albums = Album.query().all()

    return JSONResponse(content=[album.as_dict for album in albums])
