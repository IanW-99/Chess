import pygame
from util.Button import Button


class WinScreen:

    def __init__(self, width, height, winner):
        self.width = width
        self.height = height
        self.winner = winner
        self.border_rect = pygame.Rect(0, 0, self.width, self.height)
        self.main_rect = pygame.Rect(5, 5, self.width - 10, self.height - 10)
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.msg = self.font.render(f"Checkmate! {self.winner} wins!",
                                    True,
                                    "Black")
        self.msg_rect = self.msg.get_rect(center=(self.width / 2, self.height / 5))

        button_width = self.width // 2
        button_x = button_width // 2

        self.view_btn = Button(button_x,
                               self.height // 5 * 2,
                               button_width,
                               self.height // 10,
                               'gray',
                               'Show Board',
                               'black')

        self.new_game_btn = Button(button_x,
                                   self.height // 5 * 3,
                                   button_width,
                                   self.height // 10,
                                   'gray',
                                   'New Game',
                                   'black')

        self.quit_btn = Button(button_x,
                               self.height // 5 * 4,
                               button_width,
                               self.height // 10,
                               'gray',
                               'Quit',
                               'black')

    def draw(self, surface):
        pygame.draw.rect(surface, 'black', self.border_rect)
        pygame.draw.rect(surface, 'gray', self.main_rect, border_radius=5)

        surface.blit(self.msg, self.msg_rect)

        self.view_btn.draw(surface)
        self.new_game_btn.draw(surface)
        self.quit_btn.draw(surface)
