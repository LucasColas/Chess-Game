import pygame

from chess_game.constants import *
from chess_game.board import newBoard

pygame.init()

Win = pygame.display.set_mode((Width, Height))
Board = newBoard(Width, Height, Win)

def update_window(Win):
    Win.fill(beige)
    pygame.display.update()

def main():
    run = True

    while run:
        update_window(Win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

main()
