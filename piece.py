from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
from board import Board
board = Board()
position = board.create_board()
coordinate = position[1]#squeares
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

'''
BLACK PIECES
'''
#x213.update({position_name:{"position":position, "Color":colorSquare, "Piece":None, "position_xy":position_xy}})
#[Black]
#Moveset of the piece
position[0]['A8']['piece'] = black_rook()
position[0]['B8']['piece'] = black_knight()
position[0]['C8']['piece'] = black_bishop()
position[0]['D8']['piece'] = black_queen()
position[0]['E8']['piece'] = black_king()
position[0]['F8']['piece'] = black_bishop()
position[0]['G8']['piece'] = black_knight()
position[0]['H8']['piece'] = black_rook()
position[0]['A7']['piece'] = black_pawn()
position[0]['B7']['piece'] = black_pawn()
position[0]['C7']['piece'] = black_pawn()
position[0]['D7']['piece'] = black_pawn()
position[0]['E7']['piece'] = black_pawn()
position[0]['F7']['piece'] = black_pawn()
position[0]['G7']['piece'] = black_pawn()
position[0]['H7']['piece'] = black_pawn()
# Picture of the Piece
position[0]['A8']['picture'] = b_rook
position[0]['B8']['picture'] = b_knight
position[0]['C8']['picture'] = b_bishop
position[0]['D8']['picture'] = b_queen
position[0]['E8']['picture'] = b_king
position[0]['F8']['picture'] = b_bishop
position[0]['G8']['picture'] = b_knight
position[0]['H8']['picture'] = b_rook
position[0]['A7']['picture'] = b_pawn
position[0]['B7']['picture'] = b_pawn
position[0]['C7']['picture'] = b_pawn
position[0]['D7']['picture'] = b_pawn
position[0]['E7']['picture'] = b_pawn
position[0]['F7']['picture'] = b_pawn
position[0]['G7']['picture'] = b_pawn
position[0]['H7']['picture'] = b_pawn
#Owner of the piece
position[0]['A8']['owner'] = 'black'
position[0]['B8']['owner'] = 'black'
position[0]['C8']['owner'] = 'black'
position[0]['D8']['owner'] = 'black'
position[0]['E8']['owner'] = 'black'
position[0]['F8']['owner'] = 'black'
position[0]['G8']['owner'] = 'black'
position[0]['H8']['owner'] = 'black'
position[0]['A7']['owner'] = 'black'
position[0]['B7']['owner'] = 'black'
position[0]['C7']['owner'] = 'black'
position[0]['D7']['owner'] = 'black'
position[0]['E7']['owner'] = 'black'
position[0]['F7']['owner'] = 'black'
position[0]['G7']['owner'] = 'black'
position[0]['H7']['owner'] = 'black'

#[WHITE]
#moveset of the piece
position[0]['A1']['piece'] = white_rook()
position[0]['B1']['piece'] = white_knight()
position[0]['C1']['piece'] = white_bishop()
position[0]['D1']['piece'] = white_queen()
position[0]['E1']['piece'] = white_king()
position[0]['F1']['piece'] = white_bishop()
position[0]['G1']['piece'] = white_knight()
position[0]['H1']['piece'] = white_rook()
position[0]['A2']['piece'] = white_pawn()
position[0]['B2']['piece'] = white_pawn()
position[0]['C2']['piece'] = white_pawn()
position[0]['D2']['piece'] = white_pawn()
position[0]['E2']['piece'] = white_pawn()
position[0]['F2']['piece'] = white_pawn()
position[0]['G2']['piece'] = white_pawn()
position[0]['H2']['piece'] = white_pawn()
# Picture of the Piece
position[0]['A1']['picture'] = w_rook
position[0]['B1']['picture'] = w_knight
position[0]['C1']['picture'] = w_bishop
position[0]['D1']['picture'] = w_queen
position[0]['E1']['picture'] = w_king
position[0]['F1']['picture'] = w_bishop
position[0]['G1']['picture'] = w_knight
position[0]['H1']['picture'] = w_rook
position[0]['A2']['picture'] = w_pawn
position[0]['B2']['picture'] = w_pawn
position[0]['C2']['picture'] = w_pawn
position[0]['D2']['picture'] = w_pawn
position[0]['E2']['picture'] = w_pawn
position[0]['F2']['picture'] = w_pawn
position[0]['G2']['picture'] = w_pawn
position[0]['H2']['picture'] = w_pawn
#owner of the piece
position[0]['A1']['owner'] = 'white'
position[0]['B1']['owner'] = 'white'
position[0]['C1']['owner'] = 'white'
position[0]['D1']['owner'] = 'white'
position[0]['E1']['owner'] = 'white'
position[0]['F1']['owner'] = 'white'
position[0]['G1']['owner'] = 'white'
position[0]['H1']['owner'] = 'white'
position[0]['A2']['owner'] = 'white'
position[0]['B2']['owner'] = 'white'
position[0]['C2']['owner'] = 'white'
position[0]['D2']['owner'] = 'white'
position[0]['E2']['owner'] = 'white'
position[0]['F2']['owner'] = 'white'
position[0]['G2']['owner'] = 'white'
position[0]['H2']['owner'] = 'white'


