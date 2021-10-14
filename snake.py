import pygame
import sys

from pygame.constants import RESIZABLE

from py_matrix import Matriz

# Ignorar, esto es de mi clase py_matrix
# from py_matrix import *

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)

INITIAL_WINDOW_HEIGHT = 900
INITIAL_WINDOW_WIDTH = 900

matriz_a = Matriz(2, 2)

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
            
            # Innecesario, pero lo dejo por si en un futuro
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        

def drawGrid():

    block_height = SCREEN.get_height() // matriz_a.get_height()
    block_width = SCREEN.get_width() // matriz_a.get_width()

    # blockSize = 5 #Set the size of the grid block
    for x in range(0, SCREEN.get_width(), block_width):

        # Auxiliar
        auxiliar_x = (x // block_width) % matriz_a.get_width()

        for y in range(0, SCREEN.get_height(), block_height):
            
            # Auxiliar
            auxiliar_y = (y // block_height) % matriz_a.get_height()

            rect = pygame.Rect(x, y, block_width, block_height)

            print(auxiliar_x, auxiliar_y)

            if (auxiliar_x % 2 == 0) & (auxiliar_y % 2 == 0):
                pygame.draw.rect(SCREEN, RED, rect, 0)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect, 1)

main()