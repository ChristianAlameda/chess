import pygame
import mapping
from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
from pieces import Piece, black_bishop, black_knight, black_queen, black_king, black_rook, black_pawn
from pieces import white_bishop, white_knight, white_queen, white_king, white_rook, white_pawn
import time
class Board:
    def __init__(self):
        self.field = {}
        self.make_board()
        
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
                color_square = blackOrWhite
                if blackOrWhite % 2 == 0:
                    color_square = 'W'
                else:
                    color_square = 'B'
                squares.append(position_xy)
                self.field.update({position_name:{"position":position, "color_square":color_square, "owner":None ,"piece":None,"picture":None, "position_xy":position_xy}})
                blackOrWhite = blackOrWhite + 1
        return self.field, squares # self.field is a dictionary of dictionaries {{key:{value1,value2}}} # squares is a list of lists for coordinates [[0,0],[0,1],[0,2]]

    def make_board(self):
        #initializing board
        x = 1000
        y = 1000
        background = pygame.display.set_mode((x, y))
        image = mapping.board
        background.blit(image, (150, 100))
        pygame.display.update()
    
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
    
    def black_or_white(self,owners_turn):
        color = ''
        if owners_turn % 2 == 0:
            color = 'W'
        else:
            color = 'B'
        return color
    
    def start_game(self):
        self.make_board()
        self.initialize_game()
        not_gameover = True
        #start the game
        while not_gameover:
            clicked = 0
            decider = self.black_or_white(clicked)
            if decider == "W":
                self.white1()
                self.create_colors_for_white()
                self.white2()
            elif decider == "B":
                self.black1()
                self.create_colors_for_black()
                self.white2()
            else:
                not_gameover = True
    
    def white1(self):
        click1_not_clicked = True
        while click1_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'black':
                            self.white1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'None':
                            self.white1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'white':
                            return self.field[i]["piece"].move(i, self.get_field()), i #black_queen.move(i) will return list of moves
                            #after this function make the squares that are in the list the piece can go to a different color
                            # have the list given to white2
                            
    def create_colors_for_white(self):
        for i in self.white1()[0]:
            pygame.draw.rect(self.field[i]['position'], [255, 0, 0], [50, 50, 90, 180], 1)
          
    def white2(self):
        click2_not_clicked = True
        while click2_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            if self.field[i] in self.white1()[0]: 
                                #replace the old square with none and transfer class, picture, and owner to new square
                                self.field[i]["picture"] = self.field[self.white1()[1]]["picture"] 
                                self.field[i]["piece"] = self.field[self.white1()[1]]["piece"]
                                self.field[i]["owner"] = self.field[self.white1()[1]]["owner"]
                                self.field[self.white1()[1]]["picture"] = None
                                self.field[self.white1()[1]]["piece"] = None
                                self.field[self.white1()[1]]["owner"] = None
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
                            return self.field[i]["piece"].move(i, self.get_field()), i #black_queen.move(i) will return list of moves
                            #after this function make the squares that are in the list the piece can go to a different color
                            # have the list given to white2
    
    def create_colors_for_black(self):
        for i in self.black1()[0]:
            pygame.draw.rect(self.field[i]['position'], [255, 0, 0], [50, 50, 90, 180], 1)
            
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
                            else:
                                self.white2()