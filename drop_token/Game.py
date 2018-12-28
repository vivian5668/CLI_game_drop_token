from .Board import Board

class Game:
    def __init__(self, width):
        self.board = Board(width)
        self.total_iteration_count = 0
        self.players = [1, 2]
        self.current_player = 1
        self.successful_puts = []

    def get(self):
        if len(self.successful_puts) == 0:
            print("no successful puts yet")
            return
        print(self.successful_puts)

    def print_board(self):
        self.board.print_board()

    def check_wins(self):
        """
        A player wins when they have 4 tokens next to each
        other either along a row, in a column, or on a diagonal. If the board is
        filled, and nobody has won then the game is a draw. 
        """
        pass

    def put(self, position):
        while not self.board.put(position, self.current_player):
            position = input('That position is full, choose another one:  ')
        self.board.put(position, self.current_player)