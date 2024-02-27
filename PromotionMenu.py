import pygame
import pygame_widgets as widgets


class PromotionMenu:

    def __init__(self, width, height, board):
        self.width = width
        self.height = height
        self.board = board
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def draw_menu(self, promotion_menu_surface):

        pygame.draw.rect(promotion_menu_surface, "pink", self.rect)
        font = pygame.font.Font('freesansbold.ttf', 32)
        promotion_message = font.render('Choose Promotion:', True, 'Black')
        promotion_message.get_rect().center = (self.width // 2, self.height // 2)

        promotion_menu_surface.blit(promotion_message, promotion_message.get_rect())

    def handle_click(self, x, y):
        print("clicked on menu at {x,y}")
