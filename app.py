from config import config
from nest.core.app import App
from src.contracts.contracts_module import ContractsModule
from src.rooms.rooms_module import RoomsModule
from src.users.users_module import UsersModule

app = App(
    description="PyNest service", modules=[ContractsModule, RoomsModule, UsersModule]
)


@app.on_event("startup")
def startup():
    config.create_all()
