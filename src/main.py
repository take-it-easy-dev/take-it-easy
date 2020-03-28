from visualization.vizualization import visualize_board
import game_manager as game_manager_module
import random_player as random_player_module
import dummy_evaluator as dummy_evaluator_module

player = random_player_module.RandomPlayer()
game_evaluator = dummy_evaluator_module.DummyEvaluator()
game_manager = game_manager_module.GameManager(player, game_evaluator)

success, score = game_manager.play_one_game()

visualize_board(game_manager.current_game.board, card=game_manager.current_card)




