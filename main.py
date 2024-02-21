import pygame

from Board import Board

pygame.init()

window_size = (1280, 720)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

board_size = 640
board_surface = pygame.Surface((board_size, board_size))

board_x = window_size[0] // 2 - board_size // 2
board_y = window_size[1] // 2 - board_size // 2

board = Board(board_size, board_size)

font = pygame.font.Font('freesansbold.ttf', 32)

turn_message = font.render('White Turn', True, 'Black')
turn_message_rect = turn_message.get_rect()


def draw():
    # draw board surface
    screen.fill("pink")
    board.draw_board(board_surface)

    # draw board surface onto screen
    screen.blit(board_surface, (board_x, board_y))

    # display turn message
    screen.blit(turn_message, turn_message_rect)


def get_full_color(color):
    if color == 'w':
        return 'White'
    return 'Black'


def get_game_state():
    return


def get_opposite_color(color):
    if color == 'w':
        return 'b'
    return 'w'


def is_on_board(x, y):
    if (board_x <= x <= board_x+board_size) and (board_y <= y <= board_y+board_size):
        return True
    else:
        return False


while True:
    # Process player inputs.
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_on_board(mouse[0], mouse[1]):
                board.handle_click(mouse[0]-board_x, mouse[1]-board_y)

    if board.is_checkmate:
        turn_message = font.render(f"Checkmate! {get_full_color(get_opposite_color(board.turn))} wins!", True, 'Black')

    elif board.turn == 'w':
        turn_message = font.render('White Turn', True, 'Black')
    else:
        turn_message = font.render('Black Turn', True, 'Black')

    draw()

    pygame.display.flip()
    clock.tick(60)
