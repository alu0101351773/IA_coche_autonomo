TRUE = 1

from pygame import draw, init, display, mouse, Rect, QUIT, RESIZABLE, KEYDOWN, K_SPACE, VIDEORESIZE
from pygame import event as Event
from pygame import quit as Quit

import random

from py_matrix import Matriz
from Algoritmo_A import *

# Constantes de colores
OBSTACLE_ID = 1
OBSTACLE_RGB = (0, 0, 0)

FLOOR_ID = 0
FLOOR_RGB = (200, 200, 200)

START_ID = 2
START_RGB = (0, 255, 0)

PATH_ID = 3
PATH_RGB = (255, 222, 84)

END_ID = 4
END_RGB = (255, 0, 0)

ROUTE_ID = 5
ROUTE_RGB = (133, 136, 239)

CHECK_ID = 6
CHECK_RGB = (224, 191, 148)


# Tamaño inicial de la ventana
INITIAL_WINDOW_HEIGHT = 600
INITIAL_WINDOW_WIDTH = 500

# Matriz de la que partimos (por defecto)
matriz_a = Matriz()

def ResetGrid():
    x = 0
    while x < matriz_a.get_width() :
        y = 0
        while y < matriz_a.get_height() :
            cell_value = matriz_a.get_value(x, y)
            if (cell_value == ROUTE_ID) | (cell_value == CHECK_ID):
                matriz_a.set_value(x, y, FLOOR_ID)

            y += 1
        
        x += 1

