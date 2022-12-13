from typing import Any

from sqlalchemy import Column, Integer, MetaData, String, ForeignKey
from sqlalchemy.ext.declarative import as_declarative

from src.db import Session, engine

SCHEMA = 'public'


@as_declarative(metadata=(MetaData(schema=SCHEMA)))
class Base:
    id = Column(Integer, primary_key=True)
    __name__: str

    @classmethod
    def query(cls):
        return Session.query(cls)


class Genre(Base):
    __tablename__ = 'genres'

    name = Column(String)

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Subgenre(Base):
    __tablename__ = 'subgenres'

    name = Column(String)
    genre_id = Column(Integer, ForeignKey(Genre.id))

    @property
    def as_dict(self):
        return {
            'name': self.name,
            'genre_id': self.genre_id
        }

class Artist(Base):
    __tablename__ = 'artists'

    name = Column(String)
    genre_id = Column(Integer, ForeignKey(Genre.id))

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre_id': self.genre_id,
        }

class Album(Base):
    __tablename__ = 'albums'

    name = Column(String)
    artist_id = Column(Integer, ForeignKey(Artist.id))
    genre_id = Column(Integer, ForeignKey(Genre.id))


    @property
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist_id': self.artist_id,
            'genre_id': self.genre_id,
        }

class Song(Base):
    __tablename__ = 'songs'

    name = Column(String)
    artist_id = Column(Integer, ForeignKey(Artist.id))
    album_id = Column(Integer, ForeignKey(Album.id))
    genre_id = Column(Integer, ForeignKey(Genre.id))

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist_id': self.artist_id,
            'album_id': self.album_id,
            'genre_id': self.genre_id,
        }

Base.metadata.bind = engine
