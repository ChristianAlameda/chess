from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
#from board import Board
#board = Board()
#position = board.create_board()
#coordinate = position[1]#squeares
#[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7]]

#These are for after a calculation has done for a move we will swap out the first digit with the letter corresponding
#Then add it to a string number
change = {
    0:'A',
    1:'B',
    2:'C',
    3:'D',
    4:'E',
    5:'F',
    6:'G',
    7:'H'
}
"""
board[x]['piece'] = None
board[x]['owner'] = None
board[x]['picture'] = None
board[new4]['piece'] = black_rook()
board[new4]['owner'] = 'black'
board[new4]['picture'] = b_rook
"""
'''
BLACK PIECES
'''
#x213.update({position_name:{"position":position, "Color":colorSquare, "Piece":None, "position_xy":position_xy}})
#[Black]
#Moveset of the piece



class Piece:
    def __init__(self):
        self.all = []
        a = ['A','B','C','D','E','F','G','H']
        b = ['8','7','6','5','4','3','2','1']
        for i in range(0,8):
            for j in range(0,8):
                self.all.append(a[j]+b[i]) 
    def move(self, x, board):
        # get off of the square they start on unless they are blocked
        pass
    def onBoard(self, new: str):
        # when pressed A8 C6
        if new in self.all:
            return True
        else: return False
    def is_legal(self, result):
        if result[0]>= 0 and result[0]<=7 and result[1]>= 0 and result[1]<=7:
            return True
        else: return False
    def stop(self):
        print('cant move there silly')
    def can_move(self):
        print('you may move there sire/madam')
        

class black_pawn(Piece):
    def move(self, x, board):
        #Movement
        # s = south 1 time
        s = True
        # s2 = south 2 times
        s2 = True
        # sw = south west 1,-1
        sw = True
        # se = south east -1,-1
        se = True
        black_pawn_moves = []
        #white or black piece standing in front
        #of pawn
        #x == square pressed
        result = list(map(sum,zip(board[x]['position_xy'],[0,1])))   #south x1
        if self.is_legal(result):
            new = change[result[0]] + str(result[1])
        else: s = False
        result1 = list(map(sum,zip(board[x]['position_xy'],[1,1])))  #south x1 west x1
        if self.is_legal(result1):
            new1 = change[result1[0]] + str(result1[1])
        else: sw = False
        result2 = list(map(sum,zip(board[x]['position_xy'],[-1,1]))) #south x1 east x1
        if self.is_legal(result2):
            new2 = change[result2[0]] + str(result2[1])
        else: se = False
        result3 = list(map(sum,zip(board[x]['position_xy'],[0,2])))  #south x2
        if self.is_legal(result3):
            new3 = change[result3[0]] + str(result3[1])
        else: s2 = False
        
        #forward 1
        if s:
            if board[new]['piece'] == None: 
                black_pawn_moves.append(new)
            
        #forward 2
        if s2:
            if (board[new]['piece'] == None) and (board[new3]['piece'] == None):
                black_pawn_moves.append(new3)

        #capturing sw
        if sw:
            if board[new1]['owner'] == 'white':
                black_pawn_moves.append(new1)
            
        #capturing se
        if se:
            if (board[new2]['owner'] == 'white') and se:
                black_pawn_moves.append(new2)
            
        #promotion
        if board[new]['position_xy'] == ([0,7] or [1,7] or [2,7] or [3,7] or [4,7] or [5,7] or [6,7] or [7,7]):
            black_pawn_moves.append(new)
            print('what piece would you like to change to?')
            piece_selection = int(input("[1] - Queen\n[2] - bishop\n[3] - Knight\n: "))
            if piece_selection == 1:
                board[x]['piece'] = None
                board[x]['owner'] = None
                board[x]['picture'] = None
                board[new]['piece'] = black_queen() # it == not new but one of the values above 00 01 02 etc... 
                board[new]['owner'] = 'black'
                board[new]['picture'] = b_pawn
                
            elif piece_selection == 2:
                board[x]['piece'] = None
                board[x]['owner'] = None
                board[x]['picture'] = None
                board[new]['piece'] = black_bishop()
                board[new]['owner'] = 'black'
                board[new]['picture'] = b_bishop
                
            elif piece_selection == 3:
                board[x]['piece'] = None
                board[x]['owner'] = None
                board[x]['picture'] = None
                board[new]['piece'] = black_knight()
                board[new]['owner'] = 'black'
                board[new]['picture'] = b_knight
            return black_pawn_moves 
