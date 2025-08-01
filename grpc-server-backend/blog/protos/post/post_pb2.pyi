from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Post(_message.Message):
    __slots__ = ("id", "title", "content")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    content: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class PostListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PostRetrieveRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
