import pygame
import mapping
from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
from pieces import Piece, black_bishop, black_knight, black_queen, black_king, black_rook, black_pawn
from pieces import white_bishop, white_knight, white_queen, white_king, white_rook, white_pawn
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
        #[BLACK]
        #Setting up pieces
        create_board['A8']['piece']   = black_rook()
        create_board['B8']['piece']   = black_knight()
        create_board['C8']['piece']   = black_bishop()
        create_board['D8']['piece']   = black_queen()
        create_board['E8']['piece']   = black_king()
        create_board['F8']['piece']   = black_bishop()
        create_board['G8']['piece']   = black_knight()
        create_board['H8']['piece']   = black_rook()
        create_board['A7']['piece']   = black_pawn()
        create_board['B7']['piece']   = black_pawn()
        create_board['C7']['piece']   = black_pawn()
        create_board['D7']['piece']   = black_pawn()
        create_board['E7']['piece']   = black_pawn()
        create_board['F7']['piece']   = black_pawn()
        create_board['G7']['piece']   = black_pawn()
        create_board['H7']['piece']   = black_pawn()
        #setting pictures to correspond with the pieces squares
        create_board['A8']['picture'] = b_rook
        create_board['B8']['picture'] = b_knight
        create_board['C8']['picture'] = b_bishop
        create_board['D8']['picture'] = b_queen
        create_board['E8']['picture'] = b_king
        create_board['F8']['picture'] = b_bishop
        create_board['G8']['picture'] = b_knight
        create_board['H8']['picture'] = b_rook
        create_board['A7']['picture'] = b_pawn
        create_board['B7']['picture'] = b_pawn
        create_board['C7']['picture'] = b_pawn
        create_board['D7']['picture'] = b_pawn
        create_board['E7']['picture'] = b_pawn
        create_board['F7']['picture'] = b_pawn
        create_board['G7']['picture'] = b_pawn
        create_board['H7']['picture'] = b_pawn
        #setting pieces up so they know which owner they have
        create_board['A8']['owner']   = 'black'
        create_board['B8']['owner']   = 'black'
        create_board['C8']['owner']   = 'black'
        create_board['D8']['owner']   = 'black'
        create_board['E8']['owner']   = 'black'
        create_board['F8']['owner']   = 'black'
        create_board['G8']['owner']   = 'black'
        create_board['H8']['owner']   = 'black'
        create_board['A7']['owner']   = 'black'
        create_board['B7']['owner']   = 'black'
        create_board['C7']['owner']   = 'black'
        create_board['D7']['owner']   = 'black'
        create_board['E7']['owner']   = 'black'
        create_board['F7']['owner']   = 'black'
        create_board['G7']['owner']   = 'black'
        create_board['H7']['owner']   = 'black'
        #[WHITE]
        #Setting up pieces
        create_board['A1']['piece']   = white_rook()
        create_board['B1']['piece']   = white_knight()
        create_board['C1']['piece']   = white_bishop()
        create_board['D1']['piece']   = white_queen()
        create_board['E1']['piece']   = white_king()
        create_board['F1']['piece']   = white_bishop()
        create_board['G1']['piece']   = white_knight()
        create_board['H1']['piece']   = white_rook()
        create_board['A2']['piece']   = white_pawn()
        create_board['B2']['piece']   = white_pawn()
        create_board['C2']['piece']   = white_pawn()
        create_board['D2']['piece']   = white_pawn()
        create_board['E2']['piece']   = white_pawn()
        create_board['F2']['piece']   = white_pawn()
        create_board['G2']['piece']   = white_pawn()
        create_board['H2']['piece']   = white_pawn()
        #setting pictures to correspond with the pieces squares
        create_board['A1']['picture'] = w_rook
        create_board['B1']['picture'] = w_knight
        create_board['C1']['picture'] = w_bishop
        create_board['D1']['picture'] = w_queen
        create_board['E1']['picture'] = w_king
        create_board['F1']['picture'] = w_bishop
        create_board['G1']['picture'] = w_knight
        create_board['H1']['picture'] = w_rook
        create_board['A2']['picture'] = w_pawn
        create_board['B2']['picture'] = w_pawn
        create_board['C2']['picture'] = w_pawn
        create_board['D2']['picture'] = w_pawn
        create_board['E2']['picture'] = w_pawn
        create_board['F2']['picture'] = w_pawn
        create_board['G2']['picture'] = w_pawn
        create_board['H2']['picture'] = w_pawn
        #setting pieces up so they know which owner they have
        create_board['A1']['owner']   = 'white'
        create_board['B1']['owner']   = 'white'
        create_board['C1']['owner']   = 'white'
        create_board['D1']['owner']   = 'white'
        create_board['E1']['owner']   = 'white'
        create_board['F1']['owner']   = 'white'
        create_board['G1']['owner']   = 'white'
        create_board['H1']['owner']   = 'white'
        create_board['A2']['owner']   = 'white'
        create_board['B2']['owner']   = 'white'
        create_board['C2']['owner']   = 'white'
        create_board['D2']['owner']   = 'white'
        create_board['E2']['owner']   = 'white'
        create_board['F2']['owner']   = 'white'
        create_board['G2']['owner']   = 'white'
        create_board['H2']['owner']   = 'white'
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
    
            
            
        
        
        
        
        


            