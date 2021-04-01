import pygame
from .constants import *


class Piece:
    def __init__(self, Square,image,color,type,row,col):
        self.Square = Square
        self.image = image
        self.color = color
        self.row = row
        self.col = col
        self.type = type
        self.x = 0
        self.y = 0
        self.image = image
        self.available_moves = []
        self.calc_pos()


    def piece_move(self,row,col):
        self.row = row
        self.col = col
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col*self.Square
        self.y = self.row*self.Square

    def clear_available_moves(self):
        if len(self.available_moves) > 0:
            self.available_moves = []



class Pawn(Piece):
    def __init__(self,Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)
        self.first_move = True


    def get_available_moves(self,row,col,Board):

        self.clear_available_moves()

        #Works for white pawns
        #To do : add limit to avoid index out of range
        if self.color == White:
            if row-1 >= 0:
                if Board[row-1][col] == 0:
                    self.available_moves.append((row-1,col))

                if self.first_move:
                    if Board[row-2][col] == 0:
                        self.available_moves.append((row-2,col))

                if col-1 >= 0:
                    if Board[row-1][col-1] != 0:
                        piece = Board[row-1][col-1]
                        if piece.color != self.color:
                            self.available_moves.append((row-1,col-1))

            if col+1 < len(Board[0]):
                if Board[row-1][col+1] != 0:
                    piece = Board[row-1][col+1]
                    if piece.color != self.color:
                        self.available_moves.append((row-1,col+1))

        #Works for black pawns
        if self.color == Black:

            if row+1 < len(Board):
                if Board[row+1][col] == 0:
                    self.available_moves.append((row+1,col))

                if self.first_move:
                    if Board[row+1][col] == 0 and Board[row+2][col] == 0:
                        self.available_moves.append((row+2,col))

                if col-1 >= 0:
                    if Board[row+1][col-1] != 0:
                        piece = Board[row+1][col-1]
                        if piece.color != self.color:
                            self.available_moves.append((row+1,col-1))

            if row+1 < len(Board) and col+1 < len(Board[0]):
                if Board[row+1][col+1] != 0:
                    piece = Board[row+1][col+1]
                    if piece.color != self.color:
                        self.available_moves.append((row+1,col+1))


        return self.available_moves




class Rook(Piece):
    def __init__(self, Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)

    def get_available_moves(self,row,col,Board):
        self.clear_available_moves()
        for i in range(row+1, 8):

            if Board[i][col] == 0:

                self.available_moves.append((i,col))
            else:
                if Board[i][col].color != self.color:

                    self.available_moves.append((i,col))
                    break
                else:
                    break

        for j in range(row-1,-1,-1):

            if Board[j][col] == 0:

                self.available_moves.append((j,col))

            else:
                if Board[j][col].color != self.color:

                    self.available_moves.append((j,col))
                    break

                else:

                    break

        for i in range(col+1, 8):
            if Board[row][i] == 0:
                self.available_moves.append((row,i))

            else:
                if Board[row][i].color != self.color:
                    self.available_moves.append((row,i))
                    break

                else:
                    break

        for i in range(col-1, -1,-1):

            if Board[row][i] == 0:
                self.available_moves.append((row,i))

            else:
                if Board[row][i].color != self.color:
                    self.available_moves.append((row,i))
                    break

                else:
                    break


        return self.available_moves


