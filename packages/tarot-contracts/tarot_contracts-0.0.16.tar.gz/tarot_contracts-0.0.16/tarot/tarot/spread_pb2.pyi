from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TarotSpreadRequest(_message.Message):
    __slots__ = ["question", "category", "spread_profile_id"]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SPREAD_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    question: str
    category: str
    spread_profile_id: str
    def __init__(self, question: _Optional[str] = ..., category: _Optional[str] = ..., spread_profile_id: _Optional[str] = ...) -> None: ...

class TarotSpreadResponse(_message.Message):
    __slots__ = ["question", "category", "spread"]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SPREAD_FIELD_NUMBER: _ClassVar[int]
    question: str
    category: str
    spread: str
    def __init__(self, question: _Optional[str] = ..., category: _Optional[str] = ..., spread: _Optional[str] = ...) -> None: ...