def Click_Manual(is_running, aleatorio, fichero, porcentaje_obs, direcciones, nom_fich, algoritmo):
    
    count = 0
    x_end = 0
    y_end = 0
    x_start = 0
    y_start = 0

    start = [0, 0]
    end = [0, 0]
    lista_obst = []
    coordenada_obst = [0, 0]

    global SCREEN, CLOCK
    init()
    SCREEN = display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), RESIZABLE)
    display.set_caption("Ventana de coche autonomo")
    
    if aleatorio == TRUE:
        count = 2
        x = 0

        x_start = random.randint(0, matriz_a.get_width()-1)
        y_start = random.randint(0, matriz_a.get_height()-1)
        start = [x_start, y_start]

        matriz_a.set_value(x_start, y_start, START_ID)
        
        x_end = random.randint(0, matriz_a.get_width()-1)
        y_end = random.randint(0, matriz_a.get_height()-1)

        while (matriz_a.get_value(x_end, y_end) == START_ID) | (matriz_a.get_value(x_end, y_end) == OBSTACLE_ID):
            x_end = random.randint(0, matriz_a.get_width()-1)
            y_end = random.randint(0, matriz_a.get_height()-1)
        end = [x_end, y_end]
        matriz_a.set_value(x_end, y_end, END_ID)
            
        while x < porcentaje_obs:
            x_ = random.randint(0,matriz_a.get_width()-1)
            y_ = random.randint(0, matriz_a.get_height()-1)
            if ((matriz_a.get_value(x_, y_) != OBSTACLE_ID) & (matriz_a.get_value(x_, y_) != START_ID) & (matriz_a.get_value(x_, y_) != END_ID)):
                matriz_a.set_value(x_, y_, OBSTACLE_ID)
                coordenada_obst = [x_, y_]
                lista_obst.append(coordenada_obst)
            
                x = x + 1

    if fichero == TRUE:
        count = 2
        lista = []
        archivo = open(nom_fich, "r")
        caracter = archivo.read(1)
        col = 0
        fila = 0
        x = 0

        while caracter != "":
            lista.append(caracter)
            caracter = archivo.read(1)
        
        alto = int(lista[0])
        ancho = int(lista[2])
        matriz_a.resize(alto, ancho)

        for y in range(4):
            lista.pop(x)

        while x < len(lista):
                                    
            if lista[x] == "1":
                coor_obs = [col, fila]
                lista_obst.append(coor_obs)
                matriz_a.set_value(col, fila, OBSTACLE_ID)
                
            if lista[x] == "2":
                matriz_a.set_value(col, fila, START_ID)
                start = [col, fila]

            if lista[x] == "3":
                matriz_a.set_value(col, fila, END_ID)
                end = [col, fila]

            col = col + 1
            
            if lista[x] == "\n":
                col = 0
                fila = fila + 1

            x = x + 1

    while is_running:
        SCREEN.fill(FLOOR_RGB)

        
        if matriz_a.was_changed == True:
            drawGrid()
            matriz_a.was_changed = False
            print("Impreso")
            display.update()

        for event in Event.get():
            
            # Si se cierra el programa
            if event.type == QUIT:
                Quit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    ResetGrid()
                    Crear_Simulacion(start, end, lista_obst, direcciones, algoritmo)
            
            # Si se pulsa en la interfaz
            x, y = mouse.get_pos()

            actual_x = int((x / block_width) % matriz_a.get_width())
            actual_y = int((y / block_height) % matriz_a.get_height())

            # Si mantienes click izquierdo
            if (mouse.get_pressed()[0]) & ((matriz_a.get_value(actual_x, actual_y) == FLOOR_ID)
                                               | (matriz_a.get_value(actual_x, actual_y) == ROUTE_ID)
                                               | (matriz_a.get_value(actual_x, actual_y) == CHECK_ID)):
                if count == 0:
                    matriz_a.set_value(actual_x, actual_y, START_ID)
                    start = [actual_x, actual_y]
                    count = count + 1
                    break

                if count == 1:
                    matriz_a.set_value(actual_x, actual_y, END_ID)
                    x_end = actual_x
                    y_end = actual_y
                    end = [x_end, y_end]
                    count = count + 1
                    break

                if count >= 2:
                    matriz_a.set_value(actual_x, actual_y, OBSTACLE_ID)
                    coordenada_obst = [actual_x, actual_y]
                    lista_obst.append(coordenada_obst)
                    count = count + 1
                    break

            # Si mantienes click derecho
            if (mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == OBSTACLE_ID):
                lista_obst.pop(lista_obst.index([actual_x, actual_y]))
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)

            if (mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == START_ID):
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)
                start = [actual_x, actual_y]
                matriz_a.set_value(x_end, y_end, FLOOR_ID)
                end = [x_end, y_end]
                count = 0

            if (mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == END_ID):
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)
                end = [actual_x, actual_y]
                count = 1

            #
            # Espacio para el resto de colores y cosas
            #

            # Buenas practicas para cuando se redimensiona la pantalla
            if event.type == VIDEORESIZE:
                matriz_a.was_changed = True
                SCREEN = display.set_mode((event.w, event.h), RESIZABLE)

        

def drawGrid():

    global block_height
    global block_width

    block_height = SCREEN.get_height() / matriz_a.get_height()
    block_width = SCREEN.get_width() / matriz_a.get_width()

    x = 0
    while x < SCREEN.get_width():
        auxiliar_x = round(x / block_width ) % matriz_a.get_width()

        y = 0
        while y < SCREEN.get_height():
            auxiliar_y = round(y / block_height ) % matriz_a.get_height() 

            rect = Rect(x, y, block_width, block_height)

            cell_value = matriz_a.get_value(auxiliar_x, auxiliar_y)
            if cell_value == FLOOR_ID :
                draw.rect(SCREEN, OBSTACLE_RGB, rect, 1)

            elif cell_value == OBSTACLE_ID:
                draw.rect(SCREEN, OBSTACLE_RGB, rect, 0)

            elif cell_value == START_ID:
                draw.rect(SCREEN, START_RGB, rect, 0)

            elif cell_value == PATH_ID:
                draw.rect(SCREEN, PATH_RGB, rect, 0)
            
            elif cell_value == END_ID:
                draw.rect(SCREEN, END_RGB, rect, 0)
            
            elif cell_value == ROUTE_ID:
                draw.rect(SCREEN, ROUTE_RGB, rect, 0)
            
            elif cell_value == CHECK_ID:
                draw.rect(SCREEN, CHECK_RGB, rect, 0)

            y += block_height
        x += block_width


