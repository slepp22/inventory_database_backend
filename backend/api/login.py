from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.services.login_service import authenticate
from backend.db.session import get_db

router = APIRouter()


@router.post("/login", summary="Login a user")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    authenticated = await authenticate(db, username, password)
    if authenticated:
        return {True}
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
