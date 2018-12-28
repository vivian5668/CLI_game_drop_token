import sys
from .Board import Board
from .Game import Game

def main():
    while True:
        game_width = input("Please specify board size 2-9: ")
        try:
            if 2 <= int(game_width) <= 9:
                break
        except:
            continue
    game = Game(int(game_width))
    
    while True:
        user_selection = input('type a command choosing from: BOARD, PUT, GET, HELP, EXIT ---> ')
        if user_selection == 'BOARD':
            game.print_board()
            continue
        elif user_selection[:3] == 'PUT':
            put_position = int(user_selection[3:].strip())
            result = game.put(put_position)

            # if result == 'tie' or result == 'win':
            #     break
            continue
        elif user_selection == 'GET':
            game.get()
            continue
        elif user_selection == 'EXIT':
            break
        else:
            user_input = input("This is the HELP section \n \
            ........ \n \
             Type 'q' to return to the game      ")
            if user_input == 'q':
                continue

if __name__ == '__main__':
    main()

    

