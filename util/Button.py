import pygame


class Button:
    def __init__(self, x, y, image, width=100, height=50, is_active=True,):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._is_active = is_active

        img = pygame.image.load(self.image)
        self.display = pygame.transform.scale(img, (self.width, self.height)).convert()

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, status):
        self._is_active = status

    def draw(self, screen):
        if not self.is_active:
            return
        screen.blit(self.display, (self.x, self.y))


