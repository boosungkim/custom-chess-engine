#
# The Chess Board class
# Will store the state of the chess game, print the chess board, find valid moves, store move logs.
#
# Note: move log class inspired by Eddie Sharick
#
from Piece import Rook, Knight, Bishop, Queen, King, Pawn
from enums import Player

'''
y \ x     0           1           2           3           4           5           6           7 
0   [(r=0, c=0), (r=0, c=1), (r=0, c=2), (r=0, c=3), (r=0, c=4), (r=0, c=5), (r=0, c=6), (r=0, c=7)]
1   [(r=1, c=0), (r=1, c=1), (r=1, c=2), (r=1, c=3), (r=1, c=4), (r=1, c=5), (r=1, c=6), (r=1, c=7)]
2   [(r=2, c=0), (r=2, c=1), (r=2, c=2), (r=2, c=3), (r=2, c=4), (r=2, c=5), (r=2, c=6), (r=2, c=7)]
3   [(r=3, c=0), (r=3, c=1), (r=3, c=2), (r=3, c=3), (r=3, c=4), (r=3, c=5), (r=3, c=6), (r=3, c=7)]
4   [(r=4, c=0), (r=4, c=1), (r=4, c=2), (r=4, c=3), (r=4, c=4), (r=4, c=5), (r=4, c=6), (r=4, c=7)]
5   [(r=5, c=0), (r=5, c=1), (r=5, c=2), (r=5, c=3), (r=5, c=4), (r=5, c=5), (r=5, c=6), (r=5, c=7)]
6   [(r=6, c=0), (r=6, c=1), (r=6, c=2), (r=6, c=3), (r=6, c=4), (r=6, c=5), (r=6, c=6), (r=6, c=7)]
7   [(r=7, c=0), (r=7, c=1), (r=7, c=2), (r=7, c=3), (r=7, c=4), (r=7, c=5), (r=7, c=6), (r=7, c=7)]
'''


