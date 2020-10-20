#
# The Chess AI class
# Will utilize minimax and alpha beta pruning
#
# Author: Boo Sung Kim
# Note: Code inspired from the pseudocode by Sebastian Lague
from enums import Player
# TODO: switch undo moves to stack data structure

class chess_ai:
    '''
    call minimax with alpha beta pruning
    evaluate board
    get the value of each piece
    '''
    def minimax(self, game_state, depth, alpha, beta, maximizing_player, player_color):
        if depth == 0 or game_state.checkmate_stalemate_checker() != 3:
            return self.evaluate_board(game_state)
        elif maximizing_player:
            max_evaluation = [float('-inf'), None]
            all_possible_moves = game_state.get_all_legal_moves(player_color)
            for move in all_possible_moves:
                game_state.move_piece(move[0], move[1])
                evaluation = self.minimax(game_state, depth - 1, alpha, beta, False, player_color)
                game_state.move_piece(move[1], move[0])
                max_evaluation[0] = max(evaluation, max_evaluation[0])
                if max_evaluation > alpha:
                    max_evaluation[1] = evaluation[1]
                else:
                    pass
                alpha = max(alpha, evaluation[0])
                if beta <= alpha:
                    break
                return max_evaluation
        else:
            min_evaluation = [float('inf'), None]
            all_possible_moves = game_state.get_all_legal_moves(player_color)
            for move in all_possible_moves:
                game_state.move_piece(move[0], move[1])
                evaluation = self.minimax(game_state, depth - 1, alpha, beta, True, player_color)
                game_state.move_piece(move[1], move[0])
                min_evaluation[0] = min(evaluation, min_evaluation[0])
                if min_evaluation < beta:
                    min_evaluation[1] = evaluation[1]
                else:
                    pass
                beta = min(beta, evaluation[0])
                if beta <= alpha:
                    break
                return min_evaluation

    def evaluate_board(self, game_state):
        evaluation_score = 0
        for row in range(0, 8):
            for col in range(0, 8):
                if game_state.is_valid(row, col):
                    evaluated_piece = game_state.get_piece(row, col)
                    evaluation_score += self.get_piece_value(evaluated_piece, evaluated_piece.get_player())

    def get_piece_value(self, piece, player_color):
        if piece.is_player(player_color):
            if piece.get_name() is "k":
                return 1000
            elif piece.get_name() is "q":
                return 100
            elif piece.get_name() is "r":
                return 50
            elif piece.get_name() is "b":
                return 30
            elif piece.get_name() is "n":
                return 30
            elif piece.get_name() is "p":
                return 10
        else:
            if piece.get_name() is "k":
                return -1000
            elif piece.get_name() is "q":
                return -100
            elif piece.get_name() is "r":
                return -50
            elif piece.get_name() is "b":
                return -30
            elif piece.get_name() is "n":
                return -30
            elif piece.get_name() is "p":
                return -10