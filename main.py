import os
import pathlib
currentPath = pathlib.Path(__file__).parent.resolve() # Gets this python script file's current location
os.chdir(currentPath) # Sets the working directory to the current file's location

from board import Board
def main():
    newboard = Board()
    newboard.start_game()
if __name__ == "__main__":
    main()
