from util.Square import Square


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square_width = width // 8
        self.square_height = height // 8
        self.squares = self.create_squares()

    def create_squares(self):
        squares = []
        for y in range(8):
            for x in range(8):
                square = Square(x, y, self.square_width, self.square_height)
                squares.append(square)
        return squares

    def draw_board(self, screen):
        for square in self.squares:
            square.draw(screen)
