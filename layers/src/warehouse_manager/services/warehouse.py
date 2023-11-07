from typing import Optional, cast

from warehouse_manager.models.database.warehouse import Warehouse


def create_warehouse(name: str, latitude: float, longitude: float) -> Warehouse:
    return cast(Warehouse, Warehouse.create(name=name, latitude=latitude, longitude=longitude))


def retrieve_warehouse(warehouse_id: int) -> Warehouse:
    return cast(Warehouse, Warehouse.find_or_fail(warehouse_id))


def get_all_warehouses() -> list[Warehouse]:
    return cast(list[Warehouse], Warehouse.all())


def update_warehouse(
    warehouse_id: int, name: Optional[str] = None, latitude: Optional[float] = None, longitude: Optional[float] = None
) -> Warehouse:
    warehouse = Warehouse.find_or_fail(warehouse_id)
    if name:
        warehouse.name = name
    if latitude:
        warehouse.latitude = latitude
    if longitude:
        warehouse.longitude = longitude

    return cast(Warehouse, warehouse.save())
