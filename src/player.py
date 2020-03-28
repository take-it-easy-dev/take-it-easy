import board as board_module
import game
import constants


class Player:
    def __init__(self):
        pass

    def find_move(self, board: board_module.BoardRepresentation,
                  card: game.CardRepresentation) -> constants.FieldIndex:
        raise NotImplementedError("This is a base class.")
