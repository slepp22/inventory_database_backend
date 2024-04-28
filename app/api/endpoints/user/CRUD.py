import logging

from sqlalchemy.orm import Session

from app.api.endpoints.user.schemas import UserCreateSchema
from db.models import User


def create_user(schema: UserCreateSchema, db: Session):
    entity = User(**schema.dict())
    logging.info('User created with id {}'.format(entity.id))
    db.add(entity)
    db.commit()
    return entity


def get_all_users(db: Session):
    return db.query(User).all()


def login_is_valid(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email, User.password == password).first()
    return user is not None
