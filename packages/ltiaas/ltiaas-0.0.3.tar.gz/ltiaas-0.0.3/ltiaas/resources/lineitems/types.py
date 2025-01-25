from datetime import datetime
from typing import List, Optional

from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass

from ltiaas.utils.serialization import Serializable


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class LineItem(Serializable):
    label: str
    score_maximum: int | float = Field(alias="scoreMaximum")
    resource_link_id: Optional[str] = Field(None, alias="resourceLinkId")
    resource_id: Optional[str] = Field(None, alias="resourceId")
    tag: Optional[str] = None
    start_date_time: Optional[datetime] = Field(None, alias="startDateTime")
    end_date_time: Optional[datetime] = Field(None, alias="endDateTime")
    grades_released: Optional[bool] = Field(None, alias="gradesReleased")


# Have to use a mixin because pydantic complains that the
#   required "id" field cannot be declared after the optional fields
@dataclass
class IdMixin(Serializable):
    id: str


@dataclass
class LineItemWithId(LineItem, IdMixin):
    pass


@dataclass(config=ConfigDict(populate_by_name=True))
class LineItemContainer(Serializable):
    line_items: List[LineItem] = Field(alias="lineItems")
    next: Optional[str] = None
    first: Optional[str] = None
    last: Optional[str] = None
    prev: Optional[str] = None