class black_knight(Piece):
    def move(self, x, board):
        black_knight_moves = []
        a = True
        b = True
        c = True
        d = True
        e = True
        f = True
        g = True
        h = True
        # x == whatever get's passed to us through the board pressing
        result = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result):
            new = change[result[0]] + str(result[1])
        else: a = False
        
        result1 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result1):
            new1 = change[result1[0]] + str(result1[1])
        else: b = False
        
        result2 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result2):
            new2 = change[result2[0]] + str(result2[1])
        else: c = False
        
        result3 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result3):
            new3 = change[result3[0]] + str(result3[1])
        else: d = False
        
        result4 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result4):
            new4 = change[result4[0]] + str(result4[1])
        else: e = False
        
        result5 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result5):
            new5 = change[result5[0]] + str(result5[1])
        else: f = False
        
        result6 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        
        if self.is_legal(result6):
            new6 = change[result6[0]] + str(result6[1])
        else: g = False
        result7 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        
        if self.is_legal(result7):
            new7 = change[result7[0]] + str(result7[1])
        else: h = False
        
        #BLACK KNIGHT MOVES
        if a:
            if (board[new]['owner'] == 'white' or board[new]['owner'] == None):#1
                black_knight_moves.append(new)
        
        if b:
            if (board[new1]['owner'] == 'white' or board[new1]['owner'] == None):#2
                black_knight_moves.append(new1)
        
        if c:  
            if (board[new2]['owner'] == 'white' or board[new2]['owner'] == None):#3
                black_knight_moves.append(new2)
        
        if d:  
            if (board[new3]['owner'] == 'white' or board[new3]['owner'] == None):#4
                black_knight_moves.append(new3)
        
        if e:
            if (board[new4]['owner'] == 'white' or board[new4]['owner'] == None):#5
                black_knight_moves.append(new4)
        
        if f:
            if (board[new5]['owner'] == 'white' or board[new5]['owner'] == None):#6
                black_knight_moves.append(new5)
        
        if g:
            if (board[new6]['owner'] == 'white' or board[new6]['owner'] == None):#7
                black_knight_moves.append(new6)
        
        if h:
            if (board[new7]['owner'] == 'white' or board[new7]['owner'] == None):#8
                black_knight_moves.append(new7)
                
        return black_knight_moves
class black_bishop(Piece):
    def show_self(self):
        #b_bishop
        pass
        
    def move(self, x, board):
        black_bishop_moves = []
        nw,ne,sw,se = True,True,True,True
        for i in range(1,7):  
            '''
            we will have 4 lines we are interested in y = -x, x || 
            considering where:
            x increases and y increases
            x increases and y decreases
            x decreases and y increases
            x decreases and y decreases 
            '''
            result1 = list(map(sum,zip(board[x]['position_xy'],[i,i])))
            result2= list(map(sum,zip(board[x]['position_xy'],[i,-i])))
            result3 = list(map(sum,zip(board[x]['position_xy'],[-i,i])))
            result4 = list(map(sum,zip(board[x]['position_xy'],[-i,-i])))
            if self.is_legal(result1):
                new1 = change[result1[0]] + str(result1[1])
            else: nw = False
            
            if self.is_legal(result2):
                new2 = change[result2[0]] + str(result2[1])
            else: ne = False
            
            if self.is_legal(result3):
                new3 = change[result3[0]] + str(result3[1])
            else: sw = False
            
            if self.is_legal(result4):
                new4 = change[result4[0]] + str(result4[1])
            else: se = False
            
            #BLACK BISHOP MOVES
            if nw:
                if (board[new1]['owner'] == 'white' or board[new1]['owner'] == None):#1
                    black_bishop_moves.append(new1)
                else:
                    nw = False
            
            if ne:
                if (board[new2]['owner'] == 'white' or board[new2]['owner'] == None):#2
                    black_bishop_moves.append(new2)
                else:
                    ne = False
            
            if sw:
                if (board[new3]['owner'] == 'white' or board[new3]['owner'] == None):#3
                    black_bishop_moves.append(new3)
                else:
                    sw = False
            
            if se:
                if (board[new4]['owner'] == 'white' or board[new4]['owner'] == None):#4
                    black_bishop_moves.append(new4)
                else:
                    se = False 
        return black_bishop_moves
    
