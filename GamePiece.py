

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
    def generate_moves(cls):
        return list

    @classmethod
    def move(cls, x, y):
        pass

    def get_pos(self):
        return self.pos_x, self.pos_y

    def is_valid_square(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

    def causes_check(self, x, y):
        temp_board_state = self.board.sim_board_state(self, x, y)
        if self.board.is_in_check(temp_board_state, self.color):
            return True
        return False

    def get_moves(self):
        validated_moves = []
        unvalidated_moves = self.generate_moves()
        if unvalidated_moves is not None:
            validated_moves = self.validate_moves(unvalidated_moves)
        return validated_moves

    def validate_moves(self, moves: list):
        # reverse list to avoid iteration being interrupted by remove()
        for move in reversed(moves):
            if not self.causes_check(move[0][0], move[0][1]):
                continue
            moves.remove(move)
        return moves

