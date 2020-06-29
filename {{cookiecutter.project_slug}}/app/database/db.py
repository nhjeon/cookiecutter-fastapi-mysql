from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = {{ cookiecutter.mysql_url }}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)
SessionLocal = scoped_session(sessionmaker(autoflush=False, bind=engine))

Base = declarative_base()