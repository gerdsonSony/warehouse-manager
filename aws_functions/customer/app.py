import json
from typing import Any

from aws_lambda_powertools.event_handler.exceptions import NotFoundError
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from warehouse_manager.exceptions.database import ModelNotFoundError
from warehouse_manager.serializers.customer import CustomerSerializer
from warehouse_manager.services.customer import create_customer as create_customer_service
from warehouse_manager.services.customer import get_all_customers, retrieve_customer
from warehouse_manager.utils.aws import app_resolver, logger, tracer


@app_resolver.get("/customers")
@tracer.capture_method
def get_customers() -> Any:
    customers = get_all_customers()
    serializer = CustomerSerializer()

    result = {"customers": list(map(lambda c: json.loads(serializer.dumps(c)), customers))}

    return result


@app_resolver.get("/customers/<customer_id>")
@tracer.capture_method
def get_customer_by_id(customer_id: int) -> Any:
    serializer = CustomerSerializer()

    try:
        customer = retrieve_customer(customer_id)
    except ModelNotFoundError:
        raise NotFoundError("Customer not found")

    result = {"customer": json.loads(serializer.dumps(customer))}

    return result


@app_resolver.post("/customers")
@tracer.capture_method
def create_customer() -> Any:
    data = app_resolver.current_event.json_body
    customer = create_customer_service(name=str(data["name"]), latitude=data["latitude"], longitude=data["longitude"])
    serializer = CustomerSerializer()

    result = {"customer": json.loads(serializer.dumps(customer))}

    return result


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> Any:
    return app_resolver.resolve(event, context)
