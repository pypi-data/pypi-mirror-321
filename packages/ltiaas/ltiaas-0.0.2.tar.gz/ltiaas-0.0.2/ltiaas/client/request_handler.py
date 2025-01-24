from typing import Optional

from requests import RequestException, Session

from ltiaas.exceptions.api_error import APIError


class RequestHandler:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = Session()

    def __handle_error(self, e: RequestException) -> None:
        raise APIError(e) from e

    def get(
        self,
        authorization_header: str,
        path: str,
        query_parameters: Optional[dict[str, any]] = None,
    ) -> dict[str, any]:
        try:
            response = self.session.get(
                f"{self.base_url}/{path}",
                headers={"Authorization": authorization_header},
                params=query_parameters,
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            self.__handle_error(e)

    def post(
        self,
        authorization_header: str,
        path: str,
        body: Optional[dict[str, any]] = None,
    ) -> dict[str, any]:
        try:
            response = self.session.post(
                f"{self.base_url}/{path}",
                headers={"Authorization": authorization_header},
                json=body,
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            self.__handle_error(e)
