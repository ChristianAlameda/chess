import pygame
import mapping
class Board:
    def init(self):
        self.board = mapping.board
    def create_board(self):
        # sets the height and width of the board with (x,y)
        x = 1000
        y = 1000
        background = pygame.display.set_mode((x, y))
        image = mapping.board

        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            background.blit(image, (150, 100))
            pygame.display.update()