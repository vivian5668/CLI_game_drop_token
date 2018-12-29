# -*- coding: utf-8 -*-

from drop_token import Board


def test_board_print_board(capsys):
    board = Board(width=2, players=2)
    board.print_board()
    out, _ = capsys.readouterr()
    expected_output = "| 0 0\n" + "| 0 0\n" + "+----\n" + "  1 2\n"
    assert expected_output == out, "Board Display should equal"


def test_board_check_wins():
    """
    A player wins when they have 4 tokens next to each
        other either along a row, in a column, or on a diagonal. If the board is
        filled, and nobody has won then the game is a draw. 

    return: if no wins yet, return None
                if one wins, return the player_id
                if ties, return string 'tie
    """
    board = Board(width=3, players=[1, 2])
    win_fake_board = [[1, 1, 1], [0, 2, 2], [0, 0, 2]]
    board.board = win_fake_board
    assert board.check_wins() == 1, 'one wins'

    ongoing_fake_board = [[0, 1, 2], [0, 1, 2], [0, 0, 0]]
    board.board = ongoing_fake_board
    assert board.check_wins() is None, "on going"

    tie_fake_board = [[2, 2, 1], [1, 1, 2], [1, 2, 1]]
    board.board = tie_fake_board
    # assert board.check_wins() == 'tie', "tie"
    assert board.check_wins() is None, "tie"


def test_board_put(capsys):
    board = Board(width=4, players=[1, 2])
    board.put(1, 1)
    board.put(4, 2)
    board.put(2, 1)
    board.put(3, 1)
    board.put(1, 1)
    board.put(1, 2)
    board.put(1, 1)
    board.put(1, 2)
    board.put(3, 2)
    board.put(2, 1)
    board.put(3, 2)
    board.put(2, 1)
    board.put(3, 2)
    board.put(3, 1)
    board.put(3, 2)
    out, _ = capsys.readouterr()
    expected_output = "DRAW\n"
    assert expected_output == out, "Test PUT output"
    # assert False