class Piece:
    def __init__(self):
        pass
    def move(self):
        # get off of the square they start on unless they are blocked
        pass
    def capture(self):
        #can only capture the opposite color
        '''
        for piece in black_pieces:
            if piece == capturable():
                if checkColor() == ownColor:
                    noCapture()
        for piece in white_pieces:
            if piece == capturable():
                if checkColor() == ownColor:
                    noCapture()
        '''
        
    def onBoard(self, new: str):
        # when pressed A8 C6
        if new in position[0]:
            return True
        else: return False
            
                
                
        
        
            
    def stop(self):
        print('cant move there silly')
    def can_move(self):
        print('you may move there sire/madam')
class black_pawn(Piece):
    # Spaghetti Code For Now
    def move(self):
        #Normal movement
        #if touched 
        s = True
        sw = True
        se = True
        #white or black piece standing in front
        #of pawn
        #x is square pressed
        result = list(map(sum,zip(position[0][x]['postion_xy'],[0,1])))
        new = [change[result[0]] + str(result[1])]
        #forward
        if (position[0][new]['piece'] is None) and (self.onBoard() is True) and (s is True): # x is what square is pressed on
            # x is what square is pressed on
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new]['piece'] = black_pawn()
            position[0][new]['owner'] = 'black'
        elif not ((position[0][new]['piece'] is None) and (self.onBoard() is True) and (s is True)):
            s = False
        #capturing sw
        result = list(map(sum,zip(position[0][x]['postion_xy'],[1,1])))
        new = [change[result[0]] + str(result[1])]
        #capturing se
        result1 = list(map(sum,zip(position[0][x]['postion_xy'],[0,1])))
        new1 = [change[result[0]] + str(result1[1])]
        if position[0][new]['piece'] is 'white' and sw == True:
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new]['piece'] = black_pawn()
            position[0][new]['owner'] = 'black'
        elif not (position[0][new]['piece'] is 'white' and sw == True):
            sw = False
        if position[0][new1]['piece'] is 'white' and se == True:
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new]['piece'] = black_pawn()
            position[0][new]['owner'] = 'black'
        elif not (position[0][new1]['piece'] is 'white' and se == True):
            se = False
    def get_to_end(self):
        black_pawn() == black_queen()
