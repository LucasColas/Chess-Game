import pygame

from .constants import Width, Height, Rows,Cols,Square
from .constants import White, brown, Black
from .constants import Black_pawn
from .Pieces import *


class newBoard:
    def __init__(self, Width, Height, Rows, Cols, Win):
        self.Width = Width
        self.Height = Height
        self.GameBoard = self.Width//2
        self.Win = Win
        self.Rows = Rows
        self.Cols = Cols
        self.Board = []


    def create_Board(self):
        for row in range(self.Rows):
            self.Board.append([])
            for col in range(self.Cols):
                if row == 1:
                    self.Board[row].append()

    def create_Pieces(self):
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
                pass
