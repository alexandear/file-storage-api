import uuid

from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
async def post_upload(file: UploadFile = File(...)):
    return {"id": uuid.uuid4(), "filename": file.filename}


@router.get("/{file_id}")
@router.head("/{file_id}")
async def download(file_id: str):
    return JSONResponse(content={"message": "downloaded " + file_id}, headers={"Content-Length": str(123)})
