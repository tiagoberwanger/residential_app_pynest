from .contracts_model import ContractPostSchema, ContractPutSchema
from .contracts_entity import Contracts as ContractsEntity
from config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class ContractsService:

    def __init__(self):
        self.config = config
        self.session = self.config.get_db()
    
    @db_request_handler
    def add_contract(self, contract: ContractPostSchema):
        new_contract = ContractsEntity(
            **contract.dict()
        )
        self.session.add(new_contract)
        self.session.commit()
        return f'Contract with id {new_contract.id} added'

    @db_request_handler
    def get_contracts(self):
        return self.session.query(ContractsEntity).all()

    @db_request_handler
    def update_contract(self, contract_id: int, contract: ContractPutSchema):
        actual_contract = self.session.query(ContractsEntity).filter(ContractsEntity.id == contract_id)
        if not actual_contract.first():
            return f'Contract with id {contract_id} not found'
        actual_contract.update(contract.dict())
        self.session.commit()
        return f'Contract with id {contract_id} updated'

    @db_request_handler
    def delete_contract(self, contract_id: int):
        contract = self.session.query(ContractsEntity).filter(ContractsEntity.id == contract_id).first()
        if not contract:
            return f'Contract with id {contract_id} not found'
        self.session.query(ContractsEntity).filter(ContractsEntity.id == contract_id).delete()
        self.session.commit()
        return f'Contract with id {contract_id} deleted'
    