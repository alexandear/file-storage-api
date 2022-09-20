from fastapi import FastAPI

app = FastAPI()


@app.post("/files")
async def upload_file():
    return {"message": "upload_file"}


@app.get("/files/{id}")
async def download_file():
    return {"message": "download_file"}


@app.head("/files/{id}")
async def info_file():
    return None
