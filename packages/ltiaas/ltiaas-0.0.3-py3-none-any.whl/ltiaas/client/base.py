from ltiaas.client.request_handler import RequestHandler


class BaseLTIAASClient:
    def __init__(self, domain: str, api_key: str):
        self._bearer_authorization = self._build_bearer_authorization(api_key=api_key)
        self._request_handler = RequestHandler(base_url=f"https://{domain}")

    def _build_bearer_authorization(self, api_key: str) -> str:
        return f"Bearer {api_key}"
