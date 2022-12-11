import uvicorn

from src import settings

def main():
    uvicorn.run(
        app="src.server:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_RELOAD,
        workers=1,
    )


if __name__ == "__main__":
    main()
