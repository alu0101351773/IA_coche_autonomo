import pygame
import sys

from pygame.constants import RESIZABLE

from py_matrix import Matriz

# Ignorar, esto es de mi clase py_matrix
# from py_matrix import *

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

INITIAL_WINDOW_HEIGHT = 600
INITIAL_WINDOW_WIDTH = 600

matriz_a = Matriz(10, 10)

block_height = 0
block_width = 0

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Ventana de coche autonomo")
    CLOCK = pygame.time.Clock()
    

    while True:
        SCREEN.fill(WHITE)

        global block_height
        global block_width

        block_height = SCREEN.get_height() // matriz_a.get_height()
        block_width = SCREEN.get_width() // matriz_a.get_width()

        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        pygame.display.update()


def drawGrid():
    # blockSize = 5 #Set the size of the grid block
    for x in range(0, SCREEN.get_width(), block_height):
        for y in range(0, SCREEN.get_height(), block_width):
            rect = pygame.Rect(x, y, block_height, block_width)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

# https://www.programiz.com/python-programming/matrix
main()

