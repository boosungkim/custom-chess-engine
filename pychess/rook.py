
from enums import Player
from piece import Piece


class Rook(Piece):
    # Initialize the piece
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name,row_number, col_number, player)
        self.has_moved = False  

    # Get moves
    def get_valid_piece_moves(self, game_state):
        _peaceful_moves = []
        _piece_takes = []
        def check_new_position(new_row, new_col):
            # when the square to the left is empty
            if game_state.get_piece(new_row, new_col) == Player.EMPTY:
                _peaceful_moves.append((new_row, new_col))
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(new_row, new_col) and \
                    not game_state.get_piece(new_row, new_col).is_player(self.get_player()):
                _piece_takes.append((new_row, new_col))
                self._breaking_point = True
            else:
                self._breaking_point = True

        _up = 1
        _down = 1
        _left = 1
        _right = 1

        # Left of the Rook
        self._breaking_point = False
        while self.get_col_number() - _left >= 0 and not self._breaking_point:
            check_new_position(self.get_row_number(), self.get_col_number() - _left)
            _left += 1

        # Right of the Rook
        self._breaking_point = False
        while self.get_col_number() + _right < 8 and not self._breaking_point:
            check_new_position(self.get_row_number(), self.get_col_number() + _right)
            _right += 1

        # Below the Rook
        self._breaking_point = False
        while self.get_row_number() + _down < 8 and not self._breaking_point:
            check_new_position(self.get_row_number() + _down, self.get_col_number())
            _down += 1

        # Above the Rook
        self._breaking_point = False
        while self.get_row_number() - _up >= 0 and not self._breaking_point:
            check_new_position(self.get_row_number() - _up, self.get_col_number())
            _up += 1
        
        return _peaceful_moves + _piece_takes