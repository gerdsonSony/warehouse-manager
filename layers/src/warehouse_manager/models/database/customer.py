from sqlalchemy import Double, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from warehouse_manager.models.database.mixins.base_mixin import BaseMixin


class Customer(BaseMixin):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    latitude: Mapped[float] = mapped_column(Double, nullable=False)
    longitude: Mapped[float] = mapped_column(Double, nullable=False)

    def __repr__(self) -> str:
        return f"<Customer (id={self.id!r}, name={self.name!r})>"
