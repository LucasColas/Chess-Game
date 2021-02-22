import pygame

from chess_game.board import *
from chess_game.constants import *

Win = pygame.display.set_mode(())

def update_window(Win):
    pygame.display.update()

def main():
    run = True

    while run:
