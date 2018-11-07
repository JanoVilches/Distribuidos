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

    def __init__ (self, torres, nombre, coladespegue, colallegada, pistas, gate):
        Torres = torres
        nom = nombre
        Pistas = pista
        colallegada = colallegada
        coladespegue = coladespegue
        gateway = gate

    def Gate(self,request,context): #libera una pista de aterrizaje y avisa para aterrizar un avion y dejarlo asignado a una pista.!!!
        gateway.append(request.codigo_avion)
        p = 0
        for i in Pistas["aterrizaje"]:
            if i[0] == request.codigo_avion:
                i = ["",0]
                #LLamar al siguiente, enviando la pista que tiene que usar (p), sacandolo de la colallegada y asignandole la pista PISTAS.!!
            else:
                p += 1

    #DEF DESPEGAR FINAL: saca de la pista, te hace despegar, y pone al siguiente en la pista y le avisa que puede despegar.

    def Despegar(self, request, context): #comprobar condiciones, si hay espacio lo asigan a la pista de despegue, sino encola.
        print("Avion " + request.codigo_avion + " quiere despegar")
        print("Consultando destino...")
        if (request.pesoActual > request.peso):
            response = Aeropuerto_pb2.DespegarReply(estado=-1, destino="")
            return response

        elif(request.combustibleActual != request.combustible):
            response = Aeropuerto_pb2.DespegarReply(estado=-2, destino="")
            return response

        elif(request.pesoActual > request.peso and request.combustibleActual != request.combustible):
            response = Aeropuerto_pb2.DespegarReply(estado=-3, destino="")
            return response

        else:
            #Consultar por pistas de despegue disponible
            p = 0 #pista inicial
            for i in Pistas["despegue"]: #[codigo,estado]
                if i[1] != 1: #hay una pista
                    if (coladespegue != [] and coladespegue.items[-1].codigo_avion == request.codigo_avion):#verifica si es su turno en la cola
                        Pistas["despegue"][p] = [request.codigo_avion,1]
                        print("La pista de despegue asignada al avion " + request.codigo_avion + " es la " + str(p))
                        response = Aeropuerto_pb2.DespegarReply(estado=p, destino = Torres[request.torre_control_destino])
                        coladespegue.avanzar()
                        return response

                    elif (coladespegue != [] and coladespegue.items[-1].codigo_avion != request.codigo_avion):
                        response = Aeropuerto_pb2.DespegarReply(estado=0, destino="")
                        return response

                    else: #no hay nadie en cola y tiene espacio
                        Pistas["despegue"][p] = [request.codigo_avion,1]
                        print("La pista de despegue asignada al avion " + request.codigo_avion + " es la " + str(p))
                        response = Aeropuerto_pb2.DespegarReply(estado=p, destino=Torres[request.torre_control_destino])
                        return response

                    Pistas["despegue"][p] = ["",0] #despega y libera la pista automaticamente.

                else:
                    p = p + 1

            coladespegue.agregar(request)
            response = Aeropuerto_pb2.DespegarReply(estado=0, destino="")
            return response

    def Aterrizar(self, request, context): #solo aterrizara si hay pistas, sino encola!!
        print("Nuevo avion en el Aeropuerto")
        print("Asignando pista de aterrizaje")
        #consultas por pistas disponibles
        p = 0
        print(Pistas["aterrizaje"])
        for i in Pistas["aterrizaje"]: #[codigo,estado]

            if i[1] != 1: #si hay pista disponible
                if colallegada.items != [] and colallegada.items[0].codigo_avion == request.codigo_avion: #verifica si es su turno en la cola
                    Pistas["aterrizaje"][p] = [request.codigo_avion,1] #toma la pista el avion
                    print("La pista de aterrizaje asiganada es la " + str(p+1))
                    print(Pistas["aterrizaje"])
                    response = Aeropuerto_pb2.AterrizarReply(altura=0, pista=p+1) #arreglar la altura asignada
                    colallegada.avanzar()
                    return response

                else: #lo manda a una pista puesto no hay nadie en cola
                    Pistas["aterrizaje"][p] = [request.codigo_avion,1]
                    print("La pista de aterrizaje asiganada es la " + str(p+1))
                    print(Pistas["aterrizaje"])
                    response = Aeropuerto_pb2.AterrizarReply(altura=0, pista=p+1)
                    return response
            else: #pasa a la siguiente pista
                p = p + 1

        #agrega a la cola de llegada un avion,altura
        if colallegada == [] #si no hay ninguno
            item = [request,5]
            colallegada.agregar(item)
        else: #si ya existe uno lo deja volando +1
            item = [request, colallegada.items[-1][1] + 1]
            colallegada.agregar(item)

        response = Aeropuerto_pb2.AterrizarReply(altura=item[1],pista=0)
        return response

Torres = dict()
coladespegue = Cola()
colallegada = Cola()
Gate = []

print("Bienvenido a la Torre de Control")
print("Ingrese un IP valida: ")
IP = str(input())
print("[Torre de control] Nombre del Aeropuerto:")
nombre = str(input())
print("[Torre de control - " + nombre + "] Cantidad pistas de aterrizaje:")
pistas_a = int(input())
print("[Torre de control - " + nombre + "] Cantidad pistas de despegue:")
pistas_d = int(input())

#crear diccionarios de pistas
Pistas = dict()
Pistas['aterrizaje'] = []
Pistas['despegue'] = []
for i in range(pistas_a):
    Pistas['aterrizaje'].append(["",0])
for i in range(pistas_d):
    Pistas['despegue'].append(["",0])

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

Aeropuerto_pb2_grpc.add_TorresServicer_to_server(TorresServicer(Torres, nombre, coladespegue, colallegada, Pistas), server)

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
