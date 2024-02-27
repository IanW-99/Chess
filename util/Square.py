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
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.highlight_rect = pygame.Rect(self.pos_x + self.width // 10,
                                          self.pos_y + self.height // 10,
                                          self.width - self.width // 5,
                                          self.height - self.height // 5)

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
        if self.status == 'move' or self.status == 'castle_king_side' or self.status == 'castle_queen_side':
            return 115, 200, 225
        if self.status == 'attack':
            return 220, 60, 25

    def draw(self, display):
        pygame.draw.rect(display, self.get_default_color(), self.rect)
        if self.status == '':
            return
        pygame.draw.rect(display, self.determine_highlight_color(), self.highlight_rect)

    def get_coord(self):
        return self.x, self.y

    def get_coord_x(self):
        return self.x

    def get_coord_y(self):
        return self.y

    def get_default_color(self):
        if self.color == 'b':
            return 112, 102, 119
        else:
            return 204, 183, 174

