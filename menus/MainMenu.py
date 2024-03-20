import pygame
from util.Button import Button


class MainMenu:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.big_font = pygame.font.Font('freesansbold.ttf', 84)
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        button_width = self.width // 4
        button_x = self.width // 2 - button_width // 2

        self.new_game_btn = Button(button_x,
                                   self.height // 5 * 2,
                                   button_width,
                                   self.height // 10,
                                   'gray',
                                   'New Game',
                                   'black')

        self.settings_btn = Button(button_x,
                                   self.height // 5 * 3,
                                   button_width,
                                   self.height // 10,
                                   'gray',
                                   'Settings',
                                   'black')

        self.quit_btn = Button(button_x,
                               self.height // 5 * 4,
                               button_width,
                               self.height // 10,
                               'gray',
                               'Quit',
                               'black')

    def draw(self, surface):
        title = self.big_font.render('Chess', True, 'black')
        title_rect = title.get_rect(center=(self.width // 2, self.height // 4))
        pygame.draw.rect(surface, 'pink1', self.rect)

        surface.blit(title, title_rect)

        self.new_game_btn.draw(surface)
        self.settings_btn.draw(surface)
        self.quit_btn.draw(surface)
