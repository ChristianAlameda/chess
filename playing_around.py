from mapping import board
import pygames
def main():
    x = 1000
    y = 1000
    background = pygames.display.set_mode((x, y))
    image = mapping.board
    picture_of_board = background.blit(image, (150, 100))

if __name__ == "__main__":
    main()