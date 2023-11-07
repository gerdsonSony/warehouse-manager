from typing import Optional, cast

from warehouse_manager.models.database.customer import Customer


def create_customer(name: str, latitude: float, longitude: float) -> Customer:
    return cast(Customer, Customer.create(name=name, latitude=latitude, longitude=longitude))


def retrieve_customer(customer_id: int) -> Customer:
    return cast(Customer, Customer.find_or_fail(customer_id))


def get_all_customers() -> list[Customer]:
    return cast(list[Customer], Customer.all())


def update_customer(
    customer_id: int, name: Optional[str] = None, latitude: Optional[float] = None, longitude: Optional[float] = None
) -> Customer:
    customer = Customer.find_or_fail(customer_id)
    if name:
        customer.name = name
    if latitude:
        customer.latitude = latitude
    if longitude:
        customer.longitude = longitude

    return cast(Customer, customer.save())
