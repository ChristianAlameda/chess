import pygame
import os


x = (20,20)
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



#BOARD
board = pygame.image.load(os.path.join("chessBoard.png"))

#BLACK PIECES
b_bishop = pygame.image.load(os.path.join("black","b_bishop.png"))
b_knight = pygame.image.load(os.path.join("black","b_knight.png"))
b_pawn = pygame.image.load(os.path.join("black","b_pawn.png"))
b_king = pygame.image.load(os.path.join("black","b_king.png"))
b_queen = pygame.image.load(os.path.join("black","b_queen.png"))
b_rook = pygame.image.load(os.path.join("black","b_rook.png"))

#WHITE PIECES
w_bishop = pygame.image.load(os.path.join("white","w_bishop.png"))
w_knight = pygame.image.load(os.path.join("white","w_knight.png"))
w_pawn = pygame.image.load(os.path.join("white","w_pawn.png"))
w_king = pygame.image.load(os.path.join("white","w_king.png"))
w_queen = pygame.image.load(os.path.join("white","w_queen.png"))
w_rook = pygame.image.load(os.path.join("white","w_rook.png"))
