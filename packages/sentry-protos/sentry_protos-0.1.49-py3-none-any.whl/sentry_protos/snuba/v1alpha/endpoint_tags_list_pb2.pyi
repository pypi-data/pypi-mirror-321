"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sentry_protos.snuba.v1alpha.request_common_pb2
import sentry_protos.snuba.v1alpha.trace_item_attribute_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TraceItemAttributesRequest(google.protobuf.message.Message):
    """A request for "which tags are available for these projects between these dates" - used for things like autocompletion"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    limit: builtins.int
    offset: builtins.int
    type: sentry_protos.snuba.v1alpha.trace_item_attribute_pb2.AttributeKey.Type.ValueType
    @property
    def meta(self) -> sentry_protos.snuba.v1alpha.request_common_pb2.RequestMeta: ...
    def __init__(
        self,
        *,
        meta: sentry_protos.snuba.v1alpha.request_common_pb2.RequestMeta | None = ...,
        limit: builtins.int = ...,
        offset: builtins.int = ...,
        type: sentry_protos.snuba.v1alpha.trace_item_attribute_pb2.AttributeKey.Type.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "meta", b"meta", "offset", b"offset", "type", b"type"]) -> None: ...

global___TraceItemAttributesRequest = TraceItemAttributesRequest

@typing.final
class TraceItemAttributesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Tag(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        TYPE_FIELD_NUMBER: builtins.int
        name: builtins.str
        type: sentry_protos.snuba.v1alpha.trace_item_attribute_pb2.AttributeKey.Type.ValueType
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            type: sentry_protos.snuba.v1alpha.trace_item_attribute_pb2.AttributeKey.Type.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "type", b"type"]) -> None: ...

    TAGS_FIELD_NUMBER: builtins.int
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TraceItemAttributesResponse.Tag]: ...
    def __init__(
        self,
        *,
        tags: collections.abc.Iterable[global___TraceItemAttributesResponse.Tag] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["tags", b"tags"]) -> None: ...

global___TraceItemAttributesResponse = TraceItemAttributesResponse

@typing.final
class AttributeValuesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VALUE_SUBSTRING_MATCH_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    name: builtins.str
    value_substring_match: builtins.str
    """a substring of the value being searched,
    only strict substring supported, no regex
    """
    limit: builtins.int
    offset: builtins.int
    @property
    def meta(self) -> sentry_protos.snuba.v1alpha.request_common_pb2.RequestMeta: ...
    def __init__(
        self,
        *,
        meta: sentry_protos.snuba.v1alpha.request_common_pb2.RequestMeta | None = ...,
        name: builtins.str = ...,
        value_substring_match: builtins.str = ...,
        limit: builtins.int = ...,
        offset: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "meta", b"meta", "name", b"name", "offset", b"offset", "value_substring_match", b"value_substring_match"]) -> None: ...

global___AttributeValuesRequest = AttributeValuesRequest

@typing.final
class AttributeValuesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["values", b"values"]) -> None: ...

global___AttributeValuesResponse = AttributeValuesResponse
