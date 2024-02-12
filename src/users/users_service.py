from .users_model import UsersPostSchema, UsersPutSchema
from .users_entity import Users as UsersEntity
from config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class UsersService:

    def __init__(self):
        self.config = config
        self.session = self.config.get_db()
    
    @db_request_handler
    def add_user(self, user: UsersPostSchema):
        new_user = UsersEntity(
            **user.dict()
        )
        self.session.add(new_user)
        self.session.commit()
        return f'User with id {new_user.id} created'

    @db_request_handler
    def get_users(self):
        return self.session.query(UsersEntity).all()

    @db_request_handler
    def get_user_by_id(self, user_id: int):
        return self.session.query(UsersEntity).filter(UsersEntity.id == user_id).first()

    @db_request_handler
    def update_user(self, user_id: int, user: UsersPutSchema):
        users = self.session.query(UsersEntity).filter(UsersEntity.id == user_id)
        if not users.first():
            return f'User with id {user_id} not found'
        users.update(user.dict())
        self.session.commit()
        return f'User {user_id} updated'

    @db_request_handler
    def delete_user(self, user_id: int):
        users = self.session.query(UsersEntity).filter(UsersEntity.id == user_id).first()
        if not users:
            return f'User with id {user_id} not found'
        self.session.query(UsersEntity).filter(UsersEntity.id == user_id).delete()
        self.session.commit()
        return f'User {user_id} deleted'
