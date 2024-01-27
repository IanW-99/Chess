import pygame


class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = self.determine_color()
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def determine_color(self):
        if self.width + self.height % 2 == 0:
            return 0, 0, 0
        else:
            return 255, 255, 255

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)

    def get_coord(self):
        return self.x, self.y
