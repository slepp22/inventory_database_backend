from typing import List

from fastapi import APIRouter, Depends, Request, Response, status, HTTPException
from sqlalchemy.orm import Session

import app.api.endpoints.db_migration.CRUD as db_migration_crud
from app.api.endpoints.db_migration.schemas import TriggerRequestSchema
from db.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()

DB_KEY = "1337"


@router.post("/trigger-db-migration")
async def trigger_db_migration(request: TriggerRequestSchema):
    return db_migration_crud.trigger_db_migration(request)
