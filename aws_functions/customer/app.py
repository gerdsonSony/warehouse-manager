from typing import Any

from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from warehouse_manager.utils.aws import app_resolver, logger, tracer


@app_resolver.get("/customers")
@tracer.capture_method
def get_customers() -> Any:
    response = {
        "customers": [
            {"id": 1, "name": "Gerd"},
            {"id": 2, "name": "Greg"},
            {"id": 3, "name": "Tim"},
            {"id": 4, "name": "Jessica"},
        ]
    }

    return response


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> Any:
    return app_resolver.resolve(event, context)
