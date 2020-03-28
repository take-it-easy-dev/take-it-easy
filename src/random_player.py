import numpy as np

import board as board_module
import constants
import game
import player as player_module


class RandomPlayer(player_module.Player):
    def __init__(self):
        super(RandomPlayer, self).__init__()
        self._moves = np.random.permutation(
            np.array(range(board_module.NUMBER_OF_FIELDS), dtype=constants.FieldIndex))
        self._current_index = 0

    def find_move(self, board: board_module.BoardRepresentation,
                  card: game.CardRepresentation) -> constants.FieldIndex:
        self._current_index += 1
        return self._moves[self._current_index - 1]
