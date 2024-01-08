from decimal import Decimal
from datetime import date, datetime
from pydantic import BaseModel, Field, validator

from src.rooms.rooms_service import RoomsService
from src.users.users_service import UsersService
from src.utils.enums import StatusEnum


class ContractPostSchema(BaseModel):
    user_id: int
    room_id: int
    start_date: date = Field(default='2023-01-01')
    end_date: date = Field(default='2024-01-01')
    rent_value: Decimal = Field(default=Decimal(500))
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)

    @validator('user_id')
    def validate_user(cls, user_id: int):
        user = UsersService().get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        return user_id

    @validator('room_id')
    def validate_room(cls, room_id: int):
        room = RoomsService().get_room_by_id(room_id)
        if not room:
            raise ValueError(f"Room {room_id} not found")
        return room_id

    class ConfigDict:
        from_attributes = True


class ContractSchema(ContractPostSchema):
    id: int
    last_updated: datetime
