from .rooms_service import RoomsService
from .rooms_controller import RoomsController


class RoomsModule:

    def __init__(self):
        self.providers = [RoomsService]
        self.controllers = [RoomsController]
