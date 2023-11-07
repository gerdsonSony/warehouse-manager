from warehouse_manager.models.database.customer import Customer
from warehouse_manager.models.database.mixins.session_mixin import SessionMixin
from warehouse_manager.models.database.warehouse import Warehouse
from warehouse_manager.sessions.database import mysql_session

__all__ = [
    "Customer",
    "Warehouse",
]

SessionMixin.set_session(mysql_session)
