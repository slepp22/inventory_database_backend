from pydantic import BaseModel


class DeviceBaseSchema(BaseModel):
    owner: int
    date_of_purchase: str
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
