from datetime import date, datetime
from pydantic import BaseModel, Field


class UsersPostSchema(BaseModel):
    name: str = Field(default='Tiago da Silva')
    cpf: str = Field(default='01234567891234')
    birth_date: date | None = Field(default='1990-01-01')
    city: str | None = Field(default='Itapiranga')
    state: str | None = Field(default='SC')
    email: str | None

    class ConfigDict:
        from_attributes = True


class UsersSchema(UsersPostSchema):
    id: int
    last_updated: datetime
