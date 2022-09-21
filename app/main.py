import uuid

from fastapi import FastAPI, File, UploadFile, status

app = FastAPI()


@app.post("/files", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):
    return {"id": uuid.uuid4(), "filename": file.filename}


@app.get("/files/{id}")
async def download_file():
    return {"message": "download_file"}


@app.head("/files/{id}")
async def info_file():
    return None
