from enum import Enum


class ContentItemType(str, Enum):
    LTI_RESOURCE_LINK = "ltiResourceLink"
    LINK = "link"
    HTML_FRAGMENT = "html"
    FILE = "file"
    IMAGE = "image"
