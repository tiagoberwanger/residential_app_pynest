from .contracts_service import ContractsService
from .contracts_controller import ContractsController


class ContractsModule:

    def __init__(self):
        self.providers = [ContractsService]
        self.controllers = [ContractsController]
