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

    def select(self,row,col):
        #print(self.Board.Board)
        print("select / row col", row,col)
        if self.selected:
            #print("in self.selected")
            move = self._move(row,col)
            #print("move", move)
            if not move:
                #print("not move")
                self.selected = None
                self.select(row,col)

        piece = self.Board.get_piece(row,col)
        #print("piece", piece)
        if piece != 0:
            self.selected = piece
            #print(self.selected)
            self.valid_moves = piece.available_moves(row,col,self.Board.Board)


    def _move(self,row,col):
        #print("in _move")
        print("_move / row,col", row,col)
        piece = self.Board.get_piece(row,col)
        #print("valid_moves", self.valid_moves)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.Board.move(self.selected,row,col)

            return True

        return False
