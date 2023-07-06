
from enums import Player
from piece import Piece


class Knight(Piece):
    # Get moves
    def get_valid_piece_moves(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]

            if not 0 <= new_row < 8 or not 0 <= new_col < 8:
                continue

            evaluating_square = game_state.get_piece(new_row, new_col)
            
            if evaluating_square == Player.EMPTY:
                _peaceful_moves.append((new_row, new_col))
            elif not evaluating_square.is_player(self.get_player()):
                _piece_takes.append((new_row, new_col))
        
        return _peaceful_moves + _piece_takes