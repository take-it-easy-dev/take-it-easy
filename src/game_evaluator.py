import board as board_module
import game
import constants


class GameEvaluator:
    def __init__(self):
        pass

    def evaluate_failed_game(self, board: board_module.BoardRepresentation,
                             card: game.CardRepresentation) -> constants.Float:
        raise NotImplementedError("This is a base class.")

    def evaluate_successful_game(self, board: board_module.BoardRepresentation) -> constants.Float:
        raise NotImplementedError("This is a base class.")
