# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='nanopb.proto',
  package='',
  serialized_pb='\n\x0cnanopb.proto\x1a google/protobuf/descriptor.proto\"4\n\rNanoPBOptions\x12\x10\n\x08max_size\x18\x01 \x01(\x05\x12\x11\n\tmax_count\x18\x02 \x01(\x05:>\n\x06nanopb\x12\x1d.google.protobuf.FieldOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptions')


NANOPB_FIELD_NUMBER = 1010
nanopb = descriptor.FieldDescriptor(
  name='nanopb', full_name='nanopb', index=0,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_NANOPBOPTIONS = descriptor.Descriptor(
  name='NanoPBOptions',
  full_name='NanoPBOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='max_size', full_name='NanoPBOptions.max_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_count', full_name='NanoPBOptions.max_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=50,
  serialized_end=102,
)

import google.protobuf.descriptor_pb2


class NanoPBOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NANOPBOPTIONS
  
  # @@protoc_insertion_point(class_scope:NanoPBOptions)

nanopb.message_type = _NANOPBOPTIONS
google.protobuf.descriptor_pb2.FieldOptions.RegisterExtension(nanopb)
# @@protoc_insertion_point(module_scope)
