# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/app_payload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from union.internal.app import app_definition_pb2 as app_dot_app__definition__pb2
from union.internal.common import identifier_pb2 as common_dot_identifier__pb2
from union.internal.common import list_pb2 as common_dot_list__pb2
from union.internal.validate.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pp/app_payload.proto\x12\x0c\x63loudidl.app\x1a\x18\x61pp/app_definition.proto\x1a\x17\x63ommon/identifier.proto\x1a\x11\x63ommon/list.proto\x1a\x17validate/validate.proto\">\n\rCreateRequest\x12-\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x03\x61pp\"5\n\x0e\x43reateResponse\x12#\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppR\x03\x61pp\"\x99\x01\n\nGetRequest\x12;\n\x06\x61pp_id\x18\x01 \x01(\x0b\x32\x18.cloudidl.app.IdentifierB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x05\x61ppId\x12;\n\x07ingress\x18\x02 \x01(\x0b\x32\x15.cloudidl.app.IngressB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x07ingressB\x11\n\nidentifier\x12\x03\xf8\x42\x01\"2\n\x0bGetResponse\x12#\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppR\x03\x61pp\">\n\rUpdateRequest\x12-\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x03\x61pp\"5\n\x0eUpdateResponse\x12#\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppR\x03\x61pp\"J\n\rDeleteRequest\x12\x39\n\x06\x61pp_id\x18\x01 \x01(\x0b\x32\x18.cloudidl.app.IdentifierB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x05\x61ppId\"\x10\n\x0e\x44\x65leteResponse\"\x8d\x02\n\x0bListRequest\x12\x36\n\x07request\x18\x01 \x01(\x0b\x32\x1c.cloudidl.common.ListRequestR\x07request\x12\x1b\n\x03org\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00R\x03org\x12M\n\ncluster_id\x18\x03 \x01(\x0b\x32\".cloudidl.common.ClusterIdentifierB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\tclusterId\x12H\n\x07project\x18\x04 \x01(\x0b\x32\".cloudidl.common.ProjectIdentifierB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x07projectB\x10\n\tfilter_by\x12\x03\xf8\x42\x01\"K\n\x0cListResponse\x12%\n\x04\x61pps\x18\x01 \x03(\x0b\x32\x11.cloudidl.app.AppR\x04\x61pps\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\x90\x02\n\x0cWatchRequest\x12\x1b\n\x03org\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00R\x03org\x12M\n\ncluster_id\x18\x02 \x01(\x0b\x32\".cloudidl.common.ClusterIdentifierB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\tclusterId\x12H\n\x07project\x18\x03 \x01(\x0b\x32\".cloudidl.common.ProjectIdentifierB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x07project\x12;\n\x06\x61pp_id\x18\x04 \x01(\x0b\x32\x18.cloudidl.app.IdentifierB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x05\x61ppIdB\r\n\x06target\x12\x03\xf8\x42\x01\"2\n\x0b\x43reateEvent\x12#\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppR\x03\x61pp\"m\n\x0bUpdateEvent\x12\x32\n\x0bupdated_app\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppR\nupdatedApp\x12*\n\x07old_app\x18\x02 \x01(\x0b\x32\x11.cloudidl.app.AppR\x06oldApp\"2\n\x0b\x44\x65leteEvent\x12#\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppR\x03\x61pp\"\xd8\x01\n\rWatchResponse\x12>\n\x0c\x63reate_event\x18\x01 \x01(\x0b\x32\x19.cloudidl.app.CreateEventH\x00R\x0b\x63reateEvent\x12>\n\x0cupdate_event\x18\x02 \x01(\x0b\x32\x19.cloudidl.app.UpdateEventH\x00R\x0bupdateEvent\x12>\n\x0c\x64\x65lete_event\x18\x03 \x01(\x0b\x32\x19.cloudidl.app.DeleteEventH\x00R\x0b\x64\x65leteEventB\x07\n\x05\x65vent\"D\n\x13UpdateStatusRequest\x12-\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x03\x61pp\";\n\x14UpdateStatusResponse\x12#\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x11.cloudidl.app.AppR\x03\x61pp\"L\n\x0cLeaseRequest\x12<\n\x02id\x18\x01 \x01(\x0b\x32\".cloudidl.common.ClusterIdentifierB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x02id\"6\n\rLeaseResponse\x12%\n\x04\x61pps\x18\x01 \x03(\x0b\x32\x11.cloudidl.app.AppR\x04\x61ppsB\x9e\x01\n\x10\x63om.cloudidl.appB\x0f\x41ppPayloadProtoH\x02P\x01Z&github.com/unionai/cloud/gen/pb-go/app\xa2\x02\x03\x43\x41X\xaa\x02\x0c\x43loudidl.App\xca\x02\x0c\x43loudidl\\App\xe2\x02\x18\x43loudidl\\App\\GPBMetadata\xea\x02\rCloudidl::Appb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.app_payload_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.cloudidl.appB\017AppPayloadProtoH\002P\001Z&github.com/unionai/cloud/gen/pb-go/app\242\002\003CAX\252\002\014Cloudidl.App\312\002\014Cloudidl\\App\342\002\030Cloudidl\\App\\GPBMetadata\352\002\rCloudidl::App'
  _CREATEREQUEST.fields_by_name['app']._options = None
  _CREATEREQUEST.fields_by_name['app']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETREQUEST.oneofs_by_name['identifier']._options = None
  _GETREQUEST.oneofs_by_name['identifier']._serialized_options = b'\370B\001'
  _GETREQUEST.fields_by_name['app_id']._options = None
  _GETREQUEST.fields_by_name['app_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETREQUEST.fields_by_name['ingress']._options = None
  _GETREQUEST.fields_by_name['ingress']._serialized_options = b'\372B\005\212\001\002\020\001'
  _UPDATEREQUEST.fields_by_name['app']._options = None
  _UPDATEREQUEST.fields_by_name['app']._serialized_options = b'\372B\005\212\001\002\020\001'
  _DELETEREQUEST.fields_by_name['app_id']._options = None
  _DELETEREQUEST.fields_by_name['app_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LISTREQUEST.oneofs_by_name['filter_by']._options = None
  _LISTREQUEST.oneofs_by_name['filter_by']._serialized_options = b'\370B\001'
  _LISTREQUEST.fields_by_name['org']._options = None
  _LISTREQUEST.fields_by_name['org']._serialized_options = b'\372B\004r\002\020\001'
  _LISTREQUEST.fields_by_name['cluster_id']._options = None
  _LISTREQUEST.fields_by_name['cluster_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LISTREQUEST.fields_by_name['project']._options = None
  _LISTREQUEST.fields_by_name['project']._serialized_options = b'\372B\005\212\001\002\020\001'
  _WATCHREQUEST.oneofs_by_name['target']._options = None
  _WATCHREQUEST.oneofs_by_name['target']._serialized_options = b'\370B\001'
  _WATCHREQUEST.fields_by_name['org']._options = None
  _WATCHREQUEST.fields_by_name['org']._serialized_options = b'\372B\004r\002\020\001'
  _WATCHREQUEST.fields_by_name['cluster_id']._options = None
  _WATCHREQUEST.fields_by_name['cluster_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _WATCHREQUEST.fields_by_name['project']._options = None
  _WATCHREQUEST.fields_by_name['project']._serialized_options = b'\372B\005\212\001\002\020\001'
  _WATCHREQUEST.fields_by_name['app_id']._options = None
  _WATCHREQUEST.fields_by_name['app_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _UPDATESTATUSREQUEST.fields_by_name['app']._options = None
  _UPDATESTATUSREQUEST.fields_by_name['app']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LEASEREQUEST.fields_by_name['id']._options = None
  _LEASEREQUEST.fields_by_name['id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_CREATEREQUEST']._serialized_start=134
  _globals['_CREATEREQUEST']._serialized_end=196
  _globals['_CREATERESPONSE']._serialized_start=198
  _globals['_CREATERESPONSE']._serialized_end=251
  _globals['_GETREQUEST']._serialized_start=254
  _globals['_GETREQUEST']._serialized_end=407
  _globals['_GETRESPONSE']._serialized_start=409
  _globals['_GETRESPONSE']._serialized_end=459
  _globals['_UPDATEREQUEST']._serialized_start=461
  _globals['_UPDATEREQUEST']._serialized_end=523
  _globals['_UPDATERESPONSE']._serialized_start=525
  _globals['_UPDATERESPONSE']._serialized_end=578
  _globals['_DELETEREQUEST']._serialized_start=580
  _globals['_DELETEREQUEST']._serialized_end=654
  _globals['_DELETERESPONSE']._serialized_start=656
  _globals['_DELETERESPONSE']._serialized_end=672
  _globals['_LISTREQUEST']._serialized_start=675
  _globals['_LISTREQUEST']._serialized_end=944
  _globals['_LISTRESPONSE']._serialized_start=946
  _globals['_LISTRESPONSE']._serialized_end=1021
  _globals['_WATCHREQUEST']._serialized_start=1024
  _globals['_WATCHREQUEST']._serialized_end=1296
  _globals['_CREATEEVENT']._serialized_start=1298
  _globals['_CREATEEVENT']._serialized_end=1348
  _globals['_UPDATEEVENT']._serialized_start=1350
  _globals['_UPDATEEVENT']._serialized_end=1459
  _globals['_DELETEEVENT']._serialized_start=1461
  _globals['_DELETEEVENT']._serialized_end=1511
  _globals['_WATCHRESPONSE']._serialized_start=1514
  _globals['_WATCHRESPONSE']._serialized_end=1730
  _globals['_UPDATESTATUSREQUEST']._serialized_start=1732
  _globals['_UPDATESTATUSREQUEST']._serialized_end=1800
  _globals['_UPDATESTATUSRESPONSE']._serialized_start=1802
  _globals['_UPDATESTATUSRESPONSE']._serialized_end=1861
  _globals['_LEASEREQUEST']._serialized_start=1863
  _globals['_LEASEREQUEST']._serialized_end=1939
  _globals['_LEASERESPONSE']._serialized_start=1941
  _globals['_LEASERESPONSE']._serialized_end=1995
# @@protoc_insertion_point(module_scope)
