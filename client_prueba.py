import grpc

# import the generated classes
import Aeropuerto_pb2
import Aeropuerto_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
#stub = calculator_pb2_grpc.CalculatorStub(channel)
stub2 = Aeropuerto_pb2_grpc.TorresStub(channel)

# create a valid request message
#number = calculator_pb2.Number(value=16)
codigo = str(input())
avion = Aeropuerto_pb2.Avion(aerolinea="LAN", codigo_avion=codigo, peso=10000, combustible=200000, torre_control_destino="Madrid")

# make the call
#response = stub.SquareRoot(number)
#response = stub2.Despegar(avion)
response = stub2.Aterrizar(avion)
print(response)

"""
print("IP: " + response.destino)

direccion = 'localhost:' + response.destino

channel = grpc.insecure_channel(direccion)
stub2 = Aeropuerto_pb2_grpc.TorresStub(channel)
avion.torre_control_destino = "Sao Pablo"
response = stub2.Despegar(avion)

#print(response.value)
print("IP: " + response.destino)
"""
