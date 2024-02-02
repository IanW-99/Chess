

class GamePiece:

    def __init__(self, x, y, color, size, piece_type, board):

        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.size = size
        self.piece_type = piece_type
        self.board = board

    @classmethod
    def draw(cls, screen):
        pass

    def get_piece_type(self):
        return self.piece_type

    def get_color(self):
        return self.color

    def get_pos(self):
        return self.pos_x, self.pos_y
