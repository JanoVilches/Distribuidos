# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Aeropuerto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Aeropuerto.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x41\x65ropuerto.proto\"\x91\x01\n\x05\x41vion\x12\x11\n\taerolinea\x18\x01 \x01(\t\x12\x14\n\x0c\x63odigo_avion\x18\x02 \x01(\t\x12\x0c\n\x04peso\x18\x03 \x01(\x05\x12\x13\n\x0b\x63ombustible\x18\x04 \x01(\x05\x12\x1d\n\x15torre_control_inicial\x18\x05 \x01(\t\x12\x1d\n\x15torre_control_destino\x18\x06 \x01(\t\"\x1a\n\x07\x44\x65stino\x12\x0f\n\x07\x64\x65stino\x18\x01 \x01(\t2(\n\x06Torres\x12\x1e\n\x08\x44\x65spegar\x12\x06.Avion\x1a\x08.Destino\"\x00\x62\x06proto3')
)




_AVION = _descriptor.Descriptor(
  name='Avion',
  full_name='Avion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aerolinea', full_name='Avion.aerolinea', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codigo_avion', full_name='Avion.codigo_avion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peso', full_name='Avion.peso', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combustible', full_name='Avion.combustible', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torre_control_inicial', full_name='Avion.torre_control_inicial', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torre_control_destino', full_name='Avion.torre_control_destino', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=21,
  serialized_end=166,
)


_DESTINO = _descriptor.Descriptor(
  name='Destino',
  full_name='Destino',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destino', full_name='Destino.destino', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=168,
  serialized_end=194,
)

DESCRIPTOR.message_types_by_name['Avion'] = _AVION
DESCRIPTOR.message_types_by_name['Destino'] = _DESTINO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Avion = _reflection.GeneratedProtocolMessageType('Avion', (_message.Message,), dict(
  DESCRIPTOR = _AVION,
  __module__ = 'Aeropuerto_pb2'
  # @@protoc_insertion_point(class_scope:Avion)
  ))
_sym_db.RegisterMessage(Avion)

Destino = _reflection.GeneratedProtocolMessageType('Destino', (_message.Message,), dict(
  DESCRIPTOR = _DESTINO,
  __module__ = 'Aeropuerto_pb2'
  # @@protoc_insertion_point(class_scope:Destino)
  ))
_sym_db.RegisterMessage(Destino)



_TORRES = _descriptor.ServiceDescriptor(
  name='Torres',
  full_name='Torres',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=196,
  serialized_end=236,
  methods=[
  _descriptor.MethodDescriptor(
    name='Despegar',
    full_name='Torres.Despegar',
    index=0,
    containing_service=None,
    input_type=_AVION,
    output_type=_DESTINO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TORRES)

DESCRIPTOR.services_by_name['Torres'] = _TORRES

# @@protoc_insertion_point(module_scope)
