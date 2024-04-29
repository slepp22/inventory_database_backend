from pydantic import BaseModel


class TriggerRequestSchema(BaseModel):
    key: str
