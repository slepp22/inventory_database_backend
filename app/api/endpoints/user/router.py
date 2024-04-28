from typing import List

from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

import app.api.endpoints.user.CRUD as user_crud
from app.api.endpoints.user.schemas import UserSchema, UserCreateSchema
from db.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/users', response_model=List[UserSchema], tags=['user'])
def get_all_users(db: Session = Depends(get_db)):
    users = user_crud.get_all_users(db)
    return users


@router.post('/loginIsValid', response_model=bool, tags=['user'])
def login_is_valid(email: str, password: str, db: Session = Depends(get_db)):
    return user_crud.login_is_valid(email, password, db)
