from enum import Enum


class SessionType(str, Enum):
    LTIK = "ltik"
    SERVICE_KEY = "service_key"
    API_KEY = "api_key"
