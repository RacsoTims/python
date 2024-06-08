"""
This is my main driver file. It will be responsible for
handling user input and displaying the current
GameState object.
"""


import pygame as p
import chess_engine


width = height = 512
dimension = 8
sq_size = height // dimension
max_fps = 15
images = {}

"""
Initialize a global dictionary of images. This will be
called exactly once in the main.
"""


def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP',
              'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        images[piece] = p.transform.scale(
            p.image.load("images/" + piece + ".png"), (sq_size, sq_size))


"""
The main driver for our code. This will handle user input
and updating the graphics.
"""


def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess_engine.GameState()
    load_images()
    running = True
    sq_selected = ()  # no square is selected initially; keeps track of the last click of the user (tuple: (row, col))
    player_clicks = []  # keeps track of player clicks (two tuples: [(6, 4), (4, 4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x, y) location of mouse
                col = location[0] // sq_size
                row = location[1] // sq_size
                if sq_selected == (row, col):  # the user clicked the same square twice
                    sq_selected = ()  # deselect
                    player_clicks = []  # clear player clicks
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)  # append for both 1st and 2nd click
                if len(player_clicks) == 2:
                    move = chess_engine.Move(player_clicks[0],
                                             player_clicks[1], gs.board)
                    print(move.get_chess_notation())
                    gs.make_move(move)
                    sq_selected = ()  # reset user clicks
                    player_clicks = []

        draw_game_state(screen, gs)
        clock.tick(max_fps)
        p.display.flip()


"""
Responsible for all graphics within a current game state.
"""


def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    colours = [p.Color("white"), p.Color("gray")]
    for row in range(dimension):
        for column in range(dimension):
            colour = colours[((row + column) % 2)]
            p.draw.rect(screen, colour, p.Rect(
                column * sq_size, row * sq_size, sq_size, sq_size))


def draw_pieces(screen, board):
    for row in range(dimension):
        for column in range(dimension):
            piece = board[row][column]
            if piece != "--":
                screen.blit(images[piece], p.Rect(
                    column * sq_size, row * sq_size, sq_size, sq_size))


if __name__ == "__main__":
    main()
