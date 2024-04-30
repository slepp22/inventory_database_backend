import random

from fastapi import APIRouter, HTTPException

from app.api.endpoints.booking.router import router as booking_router
from app.api.endpoints.category.router import router as category_router
from app.api.endpoints.device.router import router as device_router
from app.api.endpoints.report.router import router as report_router
from app.api.endpoints.user.router import router as user_router
from app.api.endpoints.db_migration.router import router as db_migration_router

from db.config import check_database_connection, get_database_url

router = APIRouter()

@router.get("/")
async def read_root():
    return "The Backend is alive"

@router.get("/pin")
async def generate_pin():
    pin = random.randint(1000, 9999)
    return {"pin": pin}

@router.get("/database/status")
def get_database_status():
    if check_database_connection():
        return {"status": "Database connection successful"}
    else:
        raise HTTPException(status_code=503, detail="Unable to connect to the database")


@router.get("/environment")
def get_environment_variables():
    return get_database_url()


router.include_router(booking_router, tags=["booking"])
router.include_router(category_router, tags=["category"])
router.include_router(device_router, tags=["device"])
router.include_router(report_router, tags=["report"])
router.include_router(user_router, tags=["user"])
router.include_router(db_migration_router, tags=["db_migration"])
