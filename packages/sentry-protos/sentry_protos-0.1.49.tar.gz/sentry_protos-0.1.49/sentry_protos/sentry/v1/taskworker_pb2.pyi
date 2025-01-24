"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _TaskActivationStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TaskActivationStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TaskActivationStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TASK_ACTIVATION_STATUS_UNSPECIFIED: _TaskActivationStatus.ValueType  # 0
    TASK_ACTIVATION_STATUS_PENDING: _TaskActivationStatus.ValueType  # 1
    TASK_ACTIVATION_STATUS_PROCESSING: _TaskActivationStatus.ValueType  # 2
    TASK_ACTIVATION_STATUS_FAILURE: _TaskActivationStatus.ValueType  # 3
    TASK_ACTIVATION_STATUS_RETRY: _TaskActivationStatus.ValueType  # 4
    TASK_ACTIVATION_STATUS_COMPLETE: _TaskActivationStatus.ValueType  # 5

class TaskActivationStatus(_TaskActivationStatus, metaclass=_TaskActivationStatusEnumTypeWrapper): ...

TASK_ACTIVATION_STATUS_UNSPECIFIED: TaskActivationStatus.ValueType  # 0
TASK_ACTIVATION_STATUS_PENDING: TaskActivationStatus.ValueType  # 1
TASK_ACTIVATION_STATUS_PROCESSING: TaskActivationStatus.ValueType  # 2
TASK_ACTIVATION_STATUS_FAILURE: TaskActivationStatus.ValueType  # 3
TASK_ACTIVATION_STATUS_RETRY: TaskActivationStatus.ValueType  # 4
TASK_ACTIVATION_STATUS_COMPLETE: TaskActivationStatus.ValueType  # 5
global___TaskActivationStatus = TaskActivationStatus

