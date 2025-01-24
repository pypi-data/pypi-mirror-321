from typing import Type, TypeVar

from pydantic import ValidationError as PydanticValidationError

from ltiaas.exceptions.validation_error import ValidationError

T = TypeVar("T")


def validate(model: Type[T], data: dict) -> T:
    try:
        return model(**data)
    except PydanticValidationError as e:
        raise ValidationError(e)
