import grpc
from concurrent import futures
import time

# import the generated classes
import Aeropuerto_pb2
import Aeropuerto_pb2_grpc

class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

class TorresServicer(Aeropuerto_pb2_grpc.TorresServicer):

    def __init__ (self, torres, inicial):
        Torres = torres
        inicial = inicial

    def Despegar(self, request, context):
        print("Avion " + request.codigo_avion + " quiere despegar")
        print("Consultando destino...")
        if (request.peso != 0 and request.combustible != 0):
            #Consultar por pistas de despegue disponible (por hacer)
            print("La pista de despegue asignada al avion " + request.codigo_avion + " es la 2 y la altura 5km")
            response = Aeropuerto_pb2.Destino(destino = Torres[request.torre_control_destino])
            return response

Torres = dict()
Inicial = []

print("Bienvenido a la Torre de Control")
print("Ingrese un IP valida: ")
IP = str(input())
Inicial.append(IP)
print("[Torre de control] Nombre del Aeropuerto:")
nombre = str(input())
Inicial.append(nombre)
print("[Torre de control - " + nombre + "] Cantidad pistas de aterrizaje:")
pistas_a = int(input())
Inicial.append(pistas_a)
print("[Torre de control - " + nombre + "] Cantidad pistas de despegue:")
pistas_d = int(input())
Inicial.append(pistas_d)

#crear diccionarios de pistas
Pistas = dict()
Pistas['aterrizaje'] = []
Pistas['despegue'] = []
for i in range(pistas_a):
    Pistas['aterrizaje'].append(0)
for i in range(pistas_d):
    Pistas['despegue'].append(0)

print("Para agregar destino ingrese 1 || Para continuar ingrese 0")
opcion = int(input())

while True:

    if opcion == 1:
        print("Ingrese nombre e IP de destino:")
        aeropuerto = str(input())
        aeropuerto = aeropuerto.strip().split()
        aeropuerto[0] = ' '.join(aeropuerto[:-1])
        if aeropuerto[0] not in Torres:
            Torres[aeropuerto[0]] = aeropuerto[-1]
        print("Para agregar destino ingrese 1 || Para continuar ingrese 0")
        opcion = int(input())

    else:
        break

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

Aeropuerto_pb2_grpc.add_TorresServicer_to_server(TorresServicer(Torres, Inicial), server)

# listen on port 50051
print('Starting server')
#direccion = IP + ':50051'
server.add_insecure_port('localhost:' + IP)
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
