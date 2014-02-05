# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ClusterStatus.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ClusterStatus.proto',
  package='login.proto',
  serialized_pb='\n\x13\x43lusterStatus.proto\x12\x0blogin.proto*\x89\x01\n\rClusterStatus\x12\x11\n\rSTATUS_ONLINE\x10\x01\x12\x12\n\x0eSTATUS_OFFLINE\x10\x02\x12\x1a\n\x16STATUS_INVITE_REQUIRED\x10\x03\x12\"\n\x1eSTATUS_INSUFFICIENT_PRIVILEGES\x10\x04\x12\x11\n\rSTATUS_BANNED\x10\x05')

_CLUSTERSTATUS = _descriptor.EnumDescriptor(
  name='ClusterStatus',
  full_name='login.proto.ClusterStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_ONLINE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_OFFLINE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_INVITE_REQUIRED', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_INSUFFICIENT_PRIVILEGES', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_BANNED', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=37,
  serialized_end=174,
)

ClusterStatus = enum_type_wrapper.EnumTypeWrapper(_CLUSTERSTATUS)
STATUS_ONLINE = 1
STATUS_OFFLINE = 2
STATUS_INVITE_REQUIRED = 3
STATUS_INSUFFICIENT_PRIVILEGES = 4
STATUS_BANNED = 5




# @@protoc_insertion_point(module_scope)
