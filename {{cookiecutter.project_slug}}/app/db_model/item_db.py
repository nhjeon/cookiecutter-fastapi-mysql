from sqlalchemy import Column, Integer, String, DateTime

from database.db import Base


class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))
    create_time = Column(DateTime)
