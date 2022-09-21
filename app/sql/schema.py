from pydantic import BaseModel


class File(BaseModel):
    id: str
    name: str
    size: int
    content: bytes

    class Config:
        orm_mode = True
