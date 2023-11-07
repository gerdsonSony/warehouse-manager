from typing import Any

from aws_lambda_powertools.utilities.typing import LambdaContext

from warehouse_manager.services.authentication import verify_token


def lambda_handler(event: Any, context: LambdaContext) -> dict[str, Any]:
    effect = "Deny"
    token = event["authorizationToken"]

    if verify_token(token):
        effect = "Allow"

    return {
        "principalId": token,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [{"Effect": effect, "Action": "execute-api:Invoke", "Resource": event["methodArn"]}],
        },
    }
