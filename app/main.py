from fastapi import FastAPI

from app.router import file


def create_app() -> FastAPI:
    app = FastAPI(
        title="File API",
        description="API example to upload, download files to server",
        version="0.1.0",
        contact={"name": "Oleksandr Redko", "email": "oleksandr.red+github@gmail.com"},
    )

    @app.get("/")
    async def root():
        return {"message": "It works"}

    app.include_router(file.router, prefix="/files")

    return app
