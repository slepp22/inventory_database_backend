from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import app.api.endpoints.booking.CRUD as booking_crud
from app.api.endpoints.booking.schemas import BookingSchema, BookingCreateSchema, BookingUpdateSchema
from db.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/bookings', response_model=List[BookingSchema], tags=['booking'])
def get_all_bookings(db: Session = Depends(get_db)):
    bookings = booking_crud.get_all_bookings(db)
    return bookings


@router.get('/bookings/newest/', response_model=BookingSchema, tags=['booking'])
def get_newest_booking(db: Session = Depends(get_db)):
    newest_booking = booking_crud.get_newest_booking(db)
    if not newest_booking:
        return {"message": "No bookings found"}
    return newest_booking


@router.get('/bookings/{booking_id}', response_model=BookingSchema, tags=['booking'])
def get_booking_by_id(booking_id: int, db: Session = Depends(get_db)):
    booking = booking_crud.get_booking_by_id(booking_id, db)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


@router.get('/bookings/allbyUserID/{user_id}', response_model=List[BookingSchema], tags=['booking'])
def get_all_bookings_by_user_id(user_id: int, db: Session = Depends(get_db)):
    bookings = booking_crud.get_all_bookings_by_user_id(user_id, db)
    return bookings


@router.post('/bookings', response_model=BookingSchema, status_code=201, tags=['booking'])
def create_booking(booking: BookingCreateSchema, db: Session = Depends(get_db)):
    new_booking = booking_crud.create_booking(booking, db)
    return new_booking


@router.delete('/bookings/{booking_id}', response_model=None, tags=['booking'])
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking_crud.delete_booking(booking_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/bookings/{booking_id}', response_model=BookingSchema, tags=['booking'])
def update_booking(
        booking_id: int,
        updated_booking: BookingUpdateSchema,
        db: Session = Depends(get_db)
):
    booking = booking_crud.get_booking_by_id(booking_id, db)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    updated_booking_data = updated_booking.dict(exclude_unset=True)
    booking = booking_crud.update_booking(booking, updated_booking_data, db)
    return booking
