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
b_pieces = [b_rook, b_knight, b_bishop, b_queen, b_king]
b_rook = coordinate[0] #position[0]['A8']['Piece'] = black_rook()

#[Black]
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
        
    def onBoard(self):
        for i in w_pieces and b_pieces:
            for j in range(0,7):
                if i < [0,j]:
                    print("can't move off the board silly")
                    return False
                elif i < [j,0]:
                    print("can't move off the board silly")
                    return False
                elif i >[7,j]:
                    print("can't move off the board silly")
                    return False
                elif i >[j,7]:
                    print("can't move off the board silly")
                    return False
                else:
                    return True
            
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
        if position[0][new]['owner'] == 'black' or self.onBoard() or a != True:#1
            self.stop()
            a = False
        if position[0][new1]['owner'] == 'black' or self.onBoard() or a != True:#2
            self.stop()
            b = False
        if position[0][new2]['owner'] == 'black' or self.onBoard() or a != True:#3
            self.stop()
        if position[0][new3]['owner'] == 'black' or self.onBoard() or a != True:#4
            self.stop()
        if position[0][new4]['owner'] == 'black' or self.onBoard() or a != True:#5
            self.stop()
        if position[0][new5]['owner'] == 'black' or self.onBoard() or a != True:#6
            self.stop()
        if position[0][new6]['owner'] == 'black' or self.onBoard() or a != True:#7
            self.stop()
        if position[0][new7]['owner'] == 'black' or self.onBoard() or a != True:#8
            self.stop()
        '''
        for i in w_pieces: #square empty means there is no piece on that square
            if i == list(map(sum,zip(b_knight,[2,1]))) and self.onBoard():#1
                self.can_move()
            elif i == list(map(sum,zip(b_knight,[2,-1]))) and self.onBoard():#2
                self.can_move()
            elif i == list(map(sum,zip(b_knight,[-2,1]))) and self.onBoard():#3
                self.can_move()
            elif list(map(sum,zip(b_knight,[-2,-1]))) and self.onBoard():#4
                self.can_move()
            elif i == list(map(sum,zip(b_knight,[1,2]))) and self.onBoard():#5
                self.can_move()
            elif i == list(map(sum,zip(b_knight,[1,-2]))) and self.onBoard():#6
                self.can_move()
            elif i == list(map(sum,zip(b_knight,[-1,2]))) and self.onBoard():#7
                self.can_move()
            elif i == list(map(sum,zip(b_knight,[-1,2]))) and self.onBoard():#8
                self.can_move()
            else:
                self.stop()
        '''
class black_bishop(Piece):
    def move(self):
        bbishop_moves = []
        nw,ne,sw,se = True,True,True,True
        for i in range(1,7):
            for j in b_pieces:
                '''
                we will have 4 lines we are interested in y = -x, x || 
                considering where:
                x increases and y increases
                x increases and y decreases
                x decreases and y increases
                x decreases and y decreases 
                '''
                if j != list(map(sum,zip(b_knight,[i,i]))) and self.onBoard() and nw:
                    bbishop_moves.append(list(map(sum,zip(b_knight,[i,i]))))
                elif j != list(map(sum,zip(b_knight,[i,-i]))) and self.onBoard() and ne:
                    bbishop_moves.append(list(map(sum,zip(b_knight,[i,-i]))))
                elif j != list(map(sum,zip(b_knight,[-i,i]))) and self.onBoard() and sw:
                    bbishop_moves.append(list(map(sum,zip(b_knight,[-i,i])))) 
                elif j != list(map(sum,zip(b_knight,[-i,-i]))) and self.onBoard():
                    bbishop_moves.append(list(map(sum,zip(b_knight,[-i,-i]))))
                if nw:
                    pass
            
            
            
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class black_rook(Piece):
    def move(self):
        pass
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