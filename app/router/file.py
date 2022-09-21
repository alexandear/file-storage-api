import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.sql import crud, model, schema
from app.sql.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
async def post_upload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    file_m = schema.File(id=str(uuid.uuid4()), name=file.filename, size=len(content), content=content)
    return crud.create_file(db, file_m)


@router.head("/{file_id}")
async def info(file_id: str, db: Session = Depends(get_db)):
    file = crud.get_file_info(db, file_id)
    if not file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={}, headers={"Content-Length": str(file.size)})


@router.get("/{file_id}")
async def download(file_id: str, db: Session = Depends(get_db)):
    file = crud.get_file(db, file_id)
    if not file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"name": file.name}, headers={"Content-Length": str(file.size)})
