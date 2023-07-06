
from enums import Player
from piece import Piece


class Bishop(Piece):
    # Get moves
    def get_valid_piece_moves(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        def check_new_position(new_row, new_col):
            # when the square is empty
            if game_state.get_piece(new_row, new_col) is Player.EMPTY:
                _peaceful_moves.append((new_row, new_col))
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(new_row, new_col) and \
                    not game_state.get_piece(new_row, new_col).is_player(self.get_player()):
                _piece_takes.append((new_row, new_col))
                self._breaking_point = True
            else:
                self._breaking_point = True
        
        # Left up of the bishop
        _up, _left = 1, 1
        self._breaking_point = False
        while self.get_col_number() - _left >= 0 and self.get_row_number() - _up >= 0 and not self._breaking_point:
            check_new_position(self.get_row_number() - _up, self.get_col_number() - _left)
            _up += 1
            _left += 1

        # Right up of the bishop
        _up, _right = 1, 1
        self._breaking_point = False
        while self.get_col_number() + _right < 8 and self.get_row_number() - _up >= 0 and not self._breaking_point:
            check_new_position(self.get_row_number() - _up, self.get_col_number() + _right)
            _up += 1
            _right += 1

        # Down left of the bishop
        _down, _left = 1, 1
        self._breaking_point = False
        while self.get_col_number() - _left >= 0 and self.get_row_number() + _down < 8 and not self._breaking_point:
            check_new_position(self.get_row_number() + _down, self.get_col_number() - _left)
            _down += 1
            _left += 1

        # Down right of the bishop
        _down, _right = 1, 1
        self._breaking_point = False
        while self.get_col_number() + _right < 8 and self.get_row_number() + _down < 8 and not self._breaking_point:
            check_new_position(self.get_row_number() + _down, self.get_col_number() + _right)
            _down += 1
            _right += 1
        
        return _peaceful_moves + _piece_takes