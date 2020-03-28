import board as board_module
# import pytest


def test_empty_board():
    board = board_module.create_blank_board()
    board_module.assert_board_validity(board)


