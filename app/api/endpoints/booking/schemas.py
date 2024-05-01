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
    pin: int


class BookingCreateSchema(BookingBaseSchema):
    pass


class BookingSchema(BookingBaseSchema):
    id: int
    pin: int

    class Config:
        orm_mode = True


class BookingUpdateSchema(BaseModel):
    time_start: Optional[datetime]
    time_end: Optional[datetime]
    active: Optional[bool]
    price: Optional[float]
    device_id: Optional[int]
    user_id: Optional[int]
    rent_charge: Optional[str]
    pin: Optional[int]
