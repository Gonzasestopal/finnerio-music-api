from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from src.settings import config

db_settings = {
    'drivername': 'postgresql+psycopg2',
    'database': config.DB_NAME,
    'username': config.DB_USERNAME,
    'password': config.DB_PASSWORD,
    'port': config.DB_PORT,
    'host': config.DB_HOST,
}

engine = create_engine(URL(**db_settings))

Session = scoped_session(sessionmaker(expire_on_commit=False))

