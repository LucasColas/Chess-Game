import pygame

from chess_game.constants import *
from chess_game.game import Game


pygame.init()
clock = pygame.time.Clock()

Win = pygame.display.set_mode((Width, Height))

def get_positions(x,y):
    row = y//Square
    col = x//Square

    return row,col


def main():
    run = True
    game_over = False
    turn = White
    FPS = 60
    game = Game(Width,Height,Rows,Cols,Square,Win)


    while run:
        clock.tick(FPS)

        game.update_window()
        if game.check_game():
            game_over = True
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE and game_over:
                    game.reset()


            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                if pygame.mouse.get_pressed()[0]:
                    location = pygame.mouse.get_pos()
                    row,col = get_positions(location[0],location[1])
                    #print(row,col)
                    game.select(row,col)




main()