def Crear_Simulacion(start, end, lista_obst, direcciones, algoritmo):
    import time
    start_time = time.time()
    
    map = Mapa(matriz_a.get_height(), matriz_a.get_width(), lista_obst, start, end)
    abiertos = []
    cerrados = []
    abiertos.append(Nodo(end, start))
    camino = []
    sol = False
    while len(abiertos) > 0:
        menor, index = nodo_menor(abiertos)
        abiertos.pop(index)
        cerrados.append(menor)
        if menor.pos == end:
            while menor != None:
                camino.append(menor.pos)
                menor = menor.padre
            sol = True
            break

        if direcciones == 4:
            gen_hijos_4(map, abiertos, cerrados, menor, algoritmo)
        if direcciones == 8:
            gen_hijos_8(map, abiertos, cerrados, menor, algoritmo)

    end_time = time.time()
    if not sol:
        print("NO SOLUTION")
    for i in range(len(camino)-2):
        x_, y_ = camino[i+1]
        matriz_a.set_value(x_, y_, ROUTE_ID)
    
    print(end_time - start_time)


def gen_hijos_4(map, lista_abierta, lista_cerrada ,padre, algoritmo):
    # Arriba
    if map.casilla_libre(padre.pos[0] - 1,padre.pos[1]) and not is_in_set(lista_cerrada, Nodo(map.destino,[padre.pos[0] - 1,padre.pos[1]],padre, algoritmo), 0):
        if not is_in_set(lista_abierta, padre, 1):
            lista_abierta.append(Nodo(map.destino,[padre.pos[0] - 1,padre.pos[1]],padre, algoritmo))
            # if (matriz_a.get_value(padre.pos[0] - 1, padre.pos[1]) != START_ID) & (matriz_a.get_value(padre.pos[0] - 1, padre.pos[1]) != END_ID):
            #     matriz_a.set_value(padre.pos[0] - 1, padre.pos[1], CHECK_ID)
    # Abajo
    if map.casilla_libre(padre.pos[0] + 1,padre.pos[1]) and not is_in_set(lista_cerrada, Nodo(map.destino,[padre.pos[0] + 1,padre.pos[1]],padre, algoritmo), 0):
        if not is_in_set(lista_abierta, padre, 1):
            lista_abierta.append(Nodo(map.destino,[padre.pos[0] + 1,padre.pos[1]],padre, algoritmo))
            # if (matriz_a.get_value(padre.pos[0] + 1, padre.pos[1]) != START_ID) & (matriz_a.get_value(padre.pos[0] + 1, padre.pos[1]) != END_ID): 
            #     matriz_a.set_value(padre.pos[0] + 1, padre.pos[1], CHECK_ID)
    #Izquierda
    if map.casilla_libre(padre.pos[0],padre.pos[1] - 1) and not is_in_set(lista_cerrada, Nodo(map.destino,[padre.pos[0] ,padre.pos[1] - 1],padre, algoritmo), 0):
        if not is_in_set(lista_abierta, padre, 1):
            lista_abierta.append(Nodo(map.destino,[padre.pos[0],padre.pos[1] - 1],padre, algoritmo))
            # if (matriz_a.get_value(padre.pos[0], padre.pos[1] - 1) != START_ID) & (matriz_a.get_value(padre.pos[0], padre.pos[1] - 1) != END_ID): 
            #     matriz_a.set_value(padre.pos[0], padre.pos[1] - 1, CHECK_ID)
    #Derecha
    if map.casilla_libre(padre.pos[0],padre.pos[1] + 1) and not is_in_set(lista_cerrada, Nodo(map.destino,[padre.pos[0],padre.pos[1] + 1],padre, algoritmo), 0):
        if not is_in_set(lista_abierta, padre, 1):
            lista_abierta.append(Nodo(map.destino,[padre.pos[0],padre.pos[1] + 1],padre, algoritmo))
            # if (matriz_a.get_value(padre.pos[0], padre.pos[1] + 1) != START_ID) & (matriz_a.get_value(padre.pos[0], padre.pos[1] + 1) != END_ID): 
            #     matriz_a.set_value(padre.pos[0], padre.pos[1] + 1, CHECK_ID)

