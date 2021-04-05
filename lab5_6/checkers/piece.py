import pygame
from checkers.constants import RED, GREEN, GREY,SQUARE_SIZE

class Piece:
    def __init__(self, row, col, color):
        self.row=row
        self.col=col
        self.color=color

        self.x=0
        self.y=0
        self.calculate_position()

    def calculate_position(self):
        self.x=SQUARE_SIZE*self.col+SQUARE_SIZE//2
        self.y=SQUARE_SIZE*self.row+SQUARE_SIZE//2

    def draw(self, window):
        radius=SQUARE_SIZE//2-10
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row=row
        self.col=col
        self.calculate_position()

    def __repr__(self):
        return str(self.color)