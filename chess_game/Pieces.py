import pygame
from .constants import *


class Piece:
    def __init__(self, Square,image,row,col):
        self.Square = Square
        self.image = image
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.first_move = True
        self.image = image
        self.calc_pos()

    def check_color(self, piece):
        pass

    def available_moves(self):
        pass

    def calc_pos(self):
        self.x = self.col*self.Square
        self.y = self.row*self.Square

    def draw_piece(self,Win):
        Win.blit(self.image, (self.x, self.y))


class Pawn(Piece):
    def __init__(self,Square, image,row,col):
        super().__init__(Square, image,row,col)


    def available_moves(self):

        if self.first_move:
            self.first_move = False

class Rook(Piece):
    def __init__(self, Square, image,row,col):
        super().__init__(Square, image,row,col)

    def test(self):
        print("test")

class Bishop(Piece):
    def __init__(self, Square, image,row,col):
        super().__init__(Square, image,row,col)

class Knight(Piece):
    def __init__(self, Square, image,row,col):
        super().__init__(Square, image,row,col)

class Queen(Piece):
    def __init__(self, Square, image,row,col):
        super().__init__(Square, image,row,col)

class King(Piece):
    def __init__(self, image,x,y):
        super().__init__(image)