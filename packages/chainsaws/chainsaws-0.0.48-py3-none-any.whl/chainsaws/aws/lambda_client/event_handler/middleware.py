"""Middleware system for API Gateway resolvers.

Provides a way to add middleware functions that run before and after request handling.
"""

from typing import Any, Callable, TypeVar, Generic
from functools import wraps

from chainsaws.aws.lambda_client.types.events.api_gateway_proxy import (
    APIGatewayProxyV1Event,
    APIGatewayProxyV2Event,
)

T = TypeVar("T", APIGatewayProxyV1Event, APIGatewayProxyV2Event)
Handler = Callable[[T, Any], dict[str, Any]]
Middleware = Callable[[Handler, T, Any], dict[str, Any]]


class MiddlewareManager(Generic[T]):
    """Manages middleware chain for API Gateway resolvers."""

    def __init__(self):
        self.middlewares: list[Middleware] = []

    def add_middleware(self, middleware: Middleware) -> None:
        """Add a middleware to the chain."""
        self.middlewares.append(middleware)

    def apply(self, handler: Handler) -> Handler:
        """Apply all middlewares to the handler."""
        @wraps(handler)
        def wrapped(event: T, context: Any = None) -> dict[str, Any]:
            # Create handler chain from inside out
            final_handler = handler
            for middleware in reversed(self.middlewares):
                def final_handler(e, c, h=final_handler,
                                  m=middleware): return m(h, e, c)
            return final_handler(event, context)
        return wrapped