@typing.final
class RetryState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ATTEMPTS_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    DISCARD_AFTER_ATTEMPT_FIELD_NUMBER: builtins.int
    DEADLETTER_AFTER_ATTEMPT_FIELD_NUMBER: builtins.int
    AT_MOST_ONCE_FIELD_NUMBER: builtins.int
    attempts: builtins.int
    """Current attempt number"""
    kind: builtins.str
    """The classname or adapter type for the retry policy"""
    discard_after_attempt: builtins.int
    """After this attempt the task should be discarded"""
    deadletter_after_attempt: builtins.int
    """After this attempt the task should be put in the dead-letter-queue."""
    at_most_once: builtins.bool
    """Whether a task should be executed at most once."""
    def __init__(
        self,
        *,
        attempts: builtins.int = ...,
        kind: builtins.str = ...,
        discard_after_attempt: builtins.int | None = ...,
        deadletter_after_attempt: builtins.int | None = ...,
        at_most_once: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_at_most_once", b"_at_most_once", "_deadletter_after_attempt", b"_deadletter_after_attempt", "_discard_after_attempt", b"_discard_after_attempt", "at_most_once", b"at_most_once", "deadletter_after_attempt", b"deadletter_after_attempt", "discard_after_attempt", b"discard_after_attempt"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_at_most_once", b"_at_most_once", "_deadletter_after_attempt", b"_deadletter_after_attempt", "_discard_after_attempt", b"_discard_after_attempt", "at_most_once", b"at_most_once", "attempts", b"attempts", "deadletter_after_attempt", b"deadletter_after_attempt", "discard_after_attempt", b"discard_after_attempt", "kind", b"kind"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_at_most_once", b"_at_most_once"]) -> typing.Literal["at_most_once"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_deadletter_after_attempt", b"_deadletter_after_attempt"]) -> typing.Literal["deadletter_after_attempt"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_discard_after_attempt", b"_discard_after_attempt"]) -> typing.Literal["discard_after_attempt"] | None: ...

global___RetryState = RetryState

@typing.final
class TaskActivation(google.protobuf.message.Message):
    """Task message that is stored in Kafka.
    Once consumed, TaskActivations are wrapped with InflightActivation to track
    additional state
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class HeadersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    TASKNAME_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    HEADERS_FIELD_NUMBER: builtins.int
    RECEIVED_AT_FIELD_NUMBER: builtins.int
    DEADLINE_FIELD_NUMBER: builtins.int
    RETRY_STATE_FIELD_NUMBER: builtins.int
    PROCESSING_DEADLINE_DURATION_FIELD_NUMBER: builtins.int
    EXPIRES_FIELD_NUMBER: builtins.int
    id: builtins.str
    """A GUID for the task. Used to update tasks"""
    namespace: builtins.str
    """The task namespace"""
    taskname: builtins.str
    """The name of the task. This name is resolved within the worker"""
    parameters: builtins.str
    """An opaque parameter collection. Could be JSON or protobuf encoded"""
    processing_deadline_duration: builtins.int
    """The duration in seconds that a worker has to complete task execution.
    When an activation is moved from pending -> processing a result is expected
    in this many seconds.
    """
    expires: builtins.int
    """The duration in seconds that a task has to start execution.
    After received_at + expires has passed an activation is expired and will not be executed.
    """
    @property
    def headers(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A map of headers for the task."""

    @property
    def received_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp a task was stored in Kafka"""

    @property
    def deadline(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Unused. Use expires instead."""

    @property
    def retry_state(self) -> global___RetryState:
        """Retry state"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        namespace: builtins.str = ...,
        taskname: builtins.str = ...,
        parameters: builtins.str = ...,
        headers: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        received_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        deadline: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        retry_state: global___RetryState | None = ...,
        processing_deadline_duration: builtins.int = ...,
        expires: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_deadline", b"_deadline", "_expires", b"_expires", "deadline", b"deadline", "expires", b"expires", "received_at", b"received_at", "retry_state", b"retry_state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_deadline", b"_deadline", "_expires", b"_expires", "deadline", b"deadline", "expires", b"expires", "headers", b"headers", "id", b"id", "namespace", b"namespace", "parameters", b"parameters", "processing_deadline_duration", b"processing_deadline_duration", "received_at", b"received_at", "retry_state", b"retry_state", "taskname", b"taskname"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_deadline", b"_deadline"]) -> typing.Literal["deadline"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_expires", b"_expires"]) -> typing.Literal["expires"] | None: ...

global___TaskActivation = TaskActivation

@typing.final
class InflightActivation(google.protobuf.message.Message):
    """Once a TaskActivation has been received by the task consumer it is wrapped
    with InflightActivation so that processing state can be tracked.
    This proto might not be used as InflightActivations don't need to cross
    process boundaries.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACTIVATION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    ADDED_AT_FIELD_NUMBER: builtins.int
    DEADLETTER_AT_FIELD_NUMBER: builtins.int
    PROCESSING_DEADLINE_FIELD_NUMBER: builtins.int
    status: global___TaskActivationStatus.ValueType
    """The current status"""
    offset: builtins.int
    """The original offset that the WorkerTask message had
    Used to find contiguous blocks of completed tasks so that offsets
    can be commit to Kafka
    """
    @property
    def activation(self) -> global___TaskActivation:
        """The TaskActivation being tracked."""

    @property
    def added_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp this task was added to PendingTask storage"""

    @property
    def deadletter_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp that this task expires and should be deadlettered."""

    @property
    def processing_deadline(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp that processing is expected to be complete by.
        If processing is not complete by this time, a retry will be attempted.
        """

    def __init__(
        self,
        *,
        activation: global___TaskActivation | None = ...,
        status: global___TaskActivationStatus.ValueType = ...,
        offset: builtins.int = ...,
        added_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        deadletter_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        processing_deadline: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_processing_deadline", b"_processing_deadline", "activation", b"activation", "added_at", b"added_at", "deadletter_at", b"deadletter_at", "processing_deadline", b"processing_deadline"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_processing_deadline", b"_processing_deadline", "activation", b"activation", "added_at", b"added_at", "deadletter_at", b"deadletter_at", "offset", b"offset", "processing_deadline", b"processing_deadline", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_processing_deadline", b"_processing_deadline"]) -> typing.Literal["processing_deadline"] | None: ...

global___InflightActivation = InflightActivation

@typing.final
class Error(google.protobuf.message.Message):
    """//////////////////////////
    RPC messages and services
    //////////////////////////
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    DETAILS_FIELD_NUMBER: builtins.int
    code: builtins.int
    """Taken directly from the grpc docs."""
    message: builtins.str
    @property
    def details(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """A list of messages that carry any error details."""

    def __init__(
        self,
        *,
        code: builtins.int = ...,
        message: builtins.str = ...,
        details: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["code", b"code", "details", b"details", "message", b"message"]) -> None: ...

global___Error = Error

@typing.final
class GetTaskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    def __init__(
        self,
        *,
        namespace: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_namespace", b"_namespace", "namespace", b"namespace"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_namespace", b"_namespace", "namespace", b"namespace"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_namespace", b"_namespace"]) -> typing.Literal["namespace"] | None: ...

global___GetTaskRequest = GetTaskRequest

@typing.final
class GetTaskResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def task(self) -> global___TaskActivation:
        """If there are no tasks available, these will be empty"""

    @property
    def error(self) -> global___Error: ...
    def __init__(
        self,
        *,
        task: global___TaskActivation | None = ...,
        error: global___Error | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "_task", b"_task", "error", b"error", "task", b"task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_error", b"_error", "_task", b"_task", "error", b"error", "task", b"task"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_task", b"_task"]) -> typing.Literal["task"] | None: ...

global___GetTaskResponse = GetTaskResponse

@typing.final
class FetchNextTask(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    def __init__(
        self,
        *,
        namespace: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_namespace", b"_namespace", "namespace", b"namespace"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_namespace", b"_namespace", "namespace", b"namespace"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_namespace", b"_namespace"]) -> typing.Literal["namespace"] | None: ...

global___FetchNextTask = FetchNextTask

@typing.final
class SetTaskStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    FETCH_NEXT_FIELD_NUMBER: builtins.int
    FETCH_NEXT_NAMESPACE_FIELD_NUMBER: builtins.int
    FETCH_NEXT_TASK_FIELD_NUMBER: builtins.int
    id: builtins.str
    status: global___TaskActivationStatus.ValueType
    fetch_next: builtins.bool
    """If fetch_next is provided, receive a new task in the response"""
    fetch_next_namespace: builtins.str
    @property
    def fetch_next_task(self) -> global___FetchNextTask: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        status: global___TaskActivationStatus.ValueType = ...,
        fetch_next: builtins.bool | None = ...,
        fetch_next_namespace: builtins.str | None = ...,
        fetch_next_task: global___FetchNextTask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_fetch_next", b"_fetch_next", "_fetch_next_namespace", b"_fetch_next_namespace", "_fetch_next_task", b"_fetch_next_task", "fetch_next", b"fetch_next", "fetch_next_namespace", b"fetch_next_namespace", "fetch_next_task", b"fetch_next_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_fetch_next", b"_fetch_next", "_fetch_next_namespace", b"_fetch_next_namespace", "_fetch_next_task", b"_fetch_next_task", "fetch_next", b"fetch_next", "fetch_next_namespace", b"fetch_next_namespace", "fetch_next_task", b"fetch_next_task", "id", b"id", "status", b"status"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_fetch_next", b"_fetch_next"]) -> typing.Literal["fetch_next"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_fetch_next_namespace", b"_fetch_next_namespace"]) -> typing.Literal["fetch_next_namespace"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_fetch_next_task", b"_fetch_next_task"]) -> typing.Literal["fetch_next_task"] | None: ...

global___SetTaskStatusRequest = SetTaskStatusRequest

@typing.final
class SetTaskStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def task(self) -> global___TaskActivation:
        """The next task the worker should execute. Requires fetch_next to be set on the request."""

    @property
    def error(self) -> global___Error: ...
    def __init__(
        self,
        *,
        task: global___TaskActivation | None = ...,
        error: global___Error | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "_task", b"_task", "error", b"error", "task", b"task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_error", b"_error", "_task", b"_task", "error", b"error", "task", b"task"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_task", b"_task"]) -> typing.Literal["task"] | None: ...

global___SetTaskStatusResponse = SetTaskStatusResponse
