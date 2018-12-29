# -*- coding: utf-8 -*-

from .board import Board


class Game:
    def __init__(self, width):
        self.width = width
        self.total_iteration_count = 1
        self.players = [1, 2]
        self.board = Board(width, self.players)
        self.current_player = 1
        self.successful_puts = []

    def get(self):
        if len(self.successful_puts) == 0:
            print("no successful puts yet")
            return
        for position in self.successful_puts:
            print(position)

    def print_board(self):
        self.board.print_board()

    def check_wins(self):
        """
        A player wins when they have 4 tokens next to each
        other either along a row, in a column, or on a diagonal. If the board is
        filled, and nobody has won then the game is a draw. 

        return: if no wins yet, return None
                if one wins, return the player_id
                if ties, return string 'tie'
        """
        return self.board.check_wins()

    def put(self, position):
        """
        place the current player's piece on the board
        """
        if not position.isdigit():
            print('Position has to be a valid number')
            return 
        position = int(position)
        if position < 0 or position > self.width:
            print('Position has to be smaller than board width')
            return
        if self.board.available_row_index_for_positions[position] < 0:
            print('ERROR')
            return
        self.total_iteration_count += 1
        self.current_player = self.players[self.total_iteration_count % 2]
        self.board.put(position, self.current_player)

        print('OK')
        self.successful_puts.append(position)
