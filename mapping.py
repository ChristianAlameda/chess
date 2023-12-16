import pygame
import os


x = (10,10) #20,20
# CIRCLES (RED,GREEN,BLUE)
blue_50 = pygame.image.load(os.path.join("dots","blue_dot_50.png"))
blue_50 = pygame.transform.scale(blue_50, x)

blue = pygame.image.load(os.path.join("dots","blue_dot.png"))
blue = pygame.transform.scale(blue, x)

red_50 = pygame.image.load(os.path.join("dots","red_dot_50.png"))
red_50 = pygame.transform.scale(red_50, x)

red = pygame.image.load(os.path.join("dots","red_dot.png"))
red = pygame.transform.scale(red, x)

green_50 = pygame.image.load(os.path.join("dots","green_dot_50.png"))
green_50 = pygame.transform.scale(green_50, x)

green = pygame.image.load(os.path.join("dots","green_dot.png"))
green = pygame.transform.scale(green, x)


boardSize = (500,500)
#BOARD
board = pygame.image.load(os.path.join("chessBoard.png"))
board = pygame.transform.scale(board, boardSize) #just added

pieceSize = (40,40)
#BLACK PIECES
b_bishop = pygame.image.load(os.path.join("black","b_bishop.png"))
b_knight = pygame.image.load(os.path.join("black","b_knight.png"))
b_pawn   = pygame.image.load(os.path.join("black","b_pawn.png"))
b_king   = pygame.image.load(os.path.join("black","b_king.png"))
b_queen  = pygame.image.load(os.path.join("black","b_queen.png"))
b_rook   = pygame.image.load(os.path.join("black","b_rook.png"))

b_bishop = pygame.transform.scale(b_bishop, pieceSize)
b_knight = pygame.transform.scale(b_knight, pieceSize)
b_pawn   = pygame.transform.scale(b_pawn,   pieceSize)
b_king   = pygame.transform.scale(b_king,   pieceSize)
b_queen  = pygame.transform.scale(b_queen,  pieceSize)
b_rook   = pygame.transform.scale(b_rook,   pieceSize)


#WHITE PIECES
w_bishop = pygame.image.load(os.path.join("white","w_bishop.png"))
w_knight = pygame.image.load(os.path.join("white","w_knight.png"))
w_pawn = pygame.image.load(os.path.join("white","w_pawn.png"))
w_king = pygame.image.load(os.path.join("white","w_king.png"))
w_queen = pygame.image.load(os.path.join("white","w_queen.png"))
w_rook = pygame.image.load(os.path.join("white","w_rook.png"))

w_bishop = pygame.transform.scale(w_bishop, pieceSize)
w_knight = pygame.transform.scale(w_knight, pieceSize)
w_pawn   = pygame.transform.scale(w_pawn,   pieceSize)
w_king   = pygame.transform.scale(w_king,   pieceSize)
w_queen  = pygame.transform.scale(w_queen,  pieceSize)
w_rook   = pygame.transform.scale(w_rook,   pieceSize)