class black_knight(Piece):
    def move(self):
        # x is whatever get's passed to us through the board pressing
        result = list(map(sum,zip(position[0][x]['postion_xy'],[2,1])))
        new = [change[result[0]] + str(result[1])]
        result1 = list(map(sum,zip(position[0][x]['postion_xy'],[2,1])))
        new1 = [change[result1[0]] + str(result1[1])]
        result2 = list(map(sum,zip(position[0][x]['postion_xy'],[2,1])))
        new2 = [change[result2[0]] + str(result2[1])]
        result3 = list(map(sum,zip(position[0][x]['postion_xy'],[2,1])))
        new3 = [change[result3[0]] + str(result3[1])]
        result4 = list(map(sum,zip(position[0][x]['postion_xy'],[2,1])))
        new4 = [change[result4[0]] + str(result4[1])]
        result5 = list(map(sum,zip(position[0][x]['postion_xy'],[2,1])))
        new5 = [change[result5[0]] + str(result5[1])]
        result6 = list(map(sum,zip(position[0][x]['postion_xy'],[2,1])))
        new6 = [change[result6[0]] + str(result6[1])]
        result7 = list(map(sum,zip(position[0][x]['postion_xy'],[2,1])))
        new7 = [change[result7[0]] + str(result7[1])]



        a = True
        b = True
        c = True
        d = True
        e = True
        f = True
        g = True
        h = True
        if (position[0][new]['owner'] == 'white' or position[0][new]['owner'] == None) and self.onBoard() and a:#1
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new]['piece'] = black_knight()
            position[0][new]['owner'] = 'black'
        elif not ((position[0][new]['owner'] == 'white' or position[0][new]['owner'] == None) and self.onBoard() and a):
            self.stop()
            a = False
        if (position[0][new1]['owner'] == 'white' or position[0][new1]['owner'] == None) and self.onBoard() and b:#2
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new1]['piece'] = black_knight()
            position[0][new1]['owner'] = 'black'
        elif not ((position[0][new1]['owner'] == 'white' or position[0][new1]['owner'] == None) and self.onBoard() and b):
            self.stop()
            a = False
        if (position[0][new2]['owner'] == 'white' or position[0][new2]['owner'] == None) and self.onBoard() and b:#3
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new2]['piece'] = black_knight()
            position[0][new2]['owner'] = 'black'
        elif not ((position[0][new2]['owner'] == 'white' or position[0][new2]['owner'] == None) and self.onBoard() and c):
            self.stop()
            a = False
        if (position[0][new3]['owner'] == 'white' or position[0][new3]['owner'] == None) and self.onBoard() and d:#4
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new3]['piece'] = black_knight()
            position[0][new3]['owner'] = 'black'
        elif not ((position[0][new3]['owner'] == 'white' or position[0][new3]['owner'] == None) and self.onBoard() and d):
            self.stop()
            a = False
        if (position[0][new4]['owner'] == 'white' or position[0][new4]['owner'] == None) and self.onBoard() and e:#5
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new4]['piece'] = black_knight()
            position[0][new4]['owner'] = 'black'
        elif not ((position[0][new4]['owner'] == 'white' or position[0][new4]['owner'] == None) and self.onBoard() and e):
            self.stop()
            a = False
        if (position[0][new5]['owner'] == 'white' or position[0][new5]['owner'] == None) and self.onBoard() and f:#6
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new5]['piece'] = black_knight()
            position[0][new5]['owner'] = 'black'
        elif not ((position[0][new5]['owner'] == 'white' or position[0][new5]['owner'] == None) and self.onBoard() and f):
            self.stop()
            a = False
        if (position[0][new6]['owner'] == 'white' or position[0][new6]['owner'] == None) and self.onBoard() and g:#7
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new6]['piece'] = black_knight()
            position[0][new6]['owner'] = 'black'
        elif not ((position[0][new6]['owner'] == 'white' or position[0][new6]['owner'] == None) and self.onBoard() and g):
            self.stop()
            a = False
        if (position[0][new7]['owner'] == 'white' or position[0][new7]['owner'] == None) and self.onBoard() and h:#8
            position[0][x]['piece'] = None
            position[0][x]['owner'] = None
            position[0][new7]['piece'] = black_knight()
            position[0][new7]['owner'] = 'black'
        elif not ((position[0][new7]['owner'] == 'white' or position[0][new7]['owner'] == None) and self.onBoard() and h):
            self.stop()
            a = False
class black_bishop(Piece):
    def show_self(self):
        #b_bishop
        pass
        
    def move(self):
        bbishop_moves = []
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
            result1 = list(map(sum,zip(position[0][x]['postion_xy'],[i,i])))
            result2= list(map(sum,zip(position[0][x]['postion_xy'],[i,-i])))
            result3 = list(map(sum,zip(position[0][x]['postion_xy'],[-i,i])))
            result4 = list(map(sum,zip(position[0][x]['postion_xy'],[-i,-i])))
            new1 = [change[result1[0]] + str(result1[1])]
            new2 = [change[result2[0]] + str(result2[1])]
            new3 = [change[result3[0]] + str(result3[1])]
            new4 = [change[result4[0]] + str(result4[1])]
            if (position[0][new1]['owner'] == 'white' or position[0][new1]['owner'] == None) and self.onBoard(new1) and nw:#1
                position[0][x]['piece'] = None
                position[0][x]['owner'] = None
                position[0][new1]['piece'] = black_knight()
                position[0][new1]['owner'] = 'black'
                bbishop_moves.append(new1)
            elif not ((position[0][new1]['owner'] == 'white' or position[0][new1]['owner'] == None) and self.onBoard(new1) and nw):
                self.stop()
                nw = False
            if (position[0][new2]['owner'] == 'white' or position[0][new2]['owner'] == None) and self.onBoard(new2) and nw:#2
                position[0][x]['piece'] = None
                position[0][x]['owner'] = None
                position[0][new2]['piece'] = black_knight()
                position[0][new2]['owner'] = 'black'
                bbishop_moves.append(new2)
            elif not ((position[0][new2]['owner'] == 'white' or position[0][new2]['owner'] == None) and self.onBoard(new2) and nw):
                self.stop()
                nw = False
            if (position[0][new3]['owner'] == 'white' or position[0][new3]['owner'] == None) and self.onBoard(new3) and nw:#3
                position[0][x]['piece'] = None
                position[0][x]['owner'] = None
                position[0][new3]['piece'] = black_knight()
                position[0][new3]['owner'] = 'black'
                bbishop_moves.append(new3)
            elif not ((position[0][new3]['owner'] == 'white' or position[0][new3]['owner'] == None) and self.onBoard(new3) and nw):
                self.stop()
                nw = False
            if (position[0][new4]['owner'] == 'white' or position[0][new4]['owner'] == None) and self.onBoard(new4) and nw:#4
                position[0][x]['piece'] = None
                position[0][x]['owner'] = None
                position[0][new4]['piece'] = black_knight()
                position[0][new4]['owner'] = 'black'
                bbishop_moves.append(new4)
            elif not ((position[0][new4]['owner'] == 'white' or position[0][new4]['owner'] == None) and self.onBoard(new4) and nw):
                self.stop()
                nw = False
