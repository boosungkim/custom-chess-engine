#
# The Chess Piece Class
#
# Important notes:
#   Currently pieces are not capable of eating

# from abc import ABC

# General chess piece
from Board import Board


class Piece:
    # Initialize the piece
    def __init__(self, name, locX, locY, team):
        self.name = name
        self.x = locX
        self.y = locY
        self.avail = []
        self.team = team

    # Get moves
    # @later add as abstract class method
    def getMoves(self):
        pass

    # Move a piece
    def movePiece(self, locX, locY):
        if (locX, locY) in self.avail:
            self.x = locX
            self.y = locY
        else:
            print("Cannot be moved here\n")


# Rook (R)
class Rook(Piece):
    # Get moves
    def getMoves(self):
        self.avail.clear()
        # Left of the Rook
        for i in range(self.x - 1, -1, -1):
            if Board.getPiece(i, self.y) is None:
                self.avail.append((i, self.y))
            else:
                break
        # Right of the Rook
        for i in range(self.x + 1, 8):
            if Board.getPiece(i, self.y) is None:
                self.avail.append((i, self.y))
            else:
                break
        # Below the Rook
        for i in range(self.y - 1, -1, -1):
            if Board.getPiece(self.x, i) is None:
                self.avail.append((self.x, i))
            else:
                break
        # Above the Rook
        for i in range(self.y + 1, 8):
            if Board.getPiece(self.x, i) is None:
                self.avail.append((self.x, i))
            else:
                break
        return self.avail


# Knight (N)
class Knight(Piece):
    # Get moves
    def getMoves(self):
        self.avail.clear()
        xChange = [-2, -2, -1, -1, +1, +1, +2, +2]
        yChange = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(0, 9):
            newX = self.x + xChange[i]
            newY = self.y + yChange[i]
            if (-1 < newX < 9) and (-1 < newY < 9) and Board.getPiece(newX, newY) is None:
                self.avail.append((newX, newY))
        return self.avail


# Bishop
class Bishop(Piece):
    def getMoves(self):
        self.avail.clear()
        for i in range(self.x - 1, -1, -1):
            for j in range(self.y - 1, -1, -1):
                if Board.getPiece(i, j) is None:
                    self.avail.append((i, j))
                else:
                    break
            for j in range(self.y + 1, 8):
                if Board.getPiece(i, j) is None:
                    self.avail.append((i, j))
                else:
                    break
        for i in range(self.x + 1, 8):
            for j in range(self.y - 1, -1, -1):
                if Board.getPiece(i, j) is None:
                    self.avail.append((i, j))
                else:
                    break
            for j in range(self.y + 1, 8):
                if Board.getPiece(i, j) is None:
                    self.avail.append((i, j))
                else:
                    break
        return self.avail


# Pawn
class Pawn(Piece):
    def getMoves(self):
        self.avail.clear()
        if self.team == 'white' and Board.getPiece(self.x, self.y + 1) is None:
            if self.y == 1:
                self.avail.append((self.x, self.y + 1))
                self.avail.append((self.x, self.y + 2))
            else:
                self.avail.append((self.x, self.y + 1))
        elif self.team == 'black' and Board.getPiece(self.x, self.y - 1) is None:
            if self.y == 6:
                self.avail.append((self.x, self.y - 1))
                self.avail.append((self.x, self.y - 2))
            else:
                self.avail.append((self.x, self.y - 1))
        return self.avail

    def promotePawn(self):
        newPiece = input("Change pawn to: ")


# Queen
class Queen(Bishop, Rook):
    def getMoves(self):
        self.avail.clear()
        self.avail.append(Rook.getMoves(self))
        self.avail.append(Bishop.getMoves(self))


# King
class King(Piece):
    def getMoves(self):
        self.avail.clear()
        xChange = [-1, -1, -1, +0, +0, +1, +1, +1]
        yChange = [-1, +0, +1, -1, +1, -1, +0, +1]
        for i in range(0, 8):
            newX = self.x + xChange[i]
            newY = self.y + yChange[i]
            if Board.getPiece(newX, newY) is None:
                self.avail.append((newX, newY))
