import pygame
import constants

#def test_piece(Win):
    #Win.blit(constants.Black_King, (25,25))


class Piece:
    def __init__(self, image):
        self.image = image


class Pawn(Piece):
    def __init__(self, image):
        super().__init__(image)

class Rook(Piece):
    def __init__(self, image):
        super().__init__(image)

class Bishop(Piece):
    def __init__(self, image):
        super().__init__(image)

class Knight(Piece):
    def __init__(self, image):
        super().__init__(image)

class Queen(Piece):
    def __init__(self, image):
        super().__init__(image)

class King(Piece):
    def __init__(self, image):
        super().__init__(image)
