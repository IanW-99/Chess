import pygame.image

from GamePiece import GamePiece


class Rook(GamePiece):
    def __init__(self, x, y, color, size):
        super().__init__(x, y, color, size, 'Rook')

        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.size = size

    def draw(self, board_surface):
        if self.color == 'w':
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\wRook.png')
        else:
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\bRook.png')

        scaled_img = pygame.transform.scale(img, (self.size, self.size))
        board_surface.blit(scaled_img, (self.pos_x * self.size, self.pos_y * self.size))

