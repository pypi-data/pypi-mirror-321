# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sentry_protos/snuba/v1/endpoint_get_trace.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sentry_protos.snuba.v1 import request_common_pb2 as sentry__protos_dot_snuba_dot_v1_dot_request__common__pb2
from sentry_protos.snuba.v1 import trace_item_attribute_pb2 as sentry__protos_dot_snuba_dot_v1_dot_trace__item__attribute__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/sentry_protos/snuba/v1/endpoint_get_trace.proto\x12\x16sentry_protos.snuba.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a+sentry_protos/snuba/v1/request_common.proto\x1a\x31sentry_protos/snuba/v1/trace_item_attribute.proto\"\xd3\x02\n\x0fGetTraceRequest\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32#.sentry_protos.snuba.v1.RequestMeta\x12\x10\n\x08trace_id\x18\x02 \x01(\t\x12@\n\x05items\x18\x03 \x03(\x0b\x32\x31.sentry_protos.snuba.v1.GetTraceRequest.TraceItem\x1a\xb8\x01\n\tTraceItem\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32%.sentry_protos.snuba.v1.TraceItemNameB\x02\x18\x01\x12\x38\n\nattributes\x18\x02 \x03(\x0b\x32$.sentry_protos.snuba.v1.AttributeKey\x12\x38\n\titem_type\x18\x03 \x01(\x0e\x32%.sentry_protos.snuba.v1.TraceItemType\"\xe8\x04\n\x10GetTraceResponse\x12\x10\n\x08trace_id\x18\x01 \x01(\t\x12\x32\n\x04meta\x18\x02 \x01(\x0b\x32$.sentry_protos.snuba.v1.ResponseMeta\x12G\n\x0bitem_groups\x18\x03 \x03(\x0b\x32\x32.sentry_protos.snuba.v1.GetTraceResponse.ItemGroup\x1a\x85\x02\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12K\n\nattributes\x18\x03 \x03(\x0b\x32\x37.sentry_protos.snuba.v1.GetTraceResponse.Item.Attribute\x1au\n\tAttribute\x12\x31\n\x03key\x18\x01 \x01(\x0b\x32$.sentry_protos.snuba.v1.AttributeKey\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.sentry_protos.snuba.v1.AttributeValue\x1a\xbc\x01\n\tItemGroup\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32%.sentry_protos.snuba.v1.TraceItemNameB\x02\x18\x01\x12<\n\x05items\x18\x02 \x03(\x0b\x32-.sentry_protos.snuba.v1.GetTraceResponse.Item\x12\x38\n\titem_type\x18\x03 \x01(\x0e\x32%.sentry_protos.snuba.v1.TraceItemTypeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentry_protos.snuba.v1.endpoint_get_trace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETTRACEREQUEST_TRACEITEM'].fields_by_name['type']._loaded_options = None
  _globals['_GETTRACEREQUEST_TRACEITEM'].fields_by_name['type']._serialized_options = b'\030\001'
  _globals['_GETTRACERESPONSE_ITEMGROUP'].fields_by_name['type']._loaded_options = None
  _globals['_GETTRACERESPONSE_ITEMGROUP'].fields_by_name['type']._serialized_options = b'\030\001'
  _globals['_GETTRACEREQUEST']._serialized_start=205
  _globals['_GETTRACEREQUEST']._serialized_end=544
  _globals['_GETTRACEREQUEST_TRACEITEM']._serialized_start=360
  _globals['_GETTRACEREQUEST_TRACEITEM']._serialized_end=544
  _globals['_GETTRACERESPONSE']._serialized_start=547
  _globals['_GETTRACERESPONSE']._serialized_end=1163
  _globals['_GETTRACERESPONSE_ITEM']._serialized_start=711
  _globals['_GETTRACERESPONSE_ITEM']._serialized_end=972
  _globals['_GETTRACERESPONSE_ITEM_ATTRIBUTE']._serialized_start=855
  _globals['_GETTRACERESPONSE_ITEM_ATTRIBUTE']._serialized_end=972
  _globals['_GETTRACERESPONSE_ITEMGROUP']._serialized_start=975
  _globals['_GETTRACERESPONSE_ITEMGROUP']._serialized_end=1163
# @@protoc_insertion_point(module_scope)
