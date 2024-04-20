from sqlalchemy import Column, Integer, String
from backend.db import Base

from . import hasing

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255))


    def __init__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = hasing.get_password_hash(self.password)

    def check_password(self, password):
        return hasing.verify_password(self.password, password)
