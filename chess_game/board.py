import pygame

from .constants import Width, Height, cornsilk


class newBoard:
    def __init__(self, Width, Height,Win):
        self.Width = Width
        self.Height = Height
        self.GameBoard = self.Width//2
        self.Win = Win


    def create_GameBoard(self): #Add outline
        pygame.draw.rect(self.Win, cornsilk, (self.Width//3, self.Width//3,self.GameBoard, self.GameBoard))
