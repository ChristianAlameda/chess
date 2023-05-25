from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook


from board import Board

x = Board()
position = x.create_board()
coordinate = position[1]
b_rook = [0][0]
b_knight = [1][0]
b_bishop = [2][0]
b_queen = [3][0]
b_king = [4][0]
b_bishop = [5][0]
b_knight = [6][0]
b_rook =[7][0]

w_rook = [0][7]
w_knight = [1][7]
w_bishop = [2][7]
w_queen = [3][7]
w_king = [4][7]
w_bishop = [5][7]
w_knight = [6][7]
w_rook =[7][7]
class Piece:
    def __init__(self):
        pass
    def move(self):
        # get off of the square they start on unless they are blocked
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class black_pawn(Piece):
    # Spaghetti Code For Now
    def move(self):
        pawn_position[x][y-1]
        pass
    def capture(self):
        pawn_position[x-1][y-1] or pawn_position[x+1,y-1]
        pass
    def check_illegal_move(self):
        '''
        if black piece in front of pawn then 
        can't move unless capture is allowed
        '''
        pass
    def get_to_end(self):
        pass
class black_knight(Piece):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class black_bishop(Piece):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class black_queen(Piece):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
class black_king(Piece):
    def move(self):
        pass
    def capture(self):
        pass
    def check_illegal_move(self):
        pass
    
'''
fasdfads

adfadfa

asdfadsf
'''
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

if __name__=="__main__":
    Piece()