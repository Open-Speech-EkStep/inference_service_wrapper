# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio_to_text.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='audio_to_text.proto',
  package='recognize',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x61udio_to_text.proto\x12\trecognize\"Y\n\x07Message\x12\r\n\x05\x61udio\x18\x01 \x01(\x0c\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x10\n\x08speaking\x18\x04 \x01(\x08\x12\r\n\x05isEnd\x18\x05 \x01(\x08\"M\n\nSRTRequest\x12\r\n\x05\x61udio\x18\x01 \x01(\x0c\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x10\n\x08\x66ilename\x18\x04 \x01(\t\":\n\x0bSRTResponse\x12\x0b\n\x03srt\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\"T\n\x11\x46ileUploadMessage\x12\r\n\x05\x61udio\x18\x01 \x01(\x0c\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x10\n\x08\x66ilename\x18\x04 \x01(\t\"Q\n\x08Response\x12\x15\n\rtranscription\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\t2\xe5\x01\n\tRecognize\x12@\n\x0frecognize_audio\x12\x12.recognize.Message\x1a\x13.recognize.Response\"\x00(\x01\x30\x01\x12T\n\x19recognize_audio_file_mode\x12\x1c.recognize.FileUploadMessage\x1a\x13.recognize.Response\"\x00(\x01\x30\x01\x12@\n\rrecognize_srt\x12\x15.recognize.SRTRequest\x1a\x16.recognize.SRTResponse\"\x00\x62\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='recognize.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='recognize.Message.audio', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='recognize.Message.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='recognize.Message.language', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speaking', full_name='recognize.Message.speaking', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isEnd', full_name='recognize.Message.isEnd', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=123,
)


_SRTREQUEST = _descriptor.Descriptor(
  name='SRTRequest',
  full_name='recognize.SRTRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='recognize.SRTRequest.audio', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='recognize.SRTRequest.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='recognize.SRTRequest.language', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename', full_name='recognize.SRTRequest.filename', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=202,
)


_SRTRESPONSE = _descriptor.Descriptor(
  name='SRTResponse',
  full_name='recognize.SRTResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='srt', full_name='recognize.SRTResponse.srt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='recognize.SRTResponse.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='recognize.SRTResponse.language', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=262,
)


_FILEUPLOADMESSAGE = _descriptor.Descriptor(
  name='FileUploadMessage',
  full_name='recognize.FileUploadMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='recognize.FileUploadMessage.audio', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='recognize.FileUploadMessage.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='recognize.FileUploadMessage.language', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename', full_name='recognize.FileUploadMessage.filename', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=348,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='recognize.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transcription', full_name='recognize.Response.transcription', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='recognize.Response.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='recognize.Response.language', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='recognize.Response.action', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=431,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['SRTRequest'] = _SRTREQUEST
DESCRIPTOR.message_types_by_name['SRTResponse'] = _SRTRESPONSE
DESCRIPTOR.message_types_by_name['FileUploadMessage'] = _FILEUPLOADMESSAGE
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'audio_to_text_pb2'
  # @@protoc_insertion_point(class_scope:recognize.Message)
  })
_sym_db.RegisterMessage(Message)

SRTRequest = _reflection.GeneratedProtocolMessageType('SRTRequest', (_message.Message,), {
  'DESCRIPTOR' : _SRTREQUEST,
  '__module__' : 'audio_to_text_pb2'
  # @@protoc_insertion_point(class_scope:recognize.SRTRequest)
  })
_sym_db.RegisterMessage(SRTRequest)

SRTResponse = _reflection.GeneratedProtocolMessageType('SRTResponse', (_message.Message,), {
  'DESCRIPTOR' : _SRTRESPONSE,
  '__module__' : 'audio_to_text_pb2'
  # @@protoc_insertion_point(class_scope:recognize.SRTResponse)
  })
_sym_db.RegisterMessage(SRTResponse)

FileUploadMessage = _reflection.GeneratedProtocolMessageType('FileUploadMessage', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOADMESSAGE,
  '__module__' : 'audio_to_text_pb2'
  # @@protoc_insertion_point(class_scope:recognize.FileUploadMessage)
  })
_sym_db.RegisterMessage(FileUploadMessage)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'audio_to_text_pb2'
  # @@protoc_insertion_point(class_scope:recognize.Response)
  })
_sym_db.RegisterMessage(Response)



_RECOGNIZE = _descriptor.ServiceDescriptor(
  name='Recognize',
  full_name='recognize.Recognize',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=434,
  serialized_end=663,
  methods=[
  _descriptor.MethodDescriptor(
    name='recognize_audio',
    full_name='recognize.Recognize.recognize_audio',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='recognize_audio_file_mode',
    full_name='recognize.Recognize.recognize_audio_file_mode',
    index=1,
    containing_service=None,
    input_type=_FILEUPLOADMESSAGE,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='recognize_srt',
    full_name='recognize.Recognize.recognize_srt',
    index=2,
    containing_service=None,
    input_type=_SRTREQUEST,
    output_type=_SRTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOGNIZE)

DESCRIPTOR.services_by_name['Recognize'] = _RECOGNIZE

# @@protoc_insertion_point(module_scope)
