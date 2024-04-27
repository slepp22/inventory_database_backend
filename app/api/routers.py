import random

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@router.get("/pin")
async def generate_pin():
    pin = random.randint(1000, 9999)
    return {pin}