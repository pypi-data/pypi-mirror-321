from tarot.tarot import users_pb2 as _users_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TarotSpreadRequest(_message.Message):
    __slots__ = ["question", "category", "spread_profile"]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SPREAD_PROFILE_FIELD_NUMBER: _ClassVar[int]
    question: str
    category: str
    spread_profile: _users_pb2.SpreadProfile
    def __init__(self, question: _Optional[str] = ..., category: _Optional[str] = ..., spread_profile: _Optional[_Union[_users_pb2.SpreadProfile, _Mapping]] = ...) -> None: ...

class TarotSpreadResponse(_message.Message):
    __slots__ = ["question", "category", "spread"]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SPREAD_FIELD_NUMBER: _ClassVar[int]
    question: str
    category: str
    spread: str
    def __init__(self, question: _Optional[str] = ..., category: _Optional[str] = ..., spread: _Optional[str] = ...) -> None: ...