class Bishop(Piece):
    def __init__(self, Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)

    def get_available_moves(self,row,col,Board):
        self.clear_available_moves()

        row_i = row+1
        col_i = col+1
        while row_i <= 7 and col_i <= 7:
            if Board[row_i][col_i] == 0:
                #print("first loop : ",row_i, col_i)
                self.available_moves.append((row_i,col_i))
                row_i += 1
                col_i += 1

            else:
                if Board[row_i][col_i].color != self.color:
                    #print("first loop : ",row_i,col_i)
                    self.available_moves.append((row_i,col_i))
                    break
                break

        row_i = row-1
        col_i = col-1
        while row_i >= 0 and col_i >= 0:

            if Board[row_i][col_i] == 0:
                self.available_moves.append((row_i,col_i))
                #print("second loop ",row_i, col_i)
                row_i -= 1
                col_i -= 1

            else:
                if Board[row_i][col_i].color != self.color:
                    #print("second loop",row_i, col_i)
                    self.available_moves.append((row_i,col_i))
                    break
                break



        row_i = row-1
        col_i = col+1
        while row_i >= 0 and col_i <= 7:


            if Board[row_i][col_i] == 0:
                #print("third loop",row_i, col_i)
                self.available_moves.append((row_i, col_i))
                row_i -= 1
                col_i += 1

            else:
                if Board[row_i][col_i].color != self.color:
                    #print("third loop",row_i, col_i)
                    self.available_moves.append((row_i, col_i))
                    break

                break

        row_i = row+1
        col_i = col-1
        while row_i <= 7 and col_i >= 0:

            #print(Board[row_i][col_i])
            if Board[row_i][col_i] == 0:
                #print("fourth loop",row_i, col_i)
                self.available_moves.append((row_i, col_i))
                row_i += 1
                col_i -= 1
            else:
                if Board[row_i][col_i].color != self.color :
                    #print("fourth loop",row_i, col_i)
                    self.available_moves.append((row_i, col_i))
                    break

                break

        return self.available_moves


class Knight(Piece):
    def __init__(self, Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)

    def get_available_moves(self,row,col,Board):
        self.clear_available_moves()

        if row-2 >= 0 and col+1 < len(Board):
            if Board[row-2][col+1] == 0 or Board[row-2][col+1].color != self.color:
                self.available_moves.append((row-2,col+1))

        if row-1 >= 0 and col+2 < len(Board):
            if Board[row-1][col+2] == 0 or Board[row-1][col+2].color != self.color:
                self.available_moves.append((row-1,col+2))

        if row+1 < len(Board) and col+2 < len(Board):
            if Board[row+1][col+2] == 0 or Board[row+1][col+2].color != self.color:
                self.available_moves.append((row+1,col+2))

        if row+2 < len(Board) and col+1 < len(Board):
            if Board[row+2][col+1] == 0 or Board[row+2][col+1].color != self.color:
                self.available_moves.append((row+2,col+1))

        if row+2 < len(Board) and col-1 >= 0:
            if Board[row+2][col-1] == 0 or Board[row+2][col-1].color != self.color:
                self.available_moves.append((row+2,col-1))

        if row+1 < len(Board) and col-2 >= 0:
            if Board[row+1][col-2] == 0 or Board[row+1][col-2].color != self.color:
                self.available_moves.append((row+1,col-2))


        if row-1 >= 0 and col-2 >= 0:
            if Board[row-1][col-2] == 0 or Board[row-1][col-2].color != self.color:
                self.available_moves.append((row-1,col-2))

        if row-2 >= 0 and col-1 >= 0:
            if Board[row-2][col-1] == 0 or Board[row-2][col-1].color != self.color:
                self.available_moves.append((row-2,col-1))


        return self.available_moves


