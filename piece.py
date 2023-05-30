from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
from board import Board
board = Board()
position = board.create_board()
coordinate = position[1]#squeares
#[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7]]
#


'''
BLACK PIECES
'''
#x213.update({position_name:{"position":position, "Color":colorSquare, "Piece":None, "position_xy":position_xy}})
b_pieces = [b_rook, b_knight, b_bishop, b_queen, b_king]
b_rook = coordinate[0] #position[0]['A8']['Piece'] = black_rook()
'''
[WHITE]
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
[BLACK
position[0]['A1']['piece'] = black_rook()
position[0]['B1']['piece'] = black_knight()
position[0]['C1']['piece'] = black_bishop()
position[0]['D1']['piece'] = black_queen()
position[0]['E1']['piece'] = black_king()
position[0]['F1']['piece'] = black_bishop()
position[0]['G1']['piece'] = black_knight()
position[0]['H1']['piece'] = black_rook()
position[0]['A2']['piece'] = black_pawn()
position[0]['B2']['piece'] = black_pawn()
position[0]['C2']['piece'] = black_pawn()
position[0]['D2']['piece'] = black_pawn()
position[0]['E2']['piece'] = black_pawn()
position[0]['F2']['piece'] = black_pawn()
position[0]['G2']['piece'] = black_pawn()
position[0]['H2']['piece'] = black_pawn()
'''
# uuid library
#position[0][0]['']
b_knight = coordinate[1]
b_bishop = coordinate[2]
b_queen = coordinate[3]
b_king = coordinate[4]
b_bishop = coordinate[5]
b_knight = coordinate[6]
b_rook = coordinate[7]
b_pawn = coordinate[8]
b_pawn = coordinate[9]
b_pawn = coordinate[10]
b_pawn = coordinate[11]
b_pawn = coordinate[12]
b_pawn = coordinate[13]
b_pawn = coordinate[14]
b_pawn = coordinate[15]
'''
WHITE PIECES
'''
w_pieces = [w_rook, w_knight, w_bishop, w_queen, w_king]
w_pawn = coordinate[48]
w_pawn = coordinate[49]
w_pawn = coordinate[50]
w_pawn = coordinate[51]
w_pawn = coordinate[52]
w_pawn = coordinate[53]
w_pawn = coordinate[54]
w_pawn = coordinate[55]
w_rook = coordinate[56]
w_knight = coordinate[57]
w_bishop = coordinate[58]
w_queen = coordinate[59]
w_king = coordinate[60]
w_bishop = coordinate[61]
w_knight = coordinate[62]
w_rook = coordinate[63]


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
        for i in w_pieces and b_pieces:
            #white or black piece standing in front
            #of pawn
            if i == list(map(sum,zip(b_pawn,[0,1]))):
                self.stop() 
                # make a function called stop 
                #that says there are no legal 
                # moves for the piece in question
            elif list(map(sum,zip(b_pawn,[0,1]))):
                result = list(map(sum,zip(b_pawn,[0,1])))
                b_pawn = result
        #capturing
        for i in w_pieces:
            
            if i == list(map(sum,zip(b_pawn,[1,1]))):
                result = list(map(sum,zip(b_pawn,[1,1])))
                b_pawn = result
            elif i == list(map(sum,zip(b_pawn,[-1,1]))):
                result = list(map(sum,zip(b_pawn,[1,1])))
                b_pawn = result
        for i in b_pieces:
            
            if i == list(map(sum,zip(b_pawn,[1,1]))):
                self.stop()
            if i == list(map(sum,zip(b_pawn,[-1,1]))):
                self.stop()
    def get_to_end(self):
        black_pawn() == black_queen()
class black_knight(Piece):
    def move(self):
        for i in b_pieces:
            
            if i == list(map(sum,zip(b_knight,[2,1]))) or self.onBoard():#1
                self.stop()
            elif i == list(map(sum,zip(b_knight,[2,-1]))) or self.onBoard():#2
                self.stop()
            elif i == list(map(sum,zip(b_knight,[-2,1]))) or self.onBoard():#3
                self.stop()
            elif i == list(map(sum,zip(b_knight,[-2,-1]))) or self.onBoard():#4
                self.stop()
            elif i == list(map(sum,zip(b_knight,[1,2]))) or self.onBoard():#5
                self.stop()
            elif i == list(map(sum,zip(b_knight,[1,-2]))) or self.onBoard():#6
                self.stop()
            elif i == list(map(sum,zip(b_knight,[-1,2]))) or self.onBoard():#7
                self.stop()
            elif i == list(map(sum,zip(b_knight,[-1,2]))) or self.onBoard():#8
                self.stop()
            else: 
                self.can_move()
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
    print(position[0]['C7']['position_xy'])
    #position[0]['A7']['position_xy'] == [1,0]
    #coordinate[1] = [1.0]
    #coordinate[1][0] = 1
if __name__ == "__main__":
    main()