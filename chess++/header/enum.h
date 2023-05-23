#pragma once

enum class Player {
    PLAYER_WHITE,
    PLAYER_BLACK,
    PLAYER_NONE,
};

enum class ChessPiece : char {
    Pawn = 'P',
    Rook = 'R',
    Knight = 'N',
    Bishop = 'B',
    Queen = 'Q',
    King = 'K',
    EMPTY = ' ',
};

enum class GameState {
    NORMAL,
    WHITE_IN_CHECK,
    BLACK_IN_CHECK,
    CHECKMATE_WHITE_WIN,
    CHECKMATE_BLACK_WIN,
    DRAW,
};