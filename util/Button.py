import pygame


class Button:

    def __init__(self, x, y, width, height, color, text='', outline=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.outline = outline

    def draw(self, surface):
        if self.outline:
            pygame.draw.rect(surface,
                             self.outline,
                             (self.x - 2, self.y - 2, self.width + 4, self.height + 4),
                             0,
                             border_radius=2)

        pygame.draw.rect(surface,
                         self.color,
                         (self.x, self.y, self.width, self.height),
                         0,
                         border_radius=2)

        if self.text != '':
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(self.text, 1, (0, 0, 0))
            surface.blit(text,
                         (self.x + (self.width / 2 - text.get_width() / 2),
                          (self.y + (self.height / 2 - text.get_height() / 2))))

    def is_hovered(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False
