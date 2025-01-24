from pydantic import ValidationError as PydanticValidationError


class ValidationError(Exception):
    def __init__(self, error: PydanticValidationError) -> None:
        self.errors = self.__format_errors(error.errors())
        super().__init__(self.errors)

    def __format_errors(self, errors):
        return {"__".join(error["loc"]): [error["msg"]] for error in errors}
