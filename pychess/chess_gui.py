#
# The GUI engine for Python Chess
#
# Author: Boo Sung Kim, Eddie Sharick
# Note: The pygame tutorial by Eddie Sharick was used for the GUI engine. The GUI code was altered by Boo Sung Kim to
# fit in with the rest of the project.
#
import chess_engine
from button import Button
import pygame as py

import ai_engine
from enums import Player

"""Variables"""
WIDTH = HEIGHT = 512  # width and height of the chess board
CENTER = 256
DIMENSION = 8  # the dimensions of the chess board
SQ_SIZE = HEIGHT // DIMENSION  # the size of each of the squares in the board
MAX_FPS = 15  # FPS for animations
IMAGES = {}  # images for the chess pieces
colors = [py.Color("white"), py.Color("gray")]

py.init()
SCREEN = py.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = py.image.load("images/menu/Background.png")

def get_font(size):
    return py.font.Font("images/menu/font.ttf", size)

def load_images():
    '''
    Load images for the chess pieces
    '''
    for p in Player.PIECES:
        IMAGES[p] = py.transform.scale(py.image.load("images/" + p + ".png"), (SQ_SIZE, SQ_SIZE))


def draw_game_state(screen, game_state, valid_moves, square_selected):
    ''' Draw the complete chess board with pieces

    Keyword arguments:
        :param screen       -- the pygame screen
        :param game_state   -- the state of the current chess game
    '''
    draw_squares(screen)
    highlight_square(screen, game_state, valid_moves, square_selected)
    draw_pieces(screen, game_state)


def draw_squares(screen):
    ''' Draw the chess board with the alternating two colors

    :param screen:          -- the pygame screen
    '''
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            py.draw.rect(screen, color, py.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, game_state):
    ''' Draw the chess pieces onto the board

    :param screen:          -- the pygame screen
    :param game_state:      -- the current state of the chess game
    '''
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = game_state.get_piece(r, c)
            if piece is not None and piece != Player.EMPTY:
                screen.blit(IMAGES[piece.get_player() + "_" + piece.get_name()],
                            py.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def highlight_square(screen, game_state, valid_moves, square_selected):
    if square_selected != () and game_state.is_valid_piece(square_selected[0], square_selected[1]):
        row = square_selected[0]
        col = square_selected[1]

        if (game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_1)) or \
                (not game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_2)):
            # hightlight selected square
            s = py.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(py.Color("blue"))
            screen.blit(s, (col * SQ_SIZE, row * SQ_SIZE))

            # highlight move squares
            s.fill(py.Color("green"))

            for move in valid_moves:
                screen.blit(s, (move[1] * SQ_SIZE, move[0] * SQ_SIZE))

def draw_text(screen, text):
    font = py.font.SysFont("Helvitca", 32, True, False)
    text_object = font.render(text, False, py.Color("Black"))
    text_location = py.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - text_object.get_width() / 2,
                                                      HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)

def single_player():
    SCREEN.fill("black")
    clock = py.time.Clock()
    game_state = chess_engine.game_state()
    load_images()
    running = True
    square_selected = ()  # keeps track of the last selected square
    player_clicks = []  # keeps track of player clicks (two tuples)
    valid_moves = []
    game_over = False

    ai = ai_engine.chess_ai()
    game_state = chess_engine.game_state()
    ai_move = ai.minimax_black(game_state, 3, -100000, 100000, True, Player.PLAYER_1)
    game_state.move_piece(ai_move[0], ai_move[1], True)

    while running:
        for e in py.event.get():
            if e.type == py.QUIT:
                running = False
            elif e.type == py.MOUSEBUTTONDOWN:
                if not game_over:
                    location = py.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if square_selected == (row, col):
                        square_selected = ()
                        player_clicks = []
                    else:
                        square_selected = (row, col)
                        player_clicks.append(square_selected)
                    if len(player_clicks) == 2:
                        if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                        else: 
                            game_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
                                                  (player_clicks[1][0], player_clicks[1][1]), False)
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                            ai_move = ai.minimax_black(game_state, 3, -100000, 100000, True, Player.PLAYER_1)
                            game_state.move_piece(ai_move[0], ai_move[1], True)
                            # if human_player is 'w':
                            #     ai_move = ai.minimax_white(game_state, 3, -100000, 100000, True, Player.PLAYER_2)
                            #     game_state.move_piece(ai_move[0], ai_move[1], True)
                            # elif human_player is 'b':
                            #     ai_move = ai.minimax_black(game_state, 3, -100000, 100000, True, Player.PLAYER_1)
                            #     game_state.move_piece(ai_move[0], ai_move[1], True)
                    else:
                        valid_moves = game_state.get_valid_moves((row, col))
                        if valid_moves is None:
                            valid_moves = []
            elif e.type == py.KEYDOWN:
                if e.key == py.K_r:
                    game_over = False
                    game_state = chess_engine.game_state()
                    valid_moves = []
                    square_selected = ()
                    player_clicks = []
                    valid_moves = []
                elif e.key == py.K_u:
                    game_state.undo_move()
                    print(len(game_state.move_log))
        draw_game_state(SCREEN, game_state, valid_moves, square_selected)

        endgame = game_state.checkmate_stalemate_checker()
        if endgame == 0:
            game_over = True
            draw_text(SCREEN, "Black wins.")
        elif endgame == 1:
            game_over = True
            draw_text(SCREEN, "White wins.")
        elif endgame == 2:
            game_over = True
            draw_text(SCREEN, "Stalemate.")

        clock.tick(MAX_FPS)
        py.display.flip()
    

