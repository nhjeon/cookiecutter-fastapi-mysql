import logging

from fastapi import FastAPI

from api import api_router

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = FastAPI()
app.include_router(api_router)
