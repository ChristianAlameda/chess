import pygame
import mapping
class Board:
    def init(self):
        self.board = mapping.board
    def create_board(self):
        color = (255,0,0)
        outlineThickness = 1
        x1 = 81.4
        x = 1000
        y = 1000
        background = pygame.display.set_mode((x, y))
        image = mapping.board
        background.blit(image, (150, 100))
        a = ['A','B','C','D','E','F','G','H']
        b = ['8','7','6','5','4','3','2','1']
        x213 = {}
        squares = []
        #pygame.draw.rect(surface, color, (x, y, w, h), outlineThickness)
        #pygame.Rect(left, top, width, height) -> Rect
        #pygame.draw.rect(background,color, pygame.Rect(225,175,x1,x1), outlineThickness, border_radius=1)# (225,175) | (650,650)
        
        
        
        blackOrWhite = 0
        for i in range(0,8):
            for j in range(0,8):
                
                position_name = a[j]+b[i]
                position = pygame.draw.rect(background,color, pygame.Rect(225+j*x1,175+i*x1,x1,x1), outlineThickness, border_radius=1)
                position_xy = [j,i] # 0,0 0,1 0,2 0,3 0,4 0,5
                color_square = blackOrWhite
                if blackOrWhite % 2 == 0:
                    color_square = 'W'
                else:
                    color_square = 'B'
                
                
                squares.append(position_xy)
                
                x213.update({position_name:{"position":position, "color_square":color_square, "owner":None ,"piece":None,"picture":None, "position_xy":position_xy}})
                blackOrWhite = blackOrWhite + 1
        #print(x213)
        return x213, squares
        '''
        pygame.display.update()
        
        while True:
            
            background.blit(image, (150, 100))
            
            #{'a1': <rect(225, 175, 81, 81)>, 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in x213:
                        if x213[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            print('MD: ' +i)
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in x213:
                        if x213[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            print('MU: '+i)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
        
        
        '''
        
        
            
            
        
        
        
        
        


            