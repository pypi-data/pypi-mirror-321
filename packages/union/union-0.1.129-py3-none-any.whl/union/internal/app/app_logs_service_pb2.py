# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/app_logs_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from union.internal.app import app_logs_payload_pb2 as app_dot_app__logs__payload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61pp/app_logs_service.proto\x12\x0c\x63loudidl.app\x1a\x1a\x61pp/app_logs_payload.proto2b\n\x0e\x41ppLogsService\x12P\n\x08TailLogs\x12\x1d.cloudidl.app.TailLogsRequest\x1a\x1e.cloudidl.app.TailLogsResponse\"\x03\x90\x02\x01\x30\x01\x42\xa2\x01\n\x10\x63om.cloudidl.appB\x13\x41ppLogsServiceProtoH\x02P\x01Z&github.com/unionai/cloud/gen/pb-go/app\xa2\x02\x03\x43\x41X\xaa\x02\x0c\x43loudidl.App\xca\x02\x0c\x43loudidl\\App\xe2\x02\x18\x43loudidl\\App\\GPBMetadata\xea\x02\rCloudidl::Appb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.app_logs_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.cloudidl.appB\023AppLogsServiceProtoH\002P\001Z&github.com/unionai/cloud/gen/pb-go/app\242\002\003CAX\252\002\014Cloudidl.App\312\002\014Cloudidl\\App\342\002\030Cloudidl\\App\\GPBMetadata\352\002\rCloudidl::App'
  _APPLOGSSERVICE.methods_by_name['TailLogs']._options = None
  _APPLOGSSERVICE.methods_by_name['TailLogs']._serialized_options = b'\220\002\001'
  _globals['_APPLOGSSERVICE']._serialized_start=72
  _globals['_APPLOGSSERVICE']._serialized_end=170
# @@protoc_insertion_point(module_scope)
