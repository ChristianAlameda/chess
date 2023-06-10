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
        #self.make_board()
        #pygame.display.flip()
        #initializing window
        x = 1000
        y = 1000
        self.background = pygame.display.set_mode((x, y))
        self.image = mapping.board
        self.picture_of_board()
        self.white_moves = []
        self.white_press = ''
        self.black_moves = []
        self.black_press = ''
        
    def get_field(self):
        return self.field

    def create_board(self):
        color = (0,0,0)
        outlineThickness = 1
        x1 = 81.4
        self.picture_of_board()
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
                position = pygame.draw.rect(self.background,color, pygame.Rect(225+j*x1,175+i*x1,x1,x1), outlineThickness, border_radius=1)
                position_xy = [j,i] # 0,0 0,1 0,2 0,3 0,4 0,5
                top_left_corner = (225+j*x1,175+i*x1)
                middle = (225+j*x1 + x1/2 - 10,175+i*x1 + x1/2 - 10)
                color_square = blackOrWhite
                if blackOrWhite % 2 == 0:
                    color_square = 'W'
                else:
                    color_square = 'B'
                squares.append(position_xy)
                self.field.update({position_name:{"position":position, "color_square":color_square, "owner":None ,"piece":None,"picture":None, "position_xy":position_xy, "top_left_corner":top_left_corner, "middle":middle}})
                
                blackOrWhite = blackOrWhite + 1
        return self.field, squares # self.field is a dictionary of dictionaries {{key:{value1,value2}}} # squares is a list of lists for coordinates [[0,0],[0,1],[0,2]]

    def picture_of_board(self):
        self.background.blit(self.image, (150, 100))
    
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
            decider = self.black_or_white(clicked)
            if decider == "W":
                self.white1()
                self.white2()
                for i in self.field:
                    print(i, self.field[i]['position_xy'], self.field[i]['piece'])
                clicked = clicked + 1
            elif decider == "B":
                self.black1()
                self.black2()
                for i in self.field:
                    print(i, self.field[i]['position_xy'], self.field[i]['piece'])
                clicked = clicked + 1
            else:
                not_gameover = False
    
    def white1(self):
        click1_not_clicked = True
        self.make_board()
        self.clear_white_and_black_moves()
        print("It's white's first press")
        while click1_not_clicked:
            for event in pygame.event.get():
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
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    self.white_moves.append(j)
                                    pygame.display.update(self.field[j]['position'])
                                
                            elif isinstance(self.field[i]['piece'], white_knight):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    self.white_moves.append(j)
                                    pygame.display.update(self.field[j]['position'])

                            elif isinstance(self.field[i]['piece'], white_bishop):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    self.white_moves.append(j)
                                    pygame.display.update(self.field[j]['position'])
                                    
                            elif isinstance(self.field[i]['piece'], white_rook):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    self.white_moves.append(j)
                                    pygame.display.update(self.field[j]['position'])
                            
                            elif isinstance(self.field[i]['piece'], white_queen):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    self.white_moves.append(j)
                                    pygame.display.update(self.field[j]['position'])
                                    
                            elif isinstance(self.field[i]['piece'], white_king):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    self.white_moves.append(j)
                                    pygame.display.update(self.field[j]['position']) # (), w, h
                            
                                
                            click1_not_clicked = False
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
    
    def clear_whitepress_and_blackpress(self):
        self.white_press = ''
        self.black_press = ''
                                    
    def white2(self):
        click2_not_clicked = True
        self.make_board()
        print("It is white's second press")
        print(self.white_moves)
        while click2_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            if (i in self.white_moves): 
                                #replace the old square with none and transfer class, picture, and owner to new square
                                self.field[i]["picture"] = self.field[self.white_press]["picture"] 
                                self.field[i]["piece"] = self.field[self.white_press]["piece"]
                                self.field[i]["owner"] = self.field[self.white_press]["owner"]
                                self.field[self.white_press]["picture"] = None
                                self.field[self.white_press]["piece"] = None
                                self.field[self.white_press]["owner"] = None
                                self.make_board()
                                pygame.display.update()#flip
                                self.clear_white_and_black_moves()
                                self.clear_whitepress_and_blackpress()
                                click2_not_clicked = False
                            else:
                                print('Oops you touched a square without a green dot. Please try again')
                                self.white2()
                                
    def black1(self):
        click1_not_clicked = True
        self.make_board()
        self.clear_white_and_black_moves()
        print("It is black's first press")
        while click1_not_clicked:
            for event in pygame.event.get():
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
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    
                                    self.black_moves.append(j)
                                    
                                    pygame.display.update(self.field[j]['position'])
                                    
                            elif isinstance(self.field[i]['piece'], black_knight):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    
                                    self.black_moves.append(j)
                                    
                                    pygame.display.update(self.field[j]['position'])
                                    
                            elif isinstance(self.field[i]['piece'], black_bishop):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    
                                    self.black_moves.append(j)
                                    
                                    pygame.display.update(self.field[j]['position'])
                                    
                            elif isinstance(self.field[i]['piece'], black_rook):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    
                                    self.black_moves.append(j)
                                    
                                    pygame.display.update(self.field[j]['position'])
                                    
                            elif isinstance(self.field[i]['piece'], black_queen):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    
                                    self.black_moves.append(j)
                                    
                                    pygame.display.update(self.field[j]['position'])
                                    
                            elif isinstance(self.field[i]['piece'], black_king):
                                print(self.field[i]['piece'].move(i,self.get_field()))
                                for j in self.field[i]['piece'].move(i,self.get_field()):#[a8,b5,...]
                                    self.background.blit(green_50, self.field[j]['middle'])
                                    
                                    self.black_moves.append(j)
                                    
                                    pygame.display.update(self.field[j]['position'])
                            click1_not_clicked = False
                                    
    def black2(self):
        click2_not_clicked = True
        print("It's black's second press")
        while click2_not_clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in self.field:
                        if self.field[i]["position"].collidepoint(pygame.mouse.get_pos()):
                            if i in self.black_moves: 
                                #replace the old square with none and transfer class, picture, and owner to new square
                                self.field[i]["picture"] = self.field[self.black_press]["picture"] 
                                self.field[i]["piece"] = self.field[self.black_press]["piece"]
                                self.field[i]["owner"] = self.field[self.black_press]["owner"]
                                self.field[self.black_press]["picture"] = None
                                self.field[self.black_press]["piece"] = None
                                self.field[self.black_press]["owner"] = None
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
def main():
    newboard = Board()
    newboard.start_game()
if __name__ == "__main__":
    main()