def multi_player():
    SCREEN.fill("black")
    clock = py.time.Clock()
    game_state = chess_engine.game_state()
    load_images()
    running = True
    square_selected = ()  # keeps track of the last selected square
    player_clicks = []  # keeps track of player clicks (two tuples)
    valid_moves = []
    game_over = False

    while running:
        for e in py.event.get():
            if e.type == py.QUIT:
                running = False
            elif e.type == py.MOUSEBUTTONDOWN:
                if not game_over:
                    location = py.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if square_selected == (row, col):
                        square_selected = ()
                        player_clicks = []
                    else:
                        square_selected = (row, col)
                        player_clicks.append(square_selected)
                    if len(player_clicks) == 2:
                        # this if is useless right now
                        if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                        else: 
                            game_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
                                                  (player_clicks[1][0], player_clicks[1][1]), False)
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []

                    else:
                        valid_moves = game_state.get_valid_moves((row, col))
                        if valid_moves is None:
                            valid_moves = []
            elif e.type == py.KEYDOWN:
                if e.key == py.K_r:
                    game_over = False
                    game_state = chess_engine.game_state()
                    valid_moves = []
                    square_selected = ()
                    player_clicks = []
                    valid_moves = []
                elif e.key == py.K_u:
                    game_state.undo_move()
                    print(len(game_state.move_log))
        draw_game_state(SCREEN, game_state, valid_moves, square_selected)

        endgame = game_state.checkmate_stalemate_checker()
        if endgame == 0:
            game_over = True
            draw_text(SCREEN, "Black wins.")
        elif endgame == 1:
            game_over = True
            draw_text(SCREEN, "White wins.")
        elif endgame == 2:
            game_over = True
            draw_text(SCREEN, "Stalemate.")

        clock.tick(MAX_FPS)
        py.display.flip()

def menu():
    py.display.set_caption("Menu")

    while True:
        SCREEN.blit(BACKGROUND, (0,0))

        MENU_MOUSE_POS = py.mouse.get_pos()

        MENU_TEXT = get_font(45).render("Chess", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(CENTER, 50))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        CREDIT_TEXT = get_font(15).render("by Boosung Kim", True, "#b68f40")
        CREDIT_RECT = MENU_TEXT.get_rect(center=(CENTER + 7, 100))
        SCREEN.blit(CREDIT_TEXT, CREDIT_RECT)

        SINGLE_PLAYER_BUTTON = Button(image=py.image.load("images/menu/PlayRect.png"), pos=(CENTER, 160), text_input="Single Player", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        MULTI_PLAYER_BUTTON = Button(image=py.image.load("images/menu/PlayRect.png"), pos=(CENTER, 285), text_input="Multi Player", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=py.image.load("images/menu/PlayRect.png"), pos=(CENTER, 410), text_input="Quit", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        for button in [SINGLE_PLAYER_BUTTON, MULTI_PLAYER_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in py.event.get():
            if event.type == py.QUIT:
                py.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if SINGLE_PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    single_player()
                if MULTI_PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    multi_player()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    py.exit()
        
        py.display.update()


if __name__ == "__main__":
    menu()
