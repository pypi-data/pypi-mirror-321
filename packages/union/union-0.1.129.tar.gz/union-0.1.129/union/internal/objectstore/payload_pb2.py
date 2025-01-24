# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: objectstore/payload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from union.internal.common import list_pb2 as common_dot_list__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from union.internal.objectstore import definition_pb2 as objectstore_dot_definition__pb2
from union.internal.validate.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19objectstore/payload.proto\x12\x17\x63loudidl.objectstore.v1\x1a\x11\x63ommon/list.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cobjectstore/definition.proto\x1a\x17validate/validate.proto\"\x11\n\x0fMetadataRequest\"\xb9\x01\n\x10MetadataResponse\x12G\n!max_single_part_object_size_bytes\x18\x01 \x01(\x04R\x1cmaxSinglePartObjectSizeBytes\x12-\n\x13min_part_size_bytes\x18\x02 \x01(\x04R\x10minPartSizeBytes\x12-\n\x13max_part_size_bytes\x18\x03 \x01(\x04R\x10maxPartSizeBytes\"\xb4\x01\n\nPutRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\x12=\n\x08metadata\x18\x02 \x01(\x0b\x32!.cloudidl.objectstore.v1.MetadataR\x08metadata\x12\x37\n\x06object\x18\x03 \x01(\x0b\x32\x1f.cloudidl.objectstore.v1.ObjectR\x06object\"@\n\x0bPutResponse\x12\x1d\n\nsize_bytes\x18\x01 \x01(\x04R\tsizeBytes\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\"<\n\nGetRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\"\xb8\x01\n\x0bGetResponse\x12\x37\n\x06object\x18\x01 \x01(\x0b\x32\x1f.cloudidl.objectstore.v1.ObjectR\x06object\x12=\n\x08metadata\x18\x02 \x01(\x0b\x32!.cloudidl.objectstore.v1.MetadataR\x08metadata\x12\x1d\n\nsize_bytes\x18\x03 \x01(\x04R\tsizeBytes\x12\x12\n\x04\x65tag\x18\x04 \x01(\tR\x04\x65tag\"E\n\x0bListRequest\x12\x36\n\x07request\x18\x01 \x01(\x0b\x32\x1c.cloudidl.common.ListRequestR\x07request\"\x9f\x01\n\x0cListResponse\x12\x30\n\x04keys\x18\x01 \x03(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x04keys\x12\x1d\n\nnext_token\x18\x02 \x01(\tR\tnextToken\x12>\n\x0b\x64irectories\x18\x03 \x03(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x0b\x64irectories\"?\n\rDeleteRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\"\x10\n\x0e\x44\x65leteResponse\"=\n\x0bHeadRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\"\x80\x01\n\x0cHeadResponse\x12=\n\x08metadata\x18\x01 \x01(\x0b\x32!.cloudidl.objectstore.v1.MetadataR\x08metadata\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\x12\x1d\n\nsize_bytes\x18\x03 \x01(\x04R\tsizeBytes\"\xbb\x01\n\x17SuccessfulUploadRequest\x12\x61\n\x0b\x65tags_parts\x18\x01 \x03(\x0b\x32@.cloudidl.objectstore.v1.SuccessfulUploadRequest.EtagsPartsEntryR\netagsParts\x1a=\n\x0f\x45tagsPartsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"\x14\n\x12\x41\x62ortUploadRequest\"\xbe\x02\n\x1fTerminateMultipartUploadRequest\x12-\n\x0coperation_id\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\xf4\x03R\x0boperationId\x12.\n\x03key\x18\x02 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\x12_\n\x11successful_upload\x18\x03 \x01(\x0b\x32\x30.cloudidl.objectstore.v1.SuccessfulUploadRequestH\x00R\x10successfulUpload\x12P\n\x0c\x61\x62ort_upload\x18\x04 \x01(\x0b\x32+.cloudidl.objectstore.v1.AbortUploadRequestH\x00R\x0b\x61\x62ortUploadB\t\n\x07request\"f\n TerminateMultipartUploadResponse\x12.\n\x03key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\"\x8c\x01\n\x1bStartMultipartUploadRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\x12=\n\x08metadata\x18\x02 \x01(\x0b\x32!.cloudidl.objectstore.v1.MetadataR\x08metadata\"\x88\x01\n\x1cStartMultipartUploadResponse\x12-\n\x0coperation_id\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\xf4\x03R\x0boperationId\x12\x39\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\"\x8a\x02\n\x11UploadPartRequest\x12-\n\x0coperation_id\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\xf4\x03R\x0boperationId\x12.\n\x03key\x18\x02 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\x12+\n\x0bpart_number\x18\x03 \x01(\x05\x42\n\xfa\x42\x07\x1a\x05\x18\x90N \x01R\npartNumber\x12\x37\n\x06object\x18\x04 \x01(\x0b\x32\x1f.cloudidl.objectstore.v1.ObjectR\x06object\x12\x30\n\x0e\x63ontent_length\x18\x05 \x01(\x03\x42\t\x18\x01\xfa\x42\x04\"\x02 \x00R\rcontentLength\"(\n\x12UploadPartResponse\x12\x12\n\x04\x65tag\x18\x01 \x01(\tR\x04\x65tag\"_\n%ListInProgressMultipartUploadsRequest\x12\x36\n\x07request\x18\x01 \x01(\x0b\x32\x1c.cloudidl.common.ListRequestR\x07request\"p\n\x0fMultipartUpload\x12-\n\x0coperation_id\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\xf4\x03R\x0boperationId\x12.\n\x03key\x18\x02 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\"r\n&ListInProgressMultipartUploadsResponse\x12H\n\noperations\x18\x01 \x03(\x0b\x32(.cloudidl.objectstore.v1.MultipartUploadR\noperations\"\x93\x01\n\x13\x44ownloadPartRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\x12$\n\tstart_pos\x18\x02 \x01(\x03\x42\x07\xfa\x42\x04\"\x02(\x00R\x08startPos\x12&\n\nsize_bytes\x18\x03 \x01(\x03\x42\x07\xfa\x42\x04\"\x02(\x00R\tsizeBytes\"O\n\x14\x44ownloadPartResponse\x12\x37\n\x06object\x18\x01 \x01(\x0b\x32\x1f.cloudidl.objectstore.v1.ObjectR\x06object\"\x91\x01\n\x0b\x43opyRequest\x12;\n\nsource_key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\tsourceKey\x12\x45\n\x0f\x64\x65stination_key\x18\x02 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x0e\x64\x65stinationKey\"\x0e\n\x0c\x43opyResponse\"\xa3\x02\n\x0ePresignRequest\x12.\n\x03key\x18\x01 \x01(\x0b\x32\x1c.cloudidl.objectstore.v1.KeyR\x03key\x12\x38\n\nexpires_in\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\texpiresIn\x12M\n\x0bput_request\x18\x03 \x01(\x0b\x32*.cloudidl.objectstore.v1.PresignPutRequestH\x00R\nputRequest\x12M\n\x0bget_request\x18\x04 \x01(\x0b\x32*.cloudidl.objectstore.v1.PresignGetRequestH\x00R\ngetRequestB\t\n\x07request\"\xda\x01\n\x0fPresignResponse\x12\x1d\n\nsigned_url\x18\x01 \x01(\tR\tsignedUrl\x12\x65\n\x0frequest_headers\x18\x02 \x03(\x0b\x32<.cloudidl.objectstore.v1.PresignResponse.RequestHeadersEntryR\x0erequestHeaders\x1a\x41\n\x13RequestHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\xdb\x01\n\x1b\x63om.cloudidl.objectstore.v1B\x0cPayloadProtoH\x02P\x01Z.github.com/unionai/cloud/gen/pb-go/objectstore\xa2\x02\x03\x43OX\xaa\x02\x17\x43loudidl.Objectstore.V1\xca\x02\x17\x43loudidl\\Objectstore\\V1\xe2\x02#Cloudidl\\Objectstore\\V1\\GPBMetadata\xea\x02\x19\x43loudidl::Objectstore::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'objectstore.payload_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.cloudidl.objectstore.v1B\014PayloadProtoH\002P\001Z.github.com/unionai/cloud/gen/pb-go/objectstore\242\002\003COX\252\002\027Cloudidl.Objectstore.V1\312\002\027Cloudidl\\Objectstore\\V1\342\002#Cloudidl\\Objectstore\\V1\\GPBMetadata\352\002\031Cloudidl::Objectstore::V1'
  _SUCCESSFULUPLOADREQUEST_ETAGSPARTSENTRY._options = None
  _SUCCESSFULUPLOADREQUEST_ETAGSPARTSENTRY._serialized_options = b'8\001'
  _TERMINATEMULTIPARTUPLOADREQUEST.fields_by_name['operation_id']._options = None
  _TERMINATEMULTIPARTUPLOADREQUEST.fields_by_name['operation_id']._serialized_options = b'\372B\007r\005\020\001\030\364\003'
  _STARTMULTIPARTUPLOADRESPONSE.fields_by_name['operation_id']._options = None
  _STARTMULTIPARTUPLOADRESPONSE.fields_by_name['operation_id']._serialized_options = b'\372B\007r\005\020\001\030\364\003'
  _UPLOADPARTREQUEST.fields_by_name['operation_id']._options = None
  _UPLOADPARTREQUEST.fields_by_name['operation_id']._serialized_options = b'\372B\007r\005\020\001\030\364\003'
  _UPLOADPARTREQUEST.fields_by_name['part_number']._options = None
  _UPLOADPARTREQUEST.fields_by_name['part_number']._serialized_options = b'\372B\007\032\005\030\220N \001'
  _UPLOADPARTREQUEST.fields_by_name['content_length']._options = None
  _UPLOADPARTREQUEST.fields_by_name['content_length']._serialized_options = b'\030\001\372B\004\"\002 \000'
  _MULTIPARTUPLOAD.fields_by_name['operation_id']._options = None
  _MULTIPARTUPLOAD.fields_by_name['operation_id']._serialized_options = b'\372B\007r\005\020\001\030\364\003'
  _DOWNLOADPARTREQUEST.fields_by_name['start_pos']._options = None
  _DOWNLOADPARTREQUEST.fields_by_name['start_pos']._serialized_options = b'\372B\004\"\002(\000'
  _DOWNLOADPARTREQUEST.fields_by_name['size_bytes']._options = None
  _DOWNLOADPARTREQUEST.fields_by_name['size_bytes']._serialized_options = b'\372B\004\"\002(\000'
  _PRESIGNRESPONSE_REQUESTHEADERSENTRY._options = None
  _PRESIGNRESPONSE_REQUESTHEADERSENTRY._serialized_options = b'8\001'
  _globals['_METADATAREQUEST']._serialized_start=193
  _globals['_METADATAREQUEST']._serialized_end=210
  _globals['_METADATARESPONSE']._serialized_start=213
  _globals['_METADATARESPONSE']._serialized_end=398
  _globals['_PUTREQUEST']._serialized_start=401
  _globals['_PUTREQUEST']._serialized_end=581
  _globals['_PUTRESPONSE']._serialized_start=583
  _globals['_PUTRESPONSE']._serialized_end=647
  _globals['_GETREQUEST']._serialized_start=649
  _globals['_GETREQUEST']._serialized_end=709
  _globals['_GETRESPONSE']._serialized_start=712
  _globals['_GETRESPONSE']._serialized_end=896
  _globals['_LISTREQUEST']._serialized_start=898
  _globals['_LISTREQUEST']._serialized_end=967
  _globals['_LISTRESPONSE']._serialized_start=970
  _globals['_LISTRESPONSE']._serialized_end=1129
  _globals['_DELETEREQUEST']._serialized_start=1131
  _globals['_DELETEREQUEST']._serialized_end=1194
  _globals['_DELETERESPONSE']._serialized_start=1196
  _globals['_DELETERESPONSE']._serialized_end=1212
  _globals['_HEADREQUEST']._serialized_start=1214
  _globals['_HEADREQUEST']._serialized_end=1275
  _globals['_HEADRESPONSE']._serialized_start=1278
  _globals['_HEADRESPONSE']._serialized_end=1406
  _globals['_SUCCESSFULUPLOADREQUEST']._serialized_start=1409
  _globals['_SUCCESSFULUPLOADREQUEST']._serialized_end=1596
  _globals['_SUCCESSFULUPLOADREQUEST_ETAGSPARTSENTRY']._serialized_start=1535
  _globals['_SUCCESSFULUPLOADREQUEST_ETAGSPARTSENTRY']._serialized_end=1596
  _globals['_ABORTUPLOADREQUEST']._serialized_start=1598
  _globals['_ABORTUPLOADREQUEST']._serialized_end=1618
  _globals['_TERMINATEMULTIPARTUPLOADREQUEST']._serialized_start=1621
  _globals['_TERMINATEMULTIPARTUPLOADREQUEST']._serialized_end=1939
  _globals['_TERMINATEMULTIPARTUPLOADRESPONSE']._serialized_start=1941
  _globals['_TERMINATEMULTIPARTUPLOADRESPONSE']._serialized_end=2043
  _globals['_STARTMULTIPARTUPLOADREQUEST']._serialized_start=2046
  _globals['_STARTMULTIPARTUPLOADREQUEST']._serialized_end=2186
  _globals['_STARTMULTIPARTUPLOADRESPONSE']._serialized_start=2189
  _globals['_STARTMULTIPARTUPLOADRESPONSE']._serialized_end=2325
  _globals['_UPLOADPARTREQUEST']._serialized_start=2328
  _globals['_UPLOADPARTREQUEST']._serialized_end=2594
  _globals['_UPLOADPARTRESPONSE']._serialized_start=2596
  _globals['_UPLOADPARTRESPONSE']._serialized_end=2636
  _globals['_LISTINPROGRESSMULTIPARTUPLOADSREQUEST']._serialized_start=2638
  _globals['_LISTINPROGRESSMULTIPARTUPLOADSREQUEST']._serialized_end=2733
  _globals['_MULTIPARTUPLOAD']._serialized_start=2735
  _globals['_MULTIPARTUPLOAD']._serialized_end=2847
  _globals['_LISTINPROGRESSMULTIPARTUPLOADSRESPONSE']._serialized_start=2849
  _globals['_LISTINPROGRESSMULTIPARTUPLOADSRESPONSE']._serialized_end=2963
  _globals['_DOWNLOADPARTREQUEST']._serialized_start=2966
  _globals['_DOWNLOADPARTREQUEST']._serialized_end=3113
  _globals['_DOWNLOADPARTRESPONSE']._serialized_start=3115
  _globals['_DOWNLOADPARTRESPONSE']._serialized_end=3194
  _globals['_COPYREQUEST']._serialized_start=3197
  _globals['_COPYREQUEST']._serialized_end=3342
  _globals['_COPYRESPONSE']._serialized_start=3344
  _globals['_COPYRESPONSE']._serialized_end=3358
  _globals['_PRESIGNREQUEST']._serialized_start=3361
  _globals['_PRESIGNREQUEST']._serialized_end=3652
  _globals['_PRESIGNRESPONSE']._serialized_start=3655
  _globals['_PRESIGNRESPONSE']._serialized_end=3873
  _globals['_PRESIGNRESPONSE_REQUESTHEADERSENTRY']._serialized_start=3808
  _globals['_PRESIGNRESPONSE_REQUESTHEADERSENTRY']._serialized_end=3873
# @@protoc_insertion_point(module_scope)
