from math import *


class Mapa:
    def __init__(self, fil, col, lista_obst, ori =[0,0], dest = [0,0]):
        self.alto = fil
        self.ancho = col
        self.origen = ori
        self.destino = dest
        self.obstaculos = lista_obst

    def casilla_libre(self, fila,columna):
        pos = [fila,columna]
        if fila < 0 or fila > self.alto:
            return False
        if columna < 0 or columna > self.ancho:
            return False
        for i in range(len(self.obstaculos)):
            if self.obstaculos[i] == pos:
                return False
        return True
    


class Nodo:
    def __init__(self, pos_f, pos=[0, 0], padre=None, algoritmo=1):
        self.pos = pos
        self.padre = padre
        if algoritmo == 1:
            self.h = Manhattan(self.pos, pos_f)
        if algoritmo == 2:
            self.h = Euclidean(self.pos, pos_f)
        if algoritmo == 3:
            self.h = Chebyshev(self.pos, pos_f)

        if self.padre == None:
            self.g = 0
        else:
            self.g = self.padre.g + 1

        # Peso del nodo
        self.f = self.g + self.h


# Heurística de Manhattan
def Manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Heurística de Euclidean
def Euclidean(a, b):
    return dist(a,b)


# Heurística de Chebyshev
def Chebyshev(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1])) 
    

def nodo_menor(lista):
    menor = lista[0]
    for i in range(1,len(lista)):
        if lista[i].f <= menor.f:
            menor = lista[i]
    return menor
