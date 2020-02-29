#
# The Chess Board class
#

class Board:
    
    # Initialize 2D array to represent the chess board
    board = []

    def __init__(self):
        self.board=[[None]*8]*8]
    
    def getPiece(self, row, col):
        return self.board[row][col]
