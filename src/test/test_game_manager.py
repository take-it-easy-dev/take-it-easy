import dummy_evaluator
import random_player
import game_manager as game_manager_module
import board as board_module


def test_dummy_game():
    for _ in range(100):
        player = random_player.RandomPlayer()
        evaluator = dummy_evaluator.DummyEvaluator()
        game_manager = game_manager_module.GameManager(player, evaluator)
        success, score = game_manager.play_one_game()
        assert success
        game = game_manager.current_game
        board_module.assert_board_validity(game.board)
        assert board_module.is_board_complete(game.board)

