from .rooms_model import RoomPostSchema
from .rooms_entity import Rooms as RoomsEntity
from config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class RoomsService:

    def __init__(self):
        self.config = config
        self.session = self.config.get_db()
    
    @db_request_handler
    def add_rooms(self, rooms: RoomPostSchema):
        new_rooms = RoomsEntity(
            **rooms.dict()
        )
        self.session.add(new_rooms)
        self.session.commit()
        return f'Room with id {new_rooms.id} created'

    @db_request_handler
    def get_rooms(self):
        return self.session.query(RoomsEntity).all()

    @db_request_handler
    def delete_room(self, room_id: int):
        room = self.session.query(RoomsEntity).filter(RoomsEntity.id == room_id).first()
        if not room:
            return f'Room with id {room_id} not found'
        self.session.query(RoomsEntity).filter(RoomsEntity.id == room_id).delete()
        self.session.commit()
        return f'Room with id {room_id} deleted'
    