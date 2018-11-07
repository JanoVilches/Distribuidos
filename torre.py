import grpc
from concurrent import futures
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

import Aeropuerto_pb2
import Aeropuerto_pb2_grpc

class Torre(Aeropuerto_pb2_grpc.TorreServicer):

    def __init__ (self, aterrizaje, despegue, destinos):
        self.aterrizaje = aterrizaje
        self.despegue = despegue
        self.destinos = destinos
        self.aterrizajeInUse = 0
        self.despegueInUse = 0
        self.alturas = []
    
    def Aterrizar(self, request, context):
        if self.aterrizaje > self.aterrizajeInUse:
            self.aterrizajeInUse+=1
            temp = Aeropuerto_pb2.AterrizarReply(altura=0)
        else:
            temp = Aeropuerto_pb2.AterrizarReply(altura=(len(self.alturas)+1)*5)
            self.alturas.append((temp, request.codigo_avion))
        
        print(self.aterrizajeInUse)
        print(self.alturas)
        return temp


aterrizar = 2
despegue = 2
destinos = []
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Aeropuerto_pb2_grpc.add_TorreServicer_to_server(Torre(aterrizar, despegue, destinos), server)
server.add_insecure_port('[::]:50051')
server.start()
try:
    while True:
        time.sleep(_ONE_DAY_IN_SECONDS)
except KeyboardInterrupt:
    server.stop(0)

