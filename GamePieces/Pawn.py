import pygame

from GamePiece import GamePiece


class Pawn(GamePiece):
    def __init__(self, x, y, color, size, board):
        super().__init__(x, y, color, size, 'Pawn', board)

        self.initial_pos = x, y
        self.has_moved = False
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.size = size
        self.board = board

    def draw(self, board_surface):
        if self.color == 'w':
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\wPawn.png')
        else:
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\bPawn.png')

        scaled_img = pygame.transform.scale(img, (self.size, self.size))
        board_surface.blit(scaled_img, (self.pos_x * self.size, self.pos_y * self.size))

    def move(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.has_moved = True

    def get_moves(self):
        if self.color == 'b':
            return self.get_moves_black()
        else:
            return self.get_moves_white()

    def get_moves_black(self):
        # flag moves
        moves = []

        # forward moves
        if not self.has_moved \
                and self.can_move_to(self.pos_x, self.pos_y+1, 'move') \
                and self.can_move_to(self.pos_x, self.pos_y+2, 'move'):
            moves.append(((self.pos_x, self.pos_y+2), 'move'))

        if self.can_move_to(self.pos_x, self.pos_y+1, 'move'):
            moves.append(((self.pos_x, self.pos_y+1), 'move'))

        # diagonal attacks
        if self.can_move_to(self.pos_x+1, self.pos_y+1, 'attack'):
            moves.append(((self.pos_x+1, self.pos_y+1), 'attack'))

        if self.can_move_to(self.pos_x-1, self.pos_y+1, 'attack'):
            moves.append(((self.pos_x-1, self.pos_y+1), 'attack'))

        return moves

    def get_moves_white(self):
        # flag moves
        moves = []

        # forward moves
        if not self.has_moved \
                and self.can_move_to(self.pos_x, self.pos_y-1, 'move') \
                and self.can_move_to(self.pos_x, self.pos_y-2, 'move'):
            moves.append(((self.pos_x, self.pos_y-2), 'move'))

        if self.can_move_to(self.pos_x, self.pos_y-1, 'move'):
            moves.append(((self.pos_x, self.pos_y-1), 'move'))

        # diagonal attacks
        if self.can_move_to(self.pos_x+1, self.pos_y-1, 'attack'):
            moves.append(((self.pos_x+1, self.pos_y-1), 'attack'))

        if self.can_move_to(self.pos_x-1, self.pos_y-1, 'attack'):
            moves.append(((self.pos_x-1, self.pos_y-1), 'attack'))

        return moves

    def can_move_to(self, x, y, move_type):
        if not self.is_valid_square(x, y):
            return False
        square_content = self.board.get_square_content(x, y)
        if square_content is None and move_type == 'move':
            return True
        if square_content is GamePiece:
            if square_content.get_color() != self.color and move_type == 'attack':
                return True
        return False

