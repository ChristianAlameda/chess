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
        # get off the square they start on unless they are blocked
        pass
    
    def move1(self, x, board):
        pass
    
    def move2(self, x, board):
        pass

    def pinned(self, x, board):
        """
        Given a square 'x' and a chessboard 'board' with its pieces,
        this method removes a piece from the game and checks if an opposing piece can attack the king.
        """
        sking = super_king()

        piece_owner = board[x]['owner']

        def check_direction(direction_line, opponent_pieces):
            for index, value in enumerate(direction_line):
                curr = 0
                temp = []
                for i in range(0, index):
                    if board[direction_line[i]]['piece'] is not None:
                        curr += 1
                        temp.append(direction_line[i])
                if curr == 1 and x in temp:
                    return True, value
            return False, None

        directions = sking.move(x, board)

        for i in range(4):  # Check for rook and queen moves | _
            if piece_owner == 'white':
                result, value = check_direction(directions[i], (black_queen, black_rook))
            else:
                result, value = check_direction(directions[i], (white_queen, white_rook))

            if result:
                return result, value

        for i in range(4, 8):  # Check for bishop moves
            if piece_owner == 'white':
                result, value = check_direction(directions[i], (black_queen, black_bishop))
            else:
                result, value = check_direction(directions[i], (white_queen, white_bishop))

            if result:
                return result, value

        return False, None


    def is_legal(self, result):
        return 0 <= result[0] <= 7 and 0 <= result[1] <= 7

    def stop(self):
        print('Can\'t move there, silly')

    def can_move(self):
        print('You may move there, sire/madam')


class super_king(Piece):
    def move(self, x, board):
        """
        Return possible moves for a super king at position 'x' on the chessboard 'board'.
        """
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        moves = []

        for direction in directions:
            possible_moves = self.get_direction_moves(x, board, direction)
            moves.append(possible_moves)

        return moves

    def get_direction_moves(self, x, board, direction):
        """
        Return possible moves in a given direction for a super king at position 'x' on the chessboard 'board'.
        """
        moves = []
        for i in range(1, 7):
            result = list(map(sum, zip(board[x]['position_xy'], [i * direction[0], i * direction[1]])))
            if self.is_legal(result):
                new_position = change[result[0]] + change1[result[1]]
                moves.append(new_position)
            else:
                break
        return moves
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
        
        #en pessant
        # inner pieces
        inner = [[1,4] , [2,4] , [3,4] , [4,4] , [5,4] , [6,4]]
        # outer pieces
        outer_left = [0,4]
        outer_right = [7,4]
        
        # looks to the left
        result = list(map(sum,zip(board[x]['position_xy'],[-1,0]))) 
        # Looks to the right
        result1 = list(map(sum,zip(board[x]['position_xy'],[1,0])))
        
        second_rank_left  = ''
        second_rank_right = ''
        
        #change to dictionary coordinates h8
        if self.is_legal(result):
            new = change[result[0]] + change1[result[1]]
            
            # grab the second rank that we are interested in (to the left)
            second_rank_left = change[result[0]] + '2'
            
            # check 4th rank left
            fourth_rank = change[result[0]] + '4'
            
        if self.is_legal(result1):
            new1 = change[result1[0]] + change1[result1[1]]
            
            # grab the second rank that we are interested in (to the right)
            second_rank_right = change[result1[0]] + '2'
            
            # check 4th rank right
            fourth_rank = change[result1[0]] + '4'

        # check if our selected pawn is in the correct rank
        if board[x]['position_xy'] in inner:
            
            # check for a black pawn whose is only on move 1 on it's counter 
            if (isinstance(board[new]['piece'], white_pawn)) and (board[second_rank_left]['move_counter'] == 1):
                # we want to add the move to get behind the black pawn
                check = list(map(sum,zip(board[x]['position_xy'],[-1,1])))
                new2 = change[check[0]] + change1[check[1]]
                
                black_pawn_moves.append(new2) #north x1 east x1
                
                is_pinned, pinned_value = self.pinned(x, board)
                if is_pinned:
                    black_pawn_moves = [pinned_value]

                return black_pawn_moves, fourth_rank
                
            if (isinstance(board[new1]['piece'], white_pawn)) and (board[second_rank_right]['move_counter'] == 1):
                # we want to add the move to get behind the black pawn
                check = list(map(sum,zip(board[x]['position_xy'],[1,1])))
                new2 = change[check[0]] + change1[check[1]]
                
                black_pawn_moves.append(new2) #north x1 east x1
                
                is_pinned, pinned_value = self.pinned(x, board)
                if is_pinned:
                    black_pawn_moves = [pinned_value]

                return black_pawn_moves, fourth_rank
        
        if board[x]['position_xy'] == outer_left:
            # check for right
            if (isinstance(board[new1]['piece'], white_pawn)) and (board[second_rank_right]['move_counter'] == 1):
                # we want to add the move to get behind the black pawn
                check = list(map(sum,zip(board[x]['position_xy'],[-1,1])))
                new2 = change[check[0]] + change1[check[1]]
                
                black_pawn_moves.append(new2) #north x1 east x1
                
                is_pinned, pinned_value = self.pinned(x, board)
                if is_pinned:
                    black_pawn_moves = [pinned_value]

                return black_pawn_moves, fourth_rank
        
        if board[x]['position_xy'] == outer_right:
            # check for left
            if (isinstance(board[new]['piece'], white_pawn)) and (board[second_rank_left]['move_counter'] == 1):
                # we want to add the move to get behind the black pawn
                check = list(map(sum,zip(board[x]['position_xy'],[-1,1])))
                new2 = change[check[0]] + change1[check[1]]
                
                black_pawn_moves.append(new2) #north x1 east x1
                
                is_pinned, pinned_value = self.pinned(x, board)
                if is_pinned:
                    black_pawn_moves = [pinned_value]

                return black_pawn_moves, fourth_rank
        
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            black_pawn_moves = [pinned_value]

        return black_pawn_moves, ''
    
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
                
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            black_knight_moves = [pinned_value]

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
        for i in range(1,8):  #sw
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
            
        for i in range(1,8):#nw
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
            
        for i in range(1,8):#se
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
            
        for i in range(1,8):#ne
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
            
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            black_bishop_moves = [pinned_value]

        return black_bishop_moves
    
