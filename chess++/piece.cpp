// 
// Chess Piece classes
// 

#include <iostream>
#include "header/enum.h"
#include "header/piece.h"

Piece::Piece(ChessPiece name)
    : piece_name {name}, piece_row_position {-1}, piece_col_position{-1}, piece_player{Player::PLAYER_NONE}
{
}

Piece::Piece(ChessPiece name, int row, int col, Player player)
    : piece_name {name}, piece_row_position {row}, piece_col_position{col}, piece_player{player}, has_moved{false}
{
}

void Piece::changeRowValue(int new_row_number){
    piece_row_position = new_row_number;
}

void Piece::changeColValue(int new_col_number){
    piece_col_position = new_col_number;
}

void Piece::pieceHasMoved(){
    has_moved = true;
}

void Piece::printPiece(){
    std::cout << "This is a " << static_cast<char>(piece_name)
    << " and it is located at row " << piece_row_position << " and col "
    << piece_col_position << std::endl;
}

// int main(){
//     Piece rook_test{ChessPiece::Rook,0,0,Player::PLAYER_WHITE};
//     rook_test.printPiece();
//     std::cout << rook_test.checkIfMoved();
//     Piece knight_test {ChessPiece::Knight,0, 1, Player::PLAYER_BLACK};
//     knight_test.printPiece();
//     Piece empty_test{ChessPiece::EMPTY};
//     empty_test.printPiece();
//     return 0;
// }