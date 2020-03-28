from typing import Tuple

import board as board_module
import constants
import game as game_module
import game_evaluator as game_evaluator_module
import player as player_module


class GameManager:
    """TODO"""

    def __init__(self, player: player_module.Player,
                 game_evaluator: game_evaluator_module.GameEvaluator) -> None:
        self._player = player
        self._evaluator = game_evaluator
        self.current_game = game_module.Game()
        self.current_card = (0, 0, 0)

    def play_one_game(self) -> Tuple[bool, constants.Float]:
        """TODO"""
        self.current_game = game_module.Game()
        for _ in range(board_module.NUMBER_OF_FIELDS):
            self.current_card = self.current_game.generate_new_card()
            new_field_index = self._player.find_move(self.current_game.board, self.current_card)
            if self.current_game.is_move_applicable(new_field_index):
                self.current_game.apply_move(self.current_card, new_field_index)
            else:
                return False, self._evaluator.evaluate_failed_game(self.current_game.board,
                                                                   self.current_card)
        return True, self._evaluator.evaluate_successful_game(self.current_game.board)
