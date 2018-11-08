# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Aeropuerto_pb2 as Aeropuerto__pb2


class TorreStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Aterrizar = channel.unary_unary(
        '/Torre/Aterrizar',
        request_serializer=Aeropuerto__pb2.Avion.SerializeToString,
        response_deserializer=Aeropuerto__pb2.AterrizarReply.FromString,
        )
    self.Despegar = channel.unary_unary(
        '/Torre/Despegar',
        request_serializer=Aeropuerto__pb2.Avion.SerializeToString,
        response_deserializer=Aeropuerto__pb2.DespegarReply.FromString,
        )


class TorreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Aterrizar(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Despegar(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TorreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Aterrizar': grpc.unary_unary_rpc_method_handler(
          servicer.Aterrizar,
          request_deserializer=Aeropuerto__pb2.Avion.FromString,
          response_serializer=Aeropuerto__pb2.AterrizarReply.SerializeToString,
      ),
      'Despegar': grpc.unary_unary_rpc_method_handler(
          servicer.Despegar,
          request_deserializer=Aeropuerto__pb2.Avion.FromString,
          response_serializer=Aeropuerto__pb2.DespegarReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Torre', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class PlaneStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Aterrizaje = channel.unary_unary(
        '/Plane/Aterrizaje',
        request_serializer=Aeropuerto__pb2.AterrizarReply.SerializeToString,
        response_deserializer=Aeropuerto__pb2.Empty.FromString,
        )
    self.Despegue = channel.unary_unary(
        '/Plane/Despegue',
        request_serializer=Aeropuerto__pb2.DespegarReply.SerializeToString,
        response_deserializer=Aeropuerto__pb2.Empty.FromString,
        )


class PlaneServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Aterrizaje(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Despegue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PlaneServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Aterrizaje': grpc.unary_unary_rpc_method_handler(
          servicer.Aterrizaje,
          request_deserializer=Aeropuerto__pb2.AterrizarReply.FromString,
          response_serializer=Aeropuerto__pb2.Empty.SerializeToString,
      ),
      'Despegue': grpc.unary_unary_rpc_method_handler(
          servicer.Despegue,
          request_deserializer=Aeropuerto__pb2.DespegarReply.FromString,
          response_serializer=Aeropuerto__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Plane', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))