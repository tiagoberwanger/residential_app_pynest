from nest.core import Controller, Get, Post, Delete, Depends

from .rooms_service import RoomsService
from .rooms_model import RoomPostSchema


@Controller("rooms")
class RoomsController:

    service: RoomsService = Depends(RoomsService)
    
    @Get("/")
    def get_rooms(self):
        return self.service.get_rooms()
                
    @Post("/")
    def add_room(self, room: RoomPostSchema):
        return self.service.add_room(room)
 
    @Delete("/")
    def delete_room(self, room_id: int):
        return self.service.delete_room(room_id)