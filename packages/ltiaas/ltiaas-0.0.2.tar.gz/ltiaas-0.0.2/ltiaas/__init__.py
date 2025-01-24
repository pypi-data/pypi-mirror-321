# https://gist.github.com/CMCDragonkai/510ce9456a0429f616baa243d1de3dbf
# TODO: Document working with extra values
# TODO: Pre-commit hooks for ruff
# TODO: Implement custom validation errors
# TODO: Fix Deep Linking with aliases (check other types as well)
# TODO: Document usage of extra values through dict deconstruction in constructor

__all__ = [
    "LTIAASLaunch",
    "IdToken",
    "RawIdToken",
    "RawOauthPayload",
    "LTIVersion",
    "LTILaunchType",
    "ContentItem",
    "Icon",
    "Thumbnail",
    "Available",
    "Submission",
    "Iframe",
    "Window",
    "LTIResourceLinkContentItem",
    "LinkContentItem",
    "FileContentItem",
    "ImageContentItem",
    "HTMLFragmentContentItem",
    "DeepLinkingFormComponents",
    "DeepLinkingFormResponse",
    "ContentItemType",
    "Membership",
    "MembershipContainer",
    "MembershipsFilter",
    "LTIUserRole",
    "MembershipStatus",
    "LineItem",
    "LineItemContainer",
    "LineItemWithId",
]

from .client.launch import LTIAASLaunch
from .resources.deep_linking.enums import ContentItemType
from .resources.deep_linking.types import (
    Available,
    ContentItem,
    DeepLinkingFormComponents,
    DeepLinkingFormResponse,
    FileContentItem,
    HTMLFragmentContentItem,
    Icon,
    Iframe,
    ImageContentItem,
    LinkContentItem,
    LTIResourceLinkContentItem,
    Submission,
    Thumbnail,
    Window,
)
from .resources.idtoken.enums import LTILaunchType, LTIVersion
from .resources.idtoken.types import IdToken, RawIdToken, RawOauthPayload
from .resources.lineitems.types import LineItem, LineItemContainer, LineItemWithId
from .resources.memberships.enums import LTIUserRole, MembershipStatus
from .resources.memberships.types import (
    Membership,
    MembershipContainer,
    MembershipsFilter,
)
