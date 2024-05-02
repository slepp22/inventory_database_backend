from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ReportBaseSchema(BaseModel):
    date: datetime = Field(..., format="%Y-%m-%d %H-%M-%S")
    description: str
    image: Optional[str]
    booking_id: int


class ReportCreateSchema(ReportBaseSchema):
    pass


class ReportSchema(ReportBaseSchema):
    id: int

    class Config:
        orm_mode = True
