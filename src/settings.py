import os

from dotenv import load_dotenv
from distutils.util import strtobool

load_dotenv()

APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
APP_RELOAD = bool(strtobool(os.getenv("APP_RELOAD", "True")))

DEBUG = os.getenv("DEBUG", "False")

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_USERNAME = os.getenv("DB_USERNAME", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "docker")
DB_NAME = os.getenv("DB_NAME", "postgres")
