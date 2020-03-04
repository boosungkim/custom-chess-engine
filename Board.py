#
# The Chess Board class
#
from Piece import Rook, Knight, Bishop, Queen, King, Pawn
from enums import Player

# TODO: update teams to players
# TODO: Finalize move piece
# TODO: Change printBoard to for loops
class Board:
    # Initialize 2D array to represent the chess board
    def __init__(self):
        self.board = [[None] * 8] * 8
        self.whiteCaptives = []
        self.blackCaptives = []

        # Initialize White pieces
        wR1 = Rook('R', 0, 0, Player.PLAYER_1)
        wR2 = Rook('R', 7, 0, 'white')
        wN1 = Knight('N', 2, 0, 'white')
        wN2 = Knight('N', 6, 0, 'white')
        wB1 = Bishop('B', 2, 0, 'white')
        wB2 = Bishop('B', 5, 0, 'white')
        wQ = Queen('Q', 3, 0, 'white')
        wK = King('K', 4, 0, 'white')
        wP1 = Pawn('P', 0, 1, 'white')
        wP2 = Pawn('P', 1, 1, 'white')
        wP3 = Pawn('P', 2, 1, 'white')
        wP4 = Pawn('P', 3, 1, 'white')
        wP5 = Pawn('P', 4, 1, 'white')
        wP6 = Pawn('P', 5, 1, 'white')
        wP7 = Pawn('P', 6, 1, 'white')
        wP8 = Pawn('P', 7, 1, 'white')
        self.whitePieces = [wR1, wR2, wN1, wN2, wB1, wB2, wQ, wK, wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8]

        # Initialize Black Pieces
        bR1 = Rook('r', 0, 7, 'white')
        bR2 = Rook('r', 7, 7, 'white')
        bN1 = Knight('n', 2, 7, 'white')
        bN2 = Knight('n', 6, 7, 'white')
        bB1 = Bishop('b', 2, 7, 'white')
        bB2 = Bishop('b', 5, 7, 'white')
        bQ = Queen('q', 3, 7, 'white')
        bK = King('k', 4, 7, 'white')
        bP1 = Pawn('p', 0, 6, 'white')
        bP2 = Pawn('p', 1, 6, 'white')
        bP3 = Pawn('p', 2, 6, 'white')
        bP4 = Pawn('p', 3, 6, 'white')
        bP5 = Pawn('p', 4, 6, 'white')
        bP6 = Pawn('p', 5, 6, 'white')
        bP7 = Pawn('p', 6, 6, 'white')
        bP8 = Pawn('p', 7, 6, 'white')
        self.blackPieces = [bR1, bR2, bN1, bN2, bB1, bB2, bQ, bK, bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8]

        for i in range(0, 16):
            self.board[self.whitePieces[i].getX()][self.whitePieces[i].getY()] = self.whitePieces[i]
            self.board[self.blackPieces[i].getX()][self.blackPieces[i].getY()] = self.blackPieces[i]

    def getPiece(self, row, col):
        return self.board[row][col]

    # Move a piece
    def movePiece(self, currentX, currentY, nextX, nextY):
        currentPiece = self.getPiece(currentX, currentY)
        if (currentX, currentY) in currentPiece.getMoves():
            currentPiece.x = nextX
            currentPiece.y = nextY
        else:
            print("Cannot be moved here\n")

    def printBoard(self):
        print("_ _ _ _ _ _ _ _\n")
        print("|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.getPiece(0, 7), self.getPiece(1, 7), self.getPiece(2, 7),
                                                   self.getPiece(3, 7), self.getPiece(4, 7), self.getPiece(5, 7),
                                                   self.getPiece(6, 7), self.getPiece(7, 7)))
        print("|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.getPiece(0, 6), self.getPiece(1, 6), self.getPiece(2, 6),
                                                   self.getPiece(3, 6), self.getPiece(4, 6), self.getPiece(5, 6),
                                                   self.getPiece(6, 6), self.getPiece(7, 6)))
        print("|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.getPiece(0, 5), self.getPiece(1, 5), self.getPiece(2, 5),
                                                   self.getPiece(3, 5), self.getPiece(4, 5), self.getPiece(5, 5),
                                                   self.getPiece(6, 5), self.getPiece(7, 5)))
        print("|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.getPiece(0, 4), self.getPiece(1, 4), self.getPiece(2, 4),
                                                   self.getPiece(3, 4), self.getPiece(4, 4), self.getPiece(5, 4),
                                                   self.getPiece(6, 4), self.getPiece(7, 4)))
        print("|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.getPiece(0, 3), self.getPiece(1, 3), self.getPiece(2, 3),
                                                   self.getPiece(3, 3), self.getPiece(4, 3), self.getPiece(5, 3),
                                                   self.getPiece(6, 3), self.getPiece(7, 3)))
        print("|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.getPiece(0, 2), self.getPiece(1, 2), self.getPiece(2, 2),
                                                   self.getPiece(3, 2), self.getPiece(4, 2), self.getPiece(5, 2),
                                                   self.getPiece(6, 2), self.getPiece(7, 2)))
        print("|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.getPiece(0, 1), self.getPiece(1, 1), self.getPiece(2, 1),
                                                   self.getPiece(3, 1), self.getPiece(4, 1), self.getPiece(5, 1),
                                                   self.getPiece(6, 1), self.getPiece(7, 1)))
        print("|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.getPiece(0, 0), self.getPiece(1, 0), self.getPiece(2, 0),
                                                   self.getPiece(3, 0), self.getPiece(4, 0), self.getPiece(5, 0),
                                                   self.getPiece(6, 0), self.getPiece(7, 0)))
        print("_ _ _ _ _ _ _ _\n")
