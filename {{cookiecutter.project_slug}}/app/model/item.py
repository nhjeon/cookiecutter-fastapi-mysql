from datetime import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    create_time: datetime = datetime.utcnow()


class ItemCreate(ItemBase):
    name: str


class ItemUpdate(ItemBase):
    name: str


class Item(ItemBase):
    id: str
    name: str
    create_time: datetime

    class Config:
        orm_mode = True
