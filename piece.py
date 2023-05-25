from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
from board import Board
board = Board()
position = board.create_board()
coordinate = position[1]
'''
BLACK PIECES
'''
b_pieces = [b_rook, b_knight, b_bishop, b_queen, b_king]
b_rook = [0][0]
b_knight = [1][0]
b_bishop = [2][0]
b_queen = [3][0]
b_king = [4][0]
b_bishop = [5][0]
b_knight = [6][0]
b_rook = [7][0]
b_pawn = [0][1]
b_pawn = [1][1]
b_pawn = [2][1]
b_pawn = [3][1]
b_pawn = [4][1]
b_pawn = [5][1]
b_pawn = [6][1]
b_pawn = [7][1]
'''
WHITE PIECES
'''
w_pieces = [w_rook, w_knight, w_bishop, w_queen, w_king]
w_rook = [0][7]
w_knight = [1][7]
w_bishop = [2][7]
w_queen = [3][7]
w_king = [4][7]
w_bishop = [5][7]
w_knight = [6][7]
w_rook =[7][7]
w_pawn = [0][6]
w_pawn = [1][6]
w_pawn = [2][6]
w_pawn = [3][6]
w_pawn = [4][6]
w_pawn = [5][6]
w_pawn = [6][6]
w_pawn = [7][6]
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
            if i == b_pawn[x][y-1]:
                self.self.stop() 
                # make a function called stop 
                #that says there are no legal 
                # moves for the piece in question
            elif i != b_pawn[x][y-1]:
                b_pawn[x][y-1]
        #capturing
        for i in w_pieces:
            if i == b_pawn[x+1][y+1]:
                b_pawn[x+1][y-1]
            elif i == b_pawn[x-1][y+1]:
                b_pawn[x+1,y-1]
        for i in b_pieces:
            if i == b_pawn[x+1][y+1]:
                self.stop()
            if i == b_pawn[x-1][y+1]:
                self.stop()
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
        for i in b_pieces:
            if i == b_knight[x+2][y+1]:#1
                self.stop()
            elif i == b_knight[x+2][y-1]:#2
                self.stop()
            elif i == b_knight[x-2][y+1]:#3
                self.stop()
            elif i == b_knight[x-2][y-1]:#4
                self.stop()
            elif i == b_knight[x+1][y+2]:#5
                self.stop()
            elif i == b_knight[x+1][y-2]:#6
                self.stop()
            elif i == b_knight[x-1][y+2]:#7
                self.stop()
            elif i == b_knight[x-1][y-2]:#8
                self.stop()
        for i in w_pieces or not w_pieces: #square empty means there is no piece on that square
            if i == b_knight[x+2][y+1]:#1
                can_move()
            elif i == b_knight[x+2][y-1]:#2
                can_move()
            elif i == b_knight[x-2][y+1]:#3
                can_move()
            elif i == b_knight[x-2][y-1]:#4
                can_move()
            elif i == b_knight[x+1][y+2]:#5
                can_move()
            elif i == b_knight[x+1][y-2]:#6
                can_move()
            elif i == b_knight[x-1][y+2]:#7
                can_move()
            elif i == b_knight[x-1][y-2]:#8
                can_move()
        # make it so a knight can't jump off the board
        
        if b_knight[x+2][y+1] != onBoard:#1
            self.stop()
        elif b_knight[x+2][y-1] != onBoard:#2
            self.stop()
        elif b_knight[x-2][y+1] != onBoard:#3
            self.stop()
        elif b_knight[x-2][y-1] != onBoard:#4
            self.stop()
        elif b_knight[x+1][y+2] != onBoard:#5
            self.stop()
        elif b_knight[x+1][y-2] != onBoard:#6
            self.stop()
        elif b_knight[x-1][y+2] != onBoard:#7
            self.stop()
        elif b_knight[x-1][y-2] != onBoard:#8
            self.stop()
class black_bishop(Piece):
    def move(self):
        for i in b_pieces:
            ###########################1
            if i == b_bishop[x+1][y+1]:
                self.stop()
            if i == b_bishop[x+1][y-1]:
                self.stop()
            if i == b_bishop[x-1][y+1]:
                self.stop()
            if i == b_bishop[x-1][y-1]:
                self.stop()
            ############################2
            if i == b_bishop[x+2][y+2]:
                #check 1 less than 2
                pass
            if i == b_bishop[x+2][y-2]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-2][y+2]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-2][y-2]:
                #check 1 less than 2
                pass
            ############################3
            if i == b_bishop[x+3][y+3]:
                #check 1 less than 2
                pass
            if i == b_bishop[x+3][y-3]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-3][y+3]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-3][y-3]:
                #check 1 less than 2
                pass
            ###########################4
            if i == b_bishop[x+4][y+4]:
                #check 1 less than 2
                pass
            if i == b_bishop[x+4][y-4]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-4][y+4]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-4][y-4]:
                #check 1 less than 2
                pass
            ###########################5
            if i == b_bishop[x+5][y+5]:
                #check 1 less than 2
                pass
            if i == b_bishop[x+5][y-5]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-5][y+5]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-5][y-5]:
                #check 1 less than 2
                pass
            ##############################6
            if i == b_bishop[x+6][y+6]:
                #check 1 less than 2
                pass
            if i == b_bishop[x+6][y-6]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-6][y+6]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-6][y-6]:
                #check 1 less than 2
                pass
            #############################7
            if i == b_bishop[x+7][y+7]:
                #check 1 less than 2
                pass
            if i == b_bishop[x+7][y-7]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-7][y+7]:
                #check 1 less than 2
                pass
            if i == b_bishop[x-7][y-7]:
                #check 1 less than 2
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
class black_king(black_pawn):
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