from tkinter.constants import TRUE
import pygame
import sys
import random
from pygame import draw
from pygame.constants import RESIZABLE
from pygame.mouse import get_pressed

from py_matrix import Matriz
from Algoritmo_A import *

# Constantes de colores
OBSTACLE_ID = 1
OBSTACLE_RGB = (0, 0, 0)

FLOOR_ID = 0
FLOOR_RGB = (200, 200, 200)

END_ID = 4
END_RGB = (255, 0, 0)

START_ID = 2
START_RGB = (0, 255, 0)

PATH_ID = 3
PATH_RGB = (255, 222, 84)


# Tamaño inicial de la ventana
INITIAL_WINDOW_HEIGHT = 600
INITIAL_WINDOW_WIDTH = 500

# Matriz de la que partimos (por defecto)
matriz_a = Matriz()
start = []
end = []
lista_obst = [[]]

def Click_Manual(is_running, aux):
    
    count = 0
    x_end = 0
    y_end = 0
    
    if aux == TRUE:
        count = 2

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Ventana de coche autonomo")
    CLOCK = pygame.time.Clock()     # Creo que es necesario para funciones del sistema

    while is_running:
        SCREEN.fill(FLOOR_RGB)

        drawGrid()
        pygame.display.update()

        for event in pygame.event.get():
            
            # Si se cierra el programa
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Crear_Simulacion()
            
            # Si se pulsa en la interfaz
            x, y = pygame.mouse.get_pos()

            actual_x = int( (x / block_width ) % matriz_a.get_width() )
            actual_y = int( (y / block_height ) % matriz_a.get_height() )

            # Si mantienes click izquierdo
            if (pygame.mouse.get_pressed()[0]) & (matriz_a.get_value(actual_x, actual_y) == FLOOR_ID):
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
                    lista_obst.insert([actual_x, actual_y])
                    count = count + 1
                    break

            # Si mantienes click derecho
            if (pygame.mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == OBSTACLE_ID):
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)
                lista_obst.remove([actual_x, actual_y])

            if (pygame.mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == START_ID):
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)
                matriz_a.set_value(x_end, y_end, FLOOR_ID)
                count = 0
                start = []
                end = []

            if (pygame.mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == END_ID):
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)
                count = 1
                end = []

            #
            # Espacio para el resto de colores y cosas
            #

            # Buenas practicas para cuando se redimensiona la pantalla
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        

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

            rect = pygame.Rect(x, y, block_width, block_height)

            cell_value = matriz_a.get_value(auxiliar_x, auxiliar_y)
            if cell_value == FLOOR_ID :
                pygame.draw.rect(SCREEN, OBSTACLE_RGB, rect, 1)

            elif cell_value == OBSTACLE_ID:
                pygame.draw.rect(SCREEN, OBSTACLE_RGB, rect, 0)

            elif cell_value == START_ID:
                pygame.draw.rect(SCREEN, START_RGB, rect, 0)

            elif cell_value == PATH_ID:
                pygame.draw.rect(SCREEN, PATH_RGB, rect, 0)
            
            elif cell_value == END_ID:
                pygame.draw.rect(SCREEN, END_RGB, rect, 0)

            y += block_height
        x += block_width


def Crear_Simulacion():
    lista_obst = [[0,1],[1,1],[1,3],[1,4],[3,2],[3,4],[4,2]]
    map = Mapa(matriz_a.get_height(), matriz_a.get_width(), lista_obst, start, end)
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
    #print("Crear")

    
def Crear_Aleatorio(porcentaje_obs):   
    
    x = 0

    x_start = random.randint(0, matriz_a.get_width()-1)
    y_start = random.randint(0, matriz_a.get_height()-1)
        
    matriz_a.set_value(random.randint(0, matriz_a.get_height()-1), random.randint(0, matriz_a.get_width()-1), START_ID)
    if matriz_a.get_value(y_start, x_start) != START_ID:
        matriz_a.set_value(y_start, x_start, END_ID)
        
    while x < porcentaje_obs:
        x_ = random.randint(0,matriz_a.get_width()-1)
        y_ = random.randint(0, matriz_a.get_height()-1)
        if ((matriz_a.get_value(y_, x_) != OBSTACLE_ID) & (matriz_a.get_value(y_, x_) != START_ID) & (matriz_a.get_value(y_, x_) != END_ID)):
            matriz_a.set_value(y_, x_, OBSTACLE_ID)
            x = x + 1