def gen_hijos_8(map, lista_abierta, lista_cerrada, padre, algoritmo):
    gen_hijos_4(map, lista_abierta, lista_cerrada, padre, algoritmo)
    # Arriba-Izquierda
    if map.casilla_libre(padre.pos[0] - 1,padre.pos[1] - 1) and not is_in_set(lista_cerrada, Nodo(map.destino,[padre.pos[0] - 1,padre.pos[1] - 1],padre, algoritmo), 0):
        if not is_in_set(lista_abierta, padre, 1):
            lista_abierta.append(Nodo(map.destino,[padre.pos[0] - 1,padre.pos[1] - 1],padre, algoritmo))
            # if (matriz_a.get_value(padre.pos[0] - 1, padre.pos[1] - 1) != START_ID) & (matriz_a.get_value(padre.pos[0] - 1, padre.pos[1] - 1) != END_ID): 
            #     matriz_a.set_value(padre.pos[0] - 1, padre.pos[1] - 1, CHECK_ID)
    # Arriba-Derecha
    if map.casilla_libre(padre.pos[0] - 1,padre.pos[1] + 1) and not is_in_set(lista_cerrada, Nodo(map.destino,[padre.pos[0] - 1,padre.pos[1] + 1],padre, algoritmo), 0):
        if not is_in_set(lista_abierta, padre, 1):
            lista_abierta.append(Nodo(map.destino,[padre.pos[0] - 1,padre.pos[1] + 1],padre, algoritmo))
            # if (matriz_a.get_value(padre.pos[0] - 1, padre.pos[1] + 1) != START_ID) & (matriz_a.get_value(padre.pos[0] - 1, padre.pos[1] + 1) != END_ID): 
            #     matriz_a.set_value(padre.pos[0] - 1, padre.pos[1] + 1, CHECK_ID)
    # Abajo-Izquierda
    if map.casilla_libre(padre.pos[0] + 1,padre.pos[1] - 1) and not is_in_set(lista_cerrada, Nodo(map.destino,[padre.pos[0] + 1,padre.pos[1] - 1],padre, algoritmo), 0):
        if not is_in_set(lista_abierta, padre, 1):
            lista_abierta.append(Nodo(map.destino,[padre.pos[0] + 1,padre.pos[1] - 1],padre, algoritmo))
            # if (matriz_a.get_value(padre.pos[0] + 1, padre.pos[1] - 1) != START_ID) & (matriz_a.get_value(padre.pos[0] + 1, padre.pos[1] - 1) != END_ID): 
            #     matriz_a.set_value(padre.pos[0] + 1, padre.pos[1] - 1, CHECK_ID)
    # Abajo-Derecha
    if map.casilla_libre(padre.pos[0] + 1,padre.pos[1] + 1) and not is_in_set(lista_cerrada, Nodo(map.destino,[padre.pos[0] + 1,padre.pos[1] + 1],padre, algoritmo), 0):
        if not is_in_set(lista_abierta, padre, 1):
            lista_abierta.append(Nodo(map.destino,[padre.pos[0] + 1,padre.pos[1] + 1],padre, algoritmo))
            # if (matriz_a.get_value(padre.pos[0] + 1, padre.pos[1] + 1) != START_ID) & (matriz_a.get_value(padre.pos[0] + 1, padre.pos[1] + 1) != END_ID): 
            #     matriz_a.set_value(padre.pos[0] + 1, padre.pos[1] + 1, CHECK_ID)
