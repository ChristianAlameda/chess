import pygame
import map
class Board:
    def init(self):
        self.board = map.board
    def create_board(self):
        pygame.display(map.board)
        