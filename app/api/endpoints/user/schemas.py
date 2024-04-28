from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    email: str
    name: str
    role: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
