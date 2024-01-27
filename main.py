import pygame

from Board import Board

pygame.init()

window_size = (1280, 720)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

board_size = 640
board_surface = pygame.Surface((board_size, board_size))


def draw():
    # draw board surface
    screen.fill("pink")
    board = Board(board_size, board_size)
    board.draw_board(board_surface)

    # draw board surface onto screen
    screen.blit(board_surface, ((window_size[0] // 2 - board_size // 2), (window_size[1] // 2 - board_size // 2)))


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    draw()

    pygame.display.flip()
    clock.tick(60)
