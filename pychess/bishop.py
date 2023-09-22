from enums import Player
from piece import Piece

class Bishop(Piece):
    def get_valid_piece_moves(self, game_state):
        moves = []
        current_row, current_col = self.get_row_number(), self.get_col_number()

        def check_new_position(row_step, col_step):
            row, col = current_row + row_step, current_col + col_step
            while 0 <= row < 8 and 0 <= col < 8:
                piece = game_state.get_piece(row, col)
                if piece is Player.EMPTY:
                    moves.append((row, col))
                elif game_state.is_valid_piece(row, col) and not piece.is_player(self.get_player()):
                    moves.append((row, col))
                    break
                else:
                    break
                row += row_step
                col += col_step

        check_new_position(-1, -1)  
        check_new_position(-1, 1)   
        check_new_position(1, -1)   
        check_new_position(1, 1)   

        return moves
