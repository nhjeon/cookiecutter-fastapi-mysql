import logging
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import SessionLocal
from model.item import ItemCreate, ItemUpdate, Item
from service import item_service

router = APIRouter()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logging.info(e)
        db.rollback()
        raise
    finally:
        db.close()


@router.get("/", response_model=List[Item])
def read_items(db: Session = Depends(get_db)):
    return item_service.read_items(db)


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    return item_service.read_item(item_id, db)


@router.post("/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(item, db)


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    return item_service.update_item(item_id, item, db)


@router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return item_service.delete_item(item_id, db)
