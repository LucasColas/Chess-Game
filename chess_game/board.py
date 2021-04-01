import pygame
from .Pieces import *
from .constants import *


class newBoard:
    def __init__(self, Width, Height, Rows, Cols, Square, Win):
        self.Width = Width
        self.Height = Height
        self.Square = Square
        self.GameBoard = self.Width//2
        self.Win = Win
        self.Rows = Rows
        self.Cols = Cols
        self.Board = []
        self.create_Board()



    def create_Board(self):
        for row in range(self.Rows):

            self.Board.append([0 for i in range(self.Cols)])

            for col in range(self.Cols):
                if row == 1:
                    self.Board[row][col] = Pawn(self.Square,Black_pawn,Black,"Pawn",row,col)
                if row == 6:
                    self.Board[row][col] = Pawn(self.Square,White_pawn,White,"Pawn",row,col)

                if row == 0:
                    if col == 0 or col == 7:
                        self.Board[row][col] = Rook(self.Square, Black_Rook,Black,"Rook",row,col)

                    if col == 1 or col == 6:
                        self.Board[row][col] = Knight(self.Square, Black_Knight,Black,"Knight",row,col)

                    if col == 2 or col == 5:
                        self.Board[row][col] = Bishop(self.Square, Black_Bishop,Black,"Bishop",row,col)

                    if col == 3:
                        self.Board[row][col] = Queen(self.Square, Black_Queen,Black,"Queen",row,col)

                    if col == 4:
                        self.Board[row][col] = King(self.Square, Black_King,Black,"King",row,col)

                if row == 7:
                    if col == 0 or col  == 7:
                        self.Board[row][col] = Rook(self.Square, White_Rook,White,"Rook",row,col)

                    if col == 1 or col == 6:
                        self.Board[row][col] = Knight(self.Square, White_Knight,White,"Knight",row,col)

                    if col == 2 or col == 5:
                        self.Board[row][col] = Bishop(self.Square, White_bishop,White,"Bishop",row,col)

                    if col == 3:
                        self.Board[row][col] = Queen(self.Square, White_Queen,White,"Queen",row,col)

                    if col == 4:
                        self.Board[row][col] = King(self.Square, White_King,White,"King",row,col)

    def get_piece(self,row,col):
        return self.Board[row][col]

    def move(self,piece,row,col):
        self.Board[piece.row][piece.col], self.Board[row][col] = self.Board[row][col], self.Board[piece.row][piece.col]
        piece.piece_move(row,col)

        if piece.type == "Pawn":
            if piece.first_move:
                piece.first_move = False


    def draw_Board(self):
        self.Win.fill(brown)

        for row in range(Rows):
            for col in range(row%2, Cols,2):
                pygame.draw.rect(self.Win,White,(Square*(row), Square*(col),Square,Square))

    def draw_piece(self,piece,Win):
        Win.blit(piece.image, (piece.x, piece.y))

    def draw_pieces(self):
        for row in range(self.Rows):
            for col in range(self.Cols):
                if self.Board[row][col] != 0:
                    self.draw_piece(self.Board[row][col], self.Win)
