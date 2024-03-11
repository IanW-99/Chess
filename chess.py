import pygame

from Board import Board
from menus.PromotionMenu import PromotionMenu

pygame.init()

window_size = (1280, 720)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Chess")

board_size = 640
board_surface = pygame.Surface((board_size, board_size))

board_x = window_size[0] // 2 - board_size // 2
board_y = window_size[1] // 2 - board_size // 2

board = Board(board_size, board_size)

promotion_menu_size = ((window_size[0] - board_size) // 2, board_size)
promotion_menu_surface = pygame.Surface(promotion_menu_size)

promotion_menu_x = board_x + window_size[0] // 2
promotion_menu_y = board_y

promotion_menu = PromotionMenu(*promotion_menu_size, board)


def draw_game(turn_message):
    screen.fill("pink")

    board.draw_board(board_surface)
    screen.blit(board_surface, (board_x, board_y))

    screen.blit(turn_message, turn_message.get_rect())

    if board.active_promotion:
        promotion_menu.draw_menu(promotion_menu_surface)
        screen.blit(promotion_menu_surface, (promotion_menu_x, promotion_menu_y))

    pygame.display.flip()
    clock.tick(60)


def get_full_color(color):
    if color == 'w':
        return 'White'
    return 'Black'


def get_opposite_color(color):
    if color == 'w':
        return 'b'
    return 'w'


def is_on_board(x, y):
    if (board_x <= x <= board_x+board_size) and (board_y <= y <= board_y+board_size):
        return True
    else:
        return False


def is_on_promotion_menu(x, y):
    if (promotion_menu_x <= x <= promotion_menu_x+promotion_menu_size[0]) \
            and (promotion_menu_y <= y <= promotion_menu_y+promotion_menu_size[1]):
        return True
    else:
        return False


def run_game():
    running = True

    font = pygame.font.Font('freesansbold.ttf', 32)

    while running:
        # Process player inputs.
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_on_board(mouse[0], mouse[1]) and not board.active_promotion:
                    board.handle_click(mouse[0]-board_x, mouse[1]-board_y)
                if is_on_promotion_menu(mouse[0], mouse[1]) and board.active_promotion:
                    promotion_menu.handle_click((mouse[0]-promotion_menu_x, mouse[1]-promotion_menu_y))

        if board.is_checkmate:
            turn_message = font.render(f"Checkmate! {get_full_color(get_opposite_color(board.turn))} wins!",
                                       True,
                                       "Black")
        elif board.turn == 'w':
            turn_message = font.render('White Turn', True, 'Black')
        else:
            turn_message = font.render('Black Turn', True, 'Black')

        draw_game(turn_message)


run_game()
