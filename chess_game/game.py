import pygame
from .board import newBoard
from .constants import *

class Game:
    def __init__(self, Width, Height, Rows, Cols, Win):
        self.Win = Win
        self.Board = newBoard(Width, Height, Rows, Cols,Win)
        self.selected = None

    def update_window(self):

        self.Board.draw_Board()
        #Board.draw_test()
        self.Board.draw_pieces()
        pygame.display.update()

    def reset(self):
        pass


    def select(self,row,col):
        if self.select:
            move = self._move(row,col)


    def _move(self,row,col):
        pass 
