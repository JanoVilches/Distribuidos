import math

def square_root(x):
    y = math.sqrt(x)
    return y

def confirmacion(estado):
    if (estado == 0):
        estado = 1
        return estado
    else:
        print("El avion ya se encuentra en vuelo")
        return estado
