# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sentry_protos/snuba/v1alpha/trace_item_attribute.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6sentry_protos/snuba/v1alpha/trace_item_attribute.proto\x12\x1bsentry_protos.snuba.v1alpha\"\xce\x01\n\x0c\x41ttributeKey\x12<\n\x04type\x18\x01 \x01(\x0e\x32..sentry_protos.snuba.v1alpha.AttributeKey.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\"r\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cTYPE_BOOLEAN\x10\x01\x12\x0f\n\x0bTYPE_STRING\x10\x02\x12\x0e\n\nTYPE_FLOAT\x10\x03\x12\x0c\n\x08TYPE_INT\x10\x04\x12\x13\n\x0bTYPE_DOUBLE\x10\x05\x1a\x02\x08\x01\"\xcd\x01\n\x14VirtualColumnContext\x12\x18\n\x10\x66rom_column_name\x18\x01 \x01(\t\x12\x16\n\x0eto_column_name\x18\x02 \x01(\t\x12R\n\tvalue_map\x18\x03 \x03(\x0b\x32?.sentry_protos.snuba.v1alpha.VirtualColumnContext.ValueMapEntry\x1a/\n\rValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"h\n\x0e\x41ttributeValue\x12\x12\n\x08val_bool\x18\x01 \x01(\x08H\x00\x12\x11\n\x07val_str\x18\x02 \x01(\tH\x00\x12\x13\n\tval_float\x18\x03 \x01(\x02H\x00\x12\x11\n\x07val_int\x18\x04 \x01(\x03H\x00\x42\x07\n\x05valueb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentry_protos.snuba.v1alpha.trace_item_attribute_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ATTRIBUTEKEY_TYPE'].values_by_name["TYPE_DOUBLE"]._loaded_options = None
  _globals['_ATTRIBUTEKEY_TYPE'].values_by_name["TYPE_DOUBLE"]._serialized_options = b'\010\001'
  _globals['_VIRTUALCOLUMNCONTEXT_VALUEMAPENTRY']._loaded_options = None
  _globals['_VIRTUALCOLUMNCONTEXT_VALUEMAPENTRY']._serialized_options = b'8\001'
  _globals['_ATTRIBUTEKEY']._serialized_start=88
  _globals['_ATTRIBUTEKEY']._serialized_end=294
  _globals['_ATTRIBUTEKEY_TYPE']._serialized_start=180
  _globals['_ATTRIBUTEKEY_TYPE']._serialized_end=294
  _globals['_VIRTUALCOLUMNCONTEXT']._serialized_start=297
  _globals['_VIRTUALCOLUMNCONTEXT']._serialized_end=502
  _globals['_VIRTUALCOLUMNCONTEXT_VALUEMAPENTRY']._serialized_start=455
  _globals['_VIRTUALCOLUMNCONTEXT_VALUEMAPENTRY']._serialized_end=502
  _globals['_ATTRIBUTEVALUE']._serialized_start=504
  _globals['_ATTRIBUTEVALUE']._serialized_end=608
# @@protoc_insertion_point(module_scope)
