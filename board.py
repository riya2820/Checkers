import sys
import pygame
# from .constants import BLACK, WIDTH, HEIGHT, ROWS, RED, SQUARE_SIZE, COLS, WHITE

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS 
# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        # self.create_board()
    
    def draw_squares(self):
        # start by making 8x8 board so 64 squares 
        # alternate red and black squares 
        win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Checkers')
        win.fill(BLACK)
        # pygame.draw.pygame.draw.rect(surface, color, Rect, width=0)
        # pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
        # pygame.draw.rect(win, RED, pygame.Rect(WIDTH, HEIGHT))

        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

b = Board()
b.draw_squares()
