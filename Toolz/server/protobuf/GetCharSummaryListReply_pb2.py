# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetCharSummaryListReply.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import ResultCodes_pb2
import CharSummary_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetCharSummaryListReply.proto',
  package='login.proto',
  serialized_pb='\n\x1dGetCharSummaryListReply.proto\x12\x0blogin.proto\x1a\x11ResultCodes.proto\x1a\x11\x43harSummary.proto\"w\n\x17GetCharSummaryListReply\x12,\n\x0bresult_code\x18\x01 \x02(\x0e\x32\x17.login.proto.ResultCode\x12.\n\x0csummary_list\x18\x02 \x03(\x0b\x32\x18.login.proto.CharSummary')




_GETCHARSUMMARYLISTREPLY = _descriptor.Descriptor(
  name='GetCharSummaryListReply',
  full_name='login.proto.GetCharSummaryListReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_code', full_name='login.proto.GetCharSummaryListReply.result_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary_list', full_name='login.proto.GetCharSummaryListReply.summary_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=84,
  serialized_end=203,
)

_GETCHARSUMMARYLISTREPLY.fields_by_name['result_code'].enum_type = ResultCodes_pb2._RESULTCODE
_GETCHARSUMMARYLISTREPLY.fields_by_name['summary_list'].message_type = CharSummary_pb2._CHARSUMMARY
DESCRIPTOR.message_types_by_name['GetCharSummaryListReply'] = _GETCHARSUMMARYLISTREPLY

class GetCharSummaryListReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETCHARSUMMARYLISTREPLY

  # @@protoc_insertion_point(class_scope:login.proto.GetCharSummaryListReply)


# @@protoc_insertion_point(module_scope)
