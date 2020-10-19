#
# The Chess AI class
# Will utilize minimax and alpha beta pruning
#
# Author: Boo Sung Kim
# Note: Code inspired from the pseudocode by Sebastian Lague
from enums import Player


class chess_ai:
    '''
    call minimax with alpha beta pruning
    evaluate board
    get the value of each piece
    '''
    def minimax(self, game_state, depth, alpha, beta, maximizing_player):
        if depth == 0 or game_state.checkmate_stalemate_checker() != 3:
            return self.evaluate_board(game_state)
        elif maximizing_player:
            pass
        else:
            pass

    def evaluate_board(self, game_state):
        pass

    def get_piece_value(self, piece):
        if piece.is_player(Player.PLAYER_1):
            pass
        else:
            pass