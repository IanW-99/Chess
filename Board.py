from util.Square import Square
from GamePiece import GamePiece


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square_width = width // 8
        self.square_height = height // 8
        self.squares = self.create_squares()
        self.board_state = self.place_initial_pieces()

    def create_squares(self):
        squares = []
        for y in range(8):
            for x in range(8):
                square = Square(x, y, self.square_width, self.square_height)
                squares.append(square)
        return squares

    def place_initial_pieces(self):
        init_board_state = [
            ['bRook', 'bKnight', 'bBishop', 'bQueen', 'bKing', 'bBishop', 'bKnight', 'bRook'],
            ['bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn'],
            ['wRook', 'wKnight', 'wBishop', 'wQueen', 'wKing', 'wBishop', 'wKnight', 'wRook'],
        ]

        board_state = [[None]*8]*8
        '''
        for i in range(8):
            for j in range(8):
                piece_code = init_board_state[i][j]
                if piece_code == '':
                    board_state[i][j] = None
                    continue
                color = piece_code[:1]
                piece_type = piece_code[1:]

                board_state[i][j] = GamePiece(i, j, color, piece_type, self.square_width)
        '''

        return board_state

    def draw_board(self, screen):
        for square in self.squares:
            square.draw(screen)
