from __future__ import print_function

import grpc

import Aeropuerto_pb2
import Aeropuerto_pb2_grpc

aviones = []
for i in range(5):
    aviones.append(Aeropuerto_pb2.Avion(aerolinea="a", codigo_avion=str(i), peso=1, combustible=1, torre_control_inicial="as", torre_control_destino="asd"))
with grpc.insecure_channel('[::]:50051') as channel:
    stub = Aeropuerto_pb2_grpc.EntrarStub(channel)
    for i in aviones:
        responses = stub.Aterrizar(i)
        print(responses)
    