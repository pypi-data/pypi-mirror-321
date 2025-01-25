"""Models for AWS Lambda handler utilities.

Defines request and response structures for Lambda functions.
"""
import json
from typing import Any, Optional, Dict

from pydantic import BaseModel, ConfigDict, Field

from chainsaws.utils.dict_utils import convert_decimal_to_number


class RequestContext(BaseModel):
    """AWS API Gateway request context."""

    identity: dict[str, Any] = Field(default_factory=dict)
    request_id: Optional[str] = None

    def get_source_ip(self) -> Optional[str]:
        """Get source IP address from request context."""
        return self.identity.get("sourceIp", None)


class ResponseHeaders(BaseModel):
    """API Gateway response headers."""

    Access_Control_Allow_Origin: str = Field(
        default="*", alias="Access-Control-Allow-Origin")
    Access_Control_Allow_Headers: str = Field(
        default="*", alias="Access-Control-Allow-Headers")
    Access_Control_Allow_Credentials: bool = Field(
        default=True, alias="Access-Control-Allow-Credentials")
    Access_Control_Allow_Methods: str = Field(
        default="*", alias="Access-Control-Allow-Methods")
    Content_Type: str = Field(default="application/json", alias="Content-Type")
    charset: str = Field(default="UTF-8")


class HandlerConfig(BaseModel):
    """Handler wrapper configuration."""

    error_receiver: Optional[Any] = None
    content_type: str = "application/json"
    use_traceback: bool = True
    ignore_app_errors: list = Field(default_factory=list)


class LambdaEvent(BaseModel):
    """AWS Lambda event structure."""

    body: Optional[str] = None
    headers: dict[str, str] = Field(default_factory=dict)
    request_context: RequestContext = Field(default_factory=RequestContext)

    model_config = ConfigDict(
        extra="allow",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def is_api_gateway_event(cls, event: Dict[str, Any]) -> bool:
        """Check if the event is from API Gateway (REST or HTTP) using execute-api URL.

        Args:
            event (dict): The Lambda event dictionary.

        Returns:
            bool: True if the event is from API Gateway (REST or HTTP), False otherwise.
        """
        # Safely get requestContext
        request_context = event.get("requestContext", {})

        # Check if the domainName contains 'execute-api' (common for API Gateway)
        domain_name = request_context.get("domainName", "")
        is_execute_api_url = "execute-api" in domain_name

        # Check for HTTP API (v2)
        is_http_api = (
            is_execute_api_url and
            request_context.get("apiId") is not None and
            event.get("version") == "2.0" and
            request_context.get("accountId") != "anonymous"
        )

        # Check for REST API (v1)
        is_rest_api = (
            is_execute_api_url and
            request_context.get("apiId") is not None and
            request_context.get("stage") is not None and
            # REST API doesn't include the "version" field
            event.get("version") is None
        )

        # Return True if either condition is met
        return is_http_api or is_rest_api

    def get_json_body(self) -> dict[str, Any] | None:
        """Get JSON body from event."""
        if not self.body:
            return None
        try:
            return json.loads(self.body)
        except json.JSONDecodeError:
            return None


class LambdaResponse:
    """Lambda response model."""

    def __init__(self, body: Any, status_code: int = 200, headers: Optional[dict[str, str]] = None):
        self.body = body
        self.status_code = status_code
        self.headers = headers or {}

    @classmethod
    def create(
        cls,
        body: Any,
        status_code: int = 200,
        content_type: str = "application/json",
        serialize: bool = False
    ) -> dict:
        """Create formatted Lambda response.

        Args:
            body: Response body
            status_code: HTTP status code
            content_type: Response content type
            serialize: Whether to serialize the response body (needed for API Gateway)
        """
        headers = {
            "Content-Type": f"{content_type}; charset=utf-8",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        }

        if isinstance(body, dict):
            response_data = {
                "data": {
                    k: v for k, v in body.items()
                    if k not in ["rslt_cd", "rslt_msg", "duration", "traceback", "error_receiver_failed"]
                }
            }
            for meta_key in ["rslt_cd", "rslt_msg", "duration", "traceback", "error_receiver_failed"]:
                if meta_key in body:
                    response_data[meta_key] = body[meta_key]

            body = convert_decimal_to_number(dict_detail=response_data)

            # API Gateway를 통한 호출인 경우 True
            if serialize:
                body = json.dumps(body, ensure_ascii=False)

        response = {
            "statusCode": status_code,
            "headers": headers,
            "body": body,
        }

        if serialize:
            response["isBase64Encoded"] = False

        return response