class Queen(Piece):
    def __init__(self, Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)

    def get_available_moves(self,row,col,Board):
        self.clear_available_moves()

        row_i = row+1
        col_i = col+1
        while row_i <= 7 and col_i <= 7:
            if Board[row_i][col_i] == 0:
                #print("first loop : ",row_i, col_i)
                self.available_moves.append((row_i,col_i))
                row_i += 1
                col_i += 1

            else:
                if Board[row_i][col_i].color != self.color:
                    #print("first loop : ",row_i,col_i)
                    self.available_moves.append((row_i,col_i))
                    break
                break

        row_i = row-1
        col_i = col-1
        while row_i >= 0 and col_i >= 0:

            if Board[row_i][col_i] == 0:
                self.available_moves.append((row_i,col_i))
                #print("second loop ",row_i, col_i)
                row_i -= 1
                col_i -= 1

            else:
                if Board[row_i][col_i].color != self.color:
                    #print("second loop",row_i, col_i)
                    self.available_moves.append((row_i,col_i))
                    break
                break



        row_i = row-1
        col_i = col+1
        while row_i >= 0 and col_i <= 7:


            if Board[row_i][col_i] == 0:
                #print("third loop",row_i, col_i)
                self.available_moves.append((row_i, col_i))
                row_i -= 1
                col_i += 1
            else:
                if Board[row_i][col_i].color != self.color:
                    #print("third loop",row_i, col_i)
                    self.available_moves.append((row_i, col_i))
                    break

                break

        row_i = row+1
        col_i = col-1
        while row_i <= 7 and col_i >= 0:

            #print(Board[row_i][col_i])
            if Board[row_i][col_i] == 0:
                #print("fourth loop",row_i, col_i)
                self.available_moves.append((row_i, col_i))
                row_i += 1
                col_i -= 1

            else:
                if Board[row_i][col_i].color != self.color :
                    #print("fourth loop",row_i, col_i)
                    self.available_moves.append((row_i, col_i))
                    break

                break


        for i in range(row+1, 8):

            if Board[i][col] == 0:

                self.available_moves.append((i,col))
            else:
                if Board[i][col].color != self.color:

                    self.available_moves.append((i,col))
                    break
                else:
                    break

        for j in range(row-1,-1,-1):

            if Board[j][col] == 0:

                self.available_moves.append((j,col))

            else:
                if Board[j][col].color != self.color:

                    self.available_moves.append((j,col))
                    break

                else:

                    break

        for i in range(col+1, 8):
            if Board[row][i] == 0:
                self.available_moves.append((row,i))

            else:
                if Board[row][i].color != self.color:
                    self.available_moves.append((row,i))
                    break

                else:
                    break

        for i in range(col-1, -1,-1):

            if Board[row][i] == 0:
                self.available_moves.append((row,i))

            else:
                if Board[row][i].color != self.color:
                    self.available_moves.append((row,i))
                    break

                else:
                    break

        return self.available_moves



class King(Piece):
    def __init__(self,Square, image,color,type,row,col):
        super().__init__(Square, image,color,type,row,col)




    def get_available_moves(self,row,col,Board):
        self.clear_available_moves()

        if row-1 >= 0:
            if Board[row-1][col] == 0 or Board[row-1][col].color != self.color:
                self.available_moves.append((row-1,col))

        if row-1 >= 0 and col+1 < len(Board):
            if Board[row-1][col+1] == 0 or Board[row-1][col+1].color != self.color:
                self.available_moves.append((row-1,col+1))

        if col+1 < len(Board):
            if Board[row][col+1] == 0 or Board[row][col+1].color != self.color:
                self.available_moves.append((row,col+1))

        if row+1 < len(Board) and col+1 < len(Board):
            if Board[row+1][col+1] == 0 or Board[row+1][col+1].color != self.color:
                self.available_moves.append((row+1,col+1))

        if row+1 < len(Board):
            if Board[row+1][col] == 0 or Board[row+1][col].color != self.color:
                self.available_moves.append((row+1,col))

        if row+1 < len(Board) and col-1 >= 0:
            if Board[row+1][col-1] == 0 or Board[row+1][col-1].color != self.color:
                self.available_moves.append((row+1,col-1))

        if col-1 >= 0:
            if Board[row][col-1] == 0 or Board[row][col-1].color != self.color:
                self.available_moves.append((row,col-1))

        if row-1 >= 0 and col-1 >= 0:
            if Board[row-1][col-1] == 0 or Board[row-1][col-1].color != self.color:
                self.available_moves.append((row-1, col-1))


        return self.available_moves
