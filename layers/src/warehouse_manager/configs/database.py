from os import getenv
from typing import TypedDict


class DBParamsType(TypedDict):
    HOST: str
    PORT: int
    DATABASE: str
    USERNAME: str
    PASSWORD: str


DATABASE_PARAMS: DBParamsType = {
    "HOST": getenv("DATABASE_HOST", "localhost"),
    "PORT": int(getenv("DATABASE_PORT", 4306)),
    "DATABASE": getenv("DATABASE_DATABASE", "warehouse_manager"),
    "USERNAME": getenv("DATABASE_USERNAME", "root"),
    "PASSWORD": getenv("DATABASE_PASSWORD", "password"),
}
