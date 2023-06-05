import pygame
import mapping
import time
class Board:
    def init(self):
        pass
    def create_board(self):
        color = (0,0,0)
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
        #Creating 64 squares and classifying what they should be called as well as giving them a coordinate (x,y)
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
        return x213, squares # x213 is a dictionary of dictionaries {{key:{value1,value2}}} # squares is a list of lists for coordinates [[0,0],[0,1],[0,2]]
        
        
        '''
        click1_not_clicked = True
        click2_not_clicked = True
        move_selections = [] 
        while True:
        
            background.blit(image, (150, 100))
            
            #{'a1': <rect(225, 175, 81, 81)>, 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and click1_not_clicked:
                    for i in x213:
                        if x213[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            print('MD: ' +i)
                            click1_not_clicked = False
                            move_selections.append(x213[i])
                if event.type == pygame.MOUSEBUTTONDOWN and click2_not_clicked:
                    for i in x213:
                        if x213[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            print('MU: '+i)
                            click2_not_clicked = False
                            move_selections.append(x213[i])
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
        
        
        '''
        
    def start_game(self):
        #initializing board
        x = 1000
        y = 1000
        background = pygame.display.set_mode((x, y))
        image = mapping.board
        background.blit(image, (150, 100))
        
        # Grabbing the pieces on which squares
        create_board = self.create_board()[0]
        pygame.display.update()
        not_gameover = True
        move_selections = [] 
        owners_turn = 0 
        color = 'W'
        #start the game
        while not_gameover:
            
            clicked = 0
            if owners_turn % 2 == 0:
                color = 'W'
            else:
                color = 'B'
            if color == 'W':
                click1_not_clicked = True
                click2_not_clicked = True
                while click1_not_clicked or click2_not_clicked:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            for i in create_board:
                                if create_board[i]["position"].collidepoint(pygame.mouse.get_pos()) and create_board[i]["owner"] == 'white' and clicked == 0:
                                    print('M1: ' +i)
                                    click1_not_clicked = False
                                    move_selections.append(color, i)
                                    clicked = clicked + 1
                        if event.type == pygame.MOUSEBUTTONUP:
                            for i in create_board:
                                if create_board[i]["position"].collidepoint(pygame.mouse.get_pos()) and create_board[i]["owner"] == 'white' and clicked == 1:
                                    print('M2: ' +i)
                                    click1_not_clicked = False
                                    move_selections.append(color, i)
                                    clicked = clicked + 1
                    owners_turn = owners_turn + 1

            elif color == 'B':
                click1_not_clicked = True
                click2_not_clicked = True
                while click1_not_clicked or click2_not_clicked:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            for i in create_board:
                                if create_board[i]["position"].collidepoint(pygame.mouse.get_pos()) and create_board[i]["owner"] == 'black' and clicked == 0:
                                    print('M1: ' +i)
                                    click1_not_clicked = False
                                    move_selections.append(color, i)
                                    clicked = clicked + 1
                        if event.type == pygame.MOUSEBUTTONUP:
                            for i in create_board:
                                if create_board[i]["position"].collidepoint(pygame.mouse.get_pos()) and create_board[i]["owner"] == 'black' and clicked == 1:
                                    decision = int(input("Is this the square you intended?\n[0] - Yes\n[1] - Non\nInput Here: "))
                                    if decision == 0:
                                        print('M2: ' +i)
                                        click2_not_clicked = False
                                        move_selections.append(i)
                                        clicked = clicked + 1
                                    elif decision == 1:
                                        click_not_clicked = True
                owners_turn = owners_turn + 1
            
            
            
            pygame.display.update()
        
        
        
        
if __name__ == "__main__":
    x = Board()
    x.start_game()
    
            
            
        
        
        
        
        


            