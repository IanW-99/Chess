import pygame

from GamePiece import GamePiece
from GamePieces.Rook import Rook


class King(GamePiece):
    def __init__(self, x, y, color, size, board):
        super().__init__(x, y, color, size, 'King', board)

        self.has_moved = False
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.size = size
        self.board = board

    def can_king_side_castle(self):
        if self.board.is_in_check(None, self.color):
            return False

        if self.color == 'b':
            squares_to_check = {"king": (4, 0),
                                "first_empty": (5, 0),
                                "second_empty": (6, 0),
                                "rook": (7, 0)}
        else:
            squares_to_check = {"king": (4, 7),
                                "first_empty": (5, 7),
                                "second_empty": (6, 7),
                                "rook": (7, 7)}

        king = self.board.get_square_content(*squares_to_check.get("king"))
        if not isinstance(king, King) or king.color != self.color or king.has_moved is True:
            return False

        rook = self.board.get_square_content(*squares_to_check.get("rook"))
        if not isinstance(rook, Rook) or rook.color != self.color or rook.has_moved is True:
            return False

        if self.board.get_square_content(*squares_to_check.get("first_empty")) is not None \
                or self.board.get_square_content(*squares_to_check.get("second_empty")) is not None:
            return False

        for square_location in squares_to_check.values():
            simulated_board_state = self.board.sim_board_state(king, *square_location)
            if self.board.is_in_check(simulated_board_state, self.color):
                return False

        return True

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

    def can_queen_side_castle(self):
        if self.board.is_in_check(None, self.color):
            return False

        if self.color == 'b':
            squares_to_check = {"king": (4, 0),
                                "first_empty": (3, 0),
                                "second_empty": (2, 0),
                                "third_empty": (1, 0),
                                "rook": (0, 0)}
        else:
            squares_to_check = {"king": (4, 7),
                                "first_empty": (3, 7),
                                "second_empty": (2, 7),
                                "third_empty": (1, 7),
                                "rook": (0, 7)}

        king = self.board.get_square_content(*squares_to_check.get("king"))
        if not isinstance(king, King) or king.color != self.color or king.has_moved is True:
            return False

        rook = self.board.get_square_content(*squares_to_check.get("rook"))
        if not isinstance(rook, Rook) or rook.color != self.color or rook.has_moved is True:
            return False

        if self.board.get_square_content(*squares_to_check.get("first_empty")) is not None \
                or self.board.get_square_content(*squares_to_check.get("second_empty")) is not None \
                or self.board.get_square_content(*squares_to_check.get("third_empty")) is not None:
            return False

        for square_location in squares_to_check.values():
            simulated_board_state = self.board.sim_board_state(king, *square_location)
            if self.board.is_in_check(simulated_board_state, self.color):
                return False

        return True

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

    def validate_moves(self, moves: list):
        # reverse list to avoid iteration being interrupted by remove()
        for move in reversed(moves):
            if not self.causes_check(move[0][0], move[0][1]):
                continue
            moves.remove(move)

        if self.can_king_side_castle():
            if self.color == 'b':
                moves.append(((6, 0), 'castle_king_side'))
            else:
                moves.append(((6, 7), 'castle_king_side'))

        if self.can_queen_side_castle():
            if self.color == 'b':
                moves.append(((2, 0), 'castle_queen_side'))
            else:
                moves.append(((2, 7), 'castle_queen_side'))
        return moves
