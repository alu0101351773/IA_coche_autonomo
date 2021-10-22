
class Mapa:
    def __init__(self, fil, col, lista_obst, ori =[0,0], dest = [0,0]):
        self.alto = fil
        self.ancho = col
        self.origen = Nodo(dest,ori)
        self.destino = Nodo(dest,dest)
        self.obstaculos = lista_obst

    def casilla_libre(self, fila,columna):
        pos = [fila,columna]
        if fila < 0 or fila > self.alto:
            return False
        if columna < 0 or columna > self.ancho:
            return False
        for i in self.obstaculos:
            if i == pos:
                return False
        return True
    

class Nodo:
    def __init__(self, pos_f, pos=[0, 0], padre=None):
        self.pos = pos
        self.padre = padre
        self.h = distancia(self.pos, pos_f)

        if self.padre == None:
            self.g = 0
        else:
            self.g = self.padre.g + 1

        # Peso del nodo
        self.f = self.g + self.h


class Aestrella:
    def __init__(self, map):
        self.abiertos = []
        self.cerrados = []
        self.mapa = map
        self.abiertos.append(self.mapa.origen)

    def algoritmo(self):
        while nodo_menor(self.abiertos).pos != self.mapa.destino.pos:
            menor = nodo_menor(self.abiertos)
            self.abiertos.remove(menor)
            self.gen_hijos(menor)
            self.cerrados.append(menor)
        return nodo_menor(self.abiertos)

    def imprimir_camino(self,nodo):
        camino = []
        while True:
            camino.append(nodo.pos)
            if nodo.padre == None:
                break
            nodo = nodo.padre
        for i in reversed(camino):
            print(i)
    
    def gen_hijos(self, padre):
        # Arriba
        if self.mapa.casilla_libre(padre.pos[0] - 1,padre.pos[1]):
            hijo = Nodo(self.mapa.destino.pos,[padre.pos[0] - 1,padre.pos[1]],padre)
            self.meter_en_lista(hijo)  
        # Abajo
        if self.mapa.casilla_libre(padre.pos[0] + 1,padre.pos[1]):
            hijo = Nodo(self.mapa.destino.pos,[padre.pos[0] + 1,padre.pos[1]],padre)
            self.meter_en_lista(hijo)
        #Izquierda
        if self.mapa.casilla_libre(padre.pos[0],padre.pos[1] - 1):
            hijo = Nodo(self.mapa.destino.pos,[padre.pos[0],padre.pos[1] - 1],padre)
            self.meter_en_lista(hijo)
        #Derecha
        if self.mapa.casilla_libre(padre.pos[0],padre.pos[1] + 1):
            hijo = Nodo(self.mapa.destino.pos,[padre.pos[0],padre.pos[1] + 1],padre)
            self.meter_en_lista(hijo)
   
    def meter_en_lista(self, nodo):
        nodo_igual = 0
        for i in self.abiertos:
            if nodo.pos == i.pos:
                nodo_igual = i
        if nodo_igual == 0:
            self.abiertos.append(nodo)
        elif nodo.f < nodo_igual.f:
            self.abiertos.remove(nodo_igual)
            self.abiertos.append(nodo)


# Distancia entre dos puntos.
def distancia(a, b):
    # heurística de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Valor absoluto.

def nodo_menor(lista):
    menor = lista[0]
    for i in range(1,len(lista)):
        if lista[i].f <= menor.f:
            menor = lista[i]
    return menor

def main():
    fil = 5
    col = 5
    lista_obst = [[0,1],[1,1],[1,3],[1,4],[3,2],[3,4],[4,2]]
    ori = [0,0]
    dest = [4,4]

    map = Mapa(fil,col,lista_obst,ori,dest)
    astar = Aestrella(map)
    astar.imprimir_camino(astar.algoritmo())

main()



