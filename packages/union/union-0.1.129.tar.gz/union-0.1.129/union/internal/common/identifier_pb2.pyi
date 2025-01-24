from union.internal.validate.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectIdentifier(_message.Message):
    __slots__ = ["organization", "domain", "name"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    organization: str
    domain: str
    name: str
    def __init__(self, organization: _Optional[str] = ..., domain: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ClusterIdentifier(_message.Message):
    __slots__ = ["organization", "name"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    organization: str
    name: str
    def __init__(self, organization: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ClusterPoolIdentifier(_message.Message):
    __slots__ = ["organization", "name"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    organization: str
    name: str
    def __init__(self, organization: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ClusterConfigIdentifier(_message.Message):
    __slots__ = ["organization", "id"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    organization: str
    id: str
    def __init__(self, organization: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class UserIdentifier(_message.Message):
    __slots__ = ["subject"]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    subject: str
    def __init__(self, subject: _Optional[str] = ...) -> None: ...

class ApplicationIdentifier(_message.Message):
    __slots__ = ["subject"]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    subject: str
    def __init__(self, subject: _Optional[str] = ...) -> None: ...

class RoleIdentifier(_message.Message):
    __slots__ = ["organization", "name"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    organization: str
    name: str
    def __init__(self, organization: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class OrgIdentifier(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ManagedClusterIdentifier(_message.Message):
    __slots__ = ["name", "org"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_FIELD_NUMBER: _ClassVar[int]
    name: str
    org: OrgIdentifier
    def __init__(self, name: _Optional[str] = ..., org: _Optional[_Union[OrgIdentifier, _Mapping]] = ...) -> None: ...

class PolicyIdentifier(_message.Message):
    __slots__ = ["organization", "name"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    organization: str
    name: str
    def __init__(self, organization: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
