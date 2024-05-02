import logging

from sqlalchemy import not_
from sqlalchemy.orm import Session

from app.api.endpoints.device.schemas import DeviceCreateSchema
from db.models import Device, Booking


def create_device(schema: DeviceCreateSchema, db: Session):
    entity = Device(**schema.dict())
    logging.info('Device created with id {}'.format(entity.id))
    db.add(entity)
    db.commit()
    return entity


def get_device_by_id(device_id: int, db: Session):
    entity = db.query(Device).filter(Device.id == device_id).first()
    return entity


def get_all_devices(db: Session):
    return db.query(Device).all()


def update_device(device_id: int, changed_device: DeviceCreateSchema, db: Session):
    device = get_device_by_id(device_id, db)
    if device:
        for key, value in changed_device.dict().items():
            setattr(device, key, value)
        logging.info('Device updated with id {}'.format(device.id))
        db.commit()
        db.refresh(device)
        return device
    else:
        return None


def delete_device_by_id(device_id: int, db: Session):
    device = get_device_by_id(device_id, db)
    if device:
        db.delete(device)
        db.commit()


def get_devices_by_category(category_id: int, db: Session):
    return db.query(Device).filter(Device.category_id == category_id).all()


def get_devices_not_in_use(db):
    return db.query(Device).outerjoin(Booking, Device.id == Booking.device_id).filter(Booking.active).all()