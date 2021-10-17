import pygame
import sys
from pygame.constants import RESIZABLE

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
INITIAL_WINDOW_HEIGHT = 900
INITIAL_WINDOW_WIDTH = 900

# Matriz de la que partimos (por defecto)
matriz_a = Matriz(50, 50)



def main(is_running):
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
                sys.exit()
            
            # si se pulsa en la interfaz
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                actual_x = int( (x / block_width ) % matriz_a.get_width() )
                actual_y = int( (y / block_height ) % matriz_a.get_height() )
            
                if (event.button == 1) & (matriz_a.get_value(actual_x, actual_y) == FLOOR_ID):
                    matriz_a.set_value(actual_x, actual_y, OBSTACLE_ID)
                    print("pinchado para colocar bloque")

                if (event.button == 3) & (matriz_a.get_value(actual_x, actual_y) == OBSTACLE_ID):
                    matriz_a.set_value(actual_x, actual_y, FLOOR_ID)
                    print("pinchado para colocar camino")

                #
                # Espacio para cuando se implemente el algoritmo
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
                pygame.draw.rect(SCREEN, END_ID, rect, 0)

            y += block_height
        x += block_width

# Inicio del programa
main(True)