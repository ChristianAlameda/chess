import pygame
import mapping
from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
from mapping import blue_50, green_50, red_50
from pieces import Piece, black_bishop, black_knight, black_queen, black_king, black_rook, black_pawn
from pieces import white_bishop, white_knight, white_queen, white_king, white_rook, white_pawn
import time
class Board:
    def __init__(self):
        self.field = {}
        self.make_board()
        pygame.display.flip()
        self.white_moves = []
        self.whites_press = 0
        self.black_moves = []
        self.blacks_press = 0
    def get_field(self):
        return self.field

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
                top_left_corner = (225+j*x1,175+i*x1)
                color_square = blackOrWhite
                if blackOrWhite % 2 == 0:
                    color_square = 'W'
                else:
                    color_square = 'B'
                squares.append(position_xy)
                self.field.update({position_name:{"position":position, "color_square":color_square, "owner":None ,"piece":None,"picture":None, "position_xy":position_xy, "top_left_corner":top_left_corner}})
                blackOrWhite = blackOrWhite + 1
        return self.field, squares # self.field is a dictionary of dictionaries {{key:{value1,value2}}} # squares is a list of lists for coordinates [[0,0],[0,1],[0,2]]

    def make_board(self):
        #initializing window
        x = 1000
        y = 1000
        background = pygame.display.set_mode((x, y))
        #initialzing board image
        #via block trnasfering: blit() with window
        image = mapping.board
        background.blit(image, (150, 100))
        for i in self.field:
            if self.field[i]['picture'] == None:
                pass
            elif self.field[i]['picture'] == b_bishop or b_king or b_knight or b_pawn or b_queen or b_rook or w_bishop or w_king or w_knight or w_pawn or w_queen or w_rook:
                background.blit(self.field[i]['picture'],self.field[i]['top_left_corner'])
        #pygame.display.flip()
                  
    def black_or_white(self,owners_turn):
        color = ''
        if owners_turn % 2 == 0:
            color = 'W'
        else:
            color = 'B'
        return color
    
    def start_game(self):
        self.create_board()
        self.initialize_game()
        self.make_board()
        pygame.display.flip()
        #self.pieces_appear()
        not_gameover = True
        #start the game
        while not_gameover:
            clicked = 0
            decider = self.black_or_white(clicked)
            if decider == "W":
                self.white1()
                self.white2()
            elif decider == "B":
                self.black1()
                self.white2()
            else:
                not_gameover = True
    
    def white1(self):
        click1_not_clicked = True
        self.make_board()
        while click1_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'black':
                            self.white1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'None':
                            self.white1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'white':
                            p = white_pawn()
                            kn = white_knight()
                            b = white_bishop()
                            r = white_rook()
                            q = white_queen()
                            k = white_king()
                            print(self.field[i]['piece'])#<pieces.white_pawn object at 0x0000020D82E8E620>
                            #initializing window
                            x = 1000
                            y = 1000
                            background = pygame.display.set_mode((x, y))
                            #initialzing board image
                            #via block trnasfering: blit() with window
                            image = mapping.board
                            background.blit(image, (150, 100))
                            
                            #print(str(self.field[i]['piece']()))#TypeError: 'white_pawn' object is not callable
                            
                            #if isinstance(self.field[i]['piece'], white_pawn)
                            if isinstance(self.field[i]['piece'], white_pawn):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    background.blit(green_50, self.field[j]['top_left_corner'])
                                    
                                    
                                    self.white_moves.append(j)
                                    click1_not_clicked = False
                                
                                    pygame.display.update(self.field[j]['position'])
                                
                            elif isinstance(self.field[i]['piece'], white_knight):
                                for j in self.field[i]['piece'].move(i,self.get_field()):
                                    print(j)
                                    background.blit(self.field[j]['picture'], self.field[j]['top_left_corner'])
                                    self.white_moves.append(i)
                            
                            elif isinstance(self.field[i]['piece'], white_bishop):
                                for j in self.field[i]['piece'].move(i,self.get_field()):
                                    print(j)
                                    background.blit(self.field[j]['picture'], self.field[j]['top_left_corner'])
                                    self.white_moves.append(i)
                                    
                            elif isinstance(self.field[i]['piece'], white_rook):
                                for j in self.field[i]['piece'].move(i,self.get_field()):
                                    print(j)
                                    background.blit(self.field[j]['picture'], self.field[j]['top_left_corner'])
                                    self.white_moves.append(i)
                            
                            elif isinstance(self.field[i]['piece'], white_queen):
                                for j in self.field[i]['piece'].move(i,self.get_field()):
                                    print(j)
                                    background.blit(self.field[j]['picture'], self.field[j]['top_left_corner'])
                                    self.white_moves.append(i)
                                    
                            elif isinstance(self.field[i]['piece'], white_king):
                                for j in self.field[i]['piece'].move(i,self.get_field()):
                                    print(j)
                                    background.blit(self.field[j]['picture'], self.field[j]['top_left_corner'])
                                    self.white_moves.append(i)
                            self.white_press = i
                                    
    def clear_white_and_black_moves(self):
        self.white_moves = []
        self.black_moves = []
    
    def clear_whitepress_and_blackpress(self):
        self.white_press = 0
        self.black_press = 0
                                    
    def white2(self):
        click2_not_clicked = True
        self.make_board()
        while click2_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            if i in self.white_moves[0]: 
                                #replace the old square with none and transfer class, picture, and owner to new square
                                self.field[i]["picture"] = self.field[self.white1()[1]]["picture"] 
                                self.field[i]["piece"] = self.field[self.white1()[1]]["piece"]
                                self.field[i]["owner"] = self.field[self.white1()[1]]["owner"]
                                self.field[self.white1()[1]]["picture"] = None
                                self.field[self.white1()[1]]["piece"] = None
                                self.field[self.white1()[1]]["owner"] = None
                                self.make_board()
                                pygame.display.flip()
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                            else:
                                self.white2()
                                
    def black1(self):
        click1_not_clicked = True
        while click1_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'white':
                            self.white1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'None':
                            self.white1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'black':
                            if self.field[i]['piece']() == black_pawn():
                                print(black_pawn().move(i,self.get_field()))
                                for j in black_pawn().move(i,self.get_field()):
                                    print(j)
                                    
                                    self.white_moves.append(i)
                            elif self.field[i]['piece']() == black_knight():
                                for j in black_knight().move(i,self.get_field()):
                                    print(j)
                                    
                                    self.white_moves.append(i)
                            elif self.field[i]['piece']() == black_bishop():
                                for j in black_bishop().move(i,self.get_field()):
                                    print(j)
                                    
                                    self.white_moves.append(i)
                            elif self.field[i]['piece']() == black_rook():
                                for j in black_rook().move(i,self.get_field()):
                                    print(j)
                                    
                                    self.white_moves.append(i)
                            elif self.field[i]['piece']() == black_queen():
                                for j in black_queen().move(i,self.get_field()):
                                    print(j)
                                    
                                    self.white_moves.append(i)
                            elif self.field[i]['piece']() == black_king():
                                for j in black_king().move(i,self.get_field()):
                                    print(j)
                                    
                                    self.white_moves.append(j)
                            self.white_press = i
    def black2(self):
        click2_not_clicked = True
        while click2_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            if self.field[i] in self.black1()[0]: 
                                #replace the old square with none and transfer class, picture, and owner to new square
                                self.field[i]["picture"] = self.field[self.white1()[1]]["picture"] 
                                self.field[i]["piece"] = self.field[self.white1()[1]]["piece"]
                                self.field[i]["owner"] = self.field[self.white1()[1]]["owner"]
                                self.field[self.white1()[1]]["picture"] = None
                                self.field[self.white1()[1]]["piece"] = None
                                self.field[self.white1()[1]]["owner"] = None
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                            else:
                                self.white2()
    def initialize_game(self):
        #[BLACK]
        #Setting up pieces
        self.field['A8']['piece']   = black_rook()
        self.field['B8']['piece']   = black_knight()
        self.field['C8']['piece']   = black_bishop()
        self.field['D8']['piece']   = black_queen()
        self.field['E8']['piece']   = black_king()
        self.field['F8']['piece']   = black_bishop()
        self.field['G8']['piece']   = black_knight()
        self.field['H8']['piece']   = black_rook()
        self.field['A7']['piece']   = black_pawn()
        self.field['B7']['piece']   = black_pawn()
        self.field['C7']['piece']   = black_pawn()
        self.field['D7']['piece']   = black_pawn()
        self.field['E7']['piece']   = black_pawn()
        self.field['F7']['piece']   = black_pawn()
        self.field['G7']['piece']   = black_pawn()
        self.field['H7']['piece']   = black_pawn()
        #setting pictures to correspond with the pieces squares
        self.field['A8']['picture'] = b_rook
        self.field['B8']['picture'] = b_knight
        self.field['C8']['picture'] = b_bishop
        self.field['D8']['picture'] = b_queen
        self.field['E8']['picture'] = b_king
        self.field['F8']['picture'] = b_bishop
        self.field['G8']['picture'] = b_knight
        self.field['H8']['picture'] = b_rook
        self.field['A7']['picture'] = b_pawn
        self.field['B7']['picture'] = b_pawn
        self.field['C7']['picture'] = b_pawn
        self.field['D7']['picture'] = b_pawn
        self.field['E7']['picture'] = b_pawn
        self.field['F7']['picture'] = b_pawn
        self.field['G7']['picture'] = b_pawn
        self.field['H7']['picture'] = b_pawn
        #setting pieces up so they know which owner they have
        self.field['A8']['owner']   = 'black'
        self.field['B8']['owner']   = 'black'
        self.field['C8']['owner']   = 'black'
        self.field['D8']['owner']   = 'black'
        self.field['E8']['owner']   = 'black'
        self.field['F8']['owner']   = 'black'
        self.field['G8']['owner']   = 'black'
        self.field['H8']['owner']   = 'black'
        self.field['A7']['owner']   = 'black'
        self.field['B7']['owner']   = 'black'
        self.field['C7']['owner']   = 'black'
        self.field['D7']['owner']   = 'black'
        self.field['E7']['owner']   = 'black'
        self.field['F7']['owner']   = 'black'
        self.field['G7']['owner']   = 'black'
        self.field['H7']['owner']   = 'black'
        #[WHITE]
        #Setting up pieces
        self.field['A1']['piece']   = white_rook()
        self.field['B1']['piece']   = white_knight()
        self.field['C1']['piece']   = white_bishop()
        self.field['D1']['piece']   = white_queen()
        self.field['E1']['piece']   = white_king()
        self.field['F1']['piece']   = white_bishop()
        self.field['G1']['piece']   = white_knight()
        self.field['H1']['piece']   = white_rook()
        self.field['A2']['piece']   = white_pawn()
        self.field['B2']['piece']   = white_pawn()
        self.field['C2']['piece']   = white_pawn()
        self.field['D2']['piece']   = white_pawn()
        self.field['E2']['piece']   = white_pawn()
        self.field['F2']['piece']   = white_pawn()
        self.field['G2']['piece']   = white_pawn()
        self.field['H2']['piece']   = white_pawn()
        #setting pictures to correspond with the pieces squares
        self.field['A1']['picture'] = w_rook
        self.field['B1']['picture'] = w_knight
        self.field['C1']['picture'] = w_bishop
        self.field['D1']['picture'] = w_queen
        self.field['E1']['picture'] = w_king
        self.field['F1']['picture'] = w_bishop
        self.field['G1']['picture'] = w_knight
        self.field['H1']['picture'] = w_rook
        self.field['A2']['picture'] = w_pawn
        self.field['B2']['picture'] = w_pawn
        self.field['C2']['picture'] = w_pawn
        self.field['D2']['picture'] = w_pawn
        self.field['E2']['picture'] = w_pawn
        self.field['F2']['picture'] = w_pawn
        self.field['G2']['picture'] = w_pawn
        self.field['H2']['picture'] = w_pawn
        #setting pieces up so they know which owner they have
        self.field['A1']['owner']   = 'white'
        self.field['B1']['owner']   = 'white'
        self.field['C1']['owner']   = 'white'
        self.field['D1']['owner']   = 'white'
        self.field['E1']['owner']   = 'white'
        self.field['F1']['owner']   = 'white'
        self.field['G1']['owner']   = 'white'
        self.field['H1']['owner']   = 'white'
        self.field['A2']['owner']   = 'white'
        self.field['B2']['owner']   = 'white'
        self.field['C2']['owner']   = 'white'
        self.field['D2']['owner']   = 'white'
        self.field['E2']['owner']   = 'white'
        self.field['F2']['owner']   = 'white'
        self.field['G2']['owner']   = 'white'
        self.field['H2']['owner']   = 'white'