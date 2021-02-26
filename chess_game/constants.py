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
Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bN.png")), (Square, Square))
Black_Bishop = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bB.png")), (Square, Square))
Black_King = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bK.png")), (Square, Square))
Black_pawn = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bp.png")), (Square, Square))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bQ.png")), (Square, Square))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "bR.png")), (Square, Square))
#White pieces
White_Knight = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "wN.png")), (Square, Square))
White_bishop = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "wB.png")), (Square, Square))
White_King = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "wK.png")), (Square, Square))
White_pawn = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "wp.png")), (Square, Square))
White_Queen = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "wQ.png")), (Square, Square))
White_Rook = pygame.transform.scale(pygame.image.load(os.path.join("chess_images", "wR.png")), (Square, Square))
