"""Models for AWS Lambda handler utilities.

Defines request and response structures for Lambda functions.
"""
import json
from base64 import b64encode
from typing import Any, Optional

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
    def create(cls, body: Any, status_code: int = 200, content_type: str = "application/json") -> dict:
        """Create formatted Lambda response with Base64 encoding for Unicode support."""
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
            json_str = json.dumps(body, ensure_ascii=False)
            body = b64encode(json_str.encode('utf-8')).decode('utf-8')

        return {
            "statusCode": status_code,
            "headers": headers,
            "body": body,
            "isBase64Encoded": True
        }
