from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.models import Album, Artist, Song

artists_router = APIRouter()


@artists_router.get("/artists/{artist_id}/albums")
async def get_albums_by_artist(artist_id):
    albums = Album.query().join(Artist, Artist.id == Album.artist_id).filter(Artist.id == artist_id).all()

    if not albums:
        return HTTPException(status_code=404)

    albums = [album.as_dict for album in albums]

    return JSONResponse(content=albums)


@artists_router.get("/artists")
async def get_artists(song_id = None):
    if not song_id:
        artists = Artist.query().all()

        return JSONResponse(content=[artist.as_dict for artist in artists])

    song = Song.query().filter(Song.id == song_id).first()
    if not song:
        return HTTPException(status_code=404)

    artist = Artist.query().join(Song, Song.artist_id == Artist.id).filter(Artist.id == song.artist_id).first()

    if not artist:
        return HTTPException(status_code=404)

    return JSONResponse(content=[artist.as_dict])

