import pygame
from util.Square import Square


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square_size = 10
        self.square_width = width // self.square_size
        self.square_height = height // self.square_size
        self.squares = self.create_squares()

    def create_squares(self):
        squares = []
        for y in range(8):
            for x in range(8):
                square = Square(x, y, self.square_width, self.square_height)

        return squares
    
