from fastapi import FastAPI

import db.config
from db.config import SessionLocal
from app.api import routers

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(routers.router)





