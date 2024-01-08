from .users_service import UsersService
from .users_controller import UsersController


class UsersModule:

    def __init__(self):
        self.providers = [UsersService]
        self.controllers = [UsersController]
