import pygame
from .board import newBoard
from .constants import *

class Game:
    def __init__(self, Width, Height, Rows, Cols, Win):
        self.Win = Win
        self.Board = newBoard(Width, Height, Rows, Cols,Win)
        self.selected = None
        self.turn = White
        self.valid_moves = []

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

    def draw_available_moves(self,Win):
        if len(available_moves) > 0:
            for pos in available_moves:
                pygame.draw.circle(Win, Green, (pos[0]*self.Square + self.Square//2, pos[1]*self.Square + self.Square//2),self.Square//4)

    def select(self,row,col):

        if self.selected:
            move = self._move(row,col)
            if not move:
                self.selected = None
                self.select(row,col)

        piece = self.Board.get_piece(row,col)
        if piece != 0 and self.turn == piece.color:
            self.selected = piece
            self.valid_moves = piece.get_available_moves(row,col,self.Board.Board)


    def _move(self,row,col):
        piece = self.Board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.Board.move(self.selected,row,col)
            self.change_turn()
            return True

        return False
