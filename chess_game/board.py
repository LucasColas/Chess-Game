import pygame
from .Pieces import *


class newBoard:
    def __init__(self, Width, Height, Rows, Cols, Win):
        self.Width = Width
        self.Height = Height
        self.Square = Width//8
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
                    self.Board[row][col] = Pawn(self.Square,Black_pawn,"Black",row,col)
                if row == 6:
                    self.Board[row][col] = Pawn(self.Square,White_pawn,"White",row,col)

                if row == 0:
                    if col == 0 or col == 7:
                        self.Board[row][col] = Rook(self.Square, Black_Rook,"Black",row,col)

                    if col == 1 or col == 6:
                        self.Board[row][col] = Knight(self.Square, Black_Knight,"Black",row,col)

                    if col == 2 or col == 5:
                        self.Board[row][col] = Bishop(self.Square, Black_Bishop,"Black",row,col)

                    if col == 3:
                        self.Board[row][col] = Queen(self.Square, Black_Queen,"Black",row,col)

                    if col == 4:
                        self.Board[row][col] = King(self.Square, Black_King,"Black",row,col)

                if row == 7:
                    if col == 0 or col  == 7:
                        self.Board[row][col] = Rook(self.Square, White_Rook,"White",row,col)

                    if col == 1 or col == 6:
                        self.Board[row][col] = Knight(self.Square, White_Knight,"White",row,col)

                    if col == 2 or col == 5:
                        self.Board[row][col] = Bishop(self.Square, White_bishop,"White",row,col)

                    if col == 3:
                        self.Board[row][col] = Queen(self.Square, White_Queen,"White",row,col)

                    if col == 4:
                        self.Board[row][col] = King(self.Square, White_King,"White",row,col)

    def select_pieces(self,x,y):
        if self.Board[y][x] != 0:
            

    def select_pieces(self,x,y):
        pass

    def draw_Board(self):
        self.Win.fill(brown)

        for row in range(Rows):
            for col in range(row%2, Cols,2):
                pygame.draw.rect(self.Win,White,(Square*(row), Square*(col),Square,Square))

    def draw_test(self):
        self.Win.blit(White_Knight, (self.Width//2, self.Width//2))

    def draw_pieces(self):
        for row in range(self.Rows):
            for col in range(self.Cols):

                if self.Board[row][col] != 0:
                    self.Board[row][col].draw_piece(self.Win)
