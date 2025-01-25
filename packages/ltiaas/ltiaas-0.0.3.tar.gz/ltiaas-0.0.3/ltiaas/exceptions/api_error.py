from typing import Any, Optional

from pydantic import ValidationError
from pydantic.dataclasses import dataclass
from requests.exceptions import RequestException

from ltiaas.utils.serialization import Serializable


@dataclass
class LTIAASErrorDetails:
    message: Optional[str] = None
    bodyReceived: Optional[Any] = None
    externalError: Optional[bool] = None
    externalUrl: Optional[str] = None
    errors: Optional[list[dict[str, Any]]] = None


@dataclass
class LTIAASErrorResponse(Serializable):
    status: int
    error: str
    details: Optional[LTIAASErrorDetails] = None


class APIError(Exception):
    response: Optional[LTIAASErrorResponse] = None

    def __init__(self, error: RequestException):
        if error.response is None:
            super().__init__(f"An unexpected error occurred: {error}")
            self.response = None
            return

        try:
            # Attempt to parse the response data
            self.response = LTIAASErrorResponse(**error.response.json())
            super().__init__(self.response.to_json())

        except (ValidationError, ValueError):
            # Handle cases where parsing fails
            super().__init__("An unexpected API error occurred")
            self.response = LTIAASErrorResponse(
                status=error.response.status_code,
                error=error.response.reason,
                details=LTIAASErrorDetails(
                    bodyReceived=error.response.text, externalError=True
                ),
            )
