
from enums import Player
from piece import Piece


class Pawn(Piece):
    # Get moves
    def get_valid_piece_moves(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        original_row_num, move_one_row, move_two_row = (1, 1, 2) if self.is_player(Player.PLAYER_1) else (6, -1, -2)
        opposing_player = Player.PLAYER_1 if self.is_player(Player.PLAYER_2) else Player.PLAYER_2

        # when the square right below the starting_square is empty
        if game_state.get_piece(self.get_row_number() + move_one_row, self.get_col_number()) == Player.EMPTY:
            _peaceful_moves.append((self.get_row_number() + move_one_row, self.get_col_number()))
            # when the pawn has not been moved yet
            if self.get_row_number() == original_row_num and game_state.get_piece(self.get_row_number() + move_two_row,
                                                                    self.get_col_number()) == Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + move_two_row, self.get_col_number()))
        
        # when the square to the bottom left of the starting_square has a black piece
        if game_state.is_valid_piece(self.get_row_number() + move_one_row, self.get_col_number() - 1) and \
                game_state.get_piece(self.get_row_number() + move_one_row, self.get_col_number() - 1).is_player(opposing_player):
            _piece_takes.append((self.get_row_number() + move_one_row, self.get_col_number() - 1))
        # when the square to the bottom right of the starting_square has a black piece
        if game_state.is_valid_piece(self.get_row_number() + move_one_row, self.get_col_number() + 1) and \
                game_state.get_piece(self.get_row_number() + move_one_row, self.get_col_number() + 1).is_player(opposing_player):
            _piece_takes.append((self.get_row_number() + move_one_row, self.get_col_number() + 1))
        # en passant (TODO: FIX)
        if game_state.can_en_passant(self.get_row_number(), self.get_col_number()):
            _piece_takes.append((self.get_row_number() + move_one_row, game_state.previous_piece_en_passant()[1]))

        return _peaceful_moves + _piece_takes