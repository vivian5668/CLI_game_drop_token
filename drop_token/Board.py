class Board:
    def __init__(self, width):
        """ 
        instantiate a square board with width of int(width)
        initial available_row_index_for_position from 1 - 4 are all width - 1,
        which is the row index of the last row on the board

        when available index is 0, it means the board can't take more tokens at that position
        """
        self.board = [[0 for _ in range(width)] for _ in range(width)]
        self.available_row_index_for_positions = {position: width - 1 for position in range(1, width + 1)}

    def put(self, position, player_id):
        """
        drop a toekn at position corresponding to the labels on the board
        """
        if self.available_row_index_for_positions[position] == 0:
            return False
        available_row = self.available_row_index_for_positions[position]
        self.available_row_index_for_positions[position] -= 1
        self.board[available_row][[position - 1]] = player_id

    def print_board(self):
        print(self.board)


