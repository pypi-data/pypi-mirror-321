from enum import Enum


class LTIUserRole(str, Enum):
    SYSTEM_ADMINISTRATOR = (
        "http://purl.imsglobal.org/vocab/lis/v2/system/person#Administrator"
    )
    SYSTEM_NONE = "http://purl.imsglobal.org/vocab/lis/v2/system/person#None"
    SYSTEM_ACCOUNT_ADMIN = (
        "http://purl.imsglobal.org/vocab/lis/v2/system/person#AccountAdmin"
    )
    SYSTEM_CRETOR = "http://purl.imsglobal.org/vocab/lis/v2/system/person#Creator"
    SYSTEM_SYS_ADMIN = "http://purl.imsglobal.org/vocab/lis/v2/system/person#SysAdmin"
    SYSTEM_SYS_SUPPORT = (
        "http://purl.imsglobal.org/vocab/lis/v2/system/person#SysSupport"
    )
    SYSTEM_USER = "http://purl.imsglobal.org/vocab/lis/v2/system/person#User"
    INSTITUTION_ADMINISTRATOR = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Administrator"
    )
    INSTITUTION_FACULTY = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Faculty"
    )
    INSTITUTION_GUEST = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Guest"
    )
    INSTITUTION_NONE = "http://purl.imsglobal.org/vocab/lis/v2/institution/person#None"
    INSTITUTION_OTHER = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Other"
    )
    INSTITUTION_STAFF = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Staff"
    )
    INSTITUTION_STUDENT = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Student"
    )
    INSTITUTION_ALUMNI = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Alumni"
    )
    INSTITUTION_INSTRUCTOR = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Instructor"
    )
    INSTITUTION_LEARNER = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Learner"
    )
    INSTITUTION_MEMBER = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Member"
    )
    INSTITUTION_MENTOR = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Mentor"
    )
    INSTITUTION_OBSERVER = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#Observer"
    )
    INSTITUTION_PROSPECTIVE = (
        "http://purl.imsglobal.org/vocab/lis/v2/institution/person#ProspectiveStudent"
    )
    CONTEXT_ADMINISTRATOR = (
        "http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator"
    )
    CONTEXT_CONTENT_DEVELOPER = (
        "http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper"
    )
    CONTEXT_INSTRUCTOR = "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"
    CONTEXT_LEARNER = "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner"
    CONTEXT_MENTOR = "http://purl.imsglobal.org/vocab/lis/v2/membership#Mentor"
    CONTEXT_MANAGER = "http://purl.imsglobal.org/vocab/lis/v2/membership#Manager"
    CONTEXT_MEMBER = "http://purl.imsglobal.org/vocab/lis/v2/membership#Member"
    CONTEXT_OFFICER = "http://purl.imsglobal.org/vocab/lis/v2/membership#Officer"
    INSTRUCTOR = "Instructor"
    LEARNER = "Learner"
    MENTOR = "Mentor"
    MANAGER = "Manager"
    MEMBER = "Member"
    OFFICER = "Officer"
    ADMINISTRATOR = "Administrator"
    CONTENT_DEVELOPER = "ContentDeveloper"
    TEACHING_ASSISTANT = "TeachingAssistant"
    TA = "TeachingAssistant"
    STUDENT = "Student"
    OBSERVER = "Observer"
    NONE = "None"
    OTHER = "Other"
    GUEST = "Guest"
    ALUMNI = "Alumni"
    PROSPECTIVE_STUDENT = "ProspectiveStudent"


class MembershipStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
