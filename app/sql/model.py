from sqlalchemy import Column, Integer, LargeBinary, String

from .database import Base


class File(Base):
    __tablename__ = "files"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    size = Column(Integer)
    content = Column(LargeBinary)
