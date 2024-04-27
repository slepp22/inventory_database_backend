import random

from fastapi import APIRouter
from app.api.endpoints import user

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@router.get("/pin")
async def generate_pin():
    pin = random.randint(1000, 9999)
    return {pin}

router.include_router(user.router, tags=["users"])
