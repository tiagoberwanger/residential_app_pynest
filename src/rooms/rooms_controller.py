from nest.core import Controller, Get, Post, Put, Delete, Depends

from .rooms_service import RoomsService
from .rooms_model import RoomPostSchema


@Controller("rooms")
class RoomsController:

    service: RoomsService = Depends(RoomsService)
    
    @Get("/")
    def get_rooms(self):
        return self.service.get_rooms()

    @Get("/{room_id}")
    def get_room_by_id(self, room_id: int):
        return self.service.get_room_by_id(room_id)

    @Post("/")
    def add_room(self, room: RoomPostSchema):
        return self.service.add_room(room)

    @Put("/{room_id}")
    def update_room(self, room_id: int, room: RoomPostSchema):
        return self.service.update_room(room_id, room)
 
    @Delete("/")
    def delete_room(self, room_id: int):
        return self.service.delete_room(room_id)