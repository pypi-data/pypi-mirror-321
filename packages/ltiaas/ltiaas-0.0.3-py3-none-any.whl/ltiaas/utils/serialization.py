import json
from typing import Any, Union


class Serializable:
    ___INDENTATION_SPACES = 4

    def to_json(self) -> str:
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=self.___INDENTATION_SPACES,
        )

    def __get_defined_fields(self, serializable: "Serializable") -> list[str]:
        fields = []
        for f in serializable.__dataclass_fields__.values():
            if isinstance(f.type, type) and issubclass(f.type, Serializable):
                fields.extend(self.__get_defined_fields(f.type))
                continue
            fields.append(f.name)
        return fields

    @property
    def _defined_fields(self) -> list[str]:
        return self.__get_defined_fields(self)

    def to_dict(self) -> dict:
        # We have to call to_json first because the json.dumps method will handle
        #  the serialization of nested objects
        return json.loads(self.to_json())


def __to_camel_case(snake_str: str) -> str:
    parts = snake_str.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def __convert_keys_to_camel_case(
    data: Union[dict, Any], defined_fields: list[str]
) -> Union[dict, Any]:
    if not isinstance(data, dict):
        return data
    return {
        __to_camel_case(key)
        # This assumes that every defined snake case field needs to be converted to camel case
        if key in defined_fields
        else key: __convert_keys_to_camel_case(value, defined_fields)
        for key, value in data.items()
    }


def prepare_for_request(item: Serializable) -> dict:
    return __convert_keys_to_camel_case(item.to_dict(), item._defined_fields)
