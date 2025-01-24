"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sentry_protos.snuba.v1.endpoint_time_series_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateSubscriptionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_SERIES_REQUEST_FIELD_NUMBER: builtins.int
    TIME_WINDOW_SECS_FIELD_NUMBER: builtins.int
    RESOLUTION_SECS_FIELD_NUMBER: builtins.int
    time_window_secs: builtins.int
    resolution_secs: builtins.int
    @property
    def time_series_request(self) -> sentry_protos.snuba.v1.endpoint_time_series_pb2.TimeSeriesRequest: ...
    def __init__(
        self,
        *,
        time_series_request: sentry_protos.snuba.v1.endpoint_time_series_pb2.TimeSeriesRequest | None = ...,
        time_window_secs: builtins.int = ...,
        resolution_secs: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time_series_request", b"time_series_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["resolution_secs", b"resolution_secs", "time_series_request", b"time_series_request", "time_window_secs", b"time_window_secs"]) -> None: ...

global___CreateSubscriptionRequest = CreateSubscriptionRequest

@typing.final
class CreateSubscriptionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSCRIPTION_ID_FIELD_NUMBER: builtins.int
    subscription_id: builtins.str
    def __init__(
        self,
        *,
        subscription_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subscription_id", b"subscription_id"]) -> None: ...

global___CreateSubscriptionResponse = CreateSubscriptionResponse
