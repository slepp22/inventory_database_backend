import logging
import random
from datetime import datetime

from sqlalchemy.orm import Session

from app.api.endpoints.booking.schemas import BookingCreateSchema
from db.models import Booking


def create_booking(schema: BookingCreateSchema, db: Session):
    entity = Booking(**schema.dict())
    entity.pin = random.randint(1000, 9999)
    logging.info('Booking created with id {}'.format(entity.id))
    db.add(entity)
    db.commit()
    return entity


def get_booking_by_id(booking_id: int, db: Session):
    entity = db.query(Booking).filter(Booking.id == booking_id).first()
    return entity


def get_all_bookings(db: Session):
    return db.query(Booking).all()


def get_all_bookings_by_user_id(user_id: int, db: Session):
    return db.query(Booking).filter(Booking.user_id == user_id).all()


def delete_booking(booking_id: int, db: Session):
    booking = get_booking_by_id(booking_id, db)
    if booking:
        db.delete(booking)
        db.commit()
        return None
    else:
        return None


def get_newest_booking(db):
    return db.query(Booking).order_by(Booking.id.desc()).first()


def update_booking(booking, updated_booking_data, db):
    if 'active' in updated_booking_data and not updated_booking_data['active'] and booking.active:
        booking.time_end = datetime.now()
        duration_hours = (booking.time_end - booking.time_start).total_seconds() / 3600
        booking.booking_price = round(duration_hours * booking.device.rent_price_per_hour, 2)

    for field, value in updated_booking_data.items():
        if field not in ['active', 'time_end', 'booking_price']:
            setattr(booking, field, value)

    if 'active' in updated_booking_data:
        setattr(booking, 'active', updated_booking_data['active'])

    db.commit()
    db.refresh(booking)
    return booking
