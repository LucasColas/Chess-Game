import pygame

from .constants import Width, Height, Rows,Cols,Square
from .constants import beige, brown_chocolate


class newBoard:
    def __init__(self, Width, Height,Win):
        self.Width = Width
        self.Height = Height
        self.GameBoard = self.Width//2
        self.Win = Win


    #def create_GameBoard(self): #Add outline
        #pygame.draw.rect(self.Win, cornsilk, (160, 160,480, 480))

    def create_Board(self):
        self.Win.fill(beige)

        for row in range(Rows):
            for col in range(Cols):
                if row%2 == 0 and col%2==0:
                    pygame.draw.rect(self.Win,brown_chocolate,(Square*row, Square*col,Square,Square))

                #if (row+1)%2 == 0 and (col+1)%2==0:
                    #pygame.draw.rect(self.Win,brown_chocolate,(Square*(row+1), Square*(col+1),Square,Square))

        #Operational
        #for row in range(Rows):
            #for col in range(row%2, Cols,2):
                #pygame.draw.rect(self.Win,brown_chocolate,(Square*(row), Square*(col),Square,Square))
