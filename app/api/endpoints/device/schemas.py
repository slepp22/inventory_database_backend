from datetime import datetime

from pydantic import BaseModel, Field


class DeviceBaseSchema(BaseModel):
    owner: int
    date_of_purchase: datetime = Field(..., format="%Y-%m-%d %H-%M-%S")
    price: float
    active: bool
    description: str
    brand: str
    model: str
    serial_no: str
    qr_code: str
    category_id: int


class DeviceCreateSchema(DeviceBaseSchema):
    pass


class DeviceSchema(DeviceBaseSchema):
    id: int
