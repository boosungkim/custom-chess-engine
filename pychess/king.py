
from enums import Player
from piece import Piece


class King(Piece):
    # Initialize the piece
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name,row_number, col_number, player)
        self.has_moved = False  

    # Get moves
    def get_valid_piece_moves(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]

            if not 0 <= new_row < 8 or not 0 <= new_col < 8:
                continue
            
            evaluating_piece = game_state.get_piece(new_row, new_col)

            # when square is empty
            if evaluating_piece == Player.EMPTY:
                _peaceful_moves.append((new_row, new_col))

            # when the square with new_row and new_col contains a valid piece
            # TODO: FIX BUG to remove isinstance
            if not isinstance(evaluating_piece, int) and not evaluating_piece.is_player(self.get_player()):
                _piece_takes.append((new_row, new_col))

        # Check for castle
        if game_state.king_can_castle_left(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _peaceful_moves.append((0, 1))
            elif self.is_player(Player.PLAYER_2):
                _peaceful_moves.append((7, 1))
        elif game_state.king_can_castle_right(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _peaceful_moves.append((0, 5))
            elif self.is_player(Player.PLAYER_2):
                _peaceful_moves.append((7, 5))

        return _peaceful_moves + _piece_takes