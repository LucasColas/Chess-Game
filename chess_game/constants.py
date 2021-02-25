import pygame
import os

#Size
Width, Height = 800,800
Rows, Cols = 8,8
Square = Width//8

#Colors
Bg = (47,79,79)
Black = (0,0,0)
White = (255,255,255)
beige = (245,245,220)
brown_chocolate = (210,105,30)
brown = (10,10,10)
cornsilk = (255,248,220)

#Images
#Black pieces
Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bN")), (Square, Square))
Black_Bishop = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bB")), (Square, Square))
Black_King = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bK")), (Square, Square))
Black_pawn = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bp")), (Square, Square))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bQ")), (Square, Square))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bR")), (Square, Square))
