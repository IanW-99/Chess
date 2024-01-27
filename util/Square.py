import pygame


class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos_x = x * width
        self.pos_y = y * height
        self.color = self.determine_color()
        self.rect = pygame.Rect(self.pos_x, self.pos_y, width, height)

    def determine_color(self):
        if (self.x + self.y) % 2 == 0:
            return 0, 0, 0
        else:
            return 255, 255, 255

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)

    def get_coord(self):
        return self.x, self.y
