from config import config
from sqlalchemy import Column, ForeignKey, Integer, Date, Enum, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.utils.enums import StatusEnum


class Contracts(config.Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    rent_value = Column(DECIMAL(precision=10, scale=2), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)
    last_updated = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    user = relationship('Users', backref='contracts')
    room = relationship('Rooms', backref='contracts')
