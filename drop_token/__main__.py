import sys
from .Board import Board
from .Game import Game

def main():
    game = Game(3)
    user_selection = input('type BOARD to see the board:   ')
    if user_selection == 'BOARD':
        game.print_board()

if __name__ == '__main__':
    main()

    

