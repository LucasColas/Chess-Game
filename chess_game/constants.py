import pygame
import os

#Size
Width, Height = 760,760
Rows, Cols = 8,8
Square = Width//Rows

#Colors
Bg = (47,79,79)
Black = (0,0,0)
White = (255,255,255)
beige = (245,245,220)
brown_chocolate = (210,105,30)
brown = (87,16,16)
cornsilk = (255,248,220)
Green = (0,255,0)

#Images
#Black pieces
Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images","bKN.png")), (Square, Square))
Black_Bishop = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "bB.png")), (Square, Square))
Black_King = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "bK.png")), (Square, Square))
Black_pawn = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "bP.png")), (Square, Square))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "bQ.png")), (Square, Square))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "bR.png")), (Square, Square))
#White pieces
White_Knight = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "wKN.png")), (Square, Square))
White_bishop = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "wB.png")), (Square, Square))
White_King = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "wK.png")), (Square, Square))
White_pawn = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "wp.png")), (Square, Square))
White_Queen = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "wQ.png")), (Square, Square))
White_Rook = pygame.transform.scale(pygame.image.load(os.path.join("chess_game\chess_images", "wR.png")), (Square, Square))
