import pygame
from .constants import *


class Piece:
    def __init__(self, image,x,y):
        self.image = image

    def available_moves(self):
        pass

    def calc_pos(self):
        self.x = self.row*self.Square
        self.y = self.row*self.Square

    def draw_piece(self,Win):
        Win.blit(self.image, (self.x, self.y))


class Pawn(Piece):
    def __init__(self,Square, image,row,col):
        super().__init__(image)
        self.Square = Square
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.first_move = True
        self.image = image
        self.calc_pos()



    def available_moves(self):

        if self.first_move:
            self.first_move = False

class Rook(Piece):
    def __init__(self, image,x,y):
        super().__init__(image)

class Bishop(Piece):
    def __init__(self, image,x,y):
        super().__init__(image)

class Knight(Piece):
    def __init__(self, image,x,y):
        super().__init__(image)

class Queen(Piece):
    def __init__(self, image,x,y):
        super().__init__(image)

class King(Piece):
    def __init__(self, image,x,y):
        super().__init__(image)
