#
# The Chess Piece Class
#
# TODO: add changeLocation function
# TODO: change avail to moves
# TODO: Fix Bishop getMoves()
# TODO: create capture ability function

# General chess piece
class Piece:
    # Initialize the piece
    def __init__(self, name, locationX, locationY, player):
        self.name = name
        self.x = locationX
        self.y = locationY
        self.moves = []
        self.player = player

    # Get the x value
    def getX(self):
        return self.x

    # Get the y value
    def getY(self):
        return self.y

    # Get the name
    def getName(self):
        return self.name

    # Get moves
    # @later add as abstract class method
    def getMoves(self, board):
        pass


# Rook (R)
class Rook(Piece):
    # Get moves
    def getMoves(self, board):
        self.avail.clear()
        # Left of the Rook
        for i in range(self.x - 1, -1, -1):
            if board.getPiece(i, self.y) is None:
                self.avail.append((i, self.y))
            else:
                break
        # Right of the Rook
        for i in range(self.x + 1, 8):
            if board.getPiece(i, self.y) is None:
                self.avail.append((i, self.y))
            else:
                break
        # Below the Rook
        for i in range(self.y - 1, -1, -1):
            if board.getPiece(self.x, i) is None:
                self.avail.append((self.x, i))
            else:
                break
        # Above the Rook
        for i in range(self.y + 1, 8):
            if board.getPiece(self.x, i) is None:
                self.avail.append((self.x, i))
            else:
                break
        return self.moves


# Knight (N)
class Knight(Piece):
    # Get moves
    def getMoves(self, board):
        self.avail.clear()
        xChange = [-2, -2, -1, -1, +1, +1, +2, +2]
        yChange = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(0, 9):
            newX = self.x + xChange[i]
            newY = self.y + yChange[i]
            if (-1 < newX < 9) and (-1 < newY < 9) and board.getPiece(newX, newY) is None:
                self.avail.append((newX, newY))
        return self.avail


# Bishop
# TODO: Fix getMoves() function
class Bishop(Piece):
    def getMoves(self, board):
        self.avail.clear()
        for i in range(self.x - 1, -1, -1):
            for j in range(self.y - 1, -1, -1):
                if board.getPiece(i, j) is None:
                    self.avail.append((i, j))
                else:
                    break
            for j in range(self.y + 1, 8):
                if board.getPiece(i, j) is None:
                    self.avail.append((i, j))
                else:
                    break
        for i in range(self.x + 1, 8):
            for j in range(self.y - 1, -1, -1):
                if board.getPiece(i, j) is None:
                    self.avail.append((i, j))
                else:
                    break
            for j in range(self.y + 1, 8):
                if board.getPiece(i, j) is None:
                    self.avail.append((i, j))
                else:
                    break
        return self.avail


# Pawn
class Pawn(Piece):
    def getMoves(self, board):
        self.avail.clear()
        if self.team == 'white' and board.getPiece(self.x, self.y + 1) is None:
            if self.y == 1:
                self.avail.append((self.x, self.y + 1))
                self.avail.append((self.x, self.y + 2))
            else:
                self.avail.append((self.x, self.y + 1))
        elif self.team == 'black' and board.getPiece(self.x, self.y - 1) is None:
            if self.y == 6:
                self.avail.append((self.x, self.y - 1))
                self.avail.append((self.x, self.y - 2))
            else:
                self.avail.append((self.x, self.y - 1))
        return self.avail

    # TODO: Change the pawn based on the input from user
    def promotePawn(self):
        newPiece = input("Change pawn to: ")


# Queen
class Queen(Bishop, Rook):
    def getMoves(self, board):
        self.avail.clear()
        self.avail.append(Rook.getMoves(self, board=board))
        self.avail.append(Bishop.getMoves(self, board=board))


# King
class King(Piece):
    def getMoves(self, board):
        self.avail.clear()
        xChange = [-1, -1, -1, +0, +0, +1, +1, +1]
        yChange = [-1, +0, +1, -1, +1, -1, +0, +1]
        for i in range(0, 8):
            newX = self.x + xChange[i]
            newY = self.y + yChange[i]
            if board.getPiece(newX, newY) is None:
                self.avail.append((newX, newY))