class black_rook(Piece):
    def move(self, x, board):
        black_rook_moves = []
        n,s,w,e = True,True,True,True
        for i in range(1,7):
            '''
            Need to know 4 directions
            1. North: x = x   || y = y+1
            2. South: x = x   || y = y-1
            3. West:  x = x+1 || y = y
            4. East:  x = x-1 || y = y
            '''
            #NORTH
            result1 = list(map(sum,zip(board[x]['position_xy'],[0,i])))  # n
            result2= list(map(sum,zip(board[x]['position_xy'],[0,-i])))  # s
            result3 = list(map(sum,zip(board[x]['position_xy'],[i,0])))  # w
            result4 = list(map(sum,zip(board[x]['position_xy'],[-i,0]))) # e
            if self.is_legal(result1):
                new1 = change[result1[0]] + str(result1[1])
            else: n = False
            
            if self.is_legal(result2):
                new2 = change[result2[0]] + str(result2[1])
            else: s = False
            
            if self.is_legal(result3):
                new3 = change[result3[0]] + str(result3[1])
            else: w = False
            
            if self.is_legal(result4):
                new4 = change[result4[0]] + str(result4[1])
            else: e = False
            
            #BLACK ROOK MOVES
            if n:
                if (board[new1]['owner'] == 'white' or board[new1]['owner'] == None):#1
                    black_rook_moves.append(new1)
                else:                    
                    n = False
                    
            if s:
                if (board[new2]['owner'] == 'white' or board[new2]['owner'] == None):#2
                    black_rook_moves.append(new2)
                else:
                    s = False
            
            if w:
                if (board[new3]['owner'] == 'white' or board[new3]['owner'] == None):#3
                    black_rook_moves.append(new3)
                else:
                    w = False
            
            if e:
                if (board[new4]['owner'] == 'white' or board[new4]['owner'] == None):#4
                    black_rook_moves.append(new4)
                else:
                    e = False
            
        return black_rook_moves
    
class black_queen(Piece):
    def move(self, x, board):
        # A queen can only move as a rook and bishop can move
        black_queen_moves = []
        black_queen_moves.append(black_rook.move(x) + black_bishop.move(x))
        return black_queen_moves
        
