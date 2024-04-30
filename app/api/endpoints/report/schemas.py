from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReportBaseSchema(BaseModel):
    date: datetime
    description: str
    image: Optional[str]
    booking_id: int


class ReportCreateSchema(ReportBaseSchema):
    pass


class ReportSchema(ReportBaseSchema):
    id: int

    class Config:
        orm_mode = True
