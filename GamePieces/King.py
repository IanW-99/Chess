import pygame

from GamePiece import GamePiece


class King(GamePiece):
    def __init__(self, x, y, color, size, board):
        super().__init__(x, y, color, size, 'King', board)

        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.size = size
        self.board = board

    def can_move_to(self, x, y, move_type):
        if not self.is_valid_square(x, y):
            return False
        square_content = self.board.get_square_content(x, y)
        if square_content is None and move_type == 'move':
            return True
        if square_content is not None:
            if square_content.color != self.color and move_type == 'attack':
                return True
        return False

    def draw(self, board_surface):
        if self.color == 'w':
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\wKing.png')
        else:
            img = pygame.image.load('C:\\Users\\iwash\\PycharmProjects\\Chess\\imgs\\bKing.png')

        scaled_img = pygame.transform.scale(img, (self.size, self.size))
        board_surface.blit(scaled_img, (self.pos_x * self.size, self.pos_y * self.size))

    def generate_moves(self):
        moves = []
        direction_sets = {(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)}
        x = self.pos_x
        y = self.pos_y
        for direction_set in direction_sets:
            x_adjustment = direction_set[0]
            y_adjustment = direction_set[1]

            if not self.is_valid_square(x + x_adjustment, y + y_adjustment):
                continue
            if self.board.get_square_content(x + x_adjustment, y + y_adjustment) is not None:
                move_type = 'attack'
            else:
                move_type = 'move'

            if self.can_move_to(x + x_adjustment, y + y_adjustment, move_type):
                moves.append(((x + x_adjustment, y + y_adjustment), move_type))
            else:
                continue

        return moves

    def move(self, x, y):
        self.pos_x = x
        self.pos_y = y
