from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.config import SessionLocal
from app.models import user as user_model
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users", response_model=List[user_model.User])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(user_model.User).all()
    return users
