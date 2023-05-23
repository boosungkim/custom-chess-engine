#pragma once

#include "enum.h"
#include "piece.h"
#include "chessmove.h"
#include <iostream>
#include <vector>

struct ChecksAndPins{
    std::vector<Piece> checking_pieces {};
    std::vector<Piece> pinned_pieces {};
};

class ChessEngine{
private:
    bool white_turn {true};
    bool can_en_passant {false};
    GameState game_state{GameState::NORMAL};
    std::vector<int> move_log{};
    
    Piece EMPTY {ChessPiece::EMPTY};

    Piece white_rook_1 {ChessPiece::Rook, 7, 0, Player::PLAYER_WHITE};
    Piece white_rook_2 {ChessPiece::Rook, 7, 7, Player::PLAYER_WHITE};
    Piece white_knight_1 {ChessPiece::Knight, 7, 1, Player::PLAYER_WHITE};
    Piece white_knight_2 {ChessPiece::Knight, 7, 6, Player::PLAYER_WHITE};
    Piece white_bishop_1 {ChessPiece::Bishop, 7, 2, Player::PLAYER_WHITE};
    Piece white_bishop_2 {ChessPiece::Bishop, 7, 5, Player::PLAYER_WHITE};
    Piece white_queen {ChessPiece::Queen, 7, 3, Player::PLAYER_WHITE};
    Piece white_king {ChessPiece::King, 7, 4, Player::PLAYER_WHITE};
    Piece white_pawn_1 {ChessPiece::Pawn, 6, 0, Player::PLAYER_WHITE};
    Piece white_pawn_2 {ChessPiece::Pawn, 6, 1, Player::PLAYER_WHITE};
    Piece white_pawn_3 {ChessPiece::Pawn, 6, 2, Player::PLAYER_WHITE};
    Piece white_pawn_4 {ChessPiece::Pawn, 6, 3, Player::PLAYER_WHITE};
    Piece white_pawn_5 {ChessPiece::Pawn, 6, 4, Player::PLAYER_WHITE};
    Piece white_pawn_6 {ChessPiece::Pawn, 6, 5, Player::PLAYER_WHITE};
    Piece white_pawn_7 {ChessPiece::Pawn, 6, 6, Player::PLAYER_WHITE};
    Piece white_pawn_8 {ChessPiece::Pawn, 6, 7, Player::PLAYER_WHITE};

    Piece black_rook_1 {ChessPiece::Rook, 0, 0, Player::PLAYER_BLACK};
    Piece black_rook_2 {ChessPiece::Rook, 0, 7, Player::PLAYER_BLACK};
    Piece black_knight_1 {ChessPiece::Knight, 0, 1, Player::PLAYER_BLACK};
    Piece black_knight_2 {ChessPiece::Knight, 0, 6, Player::PLAYER_BLACK};
    Piece black_bishop_1 {ChessPiece::Bishop, 0, 2, Player::PLAYER_BLACK};
    Piece black_bishop_2 {ChessPiece::Bishop, 0, 5, Player::PLAYER_BLACK};
    Piece black_queen {ChessPiece::Queen, 0, 3, Player::PLAYER_BLACK};
    Piece black_king {ChessPiece::King, 0, 4, Player::PLAYER_BLACK};
    Piece black_pawn_1 {ChessPiece::Pawn, 1, 0, Player::PLAYER_BLACK};
    Piece black_pawn_2 {ChessPiece::Pawn, 1, 1, Player::PLAYER_BLACK};
    Piece black_pawn_3 {ChessPiece::Pawn, 1, 2, Player::PLAYER_BLACK};
    Piece black_pawn_4 {ChessPiece::Pawn, 1, 3, Player::PLAYER_BLACK};
    Piece black_pawn_5 {ChessPiece::Pawn, 1, 4, Player::PLAYER_BLACK};
    Piece black_pawn_6 {ChessPiece::Pawn, 1, 5, Player::PLAYER_BLACK};
    Piece black_pawn_7 {ChessPiece::Pawn, 1, 6, Player::PLAYER_BLACK};
    Piece black_pawn_8 {ChessPiece::Pawn, 1, 7, Player::PLAYER_BLACK};

    Piece board[8][8] {
            {black_rook_1,black_knight_1,black_bishop_1,black_queen,black_king,black_bishop_2,black_knight_2,black_rook_2},
            {black_pawn_1,black_pawn_2,black_pawn_3,black_pawn_4,black_pawn_5,black_pawn_6,black_pawn_7,black_pawn_8},
            {EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY},
            {EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY},
            {EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY},
            {EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY},
            {white_pawn_1,white_pawn_2,white_pawn_3,white_pawn_4,white_pawn_5,white_pawn_6,white_pawn_7,white_pawn_8},
            {white_rook_1,white_knight_1,white_bishop_1,white_queen,white_king,white_bishop_2,white_knight_2,white_rook_2},
    };

public:

    Piece getPiece(int row, int col);

    void tempPrintBoard();

    bool isValidPiece(int row, int col);

    // std::vector<ChessMove> getValidPieceMoves(Piece& piece);

    ChecksAndPins checkForChecksAndPins(Player player);

    int getAllValidMoves(int row, int col);

    GameState getCurrentGameState(){return game_state;}

    void movePiece(Piece& moving_piece, int new_row, int new_col);

};
