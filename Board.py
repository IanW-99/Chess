import sys

from util.Square import Square
from GamePiece import GamePiece
from GamePieces.Bishop import Bishop
from GamePieces.King import King
from GamePieces.Knight import Knight
from GamePieces.Pawn import Pawn
from GamePieces.Queen import Queen
from GamePieces.Rook import Rook


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square_width = width // 8
        self.square_height = height // 8
        self.squares = self.create_squares()
        self.board_state = self.place_initial_pieces()
        self.selected_square = None

    def create_squares(self):
        squares = {}
        for y in range(8):
            for x in range(8):
                square = Square(x, y, self.square_width, self.square_height)
                squares[x, y] = square
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

        board_state = [[GamePiece for _ in range(8)] for _ in range(8)]

        for i in range(8):
            for j in range(8):
                piece_code = init_board_state[i][j]
                if piece_code == '':
                    board_state[i][j] = None
                    continue
                color = piece_code[:1]
                piece_type = piece_code[1:]

                if piece_type == 'Bishop':
                    board_state[i][j] = Bishop(j, i, color, self.square_width, self)
                elif piece_type == 'King':
                    board_state[i][j] = King(j, i, color, self.square_width, self)
                elif piece_type == 'Knight':
                    board_state[i][j] = Knight(j, i, color, self.square_width, self)
                elif piece_type == 'Pawn':
                    board_state[i][j] = Pawn(j, i, color, self.square_width, self)
                elif piece_type == 'Queen':
                    board_state[i][j] = Queen(j, i, color, self.square_width, self)
                else:
                    board_state[i][j] = Rook(j, i, color, self.square_width, self)

        return board_state

    def draw_board(self, board_surface):
        for square in self.squares.values():
            square.draw(board_surface)

        for i in range(8):
            for j in range(8):
                piece = self.board_state[i][j]
                if piece is not None:
                    piece.draw(board_surface)

    def handle_click(self, x_relative, y_relative):
        x = (x_relative - 1) // self.square_width
        y = (y_relative - 1) // self.square_height

        square = self.get_square(x, y)
        if self.selected_square is not None:
            if square.status == '':
                self.selected_square.status = ''
                self.selected_square = None
            else:
                square_content = self.get_square_content(self.selected_square.x, self.selected_square.y)
                if square_content is not None:
                    square_content.move(x, y)
                    self.update_square_content(self.selected_square.x, self.selected_square.y, None)
                    self.update_square_content(x, y, square_content)
                    self.selected_square = None
                    self.default_squares()
                    return

        self.default_squares()
        self.selected_square = square
        square.status = 'selected'
        square_content = self.get_square_content(x, y)
        # recolor the squares for each of the moves
        if square_content is None:
            return
        moves = square_content.get_moves()
        self.update_squares(moves)

    def get_square(self, x, y):
        return self.squares[x, y]

    def get_square_content(self, x, y):
        return self.board_state[y][x]

    def update_square_content(self, x, y, piece):
        self.board_state[y][x] = piece

    def update_squares(self, moves):

        for move in moves:
            x = move[0][0]
            y = move[0][1]
            square = self.get_square(x, y)
            square.status = move[1]

    def default_squares(self):
        for square in self.squares.values():
            square.status = ''
