from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver

tracer = Tracer()
logger = Logger()
app_resolver = APIGatewayRestResolver()
