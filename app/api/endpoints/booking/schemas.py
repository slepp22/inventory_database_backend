from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BookingBaseSchema(BaseModel):
    time_start: datetime
    time_end: datetime
    active: bool
    price: float
    device_id: int
    user_id: int
    rent_charge: str


class BookingCreateSchema(BookingBaseSchema):
    pass


class BookingSchema(BookingBaseSchema):
    id: int

    class Config:
        orm_mode = True
