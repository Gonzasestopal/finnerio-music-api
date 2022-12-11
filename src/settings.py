import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DB_HOST: str = "127.0.0.1"
    DB_PORT: str = "5432"
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "docker"
    DB_NAME: str = "napster_dev"


class DevelopmentConfig(Config):
    DB_HOST: str = "aws"
    DB_PORT: str = "5432"
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "docker"
    DB_NAME: str = "napster_dev"


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG: str = False
    DB_HOST: str = "aws"
    DB_PORT: str = "5432"
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "docker"
    DB_NAME: str = "napster_prod"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