class black_king(Piece):
    def move(self, x, board):
        black_king_check_if_bad = []
        #adding all squares a white piece could potentially go
        for key in board:
            if key['owner'] == 'white':
                black_king_check_if_bad.append(key['piece'].move(key))# gives me a list of moves that that piece can move
        #adding all squares black pieces are
        for key in board:
            if key['owner'] == 'black':
                black_king_check_if_bad.append(key['piece'].move(key))
        #Collecting position of all pieces on the board
        for key in board:
            if key['owner'] == 'white':
                black_king_check_if_bad.append(key)
        #if king move == not in line of check and has no pieces next to it and == free to roam then it has 8 moves the king can make
        result1 = list(map(sum,zip(board[x]['position_xy'],[0,1])))  # n
        result2= list(map(sum,zip(board[x]['position_xy'],[0,-1])))  # s
        result3 = list(map(sum,zip(board[x]['position_xy'],[1,0])))  # w
        result4 = list(map(sum,zip(board[x]['position_xy'],[-1,0]))) # e
        result5 = list(map(sum,zip(board[x]['position_xy'],[1,1])))  # nw
        result6= list(map(sum,zip(board[x]['position_xy'],[1,-1])))  # sw
        result7 = list(map(sum,zip(board[x]['position_xy'],[1,-1])))  # ne
        result8 = list(map(sum,zip(board[x]['position_xy'],[-1,-1]))) # se
        n,s,w,e,nw,sw,ne,se = True,True,True,True,True,True,True,True
        black_king_moves = []
        if self.is_legal(result1):
            new1 = change[result1[0]] + str(result1[1])
        else: n = False
        
        if self.is_legal(result2):
            new2 = change[result2[0]] + str(result2[1])
        else: s = False
        
        if self.is_legal(result3):
            new3 = change[result3[0]] + str(result3[1])
        else: w = False
        
        if self.is_legal(result4):
            new4 = change[result4[0]] + str(result4[1])
        else: e = False
        
        if self.is_legal(result5):
            new5 = change[result5[0]] + str(result5[1])
        else: nw = False
        
        if self.is_legal(result6):
            new6 = change[result6[0]] + str(result6[1])
        else: sw = False
        
        if self.is_legal(result7):
            new7 = change[result7[0]] + str(result7[1])
        else: ne = False
        
        if self.is_legal(result8):
            new8 = change[result8[0]] + str(result8[1])
        else: se = False
        
        #BLACK KING MOVES
        if n:
            if board[new1] not in black_king_check_if_bad:#1
                black_king_moves.append(new1)
            else:
                n = False
        
        if s:
            if board[new2] not in black_king_check_if_bad:#2
                black_king_moves.append(new2)
            else:
                s = False
        
        if w:
            if board[new3] not in black_king_check_if_bad:#3
                black_king_moves.append(new3)
            else:
                w = False
        
        if e:
            if board[new4] not in black_king_check_if_bad:#4
                black_king_moves.append(new4)
            else:
                e = False
        
        if nw:
            if board[new5] not in black_king_check_if_bad:#5
                black_king_moves.append(new5)
            else:
                nw = False
        
        if sw:
            if board[new6] not in black_king_check_if_bad:#6
                black_king_moves.append(new6)
            else:
                sw = False
        
        if ne:
            if board[new7] not in black_king_check_if_bad:#7
                black_king_moves.append(new7)
            else:
                ne = False
        if se:
            if board[new8] not in black_king_check_if_bad:#8
                black_king_moves.append(new8)
            else:
                se = False

