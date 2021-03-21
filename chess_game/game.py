import pygame
from .board import newBoard
from .constants import *

class Game:
    def __init__(self, Width, Height, Rows, Cols, Square,Win):
        self.Win = Win
        self.Board = newBoard(Width, Height, Rows, Cols,Square, Win)
        self.Square = Square
        self.selected = None
        self.turn = White
        self.valid_moves = []
        self.Black_pieces_left = 16
        self.White_pieces_left = 16

    def update_window(self):

        self.Board.draw_Board()
        #Board.draw_test()
        self.Board.draw_pieces()
        self.draw_available_moves()
        pygame.display.update()

    def reset(self):
        self.Board = newBoard(Width, Height, Rows, Cols,Square, Win)
        self.Square = Square
        self.selected = None

    def check_game(self):
        if self.Black_pieces_left == 0:
            print("Whites win")

        if self.White_pieces_left == 0:
            print("Blacks win")


    def enemies_moves(self,piece):
        enemies_moves = []
        for r in range(len(self.Board.Board)):
            for c in range(len(self.Board.Board[r])):
                if self.Board.Board[r][c] != 0:
                    if self.Board.Board[r][c].color != piece.color:
                        moves = self.Board.Board[r][c].get_available_moves(r,c,self.Board.Board)
                        for move in moves:
                            enemies_moves.append(move)

        return enemies_moves



    def checkmate(self, piece,row,col):
        if piece.type == "King":
            if (row,col) in self.enemies_moves(piece):
                if self.ennemies_moves(piece).count((row,col)) > 1:
                    while (row,col) in piece.available_moves:
                        piece.available_moves.remove((row,col))

    def change_turn(self):
        if self.turn == White:
            self.turn = Black
        else:
            self.turn = White



    def select(self,row,col):

        if self.selected:
            #print("selected")
            self.checkmate(self.selected,row,col)
            move = self._move(row,col)

            if not move:
                #print("in not move")
                self.selected = None
                self.select(row,col)

        piece = self.Board.get_piece(row,col)
        if piece != 0 and self.turn == piece.color:
            self.selected = piece
            #print(piece)
            self.valid_moves = piece.get_available_moves(row,col,self.Board.Board)



    def _move(self,row,col):
        piece = self.Board.get_piece(row,col)

        if self.selected and (row,col) in self.valid_moves:
            if piece == 0 or piece.color != self.selected.color:
                self.remove(piece,row,col)
                self.Board.move(self.selected,row,col)
                self.change_turn()
                self.valid_moves = []
                self.selected = None

            return True

        return False


    def remove(self,piece,row,col):
        if piece != 0:
            self.Board.Board[row][col] = 0
            if piece.color == White:
                self.White_pieces_left -= 1
            else:
                self.Black_pieces_left -= 1
        print("White_pieces_left : ", self.White_pieces_left)
        print("Black_pieces_left : ", self.Black_pieces_left)


    def draw_available_moves(self):
        if len(self.valid_moves) > 0:
            for pos in self.valid_moves:
                row,col = pos[0],pos[1]
                pygame.draw.circle(self.Win, Green, (col*self.Square + self.Square//2, row*self.Square + self.Square//2),self.Square//8)
