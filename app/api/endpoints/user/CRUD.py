import logging

from sqlalchemy.orm import Session

from app.api.endpoints.user.schemas import UserCreateSchema
from db.models import User
from fastapi import HTTPException


def create_user(schema: UserCreateSchema, db: Session):
    entity = User(**schema.dict())
    logging.info('User created with id {}'.format(entity.id))
    db.add(entity)
    db.commit()
    return entity


def get_all_users(db: Session):
    return db.query(User).all()


def login_is_valid(email: str, password: str, db: Session):
    entity = db.query(User).filter(User.email == email).first()
    if entity:
        return entity
    else:
        return HTTPException(status_code=404, detail='User not found')