class white_pawn(Piece):
    def move(self, x, board):
        #Movement
        # n = north 1 time
        n = True
        # n2 = north 2 times
        n2 = True
        # nw = north west 
        nw = True
        # ne = north east 
        ne = True
        white_pawn_moves = []
        #white or black piece standing in front
        #of pawn
        #x == square pressed
        result = list(map(sum,zip(board[x]['position_xy'],[0,-1])))   #north x1
        if self.is_legal(result):
            new = change[result[0]] + str(result[1])
        else: n = False
        
        result1 = list(map(sum,zip(board[x]['position_xy'],[1,-1])))  #north x1 west x1
        if self.is_legal(result1):
            new1 = change[result1[0]] + str(result1[1])
        else: nw = False
        
        result2 = list(map(sum,zip(board[x]['position_xy'],[-1,-1]))) #north x1 east x1
        if self.is_legal(result2):
            new2 = change[result2[0]] + str(result2[1])
        else: ne = False
        
        result3 = list(map(sum,zip(board[x]['position_xy'],[0,-2])))  #north x2
        if self.is_legal(result3):
            new3 = change[result3[0]] + str(result3[1])
        else: n2 = False
        
        #WHITE PAWN MOVES
        
        #forward 1
        if n:
            if (board[new]['piece'] == None): 
                white_pawn_moves.append(new)
            else:
                s = False
            
        #forward 2
        if n2:
            if (board[new]['piece'] == None) and (board[new3]['piece'] == None):
                white_pawn_moves.append(new3)
            else:
                n2 = False
        
        #north west capture
        if nw:
            if board[new1]['owner'] == 'black':
                white_pawn_moves.append(new1)
            else:
                nw = False
        
        #north east capture
        if ne:
            if (board[new2]['owner'] == 'white'):
                white_pawn_moves.append(new2)
            else:
                ne = False
            
        if board[new]['position_xy'] == ([0,0] or [0,1] or [0,2] or [0,3] or [0,4] or [0,5] or [0,6] or [0,7]):
            white_pawn_moves.append(new)
            print('what piece would you like to change to?')
            piece_selection = int(input("[1] - Queen\n[2] - bishop\n[3] - Knight\n: "))
            if piece_selection == 1:
                board[x]['piece'] = None
                board[x]['owner'] = None
                board[x]['picture'] = None
                board[new]['piece'] = black_queen() # it == not new but one of the values above 00 01 02 etc... 
                board[new]['owner'] = 'black'
                board[new]['picture'] = b_pawn
                
            elif piece_selection == 2:
                board[x]['piece'] = None
                board[x]['owner'] = None
                board[x]['picture'] = None
                board[new]['piece'] = black_bishop()
                board[new]['owner'] = 'black'
                board[new]['picture'] = b_bishop
                
            elif piece_selection == 3:
                board[x]['piece'] = None
                board[x]['owner'] = None
                board[x]['picture'] = None
                board[new]['piece'] = black_knight()
                board[new]['owner'] = 'black'
                board[new]['picture'] = b_knight
            
        return white_pawn_moves
class white_knight(Piece):
    def move(self, x, board):
        white_knight_moves = []
        a = True
        b = True
        c = True
        d = True
        e = True
        f = True
        g = True
        h = True
        # x == whatever get's passed to us through the board pressing
        result = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result):
            new = change[result[0]] + str(result[1])
        else: a = False
        result1 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result1):
            new1 = change[result1[0]] + str(result1[1])
        else: b = False
        result2 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result2):
            new2 = change[result2[0]] + str(result2[1])
        else: c = False
        result3 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result3):
            new3 = change[result3[0]] + str(result3[1])
        else: d = False
        result4 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result4):
            new4 = change[result4[0]] + str(result4[1])
        else: e = False
        result5 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result5):
            new5 = change[result5[0]] + str(result5[1])
        else: f = False
        result6 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result6):
            new6 = change[result6[0]] + str(result6[1])
        else: g = False
        result7 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result7):
            new7 = change[result7[0]] + str(result7[1])
        else: h = False
        
        # CHECK KNIGHT MOVES
        if a:
            if (board[new]['owner'] == 'black' or board[new]['owner'] == None):#1
                white_knight_moves.append(new)
            else:
                a = False
        
        if b:
            if (board[new1]['owner'] == 'black' or board[new1]['owner'] == None):#2
                white_knight_moves.append(new1)
            else:
                b = False
                
        if c:
            if (board[new2]['owner'] == 'black' or board[new2]['owner'] == None):#3
                white_knight_moves.append(new2)
            else:
                c = False
        
        if d:
            if (board[new3]['owner'] == 'black' or board[new3]['owner'] == None):#4
                white_knight_moves.append(new3)
            else:
                d = False
        if e:
            if (board[new4]['owner'] == 'black' or board[new4]['owner'] == None):#5
                white_knight_moves.append(new4)
            else:
                e = False
        
        if f:
            if (board[new5]['owner'] == 'black' or board[new5]['owner'] == None):#6
                white_knight_moves.append(new5)
            else:
                f = False
        
        if g:
            if (board[new6]['owner'] == 'black' or board[new6]['owner'] == None):#7
                white_knight_moves.append(new6)
            else:
                g = False
        
        if h:
            if (board[new7]['owner'] == 'black' or board[new7]['owner'] == None):#8
                white_knight_moves.append(new7)
            else:
                a = False
            
