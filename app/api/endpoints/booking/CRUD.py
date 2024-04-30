import logging

from sqlalchemy.orm import Session

from app.api.endpoints.booking.schemas import BookingCreateSchema
from db.models import Booking


def create_booking(schema: BookingCreateSchema, db: Session):
    entity = Booking(**schema.dict())
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
