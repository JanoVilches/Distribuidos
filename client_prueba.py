import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)
stub2 = calculator_pb2_grpc.DespegueStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=16)
avion = calculator_pb2.Avion(Aerolinea="LAN", codigo_avion="CLB1234", Peso=10000, combustible=200000, Torre_control_inicial="10.0.0.1", confirmacion=0)

# make the call
response = stub.SquareRoot(number)
response1 = stub2.Despegar(avion)

avion.confirmacion = response1.confirmacion
# et voilà
print(response.value)
print(avion)
