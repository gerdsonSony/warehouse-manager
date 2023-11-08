import json
from typing import Any

from aws_lambda_powertools.event_handler.exceptions import NotFoundError
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from warehouse_manager.exceptions.database import ModelNotFoundError
from warehouse_manager.serializers.warehouse import WarehouseSerializer
from warehouse_manager.services.customer import retrieve_customer
from warehouse_manager.services.google_maps import get_location_distance
from warehouse_manager.services.warehouse import create_warehouse as create_warehouse_service
from warehouse_manager.services.warehouse import get_all_warehouses, retrieve_warehouse
from warehouse_manager.utils.aws import app_resolver, logger, tracer


@app_resolver.get("/warehouses")
@tracer.capture_method
def get_warehouses() -> Any:
    warehouses = get_all_warehouses()
    serializer = WarehouseSerializer()

    result = {"warehouses": list(map(lambda c: json.loads(serializer.dumps(c)), warehouses))}

    return result


@app_resolver.get("/warehouses/<warehouse_id>")
@tracer.capture_method
def get_warehouse_by_id(warehouse_id: int) -> Any:
    serializer = WarehouseSerializer()

    try:
        warehouse = retrieve_warehouse(warehouse_id)
    except ModelNotFoundError:
        raise NotFoundError("Warehouse not found")

    result = {"warehouse": json.loads(serializer.dumps(warehouse))}

    return result


@app_resolver.post("/warehouses")
@tracer.capture_method
def create_warehouse() -> Any:
    data = app_resolver.current_event.json_body
    warehouse = create_warehouse_service(name=str(data["name"]), latitude=data["latitude"], longitude=data["longitude"])
    serializer = WarehouseSerializer()

    result = {"warehouse": json.loads(serializer.dumps(warehouse))}

    return result


@app_resolver.get("/warehouses/<warehouse_id>/distance/<customer_id>")
@tracer.capture_method
def get_distance_between_warehouse_and_customer(warehouse_id: int, customer_id: int) -> Any:
    WarehouseSerializer()

    try:
        warehouse = retrieve_warehouse(warehouse_id)
    except ModelNotFoundError:
        raise NotFoundError("Warehouse not found")

    try:
        customer = retrieve_customer(customer_id)
    except ModelNotFoundError:
        raise NotFoundError("Customer not found")

    result = {
        "warehouse_id": warehouse.id,
        "customer_id": customer.id,
        "distance_data": get_location_distance(warehouse, customer),
    }

    return result


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> Any:
    return app_resolver.resolve(event, context)
