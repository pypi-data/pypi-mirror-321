from typing import List

from ltiaas.client.enums import SessionType


class InvalidSessionError(Exception):
    def __init__(
        self, current_session: SessionType, allowed_session_types: List[SessionType]
    ):
        message = (
            f"Invalid session type. Please provide one of the following tokens during initialization: "
            f"{', '.join([t.value for t in allowed_session_types])}"
        )
        super().__init__(message)
        self.current_session = current_session
        self.allowed_session_types = allowed_session_types
