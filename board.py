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
        x1 = 81.4
        x = 1000
        y = 1000
        background = pygame.display.set_mode((x, y))
        image = mapping.board
        background.blit(image, (150, 100))
        #pygame.draw.rect(surface, color, (x, y, w, h), outlineThickness)
        #pygame.Rect(left, top, width, height) -> Rect
        #pygame.draw.rect(background,color, pygame.Rect(225,175,x1,x1), outlineThickness, border_radius=1)# (225,175) | (650,650)
        
        
        a = ['a','b','c','d','e','f','g','h']
        b = ['1','2','3','4','5','6','7','8']
        x213 = {
            
        }
        for i in range(0,8):
            for j in range(0,8):
                position_name = a[i]+b[j]
                position = pygame.draw.rect(background,color, pygame.Rect(225+j*x1,175+i*x1,x1,x1), outlineThickness, border_radius=1)
                x213.update({position_name:position})
        #print(x213)
                
        pygame.display.update()
    
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            background.blit(image, (150, 100))
            
            #{'a1': <rect(225, 175, 81, 81)>, 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in x213.values():
                        if i.collidepoint(pygame.mouse.get_pos()):
                            print(i)
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in x213.values():
                        if i.collidepoint(pygame.mouse.get_pos()):
                            print(i)
            pygame.display.update()
    def partition(self):
        '''
        color = (255,0,0)
        outlineThickness = 1
        x1 = 81.4
        x = 1000
        y = 1000
        background = pygame.display.set_mode((x, y))
        image = mapping.board
        background.blit(image, (150, 100))
        #pygame.draw.rect(surface, color, (x, y, w, h), outlineThickness)
        #pygame.Rect(left, top, width, height) -> Rect
        #pygame.draw.rect(background,color, pygame.Rect(225,175,x1,x1), outlineThickness, border_radius=1)# (225,175) | (650,650)
        
        
        a = ['a','b','c','d','e','f','g','h']
        b = ['1','2','3','4','5','6','7','8']
        x213 = {
            
        }
        for i in range(0,8):
            for j in range(0,8):
                x324 = a[i]+b[j]
                position = pygame.draw.rect(background,color, pygame.Rect(225+j*x1,175+i*x1,x1,x1), outlineThickness, border_radius=1)
                x213.update({'x324':position})
                # assign each rectangle to a letter and number
                # example a1, b4, c8
                #c.append(a[i]+b[j])
                
        print(x213)
                
        pygame.display.update()
        
        '''
        
    def touch(self):
        print(pygame.mouse.get_pos())
def main():
    x = Board()
    x.create_board()
    x.partition()
if __name__ == "__main__":
    main()

            