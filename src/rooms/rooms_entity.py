from config import config
from sqlalchemy import Column, Enum, Integer, String, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.sql import func

from src.utils.enums import RoomEnum


class Rooms(config.Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    room_type = Column(Enum(RoomEnum), nullable=False)
    room_number = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True, nullable=False)
    description = Column(String, nullable=True)
    value = Column(DECIMAL(precision=10, scale=2), nullable=True)
    address = Column(String, nullable=True)
    last_updated = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())

