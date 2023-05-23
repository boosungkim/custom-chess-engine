#include "header/enum.h"
#include "header/piece.h"
#include "header/chessengine.h"
#include "header/chessmove.h"
#include <iostream>
#include <vector>
#include <cassert>


Piece ChessEngine::getPiece(int row, int col){
    assert(0 <= row && row < 8);
    assert(0 <= col && col < 8);
    return board[row][col];
}

void ChessEngine::tempPrintBoard(){
    std::cout << "-----------------------\n";
    for(int i = 0; i < 8; i++){
        std::cout << "|";
        for(int j = 0; j < 8; j++){
            std::cout << " " << static_cast<char>(this->board[i][j].getName()) << " ";
        }
        std::cout << "|\n";
    }
    std::cout << "-----------------------";
}

bool ChessEngine::isValidPiece(int row, int col){
    if((0 <= row && row < 8) && (0 <= col && col < 8)){
        return this->getPiece(row, col).getName() != ChessPiece::EMPTY;
    } else{
        return false;
    }
}



// std::vector<ChessMove> ChessEngine::getValidPieceMoves(Piece& piece){
//     if(this->game_state == GameState::WHITE_IN_CHECK || 
//     this->game_state == GameState::BLACK_IN_CHECK){

//     }
//     // Rook

//     // Knight

//     // Bishop

//     // Queen

//     // King

//     // Pawn
//     return 0;
// }

ChecksAndPins ChessEngine::checkForChecksAndPins(Piece king){
    ChecksAndPins check_and_pins {};

    // Left traverse
    for (int i = king.getRowValue() - 1; i == 0; i--){
        
    }



    int left_traverse {0};
    while(this->getPiece(king.getRowValue(), king.getColValue()))

    Piece rook {ChessPiece::Rook, 7, 0, Player::PLAYER_WHITE};
    check_and_pins.checking_pieces.push_back(rook);
    std::cout << static_cast<char>(check_and_pins.checking_pieces[0].getName());
    return check_and_pins;
}

// int getAllValidMoves(int row, int col);


void ChessEngine::movePiece(Piece& moving_piece, int new_row, int new_col){
    int old_row = moving_piece.getRowValue();
    int old_col = moving_piece.getColValue();
    this->board[new_row][new_col] = moving_piece;
    this->board[old_row][old_col] = ChessEngine::EMPTY;
    
    this->white_turn = !white_turn;
}

int main(){
    ChessEngine test_board{};
    Piece piece = test_board.getPiece(7,5);
    piece.printPiece();
    test_board.tempPrintBoard();
    // test_board.movePiece(piece, 5, 7);
    // test_board.tempPrintBoard();

    test_board.checkForChecksAndPins(Player::PLAYER_BLACK);
}