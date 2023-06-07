import pygame
import os

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
