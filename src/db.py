from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from src import settings

db_settings = {
    'drivername': 'postgresql+psycopg2',
    'database': settings.DB_NAME,
    'username': settings.DB_USERNAME,
    'password': settings.DB_PASSWORD,
    'port': settings.DB_PORT,
    'host': settings.DB_HOST,
}

engine = create_engine(URL(**db_settings))

Session = scoped_session(sessionmaker(expire_on_commit=False))

