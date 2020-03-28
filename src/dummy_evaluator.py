from game_evaluator import GameEvaluator
import constants
import board as board_module
import game as game_module


class DummyEvaluator(GameEvaluator):
    def __init__(self):
        super(DummyEvaluator, self).__init__()

    def evaluate_failed_game(self, board: board_module.BoardRepresentation,
                             card: game_module.CardRepresentation) -> constants.Float:
        return constants.Float(0.)

    def evaluate_successful_game(self, board: board_module.BoardRepresentation) -> constants.Float:
        return constants.Float(0.)
