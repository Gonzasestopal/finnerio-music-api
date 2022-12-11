import os

import uvicorn

from src.settings import config

def main():
    uvicorn.run(
        app="src.server:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "production" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()
