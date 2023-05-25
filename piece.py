from mapping import b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook
from mapping import w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook
from board import Board
board = Board()
position = board.create_board()
coordinate = position[1]
#[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7]]
#


'''
BLACK PIECES
'''

b_pieces = [b_rook, b_knight, b_bishop, b_queen, b_king]
b_rook = coordinate[0]
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
                self.can_move()
            elif i == b_knight[x+2][y-1]:#2
                self.can_move()
            elif i == b_knight[x-2][y+1]:#3
                self.can_move()
            elif i == b_knight[x-2][y-1]:#4
                self.can_move()
            elif i == b_knight[x+1][y+2]:#5
                self.can_move()
            elif i == b_knight[x+1][y-2]:#6
                self.can_move()
            elif i == b_knight[x-1][y+2]:#7
                self.can_move()
            elif i == b_knight[x-1][y-2]:#8
                self.can_move()
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
    print(coordinate[1][0])
    #coordinate[1] = [1.0]
    #coordinate[1][0] = 1
if __name__ == "__main__":
    main()