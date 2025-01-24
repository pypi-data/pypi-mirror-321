"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sentry_protos.snuba.v1alpha.request_common_pb2
import sentry_protos.snuba.v1alpha.trace_item_attribute_pb2
import sentry_protos.snuba.v1alpha.trace_item_filter_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class AggregateBucketRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Function:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FunctionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AggregateBucketRequest._Function.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        FUNCTION_UNSPECIFIED: AggregateBucketRequest._Function.ValueType  # 0
        FUNCTION_SUM: AggregateBucketRequest._Function.ValueType  # 1
        FUNCTION_AVERAGE: AggregateBucketRequest._Function.ValueType  # 2
        FUNCTION_COUNT: AggregateBucketRequest._Function.ValueType  # 3
        FUNCTION_P50: AggregateBucketRequest._Function.ValueType  # 4
        FUNCTION_P95: AggregateBucketRequest._Function.ValueType  # 5
        FUNCTION_P99: AggregateBucketRequest._Function.ValueType  # 6
        FUNCTION_AVG: AggregateBucketRequest._Function.ValueType  # 7

    class Function(_Function, metaclass=_FunctionEnumTypeWrapper): ...
    FUNCTION_UNSPECIFIED: AggregateBucketRequest.Function.ValueType  # 0
    FUNCTION_SUM: AggregateBucketRequest.Function.ValueType  # 1
    FUNCTION_AVERAGE: AggregateBucketRequest.Function.ValueType  # 2
    FUNCTION_COUNT: AggregateBucketRequest.Function.ValueType  # 3
    FUNCTION_P50: AggregateBucketRequest.Function.ValueType  # 4
    FUNCTION_P95: AggregateBucketRequest.Function.ValueType  # 5
    FUNCTION_P99: AggregateBucketRequest.Function.ValueType  # 6
    FUNCTION_AVG: AggregateBucketRequest.Function.ValueType  # 7

    META_FIELD_NUMBER: builtins.int
    AGGREGATE_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    GRANULARITY_SECS_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    VIRTUAL_COLUMN_CONTEXT_FIELD_NUMBER: builtins.int
    aggregate: global___AggregateBucketRequest.Function.ValueType
    granularity_secs: builtins.int
    @property
    def meta(self) -> sentry_protos.snuba.v1alpha.request_common_pb2.RequestMeta: ...
    @property
    def filter(self) -> sentry_protos.snuba.v1alpha.trace_item_filter_pb2.TraceItemFilter: ...
    @property
    def key(self) -> sentry_protos.snuba.v1alpha.trace_item_attribute_pb2.AttributeKey: ...
    @property
    def virtual_column_context(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[sentry_protos.snuba.v1alpha.trace_item_attribute_pb2.VirtualColumnContext]: ...
    def __init__(
        self,
        *,
        meta: sentry_protos.snuba.v1alpha.request_common_pb2.RequestMeta | None = ...,
        aggregate: global___AggregateBucketRequest.Function.ValueType = ...,
        filter: sentry_protos.snuba.v1alpha.trace_item_filter_pb2.TraceItemFilter | None = ...,
        granularity_secs: builtins.int = ...,
        key: sentry_protos.snuba.v1alpha.trace_item_attribute_pb2.AttributeKey | None = ...,
        virtual_column_context: collections.abc.Iterable[sentry_protos.snuba.v1alpha.trace_item_attribute_pb2.VirtualColumnContext] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["filter", b"filter", "key", b"key", "meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["aggregate", b"aggregate", "filter", b"filter", "granularity_secs", b"granularity_secs", "key", b"key", "meta", b"meta", "virtual_column_context", b"virtual_column_context"]) -> None: ...

global___AggregateBucketRequest = AggregateBucketRequest

@typing.final
class AggregateBucketResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["result", b"result"]) -> None: ...

global___AggregateBucketResponse = AggregateBucketResponse
