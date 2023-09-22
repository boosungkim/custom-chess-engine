from enums import Player
from piece import Piece

class Knight(Piece):
    def get_valid_piece_moves(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for move in moves:
            new_row = self.get_row_number() + move[0]
            new_col = self.get_col_number() + move[1]

            if 0 <= new_row < 8 and 0 <= new_col < 8:
                evaluating_square = game_state.get_piece(new_row, new_col)
                
                if evaluating_square == Player.EMPTY:
                    _peaceful_moves.append((new_row, new_col))
                elif not evaluating_square.is_player(self.get_player()):
                    _piece_takes.append((new_row, new_col))

        return _peaceful_moves + _piece_takes
