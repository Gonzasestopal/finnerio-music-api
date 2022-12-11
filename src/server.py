from fastapi import FastAPI

from api.genres import genres_router


def init_routers(app_: FastAPI) -> None:
    app_.include_router(genres_router)

def create_app() -> FastAPI:
    app_ = FastAPI()
    init_routers(app_)
    return app_

app = create_app()
