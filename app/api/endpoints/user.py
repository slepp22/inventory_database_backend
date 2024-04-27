from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.config import SessionLocal
from app.models import user as user_model

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
