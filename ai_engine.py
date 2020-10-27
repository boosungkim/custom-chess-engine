#
# The Chess AI class
# Will utilize minimax and alpha beta pruning
#
# Author: Boo Sung Kim
# Note: Code inspired from the pseudocode by Sebastian Lague
# from enums import Player
# TODO: switch undo moves to stack data structure

class chess_ai:
    '''
    call minimax with alpha beta pruning
    evaluate board
    get the value of each piece
    '''

    def __init__(self):
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        pass


    def minimax(self, game_state, depth, alpha, beta, maximizing_player, player_color):
        if depth <= 0 or game_state.checkmate_stalemate_checker() != 3:
            return self.evaluate_board(game_state)
        if maximizing_player:
            max_evaluation = -100000
            all_possible_moves = game_state.get_all_legal_moves("black")
            print(all_possible_moves)
            for move_pair in all_possible_moves:
                print("black moving")
                print(move_pair)
                print(len(game_state.move_log))
                game_state.move_piece(move_pair[0], move_pair[1])
                print("after black move")
                print(len(game_state.move_log))
                # self.count1 += 1
                evaluation = self.minimax(game_state, depth - 1, alpha, beta, False, "white")
                a = game_state.undo_move()
                print("black undoing move")
                print(len(game_state.move_log))
                print(a.get_moving_piece())
                print(a.starting_square_row)
                print(a.starting_square_col)
                # self.count2 += 1
                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair
                # max_evaluation = max(evaluation, max_evaluation)
                alpha = max(alpha, evaluation)
                # if beta <= alpha:
                #     break
            if depth == 2:
                print("ended")
                return best_possible_move
            else:
                return max_evaluation
        else:
            min_evaluation = 100000
            all_possible_moves = game_state.get_all_legal_moves("white")
            for move_pair in all_possible_moves:
                # print(move_pair)
                game_state.move_piece(move_pair[0], move_pair[1])
                # self.count3 += 1
                print("white moving")
                print(move_pair)
                print(len(game_state.move_log))
                evaluation = self.minimax(game_state, depth - 1, alpha, beta, True, "black")
                b = game_state.undo_move()
                print("white undoing move")
                print(len(game_state.move_log))
                print(b.get_moving_piece())
                print(b.starting_square_row)
                print(b.starting_square_col)
                # self.count4 += 1
                # if min_evaluation > evaluation:
                #     min_evaluation = evaluation
                #     best_possible_move = move_pair
                min_evaluation = min(evaluation, min_evaluation)
                beta = min(beta, evaluation)
                # if beta <= alpha:
                #     break
            # if depth == 2:
            #     return best_possible_move
            print("after white")
            print(len(game_state.move_log))
            print(game_state.move_log[-1].starting_square_row)
            print(game_state.move_log[-1].starting_square_col)
            print(game_state.move_log[-1].moving_piece)

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