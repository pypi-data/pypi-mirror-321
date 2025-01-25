# Enum Definitions
from enum import Enum


class LTIVersion(str, Enum):
    LTI_1_2 = "1.2.0"
    LTI_1_3 = "1.3.0"


class LTILaunchType(str, Enum):
    CORE = "LtiResourceLinkRequest"
    DEEP_LINKING = "LtiDeepLinkingRequest"
    LEGACY_LTI_LAUNCH = "basic-lti-launch-request"
