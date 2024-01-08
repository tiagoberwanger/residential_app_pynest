from nest.core import Controller, Get, Post, Delete, Depends

from .users_service import UsersService
from .users_model import UsersPostSchema


@Controller("users")
class UsersController:

    service: UsersService = Depends(UsersService)
    
    @Get("/")
    def get_users(self):
        return self.service.get_users()
                
    @Post("/")
    def add_users(self, users: UsersPostSchema):
        return self.service.add_users(users)
    
    @Delete("/")
    def delete_user(self, user_id: int):
        return self.service.delete_user(user_id)