import pygame
from .board import newBoard
from .constants import *

class Game:
    def __init__(self, Width, Height, Rows, Cols, Square,Win):
        self.Win = Win
        self.Board = newBoard(Width, Height, Rows, Cols,Square, Win)
        self.Square = Square
        self.selected = None
        self.turn = White
        self.valid_moves = []

    def update_window(self):

        self.Board.draw_Board()
        #Board.draw_test()
        self.Board.draw_pieces()
        self.draw_available_moves()
        pygame.display.update()

    def reset(self):
        self.Board = newBoard(Width, Height, Rows, Cols,Square, Win)
        self.Square = Square
        self.selected = None

    def change_turn(self):
        if self.turn == White:
            self.turn = Black
        else:
            self.turn = White



    def select(self,row,col):

        if self.selected:
            #print("selected")
            move = self._move(row,col)

            if not move:
                #print("in not move")
                self.selected = None
                self.select(row,col)

        piece = self.Board.get_piece(row,col)
        if piece != 0 and self.turn == piece.color:
            self.selected = piece
            self.valid_moves = piece.get_available_moves(row,col,self.Board.Board)


    def _move(self,row,col):
        piece = self.Board.get_piece(row,col)

        if self.selected and (row,col) in self.valid_moves:
            if piece == 0 or piece.color != self.color:
                self.Board.move(self.selected,row,col)
                self.change_turn()
                self.valid_moves = []
                self.selected = None

            return True

        return False

    def draw_available_moves(self):
        if len(self.valid_moves) > 0:
            for pos in self.valid_moves:
                row,col = pos[0],pos[1]
                pygame.draw.circle(self.Win, Green, (col*self.Square + self.Square//2, row*self.Square + self.Square//2),self.Square//8)
