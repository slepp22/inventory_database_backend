import random

from fastapi import APIRouter

from app.api.endpoints.booking.router import router as booking_router
from app.api.endpoints.category.router import router as category_router
from app.api.endpoints.device.router import router as device_router
from app.api.endpoints.report.router import router as report_router
from app.api.endpoints.user.router import router as user_router
from app.api.endpoints.db_migration.router import router as db_migration_router

router = APIRouter()

@router.get("/")
async def read_root():
    return "The Backend is alive"

@router.get("/pin")
async def generate_pin():
    pin = random.randint(1000, 9999)
    return {"pin": pin}


router.include_router(booking_router, tags=["booking"])
router.include_router(category_router, tags=["category"])
router.include_router(device_router, tags=["device"])
router.include_router(report_router, tags=["report"])
router.include_router(user_router, tags=["user"])
router.include_router(db_migration_router, tags=["db_migration"])
