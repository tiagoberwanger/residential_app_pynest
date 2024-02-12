from .rooms_model import RoomPostSchema, RoomPutSchema
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
    def add_room(self, room: RoomPostSchema):
        new_room = RoomsEntity(
            **room.dict()
        )
        self.session.add(new_room)
        self.session.commit()
        return f'Room with id {new_room.id} created'

    @db_request_handler
    def get_rooms(self):
        return self.session.query(RoomsEntity).all()

    @db_request_handler
    def get_room_by_id(self, room_id: int):
        return self.session.query(RoomsEntity).filter(RoomsEntity.id == room_id).first()

    @db_request_handler
    def update_room(self, room_id: int, room: RoomPutSchema):
        actual_room = self.session.query(RoomsEntity).filter(RoomsEntity.id == room_id)
        if not actual_room.first():
            return f'Room with id {room_id} not found'
        actual_room.update(room.dict())
        self.session.commit()
        return f'Room with id {room_id} updated'

    @db_request_handler
    def delete_room(self, room_id: int):
        room = self.session.query(RoomsEntity).filter(RoomsEntity.id == room_id).first()
        if not room:
            return f'Room with id {room_id} not found'
        self.session.query(RoomsEntity).filter(RoomsEntity.id == room_id).delete()
        self.session.commit()
        return f'Room with id {room_id} deleted'
    