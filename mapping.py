import pygame
import os


x = (20,20)
# Circles (RED,GREEN,BLUE)
blue_50 = pygame.image.load(os.path.join("blue_dot_50.png"))
blue_50 = pygame.transform.scale(blue_50, x)

blue = pygame.image.load(os.path.join("blue_dot.png"))
blue = pygame.transform.scale(blue, x)

red_50 = pygame.image.load(os.path.join("red_dot_50.png"))
red_50 = pygame.transform.scale(red_50, x)

red = pygame.image.load(os.path.join("red_dot.png"))
red = pygame.transform.scale(red, x)

green_50 = pygame.image.load(os.path.join("green_dot_50.png"))
green_50 = pygame.transform.scale(green_50, x)

green = pygame.image.load(os.path.join("green_dot.png"))
green = pygame.transform.scale(green, x)




board = pygame.image.load(os.path.join("chessBoard.png"))

b_bishop = pygame.image.load(os.path.join("black","BBishop.png"))
b_knight = pygame.image.load(os.path.join("black","BKnight.png"))
b_pawn = pygame.image.load(os.path.join("black","BPawn.png"))
b_king = pygame.image.load(os.path.join("black","BKing.png"))
b_queen = pygame.image.load(os.path.join("black","BQueen.png"))
b_rook = pygame.image.load(os.path.join("black","BRook.png"))

w_bishop = pygame.image.load(os.path.join("white","WBishop.png"))
w_knight = pygame.image.load(os.path.join("white","WKnight.png"))
w_pawn = pygame.image.load(os.path.join("white","WPawn.png"))
w_king = pygame.image.load(os.path.join("white","WKing.png"))
w_queen = pygame.image.load(os.path.join("white","WQueen.png"))
w_rook = pygame.image.load(os.path.join("white","WRook.png"))
