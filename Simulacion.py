import pygame
import sys
import random
from pygame import draw
from pygame.constants import RESIZABLE
from pygame.mouse import get_pressed

from py_matrix import Matriz

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


def Click_Manual(is_running, ancho, alto):
    
    count = 0
    x_start = 0
    y_start = 0

    # Matriz de la que partimos (por defecto)
    matriz_a = Matriz(ancho, alto)

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Ventana de coche autonomo")
    CLOCK = pygame.time.Clock()     # Creo que es necesario para funciones del sistema
    

    while is_running:
        SCREEN.fill(FLOOR_RGB)

        drawGrid(matriz_a)
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
                    count = count + 1
                    break
                if count == 1:
                    matriz_a.set_value(actual_x, actual_y, END_ID)
                    x_start = actual_x
                    y_start = actual_y
                    count = count + 1
                    break
                if count >= 2:
                    matriz_a.set_value(actual_x, actual_y, OBSTACLE_ID)
                    count = count + 1
                    break

            # Si mantienes click derecho
            if (pygame.mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == OBSTACLE_ID):
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)

            if (pygame.mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == START_ID):
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)
                count = 0
                matriz_a.set_value(x_start, y_start, FLOOR_ID)

            if (pygame.mouse.get_pressed()[2]) & (matriz_a.get_value(actual_x, actual_y) == END_ID):
                matriz_a.set_value(actual_x, actual_y, FLOOR_ID)
                count = 1

            #
            # Espacio para el resto de colores y cosas
            #

            # Buenas practicas para cuando se redimensiona la pantalla
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        

def drawGrid(matriz_a):

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
    print("Crear")

    
def Crear_Aleatorio(is_running, ancho, alto, porcentaje_obs):   
    
    # Matriz de la que partimos (por defecto)
    matriz_b = Matriz(ancho, alto)
    x = 0

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Ventana de coche autonomo")
    CLOCK = pygame.time.Clock()   
    
    x_start = random.randint(0,ancho-1)
    y_start = random.randint(0,alto-1)
        
    matriz_b.set_value(random.randint(0,ancho-1), random.randint(0,alto-1), START_ID)
    if matriz_b.get_value(x_start, y_start) != START_ID:
        matriz_b.set_value(x_start, y_start, END_ID)
    while x < porcentaje_obs:
        x_ = random.randint(0,ancho-1)
        y_ = random.randint(0,alto-1)
        if ((matriz_b.get_value(x_, y_) != OBSTACLE_ID) & (matriz_b.get_value(x_, y_) != START_ID) & (matriz_b.get_value(x_, y_) != END_ID)):
            matriz_b.set_value(x_, y_, OBSTACLE_ID)
            x = x + 1

    while is_running:
        SCREEN.fill(FLOOR_RGB)

        drawGrid(matriz_b)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Crear_Simulacion()

