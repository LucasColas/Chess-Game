import pygame

from chess_game.constants import *
from chess_game.board import newBoard
from chess_game.Pieces import test_piece

pygame.init()

Win = pygame.display.set_mode((Width, Height))
Board = newBoard(Width, Height, Win)

def update_window(Win):

    Board.create_Board()
    Board.draw_test()
    test_piece(Win)
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
