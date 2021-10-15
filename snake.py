import pygame
import sys
import math

from pygame.constants import RESIZABLE

from py_matrix import Matriz

# Ignorar, esto es de mi clase py_matrix
# from py_matrix import *

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

INITIAL_WINDOW_HEIGHT = 900
INITIAL_WINDOW_WIDTH = 900

matriz_a = Matriz(21, 21)

# block_height = INITIAL_WINDOW_HEIGHT // matriz_a.get_height()
# block_width = INITIAL_WINDOW_WIDTH // matriz_a.get_width()


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Ventana de coche autonomo")
    CLOCK = pygame.time.Clock()
    

    while True:
        SCREEN.fill(WHITE)

        drawGrid()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print("clicked at:", x, y)
                actual_x = (x / block_width ) % matriz_a.get_width()
                actual_y = (y / block_height ) % matriz_a.get_height()
                print("Actual tiles:", actual_x, actual_y)

                math_x = int(actual_x)
                math_y = int(actual_y)
                print("Math tiles:", math_x, math_y)

                if (event.button == 1) & (matriz_a.get_value(math_x, math_y) != 1):
                    matriz_a.set_value(math_x, math_y, 1)

                if (event.button == 3) & (matriz_a.get_value(math_x, math_y) != 0):
                    matriz_a.set_value(math_x, math_y, 0)


            # Innecesario, pero lo dejo por si en un futuro
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        

def drawGrid():

    global block_height
    global block_width

    block_height = SCREEN.get_height() / matriz_a.get_height()
    block_width = SCREEN.get_width() / matriz_a.get_width()

    x = 0
    while x < SCREEN.get_width():
        
        auxiliar_x = int( (x / block_width ) % matriz_a.get_width() )

        y = 0
        while y < SCREEN.get_height():
            
            auxiliar_y = (y / block_height ) % matriz_a.get_height() 

            rect = pygame.Rect(x, y, block_width, block_height)

            cell_value = matriz_a.get_value(auxiliar_x, auxiliar_y)

            if cell_value == 1 :
                pygame.draw.rect(SCREEN, BLACK, rect, 0)
            elif cell_value == 0:
                pygame.draw.rect(SCREEN, BLACK, rect, 1)

            y += block_height
        x += block_width
main()