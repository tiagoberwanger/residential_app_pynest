from config import config

from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func


class Users(config.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    birth_date = Column(Date, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    email = Column(String, nullable=True)
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
