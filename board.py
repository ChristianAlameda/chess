import pygame
import mapping
from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
from mapping import blue_50, green_50, red_50
from pieces import Piece, black_bishop, black_knight, black_queen, black_king, black_rook, black_pawn
from pieces import white_bishop, white_knight, white_queen, white_king, white_rook, white_pawn
import time
import sys

class Board:
    def __init__(self):
        self.field = {}
        #self.make_board()
        #pygame.display.flip()
        #initializing window
        x = 500 
        y = 500 
        self.background = pygame.display.set_mode((x, y))
        
        self.image = mapping.board
        
        self.picture_of_board()
        self.white_moves = []
        self.white_press = ''
        self.black_moves = []
        self.black_press = ''
        
        self.kingside_castle = ''
        self.queenside_castle = ''
        
    def get_field(self):
        return self.field

    def create_board(self):
        color = (0,0,0)
        outlineThickness = 1
        x1 = 50 #81.4
        
        x_offset = 55
        y_offset = 55
        self.picture_of_board()
        a = ['A','B','C','D','E','F','G','H']
        b = ['8','7','6','5','4','3','2','1']
        squares = []
        #Creating 64 squares and classifying what they should be called as well as giving them a coordinate (x,y)
        #pygame.draw.rect(surface, color, (x, y, w, h), outlineThickness)
        #pygame.Rect(left, top, width, height) -> Rect
        #pygame.draw.rect(background,color, pygame.Rect(77,77,x1,x1), outlineThickness, border_radius=1)# (77,77)
        blackOrWhite = 0
        for i in range(0,8):
            for j in range(0,8):
                position_name = a[j]+b[i]
                position = pygame.draw.rect(self.background,color, pygame.Rect(x_offset+j*x1,y_offset+i*x1,x1,x1), outlineThickness, border_radius=1)
                position_xy = [j,i] # 0,0 0,1 0,2 0,3 0,4 0,5
                top_left_corner = (x_offset+j*x1,y_offset+i*x1)
                
                middle = (x_offset+j*x1 + x1/2 - 10,y_offset+i*x1 + x1/2 - 10)
                
                color_square = blackOrWhite
                if blackOrWhite % 2 == 0:
                    color_square = 'W'
                else:
                    color_square = 'B'
                squares.append(position_xy)
                self.field.update({position_name:{"position":position, 
                                                  "color_square":color_square, 
                                                  "owner":None ,"piece":None,
                                                  "picture":None, 
                                                  "position_xy":position_xy, 
                                                  "top_left_corner":top_left_corner, #top_left_corner
                                                  "middle":middle, 
                                                  "move_counter":0}
                                   })
                blackOrWhite = blackOrWhite + 1
        return self.field, squares # self.field is a dictionary of dictionaries {{key:{value1,value2}}} # squares is a list of lists for coordinates [[0,0],[0,1],[0,2]]

    def picture_of_board(self):
        self.background.blit(self.image, (0, 0))#(150,100)
    
    def make_board(self):
        #via block trnasfering: blit() with window
        
        self.picture_of_board()
        #self.background.blit(self.picture_of_board,self.field[i]['top_left_corner'])
        for i in self.field:
            if self.field[i]['picture'] == None:
                pass
            elif self.field[i]['picture'] == b_bishop or b_king or b_knight or b_pawn or b_queen or b_rook or w_bishop or w_king or w_knight or w_pawn or w_queen or w_rook:
                self.background.blit(self.field[i]['picture'],self.field[i]['top_left_corner'])
                  
    def black_or_white(self,owners_turn):
        color = ''
        if owners_turn % 2 == 0:
            color = 'W'
        else:
            color = 'B'
        return color
    
    def check_quit(self):
        # check if they press the x to leave the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return False
        return True

    def check_win(self):
        for i in self.field:
            if isinstance(self.field[i]['piece'],black_king):
                #end the game white has won
                return False
                
            elif isinstance(self.field[i]['piece'],white_king):
                #end the game black has won
                return False
            
            else: return True
            
    def start_game(self):
        self.create_board()
        self.initialize_game()
        self.make_board()
        pygame.display.update()
        #self.pieces_appear()
        not_gameover = True
        clicked = 0
        #start the game
        while not_gameover:
            not_gameover = self.check_win()
            decider = self.black_or_white(clicked)
            if decider == "W":
                self.white1()
                self.white2()
                clicked = clicked + 1
            elif decider == "B":
                self.black1()
                self.black2()
                clicked = clicked + 1
           
        #check if player has pressed x to exit
        pygame.quit()
                        
    def white1_helper(self,i):
        print(self.field[i]['piece'].move(i,self.get_field()))
        for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
            self.background.blit(green_50, self.field[j]['middle'])
            if self.field[j]['owner'] == 'black':
                self.background.blit(red_50, self.field[j]['middle'])
            self.white_moves.append(j)
            pygame.display.update(self.field[j]['position'])
    
    def white1_king_helper(self,i):
        for j in self.field[i]['piece'].move(i,self.get_field())[0]:#[a8,b5,...]
            self.background.blit(green_50, self.field[j]['middle'])
            if self.field[j]['owner'] == 'black':
                self.background.blit(red_50, self.field[j]['middle'])
            self.white_moves.append(j)
            pygame.display.update(self.field[j]['position'])
        
        king_side = self.field[i]['piece'].move(i,self.get_field())[1]
        if not king_side == "":
            self.background.blit(green_50, self.field[king_side]['middle'])
            if self.field[king_side]['owner'] == 'black':
                self.background.blit(red_50, self.field[king_side]['middle'])
            # self.white_moves.append(king_side)
            pygame.display.update(self.field[king_side]['position'])
        
        queen_side = self.field[i]['piece'].move(i,self.get_field())[2]
        if not queen_side == "":
            self.background.blit(green_50, self.field[queen_side]['middle'])
            if self.field[queen_side]['owner'] == 'black':
                self.background.blit(red_50, self.field[queen_side]['middle'])
            # self.white_moves.append(queen_side)
            pygame.display.update(self.field[queen_side]['position'])
        
    def white1(self):
        
        click1_not_clicked = True
        self.make_board()
        self.clear_white_and_black_moves()
        self.clear_whitepress_and_blackpress()
        print("It's white's first press")
        while click1_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:# c7 
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'black':
                            print('oops you clicked on a black piece')
                            self.white1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'None':
                            print('oops you clicked on a None piece')
                            self.white1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'white':
                            print(self.field[i]['piece'])#<pieces.white_pawn object at 0x0000020D82E8E620>
                            #via block trnasfering: blit() with window
                            self.picture_of_board()
                            self.white_press = i
                            #if isinstance(self.field[i]['piece'], white_pawn)
                            if isinstance(self.field[i]['piece'], white_pawn):
                                self.white1_helper(i)
                                
                            elif isinstance(self.field[i]['piece'], white_knight):
                                self.white1_helper(i)

                            elif isinstance(self.field[i]['piece'], white_bishop):
                                self.white1_helper(i)
                                    
                            elif isinstance(self.field[i]['piece'], white_rook):
                                self.white1_helper(i)
                            
                            elif isinstance(self.field[i]['piece'], white_queen):
                                self.white1_helper(i)
                                    
                            elif isinstance(self.field[i]['piece'], white_king):
                                self.white1_king_helper(i)
                                
                                kingSide = self.field[i]['piece'].move(i,self.get_field())[1]
                                if kingSide == '':
                                    pass
                                else: 
                                    self.background.blit(green_50, self.field[kingSide]['middle'])
                                    self.kingside_castle = kingSide #appending white king castling kingside
                                    pygame.display.update(self.field[kingSide]['position'])
                                
                                queenSide = self.field[i]['piece'].move(i,self.get_field())[2]
                                if queenSide == '':
                                    pass
                                else:
                                    self.background.blit(green_50, self.field[queenSide]['middle'])
                                    self.queenside_castle = queenSide #appending white king castling kingside
                                    pygame.display.update(self.field[queenSide]['position'])
                                
                            elif self.field[i]['piece'].move(i,self.get_field()) == []:
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                self.white1()
                                
                            click1_not_clicked = False
                    #here check if user pressed exit
                    
    def boolean_checker(self):
        user_input = input("Are you sure you wanted to pick that piece?\nEnter 't','true','yes' - True\nAnything else for False: ").lower()
        boolean_yes = ['t', 'true', 'yes']
        if user_input in boolean_yes:
            return True
        else:
            return False                                
        
    def clear_white_and_black_moves(self):
        self.white_moves = []
        self.black_moves = []
        self.kingside_castle = ''
        self.queenside_castle = ''
    
    def clear_whitepress_and_blackpress(self):
        self.white_press = ''
        self.black_press = ''
    
    def white_movement(self,i):
        self.field[i]["picture"] = self.field[self.white_press]["picture"] 
        self.field[i]["piece"] = self.field[self.white_press]["piece"]
        self.field[i]["owner"] = self.field[self.white_press]["owner"]
        self.field[self.white_press]["picture"] = None
        self.field[self.white_press]["piece"] = None
        self.field[self.white_press]["owner"] = None
              
    def white2(self):
        click2_not_clicked = True
        self.make_board()
        print("It is white's second press")
        print(self.white_moves)
        print(self.kingside_castle)
        print(self.queenside_castle)
        while click2_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            print('i: ',len(i), 'self.kingside_castle: ', len(self.kingside_castle))
                            if self.field[i]["owner"] == 'white':
                                print("\nyou have switched to a white piece you wanted to press on")
                                print('you will now be lead to a place where you have not clicked')
                                print('onto your first piece yet, and will be given another choice selection')
                                print('to choose from || happy pickings')
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                self.white1()
                            
                            
                                 
                            elif i == self.kingside_castle:
                                #for the king
                                
                                self.white_movement(i)
                                
                                #for the rook
                                self.field['F1']["picture"] = self.field['H1']["picture"] 
                                self.field['F1']["piece"]   = self.field['H1']["piece"]
                                self.field['F1']["owner"]   = self.field['H1']["owner"]
                                self.field['H1']["picture"] = None
                                self.field['H1']["piece"]   = None
                                self.field['H1']["owner"]   = None
                                
                                #for move_counter
                                self.field[self.white_press]['move_counter'] = self.field[self.white_press]['move_counter'] + 1
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                click2_not_clicked = False
                                
                                
                            elif i == self.queenside_castle:
                                self.white_movement(i)
                                
                                #for the rook
                                self.field['D1']["picture"] = self.field['A1']["picture"] 
                                self.field['D1']["piece"]   = self.field['A1']["piece"]
                                self.field['D1']["owner"]   = self.field['A1']["owner"]
                                self.field['A1']["picture"] = None
                                self.field['A1']["piece"]   = None
                                self.field['A1']["owner"]   = None
                                
                                #for move_counter
                                self.field[self.white_press]['move_counter'] = self.field[self.white_press]['move_counter'] + 1
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                click2_not_clicked = False
                                
                            elif (i in self.white_moves): 
                                #replace the old square with none and transfer class, picture, and owner to new square
                                
                                self.white_movement(i)
                                #for move_counter
                                self.field[self.white_press]['move_counter'] = self.field[self.white_press]['move_counter'] + 1
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                click2_not_clicked = False
                                
                            else:
                                print('Oops you touched a square without a green dot. Please try again')
                                self.white2()
                    #here check if user pressed exit
                    
    def black1_helper(self,i):
        print(self.field[i]['piece'].move(i,self.get_field()))
        for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
            self.background.blit(green_50, self.field[j]['middle'])
            if self.field[j]['owner'] == 'white':
                self.background.blit(red_50, self.field[j]['middle'])
            self.black_moves.append(j)
            pygame.display.update(self.field[j]['position'])

    def black1_king_helper(self,i):
        for j in self.field[i]['piece'].move(i,self.get_field())[0]:#[a8,b5,...]
            self.background.blit(green_50, self.field[j]['middle'])
            if self.field[j]['owner'] == 'white':
                self.background.blit(red_50, self.field[j]['middle'])
            self.white_moves.append(j)
            pygame.display.update(self.field[j]['position'])
        
        king_side = self.field[i]['piece'].move(i,self.get_field())[1]
        if not king_side == "":
            self.background.blit(green_50, self.field[king_side]['middle'])
            if self.field[king_side]['owner'] == 'white':
                self.background.blit(red_50, self.field[king_side]['middle'])
            # self.white_moves.append(king_side)
            pygame.display.update(self.field[king_side]['position'])
        
        queen_side = self.field[i]['piece'].move(i,self.get_field())[2]
        if not queen_side == "":
            self.background.blit(green_50, self.field[queen_side]['middle'])
            if self.field[queen_side]['owner'] == 'white':
                self.background.blit(red_50, self.field[queen_side]['middle'])
            # self.white_moves.append(queen_side)
            pygame.display.update(self.field[queen_side]['position'])
        
    def black1(self):
        click1_not_clicked = True
        self.make_board()
        self.clear_white_and_black_moves()
        print("It is black's first press")
        while click1_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'white':
                            print('oops you clicked on a white piece')
                            self.black1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'None':
                            print('oops you clicked on a None piece')
                            self.black1()
                        elif self.field[i]["position"].collidepoint(pygame.mouse.get_pos()) and self.field[i]["owner"] == 'black':
                            self.black_press = i
                            print(self.field[i]['piece'])#<pieces.black_pawn object at 0x0000020D82E8E620>
                            #via block trnasfering: blit() with window
                            self.picture_of_board()

                            #if isinstance(self.field[i]['piece'], black_pawn)
                            if isinstance(self.field[i]['piece'], black_pawn):
                                self.black1_helper(i)
                                    
                            elif isinstance(self.field[i]['piece'], black_knight):
                                self.black1_helper(i)
                                    
                            elif isinstance(self.field[i]['piece'], black_bishop):
                                self.black1_helper(i)
                                    
                            elif isinstance(self.field[i]['piece'], black_rook):
                                self.black1_helper(i)
                                    
                            elif isinstance(self.field[i]['piece'], black_queen):
                                self.black1_helper(i)
                                    
                            elif isinstance(self.field[i]['piece'], black_king):
                                self.black1_king_helper(i)
                                
                                # checking castling kingside e8 to g8
                                kingSide = self.field[i]['piece'].move(i,self.get_field())[1]
                                if kingSide == '':
                                    pass
                                else: 
                                    self.background.blit(green_50, self.field[kingSide]['middle'])
                                    self.kingside_castle = kingSide #appending white king castling kingside
                                    pygame.display.update(self.field[kingSide]['position'])
                                
                                # checking castling queenside e8 to c8
                                queenSide = self.field[i]['piece'].move(i,self.get_field())[2]
                                if queenSide == '':
                                    pass
                                else:
                                    self.background.blit(green_50, self.field[queenSide]['middle'])
                                    self.queenside_castle = queenSide #appending white king castling kingside
                                    pygame.display.update(self.field[queenSide]['position'])
                                    
                            elif self.field[i]['piece'].move(i,self.get_field()) == []:
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                self.black1()
                            click1_not_clicked = False
                    #here check if user pressed exit

    def black_movement(self,i):
        self.field[i]["picture"] = self.field[self.black_press]["picture"] 
        self.field[i]["piece"] = self.field[self.black_press]["piece"]
        self.field[i]["owner"] = self.field[self.black_press]["owner"]
        self.field[self.black_press]["picture"] = None
        self.field[self.black_press]["piece"] = None
        self.field[self.black_press]["owner"] = None
                                    
    def black2(self):
        click2_not_clicked = True
        print("It's black's second press")
        while click2_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            if self.field[i]["owner"] == 'black':
                                print('you have switched to a black piece you wanted to press on')
                                print('you will now be lead to a place where you have not clicked')
                                print('onto your first piece yet, and will be given another choice selection')
                                print('to choose from || happy pickings')
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                self.black1()
                             
                            
                                   
                            elif i == self.kingside_castle:
                                #for the king
                                self.black_movement(i)
                                
                                #for the rook
                                self.field['F8']["picture"] = self.field['H8']["picture"] 
                                self.field['F8']["piece"] = self.field['H8']["piece"]
                                self.field['F8']["owner"] = self.field['H8']["owner"]
                                self.field['H8']["picture"] = None
                                self.field['H8']["piece"] = None
                                self.field['H8']["owner"] = None
                                
                                #for move_counter
                                self.field[self.black_press]['move_counter'] = self.field[self.black_press]['move_counter'] + 1
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                click2_not_clicked = False
                            
                            elif i == self.queenside_castle:
                                #for the king
                                self.black_movement(i)
                                
                                #for the rook
                                self.field['D8']["picture"] = self.field['A8']["picture"] 
                                self.field['D8']["piece"] = self.field['A8']["piece"]
                                self.field['D8']["owner"] = self.field['A8']["owner"]
                                self.field['A8']["picture"] = None
                                self.field['A8']["piece"] = None
                                self.field['A8']["owner"] = None
                                
                                #for move_counter
                                self.field[self.black_press]['move_counter'] = self.field[self.black_press]['move_counter'] + 1
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                click2_not_clicked = False
                            
                            elif i in self.black_moves: 
                                #replace the old square with none and transfer class, picture, and owner to new square
                                self.black_movement(i)
                                #for move_counter
                                self.field[self.black_press]['move_counter'] = self.field[self.black_press]['move_counter'] + 1
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                click2_not_clicked = False
                            
                                
                            else:
                                print('Oops you touched a square without a green dot. Please try again')
                                self.black2()
                                
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