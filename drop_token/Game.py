from .Board import Board

class Game:
    def __init__(self, width):
        
        self.total_iteration_count = 0
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
        while self.board.put(position, self.current_player) is False:
            position = input('That position is full, choose another position -->  ')
        result = self.board.put(position, self.current_player)
        print('result is {}'.format(result))

        self.successful_puts.append(position)
        print('OK')

        if result == 'tie':
            return 'tie'
        elif result in self.players:
            return 'win'
