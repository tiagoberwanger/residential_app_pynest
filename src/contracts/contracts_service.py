from .contracts_model import ContractPostSchema
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
    def add_contracts(self, contracts: ContractPostSchema):
        new_contracts = ContractsEntity(
            **contracts.dict()
        )
        self.session.add(new_contracts)
        self.session.commit()
        return f'Contract with id {new_contracts.id} added'

    @db_request_handler
    def get_contracts(self):
        return self.session.query(ContractsEntity).all()

    @db_request_handler
    def delete_contract(self, contract_id: int):
        contract = self.session.query(ContractsEntity).filter(ContractsEntity.id == contract_id).first()
        if not contract:
            return f'Contract with id {contract_id} not found'
        self.session.query(ContractsEntity).filter(ContractsEntity.id == contract_id).delete()
        self.session.commit()
        return f'Contract with id {contract_id} deleted'
    