from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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
        content = """
    <body>
        <form action="/files" enctype="multipart/form-data" method="post">
            <input name="file" type="file">
            <input type="submit">
        </form>
    </body>
        """
        return HTMLResponse(content=content)

    app.include_router(file.router, prefix="/files")

    return app
