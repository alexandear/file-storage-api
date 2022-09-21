from sqlalchemy.orm import Session

from . import model, schema


def get_file(db: Session, file_id: str) -> model.File:
    return db.query(model.File).filter(model.File.id == file_id).first()


def get_file_info(db: Session, file_id: str) -> model.File:
    return db.query(model.File).filter(model.File.id == file_id).first()


def create_file(db: Session, file: schema.File) -> model.File:
    db_file = model.File(id=file.id, name=file.name, size=file.size, content=file.content)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file
