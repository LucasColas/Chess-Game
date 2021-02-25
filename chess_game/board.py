import pygame

from .constants import Width, Height, Rows,Cols,Square
from .constants import White, brown


class newBoard:
    def __init__(self, Width, Height,Win):
        self.Width = Width
        self.Height = Height
        self.GameBoard = self.Width//2
        self.Win = Win


    #def create_GameBoard(self): #Add outline
        #pygame.draw.rect(self.Win, cornsilk, (160, 160,480, 480))

    def create_Board(self):
        self.Win.fill(White)

        for row in range(Rows):
            for col in range(row%2, Cols,2):
                pygame.draw.rect(self.Win,brown,(Square*(row), Square*(col),Square,Square))
