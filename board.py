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
        color = (255,0,0)
        outlineThickness = 1
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            background.blit(image, (150, 100))
            #we will start the actual board at 225,
            #pygame.draw.rect(surf, color, (x, y, w, h), outlineThickness)
            pygame.draw.rect(background,color, pygame.Rect(225,175,650,650), outlineThickness, border_radius=1)# (225,175) | (650,650)
            self.touch()
            pygame.display.update()
    def touch(self):
        print(pygame.mouse.get_pos())
            

            