import copy

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
        self.is_checkmate = False
        self.width = width
        self.height = height
        self.square_width = width // 8
        self.square_height = height // 8
        self.squares = self.create_squares()
        self.board_state = self.place_initial_pieces()
        self.selected_square = None
        self._turn = 'w'
        self._active_promotion = False
        self.promoting_piece = None

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, value):
        self._turn = value

    @property
    def active_promotion(self):
        return self._active_promotion

    @active_promotion.setter
    def active_promotion(self, value):
        self._active_promotion = value

    def castle_king_side(self):
        if self.turn == 'b':
            affected_squares = {"king_start": (4, 0), "rook_start": (7, 0), "king_final": (6, 0), "rook_final": (5, 0)}
        else:
            affected_squares = {"king_start": (4, 7), "rook_start": (7, 7), "king_final": (6, 7), "rook_final": (5, 7)}

        king = self.get_square_content(*affected_squares.get("king_start"))
        rook = self.get_square_content(*affected_squares.get("rook_start"))

        king.move(*affected_squares.get("king_final"))
        self.update_square_content(*affected_squares.get("king_final"), king)
        self.update_square_content(*affected_squares.get("king_start"), None)

        rook.move(*affected_squares.get("rook_final"))
        self.update_square_content(*affected_squares.get("rook_final"), rook)
        self.update_square_content(*affected_squares.get("rook_start"), None)

    def castle_queen_side(self):
        if self.turn == 'b':
            affected_squares = {"king_start": (4, 0), "rook_start": (0, 0), "king_final": (2, 0), "rook_final": (3, 0)}
        else:
            affected_squares = {"king_start": (4, 7), "rook_start": (0, 7), "king_final": (2, 7), "rook_final": (3, 7)}

        king = self.get_square_content(*affected_squares.get("king_start"))
        rook = self.get_square_content(*affected_squares.get("rook_start"))

        king.move(*affected_squares.get("king_final"))
        self.update_square_content(*affected_squares.get("king_final"), king)
        self.update_square_content(*affected_squares.get("king_start"), None)

        rook.move(*affected_squares.get("rook_final"))
        self.update_square_content(*affected_squares.get("rook_final"), rook)
        self.update_square_content(*affected_squares.get("rook_start"), None)

    def create_squares(self):
        squares = {}
        for y in range(8):
            for x in range(8):
                square = Square(x, y, self.square_width, self.square_height)
                squares[x, y] = square
        return squares

    def default_squares(self):
        for square in self.squares.values():
            square.status = ''

    def draw_board(self, board_surface):
        for square in self.squares.values():
            square.draw(board_surface)

        for i in range(8):
            for j in range(8):
                piece = self.board_state[i][j]
                if piece is not None:
                    piece.draw(board_surface)

    @staticmethod
    def get_opposite_color(color):
        if color == 'w':
            return 'b'
        return 'w'

    def handle_click(self, x_relative, y_relative):
        x = (x_relative - 1) // self.square_width
        y = (y_relative - 1) // self.square_height

        square = self.get_square(x, y)
        square_content = self.get_square_content(x, y)
        if square_content is not None and square_content.color != self.turn and square.status != 'attack':
            return
        if self.selected_square is not None:
            if square.status == '' or square == self.selected_square:
                self.selected_square.status = ''
                self.selected_square = None
            else:
                selected_square_content = self.get_square_content(self.selected_square.x, self.selected_square.y)
                if selected_square_content is not None:
                    if square.status == 'castle_king_side':
                        self.castle_king_side()
                    elif square.status == 'castle_queen_side':
                        self.castle_queen_side()
                    else:
                        selected_square_content.move(x, y)
                        self.update_square_content(self.selected_square.x, self.selected_square.y, None)
                        self.update_square_content(x, y, selected_square_content)
                        if self.promotion_check(selected_square_content):
                            self.promotion_signal(selected_square_content)

                    self.selected_square = None
                    self.default_squares()
                    self.update_turn()
                    if not self.is_in_check(self.board_state, self.turn):
                        return
                    if self.is_in_checkmate(self.turn):
                        self.is_checkmate = True
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

    @staticmethod
    def get_king_location(board_state, color):
        for y in range(8):
            for x in range(8):
                piece = board_state[y][x]
                if not issubclass(piece.__class__, GamePiece) or piece.color != color or piece.piece_type != 'King':
                    continue
                return x, y

    def get_square(self, x, y):
        return self.squares[x, y]

    def get_square_content(self, x, y):
        return self.board_state[y][x]

    def is_in_check(self, board_state, color):
        # iterate through all moves and check if any are same square as king
        if board_state is None:
            board_state = self.board_state

        king_location = self.get_king_location(board_state, color)

        for row in board_state:
            for piece in row:
                if issubclass(piece.__class__, GamePiece) and piece.color != color:
                    moves = piece.generate_moves()
                    if len(moves) > 0 and (king_location, 'attack') in moves:
                        return True
                    else:
                        pass

    def is_in_checkmate(self, color):
        for row in self.board_state:
            for piece in row:
                if not issubclass(piece.__class__, GamePiece) or piece.color != color:
                    continue
                if len(piece.get_moves()) > 0:
                    return False
            return True

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

    def promote(self, piece_type):
        if not issubclass(self.promoting_piece.__class__, GamePiece):
            raise Exception(f"Promoting piece was not of valid type. Was of type {self.promoting_piece.__class__}")

        x = self.promoting_piece.pos_x
        y = self.promoting_piece.pos_y
        color = self.promoting_piece.color

        piece_type.lower()
        if piece_type == 'bishop':
            new_piece = Bishop(x, y, color, self.square_width, self)
        elif piece_type == 'knight':
            new_piece = Knight(x, y, color, self.square_width, self)
        elif piece_type == 'queen':
            new_piece = Queen(x, y, color, self.square_width, self)
        elif piece_type == 'rook':
            new_piece = Rook(x, y, color, self.square_width, self)
        else:
            raise Exception("Promotion choice was not of valid type")

        self.update_square_content(x, y, new_piece)

        self.active_promotion = False
        self.promoting_piece = None

    @staticmethod
    def promotion_check(piece: GamePiece):
        if not piece.piece_type == 'Pawn':
            return False
        if piece.color == 'b' and piece.pos_y != 7:
            return False
        if piece.color == 'w' and piece.pos_y != 0:
            return False
        return True

    def promotion_signal(self, piece: GamePiece):
        self.promoting_piece = piece
        self.active_promotion = True

    def sim_board_state(self, piece: GamePiece, x, y):
        temp_board_state = copy.deepcopy(self.board_state)
        origin = piece.get_pos()
        temp_board_state[y][x] = piece
        temp_board_state[origin[1]][origin[0]] = None

        return temp_board_state

    def update_square_content(self, x, y, piece):
        self.board_state[y][x] = piece

    def update_squares(self, moves):

        for move in moves:
            x = move[0][0]
            y = move[0][1]
            square = self.get_square(x, y)
            square.status = move[1]

    def update_turn(self):
        self.turn = self.get_opposite_color(self.turn)
