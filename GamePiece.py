

class GamePiece:

    def __init__(self, x, y, color, size, piece_type, board):

        self.pos_x = x
        self.pos_y = y
        self._color = color
        self.size = size
        self._piece_type = piece_type
        self.board = board

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def piece_type(self):
        return self._piece_type

    @classmethod
    def draw(cls, screen):
        pass

    @classmethod
    def get_moves(cls):
        pass

    def get_pos(self):
        return self.pos_x, self.pos_y

    def is_valid_square(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

    @classmethod
    def move(cls, x, y):
        pass
