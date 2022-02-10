from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db_model.item_db import ItemDB
from model.item import ItemCreate, ItemUpdate


def read_items(db: Session):
    return db.query(ItemDB).all()


def create_item(item_create: ItemCreate, db: Session):
    item = ItemDB(name=item_create.name, create_time=item_create.create_time)
    db.add(item)
    db.commit()
    return item


def update_item(item_id: int, item_update: ItemUpdate, db: Session):
    item: ItemDB = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(404)

    item_data = jsonable_encoder(item)
    update_data = item_update.dict(skip_defaults=True)
    for field in item_data:
        if field in update_data:
            setattr(item, field, update_data[field])
    db.add(item)
    db.commit()
    return item


def delete_item(item_id: int, db: Session):
    item: ItemDB = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(404)

    db.delete(item)
    db.commit()
    return item


def read_item(item_id: int, db: Session):
    item: ItemDB = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(404)
    return item
