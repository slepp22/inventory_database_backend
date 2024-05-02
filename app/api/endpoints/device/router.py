from typing import List

from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

import app.api.endpoints.device.CRUD as device_crud
from app.api.endpoints.device.schemas import DeviceSchema, DeviceCreateSchema
from db.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/devices', response_model=List[DeviceSchema], tags=['device'])
def get_all_devices(db: Session = Depends(get_db)):
    devices = device_crud.get_all_devices(db)
    return devices


@router.post('/devices', response_model=DeviceSchema, status_code=status.HTTP_201_CREATED, tags=['device'])
def create_device(device: DeviceCreateSchema,
                  db: Session = Depends(get_db)):
    new_device = device_crud.create_device(device, db)
    return new_device


@router.put('/devices/{device_id}', response_model=DeviceSchema, tags=['device'])
def update_device(
        device_id: int,
        changed_device: DeviceCreateSchema,
        db: Session = Depends(get_db),
):
    updated_device = device_crud.update_device(device_id, changed_device, db)
    if updated_device:
        return updated_device
    else:
        raise HTTPException(status_code=404)


@router.get('/devices/unused', response_model=List[DeviceSchema], tags=['device'])
def get_devices_not_in_use(
        db: Session = Depends(get_db),
):
    devices = device_crud.get_devices_not_in_use(db)
    return devices


@router.get('/devices/{device_id}', response_model=DeviceSchema, tags=['device'])
def get_device(
        device_id: int,
        db: Session = Depends(get_db),
):
    device = device_crud.get_device_by_id(device_id, db)
    if not device:
        raise HTTPException(status_code=404)
    return device


@router.delete('/devices/{device_id}', response_model=None, tags=['device'])
def delete_device(
        device_id: int,
        db: Session = Depends(get_db)):
    device_crud.delete_device_by_id(device_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get('/devices/by_category/{category_id}', response_model=List[DeviceSchema], tags=['device'])
def get_devices_by_category(
        category_id: int,
        db: Session = Depends(get_db),
):
    devices = device_crud.get_devices_by_category(category_id, db)
    return devices