# TODO: Flip the board according to the player
# TODO: Pawns are usually indicated by no letters
class game_state:
    # Initialize 2D array to represent the chess board
    def __init__(self):
        # The board is a 2D array
        # TODO: Change to a numpy format later
        self.white_captives = []
        self.black_captives = []
        self.move_log = []
        self.white_turn = True

        self.white_king_can_castle = [True, True, True] #Has king not moved, has Rook1(col=0) not moved, has Rook2(col=7) not moved
        self.black_king_can_castle = [True, True, True]

        # Initialize White pieces
        white_rook_1 = Rook('r', 0, 0, Player.PLAYER_1)
        white_rook_2 = Rook('r', 0, 7, Player.PLAYER_1)
        white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
        white_knight_2 = Knight('n', 0, 6, Player.PLAYER_1)
        white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
        white_bishop_2 = Bishop('b', 0, 5, Player.PLAYER_1)
        white_queen = Queen('q', 0, 4, Player.PLAYER_1)
        white_king = King('k', 0, 3, Player.PLAYER_1)
        white_pawn_1 = Pawn('p', 1, 0, Player.PLAYER_1)
        white_pawn_2 = Pawn('p', 1, 1, Player.PLAYER_1)
        white_pawn_3 = Pawn('p', 1, 2, Player.PLAYER_1)
        white_pawn_4 = Pawn('p', 1, 3, Player.PLAYER_1)
        white_pawn_5 = Pawn('p', 1, 4, Player.PLAYER_1)
        white_pawn_6 = Pawn('p', 1, 5, Player.PLAYER_1)
        white_pawn_7 = Pawn('p', 1, 6, Player.PLAYER_1)
        white_pawn_8 = Pawn('p', 1, 7, Player.PLAYER_1)
        self.white_pieces = [white_rook_1, white_rook_2, white_knight_1, white_knight_2, white_bishop_1, white_bishop_2,
                             white_queen, white_king, white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4,
                             white_pawn_5,
                             white_pawn_6, white_pawn_7, white_pawn_8]

        # Initialize Black Pieces
        black_rook_1 = Rook('r', 7, 0, Player.PLAYER_2)
        black_rook_2 = Rook('r', 7, 7, Player.PLAYER_2)
        black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
        black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
        black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
        black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
        black_queen = Queen('q', 7, 3, Player.PLAYER_2)
        black_king = King('k', 7, 4, Player.PLAYER_2)
        black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
        black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
        black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)
        black_pawn_4 = Pawn('p', 6, 3, Player.PLAYER_2)
        black_pawn_5 = Pawn('p', 6, 4, Player.PLAYER_2)
        black_pawn_6 = Pawn('p', 6, 5, Player.PLAYER_2)
        black_pawn_7 = Pawn('p', 6, 6, Player.PLAYER_2)
        black_pawn_8 = Pawn('p', 6, 7, Player.PLAYER_2)
        self.black_pieces = [black_rook_1, black_rook_2, black_knight_1, black_knight_2, black_bishop_1, black_bishop_2,
                             black_queen, black_king, black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4,
                             black_pawn_5,
                             black_pawn_6, black_pawn_7, black_pawn_8]

        self.board = [
            [white_rook_1, white_knight_1, white_bishop_1, white_king, white_queen, white_bishop_2, white_knight_2,
             white_rook_2],
            [white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7,
             white_pawn_8],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4, black_pawn_5, black_pawn_6, black_pawn_7,
             black_pawn_8],
            [black_rook_1, black_knight_1, black_bishop_1, black_king, black_queen, black_bishop_2, black_knight_2,
             black_rook_2]
        ]

    def get_piece(self, row, col):
        if (0 <= row < 8) and (0 <= col < 8):
            return self.board[row][col]

    def is_valid_piece(self, row, col):
        evaluated_piece = self.get_piece(row, col)
        return (evaluated_piece is not None) and (evaluated_piece != Player.EMPTY)

    def get_valid_moves(self, game_state, row, col):
        if self.is_valid_piece(row, col):
            return self.get_piece(row, col).get_valid_piece_moves(game_state, (row, col))
        else:
            return None

    def king_can_castle_left(self, player):
        if player is Player.PLAYER_1:
            return self.white_king_can_castle[0] and self.white_king_can_castle[1] and \
                   self.get_piece(0, 1) is Player.EMPTY and self.get_piece(0, 2) is Player.EMPTY
        elif player is Player.PLAYER_2:
            return self.black_king_can_castle[0] and self.black_king_can_castle[1] and \
                   self.get_piece(7, 1) is Player.EMPTY and self.get_piece(7, 2) is Player.EMPTY

    def king_can_castle_right(self, player):
        if player is Player.PLAYER_1:
            return self.white_king_can_castle[0] and self.white_king_can_castle[2] and \
                   self.get_piece(0, 6) is Player.EMPTY and self.get_piece(0, 5) is Player.EMPTY
        elif player is Player.PLAYER_2:
            return self.black_king_can_castle[0] and self.black_king_can_castle[2] and \
                   self.get_piece(7, 6) is Player.EMPTY and self.get_piece(7, 5) is Player.EMPTY

    def promotePawn(self, moved_piece):
        new_piece = input("Change pawn to (r, q, n, b, q): ")
        self.__init__(new_piece, self.get_row_number(), self.get_col_number(), player)

    # Move a piece
    def move_piece(self, starting_square, ending_square, game_state):
        current_square_row = starting_square[0]                   # The integer row value of the starting square
        current_square_col = starting_square[1]                   # The integer col value of the starting square
        next_square_row = ending_square[0]                        # The integer row value of the ending square
        next_square_col = ending_square[1]                        # The integer col value of the ending square

        if self.is_valid_piece(current_square_row, current_square_col) and \
            (((game_state.whose_turn() and self.get_piece(current_square_row, current_square_col).is_player(Player.PLAYER_1)) or
            (not game_state.whose_turn() and self.get_piece(current_square_row,current_square_col).is_player(Player.PLAYER_2)))):

            # The chess piece at the starting square
            moving_piece = self.get_piece(current_square_row, current_square_col)

            valid_moves = moving_piece.get_valid_piece_moves(game_state, starting_square)

            if (next_square_row, next_square_col) in valid_moves:
                moved_to_piece = self.get_piece(next_square_row, next_square_col)
                if moving_piece.get_name() is "k":
                    if moving_piece.is_player(Player.PLAYER_1):
                        if moved_to_piece == Player.EMPTY and next_square_col == 1:
                            # move rook
                            game_state.get_piece(0, 0).change_col_number(2)

                            game_state.board[0][2] = game_state.board[0][0]
                            game_state.board[0][0] = Player.EMPTY

                            self.white_king_can_castle[0] = False
                            self.white_king_can_castle[1] = False
                        elif moved_to_piece == Player.EMPTY and next_square_col == 5:
                            # move rook
                            game_state.get_piece(0, 7).change_col_number(4)

                            game_state.board[0][4] = game_state.board[0][7]
                            game_state.board[0][7] = Player.EMPTY

                            self.white_king_can_castle[0] = False
                            self.white_king_can_castle[2] = False
                        else:
                            self.white_king_can_castle[0] = False
                    else:
                        if moved_to_piece == Player.EMPTY and next_square_col == 1:
                            game_state.get_piece(7, 0).change_col_number(2)
                            # move rook
                            game_state.board[7][2] = game_state.board[7][0]
                            game_state.board[7][0] = Player.EMPTY

                            self.black_king_can_castle[0] = False
                            self.black_king_can_castle[1] = False
                        elif moved_to_piece == Player.EMPTY and next_square_col == 5:
                            game_state.get_piece(0, 7).change_col_number(4)

                            # move rook
                            game_state.board[7][4] = game_state.board[7][7]
                            game_state.board[7][7] = Player.EMPTY

                            self.black_king_can_castle[0] = False
                            self.black_king_can_castle[2] = False
                        else:
                            self.black_king_can_castle[0] = False
                elif moving_piece.get_name() is "r":
                    if moving_piece.is_player(Player.PLAYER_1) and current_square_col == 0:
                        self.white_king_can_castle[1] = False
                    elif moving_piece.is_player(Player.PLAYER_1) and current_square_col == 7:
                        self.white_king_can_castle[2] = False
                    elif moving_piece.is_player(Player.PLAYER_2) and current_square_col == 0:
                        self.white_king_can_castle[1] = False
                    elif moving_piece.is_player(Player.PLAYER_2) and current_square_col == 7:
                        self.white_king_can_castle[2] = False

                moving_piece.change_row_number(next_square_row)
                moving_piece.change_col_number(next_square_col)

                game_state.board[next_square_row][next_square_col] = game_state.board[current_square_row][current_square_col]
                game_state.board[current_square_row][current_square_col] = Player.EMPTY

                self.move_log.append(chess_move(starting_square, ending_square, game_state))
                self.white_turn = not self.white_turn

                if moving_piece.get_name() is "p":
                    if moving_piece.is_player(Player.PLAYER_1) and next_square_row == 7:
                        pass
            else:
                pass

    # true if white, false if black
    def whose_turn(self):
        return self.white_turn

    def is_check(self):
        pass


class chess_move():
    def __init__(self, starting_square, ending_square, game_state):
        self.starting_square_row = starting_square[0]
        self.starting_square_col = starting_square[1]

        self.ending_square_row = ending_square[0]
        self.ending_square_col = ending_square[1]

        self.moved_piece = game_state.get_piece(self.starting_square_row, self.starting_square_col)
        self.captured_piece = game_state.get_piece(self.ending_square_row, self.ending_square_col)

