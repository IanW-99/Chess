from GamePiece import GamePiece


class Queen(GamePiece):
    def __init__(self, x, y, color, size):
        super().__init__(x, y, color, size)

        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.size = size
