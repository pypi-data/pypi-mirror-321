"""Event handler package for AWS Lambda functions.

Provides utilities for handling various AWS Lambda event sources.
"""

from chainsaws.aws.lambda_client.event_handler.api_gateway import (
    APIGatewayRestResolver,
    APIGatewayHttpResolver,
    HttpMethod,
    Route,
    BaseResolver,
)
from chainsaws.aws.lambda_client.event_handler.handler_models import (
    LambdaEvent,
    LambdaResponse,
    HandlerConfig,
)
from chainsaws.aws.lambda_client.event_handler.event_handler import aws_lambda_handler

__all__ = [
    "aws_lambda_handler",
    "APIGatewayRestResolver",
    "APIGatewayHttpResolver",
    "HttpMethod",
    "Route",
    "BaseResolver",
    "LambdaEvent",
    "LambdaResponse",
    "HandlerConfig",
]
