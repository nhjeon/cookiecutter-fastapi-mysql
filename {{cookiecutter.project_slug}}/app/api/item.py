import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import SessionLocal
from model.item import ItemCreate, ItemUpdate
from service import item_service

router = APIRouter()


async def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        logging.info(e)
        db.rollback()
        raise
    finally:
        db.close()


@router.get("/")
def read_items(db: Session = Depends(get_db)):
    return item_service.read_items(db)


@router.get("/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return item_service.read_item(item_id, db)


@router.post("/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(item, db)


@router.put("/{item_id}")
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    return item_service.update_item(item_id, item, db)


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return item_service.delete_item(item_id, db)
