import pygame


class Square:
    def __init__(self, x, y, width, height):
        self.status = ''
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
            return 'b'
        else:
            return 'w'

    def determine_highlight_color(self):
        if self.status == 'selected':
            if self.color == 'b':
                return 150, 255, 100
            else:
                return 50, 220, 0
        if self.status == 'move':
            return 115, 200, 225
        if self.status == 'attack':
            return 220, 60, 25
        else:
            if self.color == 'b':
                return 112, 102, 119
            else:
                return 204, 183, 174

    def draw(self, display):
        highlight = self.determine_highlight_color()
        pygame.draw.rect(display, highlight, self.rect)

    def get_coord(self):
        return self.x, self.y


