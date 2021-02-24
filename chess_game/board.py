import pygame

from .constants import Width, Height, brown_chocolate, Rows,Cols


class newBoard:
    def __init__(self, Width, Height,Win):
        self.Width = Width
        self.Height = Height
        self.GameBoard = self.Width//2
        self.Win = Win


    #def create_GameBoard(self): #Add outline
        #pygame.draw.rect(self.Win, cornsilk, (160, 160,480, 480))

    def create_Board(self):
        for row in range(Rows):
            for col in range(Cols):
                if row%2 == 0 and col%2==0:
                    #Draw

                if (row+1)%2 == 0:
                    
