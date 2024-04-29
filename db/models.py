from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # Assuming role can be either 'User' or 'Admin'


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    owner = Column(Integer, ForeignKey('users.id'), nullable=False)
    date_of_purchase = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)
    active = Column(Boolean, default=True)
    description = Column(String)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    serial_no = Column(String, unique=True, nullable=False)
    qr_code = Column(String, unique=True)
    image = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", back_populates="devices")


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    time_start = Column(DateTime, nullable=False)
    time_end = Column(DateTime, nullable=False)
    active = Column(Boolean, default=True)
    price = Column(Float, nullable=False)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    device = relationship("Device", back_populates="bookings")
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="bookings")
    rent_charge = Column(String, nullable=False)


class Locker(Base):
    __tablename__ = 'lockers'

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    campus = Column(String, nullable=False)
    room = Column(String, nullable=False)
    size = Column(String, nullable=False)  # Assuming size can be 'S', 'M', or 'L'
    rent_charge = Column(String, nullable=False)


class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    description = Column(String)
    image = Column(String)


# Define relationships
User.bookings = relationship("Booking", back_populates="user")
Device.bookings = relationship("Booking", back_populates="device")
Category.devices = relationship("Device", back_populates="category")
