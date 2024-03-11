import pygame
from util.Button import Button


class PromotionMenu:

    def __init__(self, width, height, board):
        self.width = width
        self.height = height
        self.board = board
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.font = pygame.font.Font('freesansbold.ttf', 32)

        button_width = self.width // 2
        button_height = self.height // 10
        button_x = (self.width // 2) - (button_width // 2)
        button_height_slice = self.height // 5

        self.queen_btn = Button(button_x,
                                button_height_slice,
                                button_width,
                                button_height,
                                'gray',
                                'Queen',
                                'black')

        self.bishop_btn = Button(button_x,
                                 button_height_slice * 2,
                                 button_width,
                                 button_height,
                                 'gray',
                                 'Bishop',
                                 'black')

        self.knight_btn = Button(button_x,
                                 button_height_slice * 3,
                                 button_width,
                                 button_height,
                                 'gray',
                                 'Knight',
                                 'black')

        self.rook_btn = Button(button_x,
                               button_height_slice * 4,
                               button_width,
                               button_height,
                               'gray',
                               'Rook',
                               'black')

    def draw_menu(self, surface):
        pygame.draw.rect(surface, "pink", self.rect)

        promotion_message = self.font.render('Choose Promotion:', True, 'Black')
        promotion_message.get_rect().center = (self.width // 2, self.height // 2)

        surface.blit(promotion_message, promotion_message.get_rect())

        self.queen_btn.draw(surface)
        self.bishop_btn.draw(surface)
        self.knight_btn.draw(surface)
        self.rook_btn.draw(surface)

    def handle_click(self, pos):
        if self.queen_btn.is_hovered(pos):
            self.board.promote('queen')
        elif self.bishop_btn.is_hovered(pos):
            self.board.promote('bishop')
        elif self.knight_btn.is_hovered(pos):
            self.board.promote('knight')
        elif self.rook_btn.is_hovered(pos):
            self.board.promote('rook')
        else:
            return
