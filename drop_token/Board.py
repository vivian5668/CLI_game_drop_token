class Board:
    def __init__(self, width, players):
        """ 
        instantiate a square board with width of int(width)
        initial available_row_index_for_position from 1 - 4 are all width - 1,
        which is the row index of the last row on the board

        when available index is 0, it means the board can't take more tokens at that position
        """
        self.board = [[0 for _ in range(width)] for _ in range(width)]
        self.available_row_index_for_positions = {position: width - 1 for position in range(1, width + 1)}
        self.width = width
        self.players = players # players is a list of IDs, i.e, [1, 2]

    def put(self, position, player_id):
        """
        drop a toekn at position corresponding to the labels on the board
        """
        print('position, player_id')
        print(position, player_id)
        print('available row index at each position')
        print(self.available_row_index_for_positions)
        if self.available_row_index_for_positions[position] == 0:
            return False
        available_row = self.available_row_index_for_positions[position]
        self.board[available_row][position - 1] = player_id

        # update available_row_index_for_positions for future rounds
        self.available_row_index_for_positions[position] -= 1
        print('here')
        current_result = self.check_wins()
        if current_result is None:
            return
        elif current_result in self.players:
            print('{} wins!'.format(current_result))
        else:
            print('This is a tie! Your game has ended')
            return 'tie'

    def print_board(self):
        board = "\n".join(["| " + " ".join([str(i) for i in row]) for row in self.board])
        temp = "+" + '-' * (len("| " + " ".join([str(i) for i in self.board[0]])) - 1)
        board += '\n' + temp
        board += "\n  " + " ".join([str(x) for x in range(1, self.width + 1)])
        print(board)

    def check_wins(self):
        """
        A player wins when they have 4 tokens next to each
        other either along a row, in a column, or on a diagonal. If the board is
        filled, and nobody has won then the game is a draw. 

        return: if no wins yet, return None
                if one wins, return the player_id
                if ties, return string 'tie'
        """
        # check wins horizontal levels
        for row in self.board:
            for player_id in self.players:
                if sum(row) == player_id * 3:
                    return player_id
        # check wins vertical levels
        for player_id in self.players:
            for i in range(self.width):
                column_sum = 0
                for j in range(self.width):
                    column_sum += self.board[j][i]
                if column_sum == player_id * 3:
                    return player_id

        # diagonal levels
        diagonal_sum = 0
        for i in range(self.width):
            diagonal_sum += self.board[i][i]
            
            


        


        


