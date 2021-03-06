import pygame

from chess_game.constants import *
from chess_game.game import Game


pygame.init()
clock = pygame.time.Clock()

Win = pygame.display.set_mode((Width, Height))
Board = newBoard(Width, Height, Rows, Cols, Win)



def main():
    run = True
    game_over = False
    White = "White"
    Black = "Black"
    turn = White
    FPS = 60
    game = Game(Width,Height,Rows,Cols,Win)


    while run:
        clock.tick(FPS)

        #Board.update_window(Win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE and game_over:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                if pygame.mouse.get_pressed()[0]:
                    location = pygame.mouse.get_pos()

                if turn == White:
                    turn = Black

                else:
                    turn = White




main()
