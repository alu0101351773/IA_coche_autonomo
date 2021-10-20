
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


def gen_hijos(map, lista, padre):
    # Arriba
    if map.casilla_libre(padre.pos[0] - 1,padre.pos[1]):
        lista.append(Nodo(map.destino,[padre.pos[0] - 1,padre.pos[1]],padre))
    # Abajo
    if map.casilla_libre(padre.pos[0] + 1,padre.pos[1]):
        lista.append(Nodo(map.destino,[padre.pos[0] + 1,padre.pos[1]],padre))
    #Izquierda
    if map.casilla_libre(padre.pos[0],padre.pos[1] - 1):
        lista.append(Nodo(map.destino,[padre.pos[0],padre.pos[1] - 1],padre))
    #Derecha
    if map.casilla_libre(padre.pos[0],padre.pos[1] + 1):
        lista.append(Nodo(map.destino,[padre.pos[0],padre.pos[1] + 1],padre))

def main():
    fil = 5
    col = 5
    lista_obst = [[0,1],[1,1],[1,3],[1,4],[3,2],[3,4],[4,2]]
    ori = [0,0]
    dest = [4,4]
    map = Mapa(fil,col,lista_obst,ori,dest)
    abiertos = []
    cerrados = []
    abiertos.append(Nodo(map.destino,map.origen))
    while nodo_menor(abiertos).pos != map.destino:
        menor = nodo_menor(abiertos)
        abiertos.remove(menor)
        gen_hijos(map, abiertos, menor)
        cerrados.append(menor)
    casilla = nodo_menor(abiertos)
    camino = []
    while True:
        camino.append(casilla.pos)
        if casilla.padre == None:
            break
        casilla = casilla.padre
    for i in range(len(camino)):
        print(camino[i], " ")

main()



