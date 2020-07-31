import logging

from fastapi import FastAPI

from api import api_router

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = FastAPI()
app.include_router(api_router)

FORMAT = '[%(asctime)s] [%(threadName)s(%(thread)d) [%(filename)s-%(lineno)d] [%(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
