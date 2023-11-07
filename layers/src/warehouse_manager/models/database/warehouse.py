from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from warehouse_manager.models.database.mixins.base_mixin import BaseMixin


class Warehouse(BaseMixin):
    __tablename__ = "warehouses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    latitude: Mapped[int]
    longitude: Mapped[int]

    def __repr__(self) -> str:
        return f"<Warehouse (id={self.id!r}, name={self.name!r})>"