class white_bishop(Piece):
    def move(self, x, board):
        white_bishop_moves = []
        nw,ne,sw,se = True,True,True,True
        for i in range(1,7):  
            '''
            we will have 4 lines we are interested in y = -x, x || 
            considering where:
            x increases and y increases
            x increases and y decreases
            x decreases and y increases
            x decreases and y decreases 
            '''
            result1 = list(map(sum,zip(board[x]['position_xy'],[i,i])))
            result2= list(map(sum,zip(board[x]['position_xy'],[i,-i])))
            result3 = list(map(sum,zip(board[x]['position_xy'],[-i,i])))
            result4 = list(map(sum,zip(board[x]['position_xy'],[-i,-i])))
            
            if self.is_legal(result1):
                new1 = change[result1[0]] + str(result1[1])
            else: nw = False
            
            if self.is_legal(result2):
                new2 = change[result2[0]] + str(result2[1])
            else: ne = False
            
            if self.is_legal(result3):
                new3 = change[result3[0]] + str(result3[1])
            else: sw = False
            
            if self.is_legal(result4):
                new4 = change[result4[0]] + str(result4[1])
            else: se = False
            
            #CHECKING BISHOP MOVES
            if nw:
                if (board[new1]['owner'] == 'black' or board[new1]['owner'] == None):#1
                    white_bishop_moves.append(new1)
                else:
                    nw = False
            
            if ne:
                if (board[new2]['owner'] == 'black' or board[new2]['owner'] == None):#2
                    white_bishop_moves.append(new2)
                else:                    
                    ne = False
            
            if sw:
                if (board[new3]['owner'] == 'black' or board[new3]['owner'] == None):#3
                    white_bishop_moves.append(new3)
                else:                    
                    sw = False
            
            if se:
                if (board[new4]['owner'] == 'black' or board[new4]['owner'] == None):#4
                    white_bishop_moves.append(new4)
                else:                    
                    se = False
                    
        return white_bishop_moves
class white_rook(Piece):
    def move(self,x, board):
        white_rook_moves = []
        n,s,w,e = True,True,True,True
        for i in range(1,7):
            '''
            Need to know 4 directions
            1. North: x = x   || y = y+1
            2. South: x = x   || y = y-1
            3. West:  x = x+1 || y = y
            4. East:  x = x-1 || y = y
            '''
            #NORTH
            result1 = list(map(sum,zip(board[x]['position_xy'],[0,i])))  # n
            result2= list(map(sum,zip(board[x]['position_xy'],[0,-i])))  # s
            result3 = list(map(sum,zip(board[x]['position_xy'],[i,0])))  # w
            result4 = list(map(sum,zip(board[x]['position_xy'],[-i,0]))) # e
            if self.is_legal(result1):
                new1 = change[result1[0]] + str(result1[1])
            else: n = False
            
            if self.is_legal(result2):
                new2 = change[result2[0]] + str(result2[1])
            else: s = False
            
            if self.is_legal(result3):
                new3 = change[result3[0]] + str(result3[1])
            else: w = False
            
            if self.is_legal(result4):
                new4 = change[result4[0]] + str(result4[1])
            else: e = False   
           
            if n: 
                if (board[new1]['owner'] == 'black' or board[new1]['owner'] == None):#1
                    white_rook_moves.append(new1)
                else:                    
                    n = False
            
            if s:
                if (board[new2]['owner'] == 'black' or board[new2]['owner'] == None):#2
                    white_rook_moves.append(new2)
                else:                    
                    s = False
            
            if w:
                if (board[new3]['owner'] == 'black' or board[new3]['owner'] == None):#3
                    white_rook_moves.append(new3)                    
                    w = False
            
            if e:    
                if (board[new4]['owner'] == 'black' or board[new4]['owner'] == None):#4
                    white_rook_moves.append(new4)                    
                    e = False
                    
        return white_rook_moves
    
