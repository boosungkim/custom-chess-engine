#
# The Chess Piece Class
#

#from abc import ABC

# General chess piece
class Piece:
    # Initialize the piece
    def __init__(self,name,locX,locY):
        self.name=name
        self.x=locX
        self.y=locY
        self.avail=[]

    # Get moves
    # @later add as abstract class method
    def getMoves(self):
        pass

    # Move a piece
    def movePiece(self,locX,locY):
        if (locX,locY) in self.avail:
            self.x=locX
            self.y=locY
        else:
            print("Cannot be moved here\n")

# Rook (R)
class Rook(Piece):
    # Get moves
    def getMove(self):
        # Left of the Rook
        for i in range(1,self.x): 
            if Board.bd[i][self.y] == null:
                self.avail.append((i,self.y))
            else:
                break
        # Right of the Rook
        for i in range(self.x+1,9):
            if Board.bd[i][self.y]==null:
                self.avail.append((i,self.y))
            else:
                break
        # Below the Rook
        for i in range(1,self.y):
            if Board.bd[self.x][i] == null:
                self.avail.append((self.x,i))
            else:
                break
        # Above the Rook
        for i in range(self.y+1,9):
            if Board.bd[self.x][i] == null:
                self.avail.append((self.x,i))
            else:
                break

        return self.avail

# Knight (N)
class Knight(Piece):
    # Get moves
    def getMoves(self):
        if 0<(self.x-2)<9:
            if 0<(self.y-1)<9 && Board.bd[self.x-2][self.y-1]:
                self.avail.append((self.x-2,self.y-1))
            if 0<(self.y+1)<9:
                self.avail.append((self.x-2,self.y-1))
        if 0<(self.x-1)<9:
            if 0<(self.y-2)<9:
                self.avail.append((self.x-2,self.y-1))
            if 0<self.y-













