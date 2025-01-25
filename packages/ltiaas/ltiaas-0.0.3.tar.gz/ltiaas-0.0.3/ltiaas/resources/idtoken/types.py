from typing import Any, Dict, List, Optional, Union

from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass

from ltiaas.resources.idtoken.enums import LTILaunchType, LTIVersion
from ltiaas.utils.serialization import Serializable


@dataclass
class LTIVersionPartial:
    lti_version: LTIVersion = Field(alias="ltiVersion")


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class User(Serializable):
    id: str
    roles: List[str]
    name: Optional[str] = None
    email: Optional[str] = None
    given_name: Optional[str] = Field(None, alias="givenName")
    family_name: Optional[str] = Field(None, alias="familyName")
    role_scope_mentor: Optional[List[str]] = Field(None, alias="roleScopeMentor")


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class Platform(Serializable):
    id: Optional[str] = None
    url: Optional[str] = None
    client_id: Optional[str] = Field(None, alias="clientId")
    deployment_id: Optional[str] = Field(None, alias="deploymentId")
    name: Optional[str] = None
    description: Optional[str] = None
    guid: Optional[str] = None
    contact_email: Optional[str] = Field(None, alias="contactEmail")
    product_family_code: Optional[str] = Field(None, alias="productFamilyCode")
    lis: Optional[Dict[str, Any]] = None
    consumer_key: Optional[str] = Field(None, alias="consumerKey")


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class Launch(Serializable):
    type: LTILaunchType
    target: Optional[str] = None
    context: Optional[Dict[str, Any]] = None
    resource_link: Optional[Dict[str, Any]] = Field(None, alias="resourceLink")
    custom: Optional[Dict[str, Union[str, int]]] = None
    presentation: Optional[Dict[str, Any]] = None


@dataclass(config=ConfigDict(populate_by_name=True))
class Services(Serializable):
    outcomes: Dict[str, bool]
    deep_linking: Dict[str, Any] = Field(alias="deepLinking")
    assignment_and_grades: Dict[str, Any] = Field(alias="assignmentAndGrades")
    names_and_roles: Dict[str, Any] = Field(alias="namesAndRoles")
    service_key: Optional[str] = Field(None, alias="serviceKey")


@dataclass(config=ConfigDict(populate_by_name=True))
class IdToken(Serializable):
    user: User
    platform: Platform
    launch: Launch
    services: Services
    lti_version: LTIVersion = Field(alias="ltiVersion")


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class RawIdToken(Serializable):
    iss: str
    sub: str
    aud: str
    exp: int
    iat: int
    nonce: str
    lti_version: LTIVersion = Field(alias="ltiVersion")
    azp: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    locale: Optional[str] = None
    message_type: LTILaunchType = Field(
        alias="https://purl.imsglobal.org/spec/lti/claim/message_type"
    )
    deployment_id: str = Field(
        alias="https://purl.imsglobal.org/spec/lti/claim/deployment_id"
    )
    target_link_uri: str = Field(
        alias="https://purl.imsglobal.org/spec/lti/claim/target_link_uri"
    )
    roles: List[str] = Field(alias="https://purl.imsglobal.org/spec/lti/claim/roles")
    tool_platform: Optional[Dict[str, Any]] = Field(
        None, alias="https://purl.imsglobal.org/spec/lti/claim/tool_platform"
    )
    context: Optional[Dict[str, Any]] = Field(
        None, alias="https://purl.imsglobal.org/spec/lti/claim/context"
    )
    resource_link: Optional[Dict[str, Any]] = Field(
        None, alias="https://purl.imsglobal.org/spec/lti/claim/resource_link"
    )
    launch_presentation: Optional[Dict[str, Any]] = Field(
        None, alias="https://purl.imsglobal.org/spec/lti/claim/launch_presentation"
    )
    role_scope_mentor: Optional[List[str]] = Field(
        None, alias="https://purl.imsglobal.org/spec/lti/claim/role_scope_mentor"
    )
    custom: Optional[Dict[str, Union[str, int]]] = Field(
        None, alias="https://purl.imsglobal.org/spec/lti/claim/custom"
    )
    lis: Optional[Dict[str, Union[str, int]]] = Field(
        None, alias="https://purl.imsglobal.org/spec/lti/claim/lis"
    )


@dataclass(config=ConfigDict(extra="allow", populate_by_name=True))
class RawOauthPayload(Serializable):
    lti_message_type: LTILaunchType
    resource_link_id: str
    lti_version: LTIVersion = Field(alias="ltiVersion")
    resource_link_title: Optional[str] = None
    resource_link_description: Optional[str] = None
    user_id: Optional[str] = None
    roles: Optional[str] = None
    oauth_version: Optional[str] = None
    oauth_nonce: Optional[str] = None
    oauth_timestamp: Optional[str] = None
    oauth_consumer_key: Optional[str] = None
    context_id: Optional[str] = None
    context_label: Optional[str] = None
    context_title: Optional[str] = None
    context_type: Optional[str] = None
    lis_person_sourcedid: Optional[str] = None
    lis_course_section_sourcedid: Optional[str] = None
    lis_result_sourcedid: Optional[str] = None
    lis_outcome_service_url: Optional[str] = None
    lis_person_name_given: Optional[str] = None
    lis_person_name_family: Optional[str] = None
    lis_person_name_full: Optional[str] = None
    ext_user_username: Optional[str] = None
    lis_person_contact_email_primary: Optional[str] = None
    launch_presentation_locale: Optional[str] = None
    ext_lms: Optional[str] = None
    tool_consumer_info_product_family_code: Optional[str] = None
    tool_consumer_info_version: Optional[str] = None
    oauth_callback: Optional[str] = None
    tool_consumer_instance_guid: Optional[str] = None
    tool_consumer_instance_name: Optional[str] = None
    tool_consumer_instance_description: Optional[str] = None
    launch_presentation_document_target: Optional[str] = None
    launch_presentation_return_url: Optional[str] = None
    custom_gradebookservices_scope: Optional[str] = None
    custom_lineitems_url: Optional[str] = None
    custom_lineitem_url: Optional[str] = None
    oauth_signature_method: Optional[str] = None