class white_queen(Piece):
    def move(self, x, board):
        # A queen can only move as a rook and bishop can move
        white_queen_moves = []
        white_queen_moves.append(white_rook.move(x,board) + white_bishop.move(x,board))
        return white_queen_moves
        
class white_king(Piece):
    def move(self, x, board):
        white_king_check_if_bad = []
        #adding all squares a black piece could potentially go
        for key in board:
            if key['owner'] == 'black':
                white_king_check_if_bad.append(key['piece'].move(key))# gives me a list of moves that that piece can move
        #adding all squares black pieces are
        for key in board:
            if key['owner'] == 'white':
                white_king_check_if_bad.append(key['piece'].move(key))
        #Collecting position of all pieces on the board
        for key in board:
            if key['owner'] == 'black':
                white_king_check_if_bad.append(key)
        #if king move == not in line of check and has no pieces next to it and == free to roam then it has 8 moves the king can make
        result1 = list(map(sum,zip(board[x]['position_xy'],[0,1])))  # n
        result2= list(map(sum,zip(board[x]['position_xy'],[0,-1])))  # s
        result3 = list(map(sum,zip(board[x]['position_xy'],[1,0])))  # w
        result4 = list(map(sum,zip(board[x]['position_xy'],[-1,0]))) # e
        result5 = list(map(sum,zip(board[x]['position_xy'],[1,1])))  # nw
        result6= list(map(sum,zip(board[x]['position_xy'],[1,-1])))  # sw
        result7 = list(map(sum,zip(board[x]['position_xy'],[1,-1])))  # ne
        result8 = list(map(sum,zip(board[x]['position_xy'],[-1,-1]))) # se
        n,s,w,e,nw,sw,ne,se = True,True,True,True,True,True,True,True
        white_king_moves = []
        
        if self.is_legal(result1):
            new1 = change[result1[0]] + str(result1[1])
        else: n = False
        
        if self.is_legal(result2):
            new2 = change[result2[0]] + str(result2[1])
        else: s = False
        
        if self.is_legal(result3):
            new3 = change[result3[0]] + str(result3[1])
        else: w = False
        
        if self.is_legal(result4):
            new4 = change[result4[0]] + str(result4[1])
        else: e = False
        
        if self.is_legal(result5):
            new5 = change[result5[0]] + str(result5[1])
        else: nw = False
        
        if self.is_legal(result6):
            new6 = change[result6[0]] + str(result6[1])
        else: sw = False
        
        if self.is_legal(result7):
            new7 = change[result7[0]] + str(result7[1])
        else: ne = False
        
        if self.is_legal(result8):
            new8 = change[result8[0]] + str(result8[1])
        else: se = False
        
        #KING MOVES
        
        if n:
            if board[new1] not in white_king_check_if_bad:#1
                white_king_moves.append(new1)
            else:
                n = False
        
        if s:    
            if board[new2] not in white_king_check_if_bad:#2
                white_king_moves.append(new2)
            else:
                s = False
        
        if w:  
            if board[new3] not in white_king_check_if_bad:#3
                white_king_moves.append(new3)
            else:
                w = False
        
        if e:
            if board[new4] not in white_king_check_if_bad:#4
                white_king_moves.append(new4)
            else:
                e = False
                
        if nw:
            if board[new5] not in white_king_check_if_bad:#5
                white_king_moves.append(new5)
            else:
                nw = False
            
        if sw:
            if board[new6] not in white_king_check_if_bad:#6
                white_king_moves.append(new6)
            else:
                sw = False
                
        if ne:
            if board[new7] not in white_king_check_if_bad:#7
                white_king_moves.append(new7)
            else:
                ne = False
                
        if se:
            if board[new8] not in white_king_check_if_bad:#8
                white_king_moves.append(new8)
            else:
                se = False
        return white_king_moves