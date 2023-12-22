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
change1 = {
    0:'8',
    1:'7',
    2:'6',
    3:'5',
    4:'4',
    5:'3',
    6:'2',
    7:'1'
}
class Piece:
    def __init__(self):
        pass
        
    def move(self, x, board):
        # get off of the square they start on unless they are blocked
        pass
    
    def move1(self, x, board):
        pass
    
    def move2(self, x, board):
        pass

    def pinned(self,x,board):#given square and board with it's pieces
        # remove piece from game and check if an opposing piece can attack the king
        
        sking = super_king()
        if board[x]['owner'] == 'white':
            for key in board:
                if isinstance(board[key]['piece'], white_king):
                    king_line = sking.move(key,board)#[[n],[s],[w],[e],[nw],[ne],[sw],[se]]
                    #accounting for rook and queen moves | _
                    for index, value in enumerate(king_line[0]):
                        if isinstance(board[value]['piece'], black_queen) or isinstance(board[value]['piece'], black_rook):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[0][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[0][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                                
                                
                    for index, value in enumerate(king_line[1]):
                        if isinstance(board[value]['piece'], black_queen) or isinstance(board[value]['piece'], black_rook):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[1][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[1][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                    
                    for index, value in enumerate(king_line[2]):
                        if isinstance(board[value]['piece'], black_queen) or isinstance(board[value]['piece'], black_rook):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[2][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[2][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                                
                    for index, value in enumerate(king_line[3]):
                        if isinstance(board[value]['piece'], black_queen) or isinstance(board[value]['piece'], black_rook):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[3][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[3][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                                
                    for index, value in enumerate(king_line[4]):
                        if isinstance(board[value]['piece'], black_queen) or isinstance(board[value]['piece'], black_bishop):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[4][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[4][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value

                    for index, value in enumerate(king_line[5]):
                        if isinstance(board[value]['piece'], black_queen) or isinstance(board[value]['piece'], black_bishop):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[5][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[5][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value

                    for index, value in enumerate(king_line[6]):
                        if isinstance(board[value]['piece'], black_queen) or isinstance(board[value]['piece'], black_bishop):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[6][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[6][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                    
                    for index, value in enumerate(king_line[7]):
                        if isinstance(board[value]['piece'], black_queen) or isinstance(board[value]['piece'], black_bishop):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[7][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[7][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                    return False
        
        
        
        #FOR Black
        if board[x]['owner'] == 'black':
            for key in board:
                if isinstance(board[key]['piece'], black_king):
                    king_line = sking.move(key,board)#[[n],[s],[w],[e],[],[],[]]
                    #accounting for rook and queen moves | _
                    for index, value in enumerate(king_line[0]):
                        if isinstance(board[value]['piece'], white_queen) or isinstance(board[value]['piece'], white_rook):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[0][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[0][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                                
                    for index, value in enumerate(king_line[1]):
                        if isinstance(board[value]['piece'], white_queen) or isinstance(board[value]['piece'], white_rook):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[1][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[1][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                    
                    for index, value in enumerate(king_line[2]):
                        if isinstance(board[value]['piece'], white_queen) or isinstance(board[value]['piece'], white_rook):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[2][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[2][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                                
                    for index, value in enumerate(king_line[3]):
                        if isinstance(board[value]['piece'], white_queen) or isinstance(board[value]['piece'], white_rook):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[3][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[3][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                                
                    for index, value in enumerate(king_line[4]):
                        if isinstance(board[value]['piece'], white_queen) or isinstance(board[value]['piece'], white_bishop):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[4][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[4][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value

                    for index, value in enumerate(king_line[5]):
                        if isinstance(board[value]['piece'], white_queen) or isinstance(board[value]['piece'], white_bishop):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[5][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[5][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value

                    for index, value in enumerate(king_line[6]):
                        if isinstance(board[value]['piece'], white_queen) or isinstance(board[value]['piece'], white_bishop):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[6][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[6][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                    
                    for index, value in enumerate(king_line[7]):
                        if isinstance(board[value]['piece'], white_queen) or isinstance(board[value]['piece'], white_bishop):
                            curr = 0
                            temp = []
                            for i in range(0,index):
                                if board[king_line[7][i]]['piece'] != None:
                                    curr = curr + 1
                                    temp.append(king_line[7][i])
                            if curr == 1:
                                if x in temp:
                                    return True, value
                    return False
    def is_legal(self, result):
        if result[0]>= 0 and result[0]<=7 and result[1]>= 0 and result[1]<=7:
            return True
        else: return False
        
    def stop(self):
        print('cant move there silly')
        
    def can_move(self):
        print('you may move there sire/madam')

class super_king(Piece):
    def move(self,x,board):
        north,south,west,east = [],[],[],[]
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
            if self.is_legal(result1):# I am rook
                new1 = change[result1[0]] + change1[result1[1]]
            else: n = False
            
            if self.is_legal(result2):
                new2 = change[result2[0]] + change1[result2[1]]
            else: s = False
            
            if self.is_legal(result3):
                new3 = change[result3[0]] + change1[result3[1]]
            else: w = False
            
            if self.is_legal(result4):
                new4 = change[result4[0]] + change1[result4[1]]
            else: e = False
            
            if n:
                north.append(new1)
            if s:
                south.append(new2)
            if w:
                west.append(new3)
            if e:
                east.append(new4)
            
            
        
        nwest,neast,swest,seast = [], [], [], []
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
            if self.is_legal(result1):#I am bishop
                new1 = change[result1[0]] + change1[result1[1]]
            else: nw = False
            
            if self.is_legal(result2):
                new2 = change[result2[0]] + change1[result2[1]]
            else: ne = False
            
            if self.is_legal(result3):
                new3 = change[result3[0]] + change1[result3[1]]
            else: sw = False
            
            if self.is_legal(result4):
                new4 = change[result4[0]] + change1[result4[1]]
            else: se = False
            #BLACK BISHOP MOVES
            if nw:
                nwest.append(new1)
            
            if ne:
                neast.append(new2)
            
            if sw:
                swest.append(new3)
            
            if se:
                seast.append(new4)
        
        return [north,south,west,east,nwest,neast,swest,seast]
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
#BLACK PIECES
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
            new = change[result[0]] + change1[result[1]]
        else: s = False
        
        result1 = list(map(sum,zip(board[x]['position_xy'],[1,1])))  #south x1 west x1
        if self.is_legal(result1):
            new1 = change[result1[0]] + change1[result1[1]]
        else: sw = False
        
        result2 = list(map(sum,zip(board[x]['position_xy'],[-1,1]))) #south x1 east x1
        if self.is_legal(result2):
            new2 = change[result2[0]] + change1[result2[1]]
        else: se = False
        
        result3 = list(map(sum,zip(board[x]['position_xy'],[0,2])))  #south x2
        potential = [[0,1] , [1,1] , [2,1] , [3,1] , [4,1] , [5,1] , [6,1] , [7,1]]
        if self.is_legal(result3) and (board[x]['position_xy'] in potential):
            new3 = change[result3[0]] + change1[result3[1]]
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
        
        #caputuring en peasants
        if sw or se:
            pass
        
        #promotion
        from mapping import b_pawn, b_bishop, b_knight
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
                
        if self.pinned(x,board) == False:
            pass
        else:
            for i in black_pawn_moves:
                if self.pinned(x,board)[1] == i:
                    black_pawn_moves = []
                    only_move = black_pawn_moves.append(i)
                    return only_move
                else:
                    black_pawn_moves = []
                    return black_pawn_moves
                
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
            new = change[result[0]] + change1[result[1]]
        else: a = False
        
        result1 = list(map(sum,zip(board[x]['position_xy'],[2,-1])))
        if self.is_legal(result1):
            new1 = change[result1[0]] + change1[result1[1]]
        else: b = False
        
        result2 = list(map(sum,zip(board[x]['position_xy'],[-2,1])))
        if self.is_legal(result2):
            new2 = change[result2[0]] + change1[result2[1]]
        else: c = False
        
        result3 = list(map(sum,zip(board[x]['position_xy'],[-2,-1])))
        if self.is_legal(result3):
            new3 = change[result3[0]] + change1[result2[1]]
        else: d = False
        
        result4 = list(map(sum,zip(board[x]['position_xy'],[1,2])))
        if self.is_legal(result4):
            new4 = change[result4[0]] + change1[result4[1]]
        else: e = False
        
        result5 = list(map(sum,zip(board[x]['position_xy'],[1,-2])))
        if self.is_legal(result5):
            new5 = change[result5[0]] + change1[result5[1]]
        else: f = False
        
        result6 = list(map(sum,zip(board[x]['position_xy'],[-1,2])))
        
        if self.is_legal(result6):
            new6 = change[result6[0]] + change1[result6[1]]
        else: g = False
        result7 = list(map(sum,zip(board[x]['position_xy'],[-1,-2])))
        
        if self.is_legal(result7):
            new7 = change[result7[0]] + change1[result7[1]]
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
                
        if self.pinned(x,board) == False:
            pass
        else:
            for i in black_knight_moves:
                if self.pinned(x,board)[1] == i:
                    black_knight_moves = []
                    only_move = black_knight_moves.append(i)
                    return only_move
                else:
                    black_knight_moves = []
                    return black_knight_moves
                
        return black_knight_moves
    
class black_bishop(Piece):
    def show_self(self):
        #b_bishop
        pass
        
    def move(self, x, board):
        black_bishop_moves = []
        '''
        we will have 4 lines we are interested in y = -x, x || 
        considering where:
        x increases and y increases
        x increases and y decreases
        x decreases and y increases
        x decreases and y decreases 
        '''
        for i in range(1,7):  #sw
            result1 = list(map(sum,zip(board[x]['position_xy'],[i,i])))
            if self.is_legal(result1):#I am bishop
                new1 = change[result1[0]] + change1[result1[1]]
            else: break

            if board[new1]['owner'] == 'white':
                black_bishop_moves.append(new1)
                break
            elif board[new1]['owner'] == None:
                black_bishop_moves.append(new1)
            else:
                break
            
        for i in range(1,7):#nw
            result2= list(map(sum,zip(board[x]['position_xy'],[i,-i])))
            if self.is_legal(result2):
                new2 = change[result2[0]] + change1[result2[1]]
            else: break
            
            if board[new2]['owner'] == 'white':
                black_bishop_moves.append(new2)
                break
            elif board[new2]['owner'] == None:
                black_bishop_moves.append(new2)
            else:
                break
            
        for i in range(1,7):#se
            result3 = list(map(sum,zip(board[x]['position_xy'],[-i,i])))
            
            if self.is_legal(result3):
                new3 = change[result3[0]] + change1[result3[1]]
            else: break
            
            if board[new3]['owner'] == 'white':
                black_bishop_moves.append(new3)
                break
            elif board[new3]['owner'] == None:
                black_bishop_moves.append(new3)
            else:
                break
            
        for i in range(1,7):#ne
            result4 = list(map(sum,zip(board[x]['position_xy'],[-i,-i])))
            if self.is_legal(result4):
                new4 = change[result4[0]] + change1[result4[1]]
            else: break
            
            if board[new4]['owner'] == 'white':
                black_bishop_moves.append(new4)
                break
            elif board[new4]['owner'] == None:
                black_bishop_moves.append(new4)
            else:
                break
            
        if self.pinned(x,board) == False:
            pass
        else:
            for i in black_bishop_moves:
                if self.pinned(x,board)[1] == i:
                    black_bishop_moves = []
                    only_move = black_bishop_moves.append(i)
                    return only_move
                else:
                    black_bishop_moves = []
                    return black_bishop_moves
        return black_bishop_moves
    
class black_rook(Piece):
    def move(self, x, board):
        black_rook_moves = []
        for i in range(1,7):  
            result1 = list(map(sum,zip(board[x]['position_xy'],[0,-i])))
            if self.is_legal(result1):
                new1 = change[result1[0]] + change1[result1[1]]
            else: break
            
            if board[new1]['owner'] == 'white':
                black_rook_moves.append(new1)
                break
            elif board[new1]['owner'] == None:#1
                black_rook_moves.append(new1)
            else:
                break
            
        for i in range(1,7):
            result2= list(map(sum,zip(board[x]['position_xy'],[0,i])))
            if self.is_legal(result2):
                new2 = change[result2[0]] + change1[result2[1]]
            else: break
            
            if board[new2]['owner'] == 'white':
                black_rook_moves.append(new2)
                break
            elif board[new2]['owner'] == None:#1
                black_rook_moves.append(new2)
            else:                    
                break
            
        for i in range(1,7):
            result3 = list(map(sum,zip(board[x]['position_xy'],[i,0])))
            if self.is_legal(result3):
                new3 = change[result3[0]] + change1[result3[1]]
            else: break

            if board[new3]['owner'] == 'white':
                black_rook_moves.append(new3)
                break
            elif board[new3]['owner'] == None:
                black_rook_moves.append(new3)
            else:                    
                break
        
        for i in range(1,7):
            result4 = list(map(sum,zip(board[x]['position_xy'],[-i,0])))
            if self.is_legal(result4):
                new4 = change[result4[0]] + change1[result4[1]]
            else: break
            
            if board[new4]['owner'] == 'white':
                black_rook_moves.append(new4)
                break
            elif board[new4]['owner'] == None:#1
                black_rook_moves.append(new4)
            else:                    
                break
                    
        if self.pinned(x,board) == False:
            pass
        else:
            for i in black_rook_moves:
                if self.pinned(x,board)[1] == i:
                    black_rook_moves = []
                    only_move = black_rook_moves.append(i)
                    return only_move 
                else:
                    black_rook_moves = []
                    return black_rook_moves
                 
        return black_rook_moves
    
class black_queen(Piece):
    def move(self, x, board):
        # A queen can only move as a rook and bishop can move
        brook = black_rook()
        bbishop = black_bishop()
        black_queen_moves = brook.move(x,board) + bbishop.move(x,board)#[[],[]];;;
        
        if self.pinned(x,board) == False:
            pass
        elif self.pinned(x,board)[0]:
            for i in black_queen_moves:
                if self.pinned(x,board)[1] == i:
                    black_queen_moves = []
                    only_move = black_queen_moves.append(i)
                    return only_move
                else:
                    black_queen_moves = []
                    return black_queen_moves
                
        return black_queen_moves
        
class black_king(Piece):
    def move(self, x, board):
        black_king_check_if_bad = []
        #adding all squares a white piece could potentially go
        for key in board:
            #check white movement
            if isinstance(board[key]['piece'], white_king):
                pass
            elif board[key]['owner'] == 'white':
                for i in board[key]['piece'].move(key,board):
                    
                    black_king_check_if_bad.append(i)
                    #black_king_check_if_bad.append(board[key]['piece'].move(key,board))# gives me a list of moves that that piece can move
            #check if black piece is there
            elif board[key]['owner'] == 'black':
                black_king_check_if_bad.append(key)
                
        
        #if king move == not in line of check and has no pieces next to it and == free to roam then it has 8 moves the king can make
        result1 = list(map(sum,zip(board[x]['position_xy'],[0,1])))  # n
        result2= list(map(sum,zip(board[x]['position_xy'],[0,-1])))  # s
        result3 = list(map(sum,zip(board[x]['position_xy'],[1,0])))  # w
        result4 = list(map(sum,zip(board[x]['position_xy'],[-1,0]))) # e
        result5 = list(map(sum,zip(board[x]['position_xy'],[1,1])))  # nw
        result6= list(map(sum,zip(board[x]['position_xy'],[1,-1])))  # sw
        result7 = list(map(sum,zip(board[x]['position_xy'],[-1,1])))  # ne
        result8 = list(map(sum,zip(board[x]['position_xy'],[-1,-1]))) # se
        result9 = list(map(sum,zip(board[x]['position_xy'],[2,0]))) # w2
        result10 = list(map(sum,zip(board[x]['position_xy'],[-2,0]))) # e2
        
        n,s,w,e,nw,sw,ne,se,w2,e2 = True,True,True,True,True,True,True,True,True,True
        black_king_moves = []
        black_king_castle_kingside = ''
        black_king_castle_queenside = ''
        if self.is_legal(result1):
            new1 = change[result1[0]] + change1[result1[1]]
        else: n = False
        
        if self.is_legal(result2):
            new2 = change[result2[0]] + change1[result2[1]]
        else: s = False
        
        if self.is_legal(result3):
            new3 = change[result3[0]] + change1[result3[1]]
        else: w = False
        
        if self.is_legal(result4):
            new4 = change[result4[0]] + change1[result4[1]]
        else: e = False
        
        if self.is_legal(result5):
            new5 = change[result5[0]] + change1[result5[1]]
        else: nw = False
        
        if self.is_legal(result6):
            new6 = change[result6[0]] + change1[result6[1]]
        else: sw = False
        
        if self.is_legal(result7):
            new7 = change[result7[0]] + change1[result7[1]]
        else: ne = False
        
        if self.is_legal(result8):
            new8 = change[result8[0]] + change1[result8[1]]
        else: se = False
        
        if self.is_legal(result9):
            new9 = change[result9[0]] + change1[result9[1]]
        else: w2 = False
        
        if self.is_legal(result10):
            new10 = change[result10[0]] + change1[result10[1]]
        else: e2 = False
        
        #BLACK KING MOVES
        if n:
            if new1 not in black_king_check_if_bad:#1
                black_king_moves.append(new1)
            else:
                n = False
        
        if s:
            if new2 not in black_king_check_if_bad:#2
                black_king_moves.append(new2)
            else:
                s = False
        
        if w:
            if new3 not in black_king_check_if_bad:#3
                black_king_moves.append(new3)
            else:
                w = False
        
        if e:
            if new4 not in black_king_check_if_bad:#4
                black_king_moves.append(new4)
            else:
                e = False
        
        if nw:
            if new5 not in black_king_check_if_bad:#5
                black_king_moves.append(new5)
            else:
                nw = False
        
        if sw:
            if new6 not in black_king_check_if_bad:#6
                black_king_moves.append(new6)
            else:
                sw = False
        
        if ne:
            if new7 not in black_king_check_if_bad:#7
                black_king_moves.append(new7)
            else:
                ne = False
        if se:
            if new8 not in black_king_check_if_bad:#8
                black_king_moves.append(new8)
            else:
                se = False
                
        if w2:
            if (board['E8']['move_counter'] == 0) and (board['H8']['move_counter'] == 0) and (board['F8']['owner'] == None) and (board['G8']['owner'] == None):
                if ('E8' not in black_king_check_if_bad) or ('F8' not in black_king_check_if_bad) or ('G8' not in black_king_check_if_bad):
                    
                    black_king_castle_kingside = new9
        
        if e2:
            if (board['E8']['move_counter'] == 0) and (board['H8']['move_counter'] == 0) and (board['C8']['owner'] == None) and (board['D8']['owner'] == None):
                if 'E8' not in black_king_check_if_bad or 'C8' not in black_king_check_if_bad or 'D8' not in black_king_check_if_bad:
                    
                    black_king_castle_queenside = new10
        
        #list, string, string
        return black_king_moves, black_king_castle_kingside, black_king_castle_queenside 
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#WHITE PIECES BEGIN
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
        result = list(map(sum,zip(board[x]['position_xy'],[0,-1])))   # north x1 
        if self.is_legal(result):
            new = change[result[0]] + change1[result[1]]
        else: n = False
        
        result1 = list(map(sum,zip(board[x]['position_xy'],[1,-1])))  #north x1 west x1
        if self.is_legal(result1):
            new1 = change[result1[0]] + change1[result1[1]]
        else: nw = False
        
        result2 = list(map(sum,zip(board[x]['position_xy'],[-1,-1]))) #north x1 east x1
        if self.is_legal(result2):
            new2 = change[result2[0]] + change1[result2[1]]
        else: ne = False
        
        result3 = list(map(sum,zip(board[x]['position_xy'],[0,-2])))  #north x2
        potential = [[0,6] , [1,6] , [2,6] , [3,6] , [4,6] , [5,6] , [6,6] , [7,6]]
        if self.is_legal(result3) and (board[x]['position_xy'] in potential):
            new3 = change[result3[0]] + change1[result3[1]]
        else: n2 = False
        
        
        #WHITE PAWN MOVES
        
        #forward 1
        if n:
            if (board[new]['piece'] == None): 
                white_pawn_moves.append(new)
            else:
                n = False
            
        #forward 2
        if n2:
            if (board[new]['piece'] == None) and (board[new3]['piece'] == None):
                white_pawn_moves.append(new3)
        
        #north west capture
        if nw:
            if board[new1]['owner'] == 'black':
                white_pawn_moves.append(new1)
            else:
                nw = False
        
        #north east capture
        if ne:
            if (board[new2]['owner'] == 'black'):
                white_pawn_moves.append(new2)
            else:
                ne = False
            
        if board[new]['position_xy'] == ([0,0] or [0,1] or [0,2] or [0,3] or [0,4] or [0,5] or [0,6] or [0,7]):
            white_pawn_moves.append(new)
            print('what piece would you like to change to?')
            piece_selection = int(input("[1] - Queen\n[2] - bishop\n[3] - Knight\n: "))
            from mapping import b_pawn, b_bishop, b_knight
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
        
        if self.pinned(x,board) == False:
            pass
        else:
            for i in white_pawn_moves:
                if self.pinned(x,board)[1] == i:
                    white_pawn_moves = []
                    only_move = white_pawn_moves.append(i)
                    return only_move
                else:
                    white_pawn_moves = []
                    return white_pawn_moves
                
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
            new = change[result[0]] + change1[result[1]]
        else: a = False
        result1 = list(map(sum,zip(board[x]['position_xy'],[2,-1])))
        if self.is_legal(result1):
            new1 = change[result1[0]] + change1[result1[1]]
        else: b = False
        result2 = list(map(sum,zip(board[x]['position_xy'],[-2,1])))
        if self.is_legal(result2):
            new2 = change[result2[0]] + change1[result2[1]]
        else: c = False
        result3 = list(map(sum,zip(board[x]['position_xy'],[-2,-1])))
        if self.is_legal(result3):
            new3 = change[result3[0]] + change1[result3[1]]
        else: d = False
        result4 = list(map(sum,zip(board[x]['position_xy'],[1,-2])))
        if self.is_legal(result4):
            new4 = change[result4[0]] + change1[result4[1]]
        else: e = False
        result5 = list(map(sum,zip(board[x]['position_xy'],[-1,-2])))
        if self.is_legal(result5):
            new5 = change[result5[0]] + change1[result5[1]]
        else: f = False
        result6 = list(map(sum,zip(board[x]['position_xy'],[2,1])))
        if self.is_legal(result6):
            new6 = change[result6[0]] + change1[result6[1]]
        else: g = False
        result7 = list(map(sum,zip(board[x]['position_xy'],[2,-1])))
        if self.is_legal(result7):
            new7 = change[result7[0]] + change1[result7[1]]
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
        
        if self.pinned(x,board) == False:
            pass
        else:
            for i in white_knight_moves:
                if self.pinned(x,board)[1] == i:
                    white_knight_moves = []
                    only_move = white_knight_moves.append(i)
                    return only_move
                else:
                    white_knight_moves = []
                    return white_knight_moves
                
        return white_knight_moves
    
class white_bishop(Piece):
    def move(self, x, board):
        white_bishop_moves = []
        '''
        we will have 4 lines we are interested in y = -x, x || 
        considering where:
        x increases and y increases
        x increases and y decreases
        x decreases and y increases
        x decreases and y decreases 
        '''
        for i in range(1,7):  
            result1 = list(map(sum,zip(board[x]['position_xy'],[i,i])))
            if self.is_legal(result1):
                new1 = change[result1[0]] + change1[result1[1]]
            else: break
            
            if board[new1]['owner'] == 'black':
                white_bishop_moves.append(new1)
                break
            elif board[new1]['owner'] == None:#1
                white_bishop_moves.append(new1)
            else:
                break
            
        for i in range(1,7):
            result2= list(map(sum,zip(board[x]['position_xy'],[i,-i])))
            if self.is_legal(result2):
                new2 = change[result2[0]] + change1[result2[1]]
            else: break
            
            if board[new2]['owner'] == 'black':
                white_bishop_moves.append(new2)
                break
            elif board[new2]['owner'] == None:#1
                white_bishop_moves.append(new2)
            else:                    
                break
            
        for i in range(1,7):
            result3 = list(map(sum,zip(board[x]['position_xy'],[-i,i])))
            if self.is_legal(result3):
                new3 = change[result3[0]] + change1[result3[1]]
            else: break
            
            if board[new3]['owner'] == 'black':
                white_bishop_moves.append(new3)
                break
            elif board[new3]['owner'] == None:#1
                white_bishop_moves.append(new3)
            else:                    
                break
        
        for i in range(1,7):
            result4 = list(map(sum,zip(board[x]['position_xy'],[-i,-i])))
            if self.is_legal(result4):
                new4 = change[result4[0]] + change1[result4[1]]
            else: break
            
            if board[new4]['owner'] == 'black':
                white_bishop_moves.append(new4)
                break
            elif board[new4]['owner'] == None:#1
                white_bishop_moves.append(new4)
            else:                    
                break

        if self.pinned(x,board) == False:
            pass            
        else:
            for i in white_bishop_moves:
                if self.pinned(x,board)[1] == i:
                    white_bishop_moves = []
                    white_bishop_moves.append(i)
                    return white_bishop_moves     
                else:
                    white_bishop_moves = []
                    return white_bishop_moves
                       
        return white_bishop_moves
    
class white_rook(Piece):
    def move(self,x, board):
        white_rook_moves = []
        '''
        Need to know 4 directions
        1. North: x = x   || y = y-1
        2. South: x = x   || y = y+1
        3. West:  x = x+1 || y = y
        4. East:  x = x-1 || y = y
        '''
        for i in range(1,7):
            result1 = list(map(sum,zip(board[x]['position_xy'],[0,i])))  # s
            if self.is_legal(result1):# I am rook
                new1 = change[result1[0]] + change1[result1[1]]
            else: break
            
            if board[new1]['owner'] == 'black':
                white_rook_moves.append(new1)
                break
            elif board[new1]['owner'] == None:#1
                white_rook_moves.append(new1)
            else:                    
                break
            
        for i in range(1,7):
            result2= list(map(sum,zip(board[x]['position_xy'],[0,-i])))  # n
            if self.is_legal(result2):
                new2 = change[result2[0]] + change1[result2[1]]
            else: break
            
            if board[new2]['owner'] == 'black':
                white_rook_moves.append(new2)
                break
            elif board[new2]['owner'] == None:#1
                white_rook_moves.append(new2)
            else:                    
                break
                    
        for i in range(1,7):
            result3 = list(map(sum,zip(board[x]['position_xy'],[i,0])))  # w
            if self.is_legal(result3):
                new3 = change[result3[0]] + change1[result3[1]]
            else: break

            if board[new3]['owner'] == 'black':
                white_rook_moves.append(new3)
                break
            elif board[new3]['owner'] == None:#1
                white_rook_moves.append(new3)
            else:                    
                break
                
        for i in range(1,7):
            result4 = list(map(sum,zip(board[x]['position_xy'],[-i,0]))) # e
            if self.is_legal(result4):
                new4 = change[result4[0]] + change1[result4[1]]
            else: break

            if board[new4]['owner'] == 'black':
                white_rook_moves.append(new4)
                break
            elif board[new4]['owner'] == None:#1
                white_rook_moves.append(new4)
            else:                    
                break
        
        if self.pinned(x,board) == False:
            pass        
        else:
            for i in white_rook_moves:
                if self.pinned(x,board)[1] == i:
                    white_rook_moves = []
                    white_rook_moves.append(i)
                    return white_rook_moves
                else:
                    white_rook_moves = []
                    return white_rook_moves
        return white_rook_moves
    
class white_queen(Piece):
    
    def move(self, x, board):
        # A queen can only move as a rook and bishop can move
        wrook = white_rook()
        wbishop = white_bishop()
        white_queen_moves = wrook.move(x,board) + wbishop.move(x,board)
        
        if self.pinned(x,board) == False:
            pass
        else:
            for i in white_queen_moves:
                if self.pinned(x,board)[1] == i:
                    white_queen_moves = []
                    only_move = white_queen_moves.append(i)
                    return only_move
                else:
                    white_queen_moves = []
                    return white_queen_moves
        return white_queen_moves
        
class white_king(Piece):
    def move(self, x, board):
        white_king_check_if_bad = []
        for key in board:#A8
            #caring about instances where I go through a square that is the 
            #piece the white square is on or the square the black king is on
            if isinstance(board[key]['piece'], white_king):
                pass
            
            #adding moves black pieces could go
            elif board[key]['owner'] == 'black':
                for i in board[key]['piece'].move(key,board):
                    white_king_check_if_bad.append(i)
                #white_king_check_if_bad.append(board[key]['piece'].move(key,board))# gives me a list of moves that that piece can move
                
            #adding moves white pieces are 
            elif board[key]['owner'] == 'white':
                white_king_check_if_bad.append(key)
        
        #if king move == not in line of check and has no pieces next to it and == free to roam then it has 8 moves the king can make
        result1 = list(map(sum,zip(board[x]['position_xy'],[0,1])))  # n
        result2= list(map(sum,zip(board[x]['position_xy'],[0,-1])))  # s
        result3 = list(map(sum,zip(board[x]['position_xy'],[1,0])))  # w
        result4 = list(map(sum,zip(board[x]['position_xy'],[-1,0]))) # e
        result5 = list(map(sum,zip(board[x]['position_xy'],[1,1])))  # nw
        result6= list(map(sum,zip(board[x]['position_xy'],[1,-1])))  # sw
        result7 = list(map(sum,zip(board[x]['position_xy'],[-1,1])))  # ne
        result8 = list(map(sum,zip(board[x]['position_xy'],[-1,-1]))) # se
        result9 = list(map(sum,zip(board[x]['position_xy'],[2,0]))) # castle kingside
        result10 = list(map(sum,zip(board[x]['position_xy'],[-2,0]))) # castle queenside
        n,s,w,e,nw,sw,ne,se,e2,w2 = True,True,True,True,True,True,True,True,True,True
        white_king_moves = []
        white_king_castle_kingside = ''
        white_king_castle_queenside = ''
        
        if self.is_legal(result1):
            new1 = change[result1[0]] + change1[result1[1]]
        else: n = False
        
        if self.is_legal(result2):
            new2 = change[result2[0]] + change1[result2[1]]
        else: s = False
        
        if self.is_legal(result3):
            new3 = change[result3[0]] + change1[result3[1]]
        else: w = False
        
        if self.is_legal(result4):
            new4 = change[result4[0]] + change1[result4[1]]
        else: e = False
        
        if self.is_legal(result5):
            new5 = change[result5[0]] + change1[result5[1]]
        else: nw = False
        
        if self.is_legal(result6):
            new6 = change[result6[0]] + change1[result6[1]]
        else: sw = False
        
        if self.is_legal(result7):
            new7 = change[result7[0]] + change1[result7[1]]
        else: ne = False
        
        if self.is_legal(result8):
            new8 = change[result8[0]] + change1[result8[1]]
        else: se = False
        
        if self.is_legal(result9):
            new9 = change[result9[0]] + change1[result9[1]]
        else: se = False
        
        if self.is_legal(result10):
            new10 = change[result10[0]] + change1[result10[1]]
        else: se = False
        
        #print(new1,new2,new3,new4,new5,new6,new7,new8,new9,new10)
        
        #KING MOVES
        
        if n:
            if new1 not in white_king_check_if_bad:#1
                white_king_moves.append(new1)
            else:
                n = False
        
        if s:    
            if new2 not in white_king_check_if_bad:#2
                white_king_moves.append(new2)
            else:
                s = False
        
        if w:  
            if new3 not in white_king_check_if_bad:#3
                white_king_moves.append(new3)
            else:
                w = False
        
        if e:
            if new4 not in white_king_check_if_bad:#4
                white_king_moves.append(new4)
            else:
                e = False
                
        if nw:
            if new5 not in white_king_check_if_bad:#5
                white_king_moves.append(new5)
            else:
                nw = False
            
        if sw:
            if new6 not in white_king_check_if_bad:#6
                white_king_moves.append(new6)
            else:
                sw = False
                
        if ne:
            if new7 not in white_king_check_if_bad:#7
                white_king_moves.append(new7)
            else:
                ne = False
                
        if se:
            if new8 not in white_king_check_if_bad:#8
                white_king_moves.append(new8)
            else:
                se = False
        
        if w2:
            if (board['E1']['move_counter'] == 0) and (board['H1']['move_counter'] == 0) and (board['F1']['owner'] == None) and (board['G1']['owner'] == None):
                if 'E1' not in white_king_check_if_bad or 'F1' not in white_king_check_if_bad or 'G1' not in white_king_check_if_bad:
                    white_king_castle_kingside = new9 
                    
                    
                    
        if e2:
            if (board['E1']['move_counter'] == 0) and (board['H1']['move_counter'] == 0) and (board['C1']['owner'] == None) and (board['D1']['owner'] == None):
                if 'E1' not in white_king_check_if_bad or 'C1' not in white_king_check_if_bad or 'D1' not in white_king_check_if_bad:
                    white_king_castle_queenside = new10
        
        return white_king_moves, white_king_castle_kingside, white_king_castle_queenside #[],'',''