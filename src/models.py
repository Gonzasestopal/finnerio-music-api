from typing import Any

from sqlalchemy import Column, Integer, MetaData, String
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
            'name': self.name,
        }


Base.metadata.bind = engine