class black_rook(Piece):
    def move(self):
        brook_moves = []
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
            result1 = list(map(sum,zip(position[0][x]['postion_xy'],[0,i])))  # n
            result2= list(map(sum,zip(position[0][x]['postion_xy'],[0,-i])))  # s
            result3 = list(map(sum,zip(position[0][x]['postion_xy'],[i,0])))  # w
            result4 = list(map(sum,zip(position[0][x]['postion_xy'],[-i,0]))) # e
            new1 = [change[result1[0]] + str(result1[1])]
            new2 = [change[result2[0]] + str(result2[1])]
            new3 = [change[result3[0]] + str(result3[1])]
            new4 = [change[result4[0]] + str(result4[1])]
            if (position[0][new1]['owner'] == 'white' or position[0][new1]['owner'] == None) and self.onBoard(new1) and n:#1
                position[0][x]['piece'] = None
                position[0][x]['owner'] = None
                position[0][new1]['piece'] = black_rook()
                position[0][new1]['owner'] = 'black'
                brook_moves.append(new1)
            elif not ((position[0][new1]['owner'] == 'white' or position[0][new3]['owner'] == None) and self.onBoard(new3) and n):
                self.stop()
                n = False
            if (position[0][new2]['owner'] == 'white' or position[0][new2]['owner'] == None) and self.onBoard(new2) and s:#2
                position[0][x]['piece'] = None
                position[0][x]['owner'] = None
                position[0][new2]['piece'] = black_rook()
                position[0][new2]['owner'] = 'black'
                brook_moves.append(new2)
            elif not ((position[0][new2]['owner'] == 'white' or position[0][new2]['owner'] == None) and self.onBoard(new2) and s):
                self.stop()
                s = False
            if (position[0][new3]['owner'] == 'white' or position[0][new3]['owner'] == None) and self.onBoard(new3) and w:#3
                position[0][x]['piece'] = None
                position[0][x]['owner'] = None
                position[0][new3]['piece'] = black_rook()
                position[0][new3]['owner'] = 'black'
                brook_moves.append(new3)
            elif not ((position[0][new4]['owner'] == 'white' or position[0][new4]['owner'] == None) and self.onBoard(new4) and w):
                self.stop()
                w = False
            if (position[0][new4]['owner'] == 'white' or position[0][new4]['owner'] == None) and self.onBoard(new4) and e:#4
                position[0][x]['piece'] = None
                position[0][x]['owner'] = None
                position[0][new4]['piece'] = black_rook()
                position[0][new4]['owner'] = 'black'
                brook_moves.append(new4)
            elif not ((position[0][new4]['owner'] == 'white' or position[0][new4]['owner'] == None) and self.onBoard(new4) and e):
                self.stop()
                e = False
            
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class black_queen():
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class black_king(black_pawn):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
    

class white_pawn(Piece):
    def black_move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class white_knight(Piece):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class white_bishop(Piece):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class white_queen(Piece):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class white_king(Piece):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass


def main():
    print(position[0]['F4']['position_xy'])
    #position[0]['A7']['position_xy'] == [1,0]
    #coordinate[1] = [1.0]
    #coordinate[1][0] = 1
if __name__ == "__main__":
    main()