import pygame
from .board import newBoard
from .constants import *

class Game:
    def __init__(self, Width, Height, Rows, Cols, Win):
        self.Win = Win
        self.Board = newBoard(Width, Height, Rows, Cols,Win)
        self.selected = None
        self.turn = White
        self.valid_moves = {}

    def update_window(self):

        self.Board.draw_Board()
        #Board.draw_test()
        self.Board.draw_pieces()
        pygame.display.update()

    def reset(self):
        pass

    def change_turn(self):
        if self.turn == White:
            self.turn = Black
        else:
            self.turn = White

    def select(self,row,col):
        if self.selected:
            move = self._move(row,col)

            if not move:
                self.selected = None
                self.select(row,col)

        piece = self.Board.get_piece(row,col)
        if piece != 0:
            self.selected = piece


    def _move(self,row,col):
        piece = self.Board.get_piece(row,col)

        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.Board.move(piece,row,col)
            
