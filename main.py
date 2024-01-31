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


def draw():
    # draw board surface
    screen.fill("pink")
    board.draw_board(board_surface)

    # draw board surface onto screen
    screen.blit(board_surface, (board_x, board_y))


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

    draw()

    pygame.display.flip()
    clock.tick(60)
