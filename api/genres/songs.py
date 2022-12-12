from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.models import Song

songs_router = APIRouter()


@songs_router.get("/songs/{song_id}")
def get_song(song_id):
    song = Song.query().filter(Song.id == song_id).first()

    if not song:
        return HTTPException(status_code=404)

    return JSONResponse(content=song.as_dict)
