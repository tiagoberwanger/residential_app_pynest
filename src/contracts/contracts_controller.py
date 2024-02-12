from nest.core import Controller, Get, Post, Delete, Put, Depends

from .contracts_service import ContractsService
from .contracts_model import ContractPostSchema, ContractPutSchema


@Controller("contracts")
class ContractsController:

    service: ContractsService = Depends(ContractsService)
    
    @Get("/")
    def get_contracts(self):
        return self.service.get_contracts()
                
    @Post("/")
    def add_contract(self, contract: ContractPostSchema):
        return self.service.add_contract(contract)

    @Put("/")
    def update_contract(self, contract_id: int, contract: ContractPutSchema):
        return self.service.update_contract(contract_id, contract)
 
    @Delete("/")
    def delete_contract(self, contract_id: int):
        return self.service.delete_contract(contract_id)
