
from enums import Player
from piece import Piece


class Pawn(Piece):
    def get_valid_piece_moves(self, game_state):
        if self.is_player(Player.PLAYER_1):
            original_row_num, move_one_row, move_two_row = 1, 1, 2
        else:
            original_row_num, move_one_row, move_two_row = 6, -1, -2

        opposing_player = Player.PLAYER_1 if self.is_player(Player.PLAYER_2) else Player.PLAYER_2

        current_row, current_col = self.get_row_number(), self.get_col_number()

        next_square = game_state.get_piece(current_row + move_one_row, current_col)
        next_next_square = game_state.get_piece(current_row + move_two_row, current_col)

        _peaceful_moves = [(current_row + move_one_row, current_col)] if next_square == Player.EMPTY else []
        if current_row == original_row_num and next_next_square == Player.EMPTY:
            _peaceful_moves.append((current_row + move_two_row, current_col))

        _piece_takes = []
        for col in (current_col - 1, current_col + 1):
            if game_state.is_valid_piece(current_row + move_one_row, col) and \
                    game_state.get_piece(current_row + move_one_row, col).is_player(opposing_player):
                _piece_takes.append((current_row + move_one_row, col))

        if game_state.can_en_passant(current_row, current_col):
            _piece_takes.append((current_row + move_one_row, game_state.previous_piece_en_passant()[1]))

        return _peaceful_moves + _piece_takes