class black_rook(Piece):
    def move(self, x, board):
        black_rook_moves = []
        for i in range(1,8):  
            result1 = list(map(sum,zip(board[x]['position_xy'],[0,-i])))
            if self.is_legal(result1):
                new1 = change[result1[0]] + change1[result1[1]]
            else: break
            
            if board[new1]['owner'] == 'white':
                black_rook_moves.append(new1)
                break
            elif board[new1]['owner'] == None: # 1
                black_rook_moves.append(new1)
            else:
                break
            
        for i in range(1,8):
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
            
        for i in range(1,8):
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
        
        for i in range(1,8):
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
                    
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            black_rook_moves = [pinned_value]

        return black_rook_moves
    
class black_queen(Piece):
    def move(self, x, board):
        # A queen can only move as a rook and bishop can move
        brook = black_rook()
        bbishop = black_bishop()
        black_queen_moves = brook.move(x,board) + bbishop.move(x,board)#[[],[]];;;
        
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            black_queen_moves = [pinned_value]

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
                
        #en pessant
        # inner pieces
        inner = [[1,3] , [2,3] , [3,3] , [4,3] , [5,3] , [6,3]]
        # outer pieces
        outer_left = [0,3]
        outer_right = [7,3]
        
        # looks to the left
        result = list(map(sum,zip(board[x]['position_xy'],[-1,0]))) 
        # Looks to the right
        result1 = list(map(sum,zip(board[x]['position_xy'],[1,0])))
        
        second_rank_left  = ''
        second_rank_right = ''
        
        #change to dictionary coordinates h8
        if self.is_legal(result):
            new = change[result[0]] + change1[result[1]]
            
            # grab the second rank that we are interested in (to the left)
            second_rank_left = change[result[0]] + '7'
            
            # check 5th rank left
            fourth_rank = change[result[0]] + '5'
            
        if self.is_legal(result1):
            new1 = change[result1[0]] + change1[result1[1]]
            
            # grab the second rank that we are interested in (to the right)
            second_rank_right = change[result1[0]] + '7'
            
            # check 5th rank right
            fourth_rank = change[result1[0]] + '5'

        # check if our selected pawn is in the correct rank
        if board[x]['position_xy'] in inner:
            
            # check for a black pawn whose is only on move 1 on it's counter 
            if (isinstance(board[new]['piece'], black_pawn)) and (board[second_rank_left]['move_counter'] == 1):
                # we want to add the move to get behind the black pawn
                check = list(map(sum,zip(board[x]['position_xy'],[-1,-1])))
                new2 = change[check[0]] + change1[check[1]]
                
                white_pawn_moves.append(new2) #north x1 east x1
                
                is_pinned, pinned_value = self.pinned(x, board)
                if is_pinned:
                    white_pawn_moves = [pinned_value]

                return white_pawn_moves, fourth_rank
                
                
            if (isinstance(board[new1]['piece'], black_pawn)) and (board[second_rank_right]['move_counter'] == 1):
                # we want to add the move to get behind the black pawn
                check = list(map(sum,zip(board[x]['position_xy'],[1,-1])))
                new2 = change[check[0]] + change1[check[1]]
                
                white_pawn_moves.append(new2) #north x1 east x1
                
                is_pinned, pinned_value = self.pinned(x, board)
                if is_pinned:
                    white_pawn_moves = [pinned_value]

                return white_pawn_moves, fourth_rank
        
        if board[x]['position_xy'] == outer_left:
            # check for right
            if (isinstance(board[new1]['piece'], black_pawn)) and (board[second_rank_right]['move_counter'] == 1):
                # we want to add the move to get behind the black pawn
                check = list(map(sum,zip(board[x]['position_xy'],[-1,-1])))
                new2 = change[check[0]] + change1[check[1]]
                
                white_pawn_moves.append(new2) #north x1 east x1
                
                is_pinned, pinned_value = self.pinned(x, board)
                if is_pinned:
                    white_pawn_moves = [pinned_value]

                return white_pawn_moves, fourth_rank
        
        if board[x]['position_xy'] == outer_right:
            # check for left
            if (isinstance(board[new]['piece'], black_pawn)) and (board[second_rank_left]['move_counter'] == 1):
                # we want to add the move to get behind the black pawn
                check = list(map(sum,zip(board[x]['position_xy'],[-1,-1])))
                new2 = change[check[0]] + change1[check[1]]
                
                white_pawn_moves.append(new2) #north x1 east x1
                
                is_pinned, pinned_value = self.pinned(x, board)
                if is_pinned:
                    white_pawn_moves = [pinned_value]

                return white_pawn_moves, fourth_rank
        
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            white_pawn_moves = [pinned_value]

        return white_pawn_moves, ''
    
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
        
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            white_knight_moves = [pinned_value]

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
        for i in range(1,8):  
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
            
        for i in range(1,8):
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
            
        for i in range(1,8):
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
        
        for i in range(1,8):
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

        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            white_bishop_moves = [pinned_value]

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
        
        for i in range(1,8):
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
            
        for i in range(1,8):
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
                    
        for i in range(1,8):
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
                
        for i in range(1,8):
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
        
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            white_rook_moves = [pinned_value]

        return white_rook_moves
    
class white_queen(Piece):
    
    def move(self, x, board):
        # A queen can only move as a rook and bishop can move
        wrook = white_rook()
        wbishop = white_bishop()
        white_queen_moves = wrook.move(x,board) + wbishop.move(x,board)
        
        is_pinned, pinned_value = self.pinned(x, board)
        if is_pinned:
            white_queen_moves = [pinned_value]

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