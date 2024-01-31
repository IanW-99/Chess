import pygame

from GamePiece import GamePiece


class Queen(GamePiece):
    def __init__(self, x, y, color, size):
        super().__init__(x, y, color, size, 'Queen')

        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.size = size

    def draw(self, board_surface):
        if self.color == 'w':
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\wQueen.png')
        else:
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\bQueen.png')

        scaled_img = pygame.transform.scale(img, (self.size, self.size))
        board_surface.blit(scaled_img, (self.pos_x * self.size, self.pos_y * self.size))
