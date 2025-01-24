from typing import List, Optional, Union
from urllib.parse import quote

from ltiaas.client.base import BaseLTIAASClient
from ltiaas.client.enums import SessionType
from ltiaas.exceptions.invalid_session_error import InvalidSessionError
from ltiaas.resources.deep_linking.types import (
    ContentItem,
    DeepLinkingFormComponents,
    DeepLinkingFormResponse,
)
from ltiaas.resources.idtoken.enums import LTIVersion
from ltiaas.resources.idtoken.types import (
    IdToken,
    LTIVersionPartial,
    RawIdToken,
    RawOauthPayload,
)
from ltiaas.resources.lineitems.types import LineItem, LineItemContainer, LineItemWithId
from ltiaas.resources.memberships.types import MembershipContainer
from ltiaas.utils.serialization import prepare_for_request
from ltiaas.utils.validation import validate


class LTIAASLaunch(BaseLTIAASClient):
    def __init__(
        self,
        domain: str,
        api_key: str,
        ltik: Optional[str] = None,
        service_key: Optional[str] = None,
    ) -> None:
        super().__init__(domain=domain, api_key=api_key)
        self._session_type = self._determine_session_type(
            ltik=ltik, service_key=service_key
        )
        self._service_authorization = self._build_service_authorization(
            api_key=api_key, ltik=ltik, service_key=service_key
        )

    def _determine_session_type(
        self, ltik: Optional[str] = None, service_key: Optional[str] = None
    ) -> SessionType:
        if ltik is not None:
            return SessionType.LTIK
        if service_key is not None:
            return SessionType.SERVICE_KEY
        return SessionType.API_KEY

    def _build_service_authorization(
        self,
        api_key: str,
        ltik: Optional[str] = None,
        service_key: Optional[str] = None,
    ) -> str:
        if self._session_type == SessionType.LTIK:
            return f"LTIK-AUTH-V2 {api_key}:{ltik}"
        elif self._session_type == SessionType.SERVICE_KEY:
            return f"SERVICE-AUTH-V1 {api_key}:{service_key}"
        elif self._session_type == SessionType.API_KEY:
            return f"Bearer {api_key}"

    def _validate_session_type(self, allowed_session_types: List[SessionType]) -> None:
        if self._session_type not in allowed_session_types:
            raise InvalidSessionError(self._session_type, allowed_session_types)

    def get_id_token(self) -> IdToken:
        self._validate_session_type([SessionType.LTIK])
        endpoint = "/api/idtoken"
        data = self._request_handler.get(self._service_authorization, endpoint)
        return validate(IdToken, data)

    def get_raw_id_token(self) -> Union[RawIdToken, RawOauthPayload]:
        self._validate_session_type([SessionType.LTIK])
        endpoint = "/api/idtoken"
        data = self._request_handler.get(
            self._service_authorization, endpoint, {"raw": True}
        )
        partial = validate(LTIVersionPartial, data)
        if partial.lti_version == LTIVersion.LTI_1_3:
            return validate(RawIdToken, data)
        return validate(RawOauthPayload, data)

    def _perform_deep_linking_request(
        self,
        endpoint: str,
        contentItems: List[ContentItem],
        message: Optional[str] = None,
        log: Optional[str] = None,
        err_message: Optional[str] = None,
        err_log: Optional[str] = None,
    ) -> dict:
        self._validate_session_type([SessionType.LTIK])
        if (message or log) and (err_message or err_log):
            raise ValueError("Cannot send both success and error messages or logs.")
        body = {
            "contentItems": [prepare_for_request(i) for i in contentItems],
            "options": {
                "message": message,
                "log": log,
                "errMessage": err_message,
                "errLog": err_log,
            },
        }
        return self._request_handler.post(self._service_authorization, endpoint, body)

    def build_deep_linking_form(
        self,
        contentItems: List[ContentItem],
        message: Optional[str] = None,
        log: Optional[str] = None,
        err_message: Optional[str] = None,
        err_log: Optional[str] = None,
    ):
        endpoint = "/api/deeplinking/form"
        data = self._perform_deep_linking_request(
            endpoint,
            contentItems,
            message=message,
            log=log,
            err_message=err_message,
            err_log=err_log,
        )
        return validate(DeepLinkingFormResponse, data)

    def build_deep_linking_form_components(
        self,
        contentItems: List[ContentItem],
        message: Optional[str] = None,
        log: Optional[str] = None,
        err_message: Optional[str] = None,
        err_log: Optional[str] = None,
    ):
        endpoint = "/api/deeplinking"
        data = self._perform_deep_linking_request(
            endpoint,
            contentItems,
            message=message,
            log=log,
            err_message=err_message,
            err_log=err_log,
        )
        return validate(DeepLinkingFormComponents, data)

    def get_memberhips(
        self,
        url: Optional[str] = None,
        role: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> MembershipContainer:
        self._validate_session_type([SessionType.LTIK, SessionType.SERVICE_KEY])
        endpoint = "/api/memberships"
        query_parameters = {
            "url": quote(url) if url is not None else None,
            "role": quote(role) if role is not None else None,
            "limit": limit,
        }
        data = self._request_handler.get(
            self._service_authorization, endpoint, query_parameters
        )
        return validate(MembershipContainer, data)

    def get_line_items(
        self,
        url: Optional[str] = None,
        tag: Optional[str] = None,
        resourceId: Optional[str] = None,
        resourceLinkId: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> LineItemContainer:
        self._validate_session_type([SessionType.LTIK, SessionType.SERVICE_KEY])
        endpoint = "/api/lineitems"
        query_parameters = {
            "url": quote(url) if url is not None else None,
            "tag": tag,
            "resourceId": resourceId,
            "resourceLinkId": resourceLinkId,
            "limit": limit,
        }
        data = self._request_handler.get(
            self._service_authorization, endpoint, query_parameters
        )
        return validate(LineItemContainer, data)

    def create_line_item(
        self,
        lineitem: LineItem,
    ) -> LineItemWithId:
        self._validate_session_type([SessionType.LTIK, SessionType.SERVICE_KEY])
        endpoint = "/api/lineitems"
        data = self._request_handler.post(
            self._service_authorization,
            endpoint,
            prepare_for_request(lineitem),
        )
        return validate(LineItemWithId, data)
