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
            color = (255,0,0)
            outlineThickness = 1
            x1 = 81.4
            #pygame.draw.rect(surface, color, (x, y, w, h), outlineThickness)
            #pygame.Rect(left, top, width, height) -> Rect
            #pygame.draw.rect(background,color, pygame.Rect(225,175,x1,x1), outlineThickness, border_radius=1)# (225,175) | (650,650)
            a = []
            for i in range(0,8):
                for j in range(0,8):
                    pygame.draw.rect(background,color, pygame.Rect(225+j*x1,175+i*x1,x1,x1), outlineThickness, border_radius=1)# (225,175) | (650,650)
                    # assign each rectangle to a letter and number
                    # example a1, b4, c8
            pygame.display.update()
            print(a)
    def touch(self):
        print(pygame.mouse.get_pos())
def main():
    x = Board()
    x.create_board()
if __name__ == "__main__":
    main()

            