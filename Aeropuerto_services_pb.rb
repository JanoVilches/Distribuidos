# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: Aeropuerto.proto for package ''

require 'grpc'
require_relative 'Aeropuerto_pb'

module Entrar
  class Service

    include GRPC::GenericService

    self.marshal_class_method = :encode
    self.unmarshal_class_method = :decode
    self.service_name = 'Entrar'

    rpc :Aterrizar, Avion, AterrizarReply
  end

  Stub = Service.rpc_stub_class
end