import pygame
from .constants import *


class Piece:
    def __init__(self, Square,image,color,row,col):
        self.Square = Square
        self.image = image
        self.color = color
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.first_move = True
        self.image = image
        self.calc_pos()



    def available_moves(self):
        pass

    def piece_move(self,row,col):
        self.row = row
        self.col = row
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col*self.Square
        self.y = self.row*self.Square

    def draw_piece(self,Win):
        Win.blit(self.image, (self.x, self.y))


class Pawn(Piece):
    def __init__(self,Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)
        self.first_move = True
        self.type = "Pawn"


    def available_moves(self):

        if self.first_move:
            self.first_move = False

class Rook(Piece):
    def __init__(self, Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)
        self.type = "Rook"



class Bishop(Piece):
    def __init__(self, Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)
        self.type = "Bishop"

class Knight(Piece):
    def __init__(self, Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)
        self.type = "Knight"

class Queen(Piece):
    def __init__(self, Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)
        self.type = "Queen"

class King(Piece):
    def __init__(self,Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)
        self.type = "King"
