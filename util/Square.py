import pygame


class Square:
    def __init__(self, x, y, width, height):
        self.is_selected = False
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
            if self.is_selected:
                return 150, 255, 100
            else:
                return 112, 102, 119
        else:
            if self.is_selected:
                return 50, 220, 0
            else:
                return 204, 183, 174

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)

    def get_coord(self):
        return self.x, self.y
