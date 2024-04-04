import pygame
import json

from Board import Board
from menus.MainMenu import MainMenu
from menus.OptionsMenu import OptionsMenu
from menus.PromotionMenu import PromotionMenu
from menus.SettingsMenu import SettingsMenu
from menus.WinScreen import WinScreen

with open('settings.json', 'r') as openfile:
    json_object = json.load(openfile)
    window_size = (json_object['screen_width'], json_object['screen_height'])
    board_size = json_object['board_size']
    board_theme = json_object['theme']

pygame.init()

screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Chess")


def game():
    board_surface = pygame.Surface((board_size, board_size))
    board_x = window_size[0] // 2 - board_size // 2
    board_y = window_size[1] // 2 - board_size // 2
    board = Board(board_size, board_size)

    options_menu_size = ((window_size[0] / 2.5), (window_size[1] / 2.5))
    options_menu_surface = pygame.Surface((options_menu_size[0], options_menu_size[1]))
    options_menu_x = window_size[0] // 2 - options_menu_surface.get_width() // 2
    options_menu_y = window_size[1] // 2 - options_menu_surface.get_height() // 2
    options_menu = OptionsMenu(*options_menu_size)

    promotion_menu_size = ((window_size[0] - board_size) / 2.5, board_size)
    promotion_menu_surface = pygame.Surface(promotion_menu_size)
    promotion_menu_x = board_x + window_size[0] // 2 + 10
    promotion_menu_y = board_y
    promotion_menu = PromotionMenu(*promotion_menu_size, board)

    def display_board():

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run_options_menu()

            draw_game()

    def draw_game(turn_message=None):
        screen.fill("pink1")

        board_border = pygame.Rect(board_x - 5, board_y - 5, board_size + 10, board_size + 10)
        pygame.draw.rect(screen,
                         'black',
                         board_border,
                         border_radius=5)

        board.draw_board(board_surface)
        screen.blit(board_surface, (board_x, board_y))

        if turn_message is not None:
            center = (((window_size[0] - board_size) // 4), (board_y + board_size // 2))
            turn_message_border = pygame.Rect(0, 0, turn_message.get_width() + 20, turn_message.get_height() + 20)
            turn_message_border.center = center
            turn_message_background = pygame.Rect(0, 0, turn_message.get_width() + 10, turn_message.get_height() + 10)
            turn_message_background.center = center

            pygame.draw.rect(screen, 'black', turn_message_border, border_radius=2)
            pygame.draw.rect(screen, 'gray', turn_message_background, border_radius=2)
            screen.blit(turn_message, turn_message.get_rect(center=center))

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
        if (board_x <= x <= board_x + board_size) and (board_y <= y <= board_y + board_size):
            return True
        else:
            return False

    def is_on_promotion_menu(x, y):
        if (promotion_menu_x <= x <= promotion_menu_x + promotion_menu_size[0]) \
                and (promotion_menu_y <= y <= promotion_menu_y + promotion_menu_size[1]):
            return True
        else:
            return False

    def run_game():
        running = True

        font = pygame.font.Font('freesansbold.ttf', 32)

        turn_message = font.render(f'{board.turn} Turn', True, 'Black')

        while running:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if is_on_board(mouse[0], mouse[1]) and not board.active_promotion:
                        board.handle_click(mouse[0] - board_x, mouse[1] - board_y)
                    elif is_on_promotion_menu(mouse[0], mouse[1]) and board.active_promotion:
                        promotion_menu.handle_click((mouse[0] - promotion_menu_x, mouse[1] - promotion_menu_y))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run_options_menu()

            draw_game(turn_message)

            if board.is_checkmate:
                turn_message = font.render(f"Checkmate! {get_full_color(get_opposite_color(board.turn))} wins!",
                                           True,
                                           "Black")
                run_win_screen(get_full_color(get_opposite_color(board.turn)))
            elif board.turn == 'w':
                turn_message = font.render('White Turn', True, 'Black')
            else:
                turn_message = font.render('Black Turn', True, 'Black')

            draw_game(turn_message)

    def run_options_menu():
        running = True

        while running:
            mouse = pygame.mouse.get_pos()

            options_menu.draw(options_menu_surface)
            screen.blit(options_menu_surface, (options_menu_x, options_menu_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_menu.main_menu_btn.is_hovered((mouse[0] - options_menu_x, mouse[1] - options_menu_y)):
                        main()
                    elif options_menu.new_game_btn.is_hovered((mouse[0] - options_menu_x, mouse[1] - options_menu_y)):
                        restart()
                    elif options_menu.quit_btn.is_hovered((mouse[0] - options_menu_x, mouse[1] - options_menu_y)):
                        pygame.quit()
                        raise SystemExit

            pygame.display.flip()
            clock.tick(60)

    def run_win_screen(winner):
        ws_size = ((window_size[0] / 2.5), (window_size[1] / 2.5))
        ws_surface = pygame.Surface((ws_size[0], ws_size[1]))
        ws_x = window_size[0] // 2 - ws_surface.get_width() // 2
        ws_y = window_size[1] // 2 - ws_surface.get_height() // 2
        win_screen = WinScreen(*ws_size, winner)

        running = True

        while running:
            mouse = pygame.mouse.get_pos()

            win_screen.draw(ws_surface)
            screen.blit(ws_surface, (ws_x, ws_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if win_screen.view_btn.is_hovered((mouse[0] - ws_x, mouse[1] - ws_y)):
                        display_board()
                    elif win_screen.new_game_btn.is_hovered((mouse[0] - ws_x, mouse[1] - ws_y)):
                        restart()
                    elif win_screen.main_menu_btn.is_hovered((mouse[0] - ws_x, mouse[1] - ws_y)):
                        main()
                    elif win_screen.quit_btn.is_hovered((mouse[0] - ws_x, mouse[1] - ws_y)):
                        pygame.quit()
                        raise SystemExit

            pygame.display.flip()
            clock.tick(60)

    run_game()


def main():

    main_menu_surface = pygame.Surface(window_size)
    main_menu = MainMenu(*window_size)

    running = True

    while running:
        mouse = pygame.mouse.get_pos()

        main_menu.draw(main_menu_surface)
        screen.blit(main_menu_surface, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu.new_game_btn.is_hovered(mouse):
                    game()
                elif main_menu.settings_btn.is_hovered(mouse):
                    run_settings_menu()
                elif main_menu.quit_btn.is_hovered(mouse):
                    pygame.quit()
                    raise SystemExit

        pygame.display.flip()
        clock.tick(60)


def restart():
    game()
    exit()


def run_settings_menu():
    settings_menu_size = board_size, board_size
    settings_menu_surface = pygame.Surface((settings_menu_size[0], settings_menu_size[1]))
    settings_menu_x = window_size[0] // 2 - board_size // 2
    settings_menu_y = window_size[1] // 2 - board_size // 2
    settings_menu = SettingsMenu(*settings_menu_size)

    running = True

    while running:
        mouse = pygame.mouse.get_pos()

        settings_menu.draw(settings_menu_surface)
        screen.blit(settings_menu_surface, (settings_menu_x, settings_menu_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.display.flip()
        clock.tick(60)


main()
