import pygame
from util.Button import Button


class SettingsMenu:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border_rect = pygame.Rect(0, 0, self.width, self.height)
        self.main_rect = pygame.Rect(5, 5, self.width - 10, self.height - 10)
        self.font = pygame.font.Font('freesansbold.ttf', 64)

        self.msg = self.font.render(f"Settings",
                                    True,
                                    "Black")
        self.msg_rect = self.msg.get_rect(center=(self.width / 2, self.height / 8))

    def draw(self, surface):
        pygame.draw.rect(surface, 'black', self.border_rect)
        pygame.draw.rect(surface, 'gray', self.main_rect, border_radius=5)

        surface.blit(self.msg, self.msg_rect)
