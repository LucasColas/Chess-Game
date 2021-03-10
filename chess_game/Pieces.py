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
        self.image = image
        self.available_moves = []
        self.calc_pos()


    def piece_move(self,row,col):
        self.row = row
        self.col = col
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col*self.Square
        self.y = self.row*self.Square


    def draw_piece(self,Win):
        Win.blit(self.image, (self.x, self.y))

    def draw_available_moves(self,Win):
        if len(available_moves) > 0:
            for pos in available_moves:
                pygame.draw.circle(Win, Green, (pos[0]*self.Square + self.Square//2, pos[1]*self.Square + self.Square//2),self.Square//4)


class Pawn(Piece):
    def __init__(self,Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)
        self.first_move = True


    def get_available_moves(self,row,col,Board):


        if Board[row-1][col] == 0:
            self.available_moves.append((row-1,col))

        if self.first_move:
            if Board[row-2][col] == 0:
                self.available_moves.append((row-2,col))
            self.first_move = False

        if Board[row-1][col-1] != 0:
            piece = Board[row-1][col-1]
            if piece.color != self.color:
                self.available_moves.append((row-1,col-1))

        if Board[row-1][col+1] != 0:
            piece = Board[row-1][col+1]
            if piece.color != self.color:
                self.available_moves.append((row-1,col+1))

        return self.available_moves




class Rook(Piece):
    def __init__(self, Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)




class Bishop(Piece):
    def __init__(self, Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)


class Knight(Piece):
    def __init__(self, Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)


class Queen(Piece):
    def __init__(self, Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)


class King(Piece):
    def __init__(self,Square, image,color,row,col):
        super().__init__(Square, image,color,row,col)
