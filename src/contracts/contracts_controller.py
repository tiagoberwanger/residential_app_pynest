from nest.core import Controller, Get, Post, Delete, Depends

from .contracts_service import ContractsService
from .contracts_model import ContractPostSchema


@Controller("contracts")
class ContractsController:

    service: ContractsService = Depends(ContractsService)
    
    @Get("/")
    def get_contracts(self):
        return self.service.get_contracts()
                
    @Post("/")
    def add_contract(self, contract: ContractPostSchema):
        return self.service.add_contract(contract)
 
    @Delete("/")
    def delete_contract(self, contracts_id: int):
        return self.service.delete_contract(contracts_id)