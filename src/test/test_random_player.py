import random_player
import board as board_module
import game as game_module


def test_random_player():
    player = random_player.RandomPlayer()
    dummy_board = board_module.create_blank_board()
    dummy_card = (0, 0, 0)
    random_field_indices = [player.find_move(dummy_board, dummy_card) for _ in
                            range(board_module.NUMBER_OF_FIELDS)]
    for field_index in range(board_module.NUMBER_OF_FIELDS):
        assert field_index in random_field_indices, f"random_field_indices:\n{random_field_indices}."
