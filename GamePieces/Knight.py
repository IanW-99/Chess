import pygame

from GamePiece import GamePiece


class Knight(GamePiece):
    def __init__(self, x, y, color, size, board):
        super().__init__(x, y, color, size, 'Knight', board)

        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.size = size
        self.board = board

    def draw(self, board_surface):
        if self.color == 'w':
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\wKnight.png')
        else:
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\bKnight.png')

        scaled_img = pygame.transform.scale(img, (self.size, self.size))
        board_surface.blit(scaled_img, (self.pos_x * self.size, self.pos_y * self.size))
