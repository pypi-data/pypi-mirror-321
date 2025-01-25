from typing import Dict, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl
from pydantic.dataclasses import dataclass

from ltiaas.resources.deep_linking.enums import ContentItemType
from ltiaas.utils.serialization import Serializable


@dataclass
class Icon(Serializable):
    url: HttpUrl
    width: int
    height: int


@dataclass
class Thumbnail(Serializable):
    url: HttpUrl
    width: int
    height: int


@dataclass(config=ConfigDict(populate_by_name=True))
class Available(Serializable):
    startDateTime: Optional[str] = None
    endDateTime: Optional[str] = None


@dataclass(config=ConfigDict(populate_by_name=True))
class Submission(Serializable):
    startDateTime: Optional[str] = None
    endDateTime: Optional[str] = None


@dataclass
class Iframe(Serializable):
    width: Optional[int] = None
    height: Optional[int] = None


@dataclass(config=ConfigDict(populate_by_name=True))
class Window(Serializable):
    targetName: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    windowFeatures: Optional[str] = None


@dataclass(config=ConfigDict(extra="allow"))
class LTIResourceLinkContentItem(Serializable):
    type: str = ContentItemType.LTI_RESOURCE_LINK
    url: Optional[HttpUrl] = None
    title: Optional[str] = None
    text: Optional[str] = None
    icon: Optional[Icon] = None
    thumbnail: Optional[Thumbnail] = None
    available: Optional[Available] = None
    submission: Optional[Submission] = None
    iframe: Optional[Iframe] = None
    window: Optional[Window] = None
    custom: Optional[Dict[str, Union[str, int]]] = None


@dataclass(config=ConfigDict(extra="allow"))
class LinkContentItem(Serializable):
    type: str = ContentItemType.LINK
    url: HttpUrl = Field()
    title: Optional[str] = None
    text: Optional[str] = None
    icon: Optional[Icon] = None
    thumbnail: Optional[Thumbnail] = None
    embed: Optional[dict] = None
    iframe: Optional[Iframe] = None
    window: Optional[Window] = None


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class FileContentItem(Serializable):
    type: str = ContentItemType.FILE
    url: HttpUrl = Field()
    title: Optional[str] = None
    text: Optional[str] = None
    icon: Optional[Icon] = None
    thumbnail: Optional[Thumbnail] = None
    expires_at: Optional[str] = Field(None, alias="expiresAt")


@dataclass(config=ConfigDict(extra="allow"))
class ImageContentItem(Serializable):
    type: str = ContentItemType.IMAGE
    url: HttpUrl = Field()
    title: Optional[str] = None
    text: Optional[str] = None
    icon: Optional[Icon] = None
    thumbnail: Optional[Thumbnail] = None
    width: Optional[int] = None
    height: Optional[int] = None


@dataclass(config=ConfigDict(extra="allow"))
class HTMLFragmentContentItem(Serializable):
    type: str = ContentItemType.HTML_FRAGMENT
    html: str = Field()
    title: Optional[str] = None
    text: Optional[str] = None


ContentItem = Union[
    LTIResourceLinkContentItem,
    LinkContentItem,
    FileContentItem,
    ImageContentItem,
    HTMLFragmentContentItem,
]


@dataclass
class DeepLinkingFormResponse(Serializable):
    form: str


@dataclass
class DeepLinkingFormComponents(Serializable):
    message: str
    target: str
