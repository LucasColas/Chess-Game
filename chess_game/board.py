import pygame

from .constants import Width, Height, Rows,Cols,Square
from .constants import White, brown, Black
from .constants import White_Knight


class newBoard:
    def __init__(self, Width, Height, Rows, Cols, Win):
        self.Width = Width
        self.Height = Height
        self.GameBoard = self.Width//2
        self.Win = Win
        self.Rows = Rows
        self.Cols = Cols


    #def create_GameBoard(self): #Add outline
        #pygame.draw.rect(self.Win, cornsilk, (160, 160,480, 480))

    def create_Board(self):
        self.Win.fill(Black)

        for row in range(Rows):
            for col in range(row%2, Cols,2):
                pygame.draw.rect(self.Win,White,(Square*(row), Square*(col),Square,Square))

    def draw_test(self):
        self.Win.blit(White_Knight, (self.Width//2, self.Width//2))

    def draw_pieces(self):
        for row in self.Rows:
            for col in self.Cols:
                if row == 1:
                    self.Win.blit(White_pawn, (Square*col, Square*row))
