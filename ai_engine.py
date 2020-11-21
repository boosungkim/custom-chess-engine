#
# The Chess AI class
# Will utilize minimax and alpha beta pruning
#
# Author: Boo Sung Kim
# Note: Code inspired from the pseudocode by Sebastian Lague
# from enums import Player
# TODO: switch undo moves to stack data structure
import chess_engine
from enums import Player


class chess_ai:
    '''
    call minimax with alpha beta pruning
    evaluate board
    get the value of each piece
    '''
    def minimax(self, game_state, depth, alpha, beta, maximizing_player, player_color):
        if depth <= 0 or game_state.checkmate_stalemate_checker() != 3:
            return self.evaluate_board(game_state)
        if maximizing_player:
            max_evaluation = -100000
            all_possible_moves = game_state.get_all_legal_moves("black")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax(game_state, depth - 1, alpha, beta, False, "white")
                # print("pair start")
                # print(len(game_state.move_log))
                # print(move_pair[0])
                # print(move_pair[1])
                # print("pair end")
                game_state.undo_move()

                # temp = game_state.board[move_pair[0][0]][move_pair[0][1]]
                # temp2 = game_state.board[move_pair[1][0]][move_pair[1][1]]
                # game_state.board[move_pair[0][0]][move_pair[0][1]] = Player.EMPTY
                # game_state.board[move_pair[1][0]][move_pair[1][1]] = temp
                # evaluation = self.minimax(game_state, depth - 1, alpha, beta, False, "white")
                # game_state.board[move_pair[0][0]][move_pair[0][1]] = temp
                # game_state.board[move_pair[1][0]][move_pair[1][1]] = temp2

                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            if depth == 3:
                return best_possible_move
            else:
                return max_evaluation
        else:
            min_evaluation = 100000
            all_possible_moves = game_state.get_all_legal_moves("white")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax(game_state, depth - 1, alpha, beta, True, "black")
                game_state.undo_move()

                # temp = game_state.board[move_pair[0][0]][move_pair[0][1]]
                # temp2 = game_state.board[move_pair[1][0]][move_pair[1][1]]
                # game_state.board[move_pair[0][0]][move_pair[0][1]] = Player.EMPTY
                # game_state.board[move_pair[1][0]][move_pair[1][1]] = temp
                # evaluation = self.minimax(game_state, depth - 1, alpha, beta, True, "black")
                # game_state.board[move_pair[0][0]][move_pair[0][1]] = temp
                # game_state.board[move_pair[1][0]][move_pair[1][1]] = temp2

                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    best_possible_move = move_pair
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            if depth == 3:
                return best_possible_move
            else:
                return min_evaluation

    def evaluate_board(self, game_state):
        evaluation_score = 0
        for row in range(0, 8):
            for col in range(0, 8):
                if game_state.is_valid_piece(row, col):
                    evaluated_piece = game_state.get_piece(row, col)
                    evaluation_score += self.get_piece_value(evaluated_piece, evaluated_piece.get_player())
        return evaluation_score

    def get_piece_value(self, piece, player_color):
        if piece.is_player("black"):
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