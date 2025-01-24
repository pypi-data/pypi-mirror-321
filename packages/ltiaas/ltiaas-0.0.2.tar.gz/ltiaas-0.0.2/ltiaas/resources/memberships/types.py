from typing import List, Optional

from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass

from ltiaas.utils.serialization import Serializable


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class Membership(Serializable):
    user_id: str = Field(alias="userId")
    roles: List[str] = Field()
    status: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    given_name: Optional[str] = Field(None, alias="givenName")
    family_name: Optional[str] = Field(None, alias="familyName")
    middle_name: Optional[str] = Field(None, alias="middleName")
    picture: Optional[str] = None
    lis_person_sourced_id: Optional[str] = Field(None, alias="lisPersonSourcedId")
    lti11_legacy_user_id: Optional[str] = Field(None, alias="lti11LegacyUserId")


@dataclass
class Context(Serializable):
    id: str
    label: Optional[str] = None
    title: Optional[str] = None


@dataclass
class MembershipContainer(Serializable):
    id: str
    context: Context
    members: List[Membership]
    next: Optional[str] = None


@dataclass
class MembershipsFilter(Serializable):
    role: Optional[str] = None
    limit: Optional[int] = None
    url: Optional[str] = None
