#pragma once

#include <iostream>
#include "enum.h"

class Piece {
private:
    ChessPiece piece_name; // Name of the Chess piece
    int piece_row_position; // Row value of the current piece position
    int piece_col_position; // Column value of the current piece position
    Player piece_player; // The player controling the Chess piece
    bool has_moved {false};

public:
    Piece(ChessPiece name);
    Piece(ChessPiece name, int row, int col, Player player);

    // Return the current row value of the Chess piece
    int getRowValue(){ return piece_row_position; }

    // Return the current column value of the Chess piece
    int getColValue(){ return piece_col_position; }

    // Return the name of the Chess piece
    ChessPiece getName(){ return piece_name; }

    // Return the player controling the Chess piece
    Player getPlayer(){ return piece_player; }

    // Check if the piece has moved since the beginning of the game
    bool checkIfMoved(){ return has_moved; }

    // Return the current row value of the Chess piece
    void changeRowValue(int new_row_number);

    // Return the current column value of the Chess piece
    void changeColValue(int new_col_number);

    void pieceHasMoved();

    void printPiece();
};