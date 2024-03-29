from nest.core import Controller, Get, Post, Put, Delete, Depends

from .users_service import UsersService
from .users_model import UsersPostSchema, UsersPutSchema


@Controller("users")
class UsersController:

    service: UsersService = Depends(UsersService)
    
    @Get("/")
    def get_users(self):
        return self.service.get_users()

    @Get("/{user_id}")
    def get_user_by_id(self, user_id: int):
        return self.service.get_user_by_id(user_id)

    @Post("/")
    def add_user(self, user: UsersPostSchema):
        return self.service.add_user(user)

    @Put("/{user_id}")
    def update_user(self, user_id: int, user: UsersPutSchema):
        return self.service.update_user(user_id, user)
    
    @Delete("/")
    def delete_user(self, user_id: int):
        return self.service.delete_user(user_id)
