from sqlalchemy import Column, Integer, String
from backend.db.session import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)

    def __init__(self, id=None, username=None, password=None, role=None):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
