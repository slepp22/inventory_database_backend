from sqlalchemy.orm import Session
from backend.db.models import User


async def authenticate(db: Session, username: str, password: str) -> bool:
    user = db.query(User).filter(User.username == username).first()
    if user:
        if user.password == password:
            return True
    return False
