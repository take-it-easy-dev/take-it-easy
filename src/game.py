import itertools
import random
from typing import Tuple, List

import board as board_module
import constants
import rules

# TODO
ALL_CARDS = list(
    itertools.product(range(rules.NUMBER_OF_COLORS), repeat=rules.NUMBER_OF_DIRECTIONS))

CardRepresentation = Tuple[constants.FieldIndex, constants.FieldIndex, constants.FieldIndex]


def get_color_triplet_from_card_index(card_index: int) -> Tuple[int, int, int]:
    """TODO"""
    div_3, color_2 = divmod(card_index, 3)
    color_0, color_1 = divmod(div_3, 3)
    return color_0, color_1, color_2


class Game:
    """TODO"""

    def __init__(self):
        """TODO"""
        self.board = board_module.create_blank_board()
        # Note: instead of this, we could use a mask and an int length
        self.available_cards_indices = list(
            range(rules.NUMBER_OF_COLORS ** rules.NUMBER_OF_DIRECTIONS))
        self.taken_fields: List[constants.FieldIndex] = []

    def generate_new_card(self) -> CardRepresentation:
        """TODO"""
        max_card_index = len(self.available_cards_indices) - 1
        random_index = random.randint(0, max_card_index)
        card_index = self.available_cards_indices.pop(random_index)
        return get_color_triplet_from_card_index(card_index)

    def is_move_applicable(self, field_index: int) -> bool:
        """TODO"""
        return field_index not in self.taken_fields

    def apply_move(self, card: CardRepresentation, field_index: int) -> None:
        """TODO"""
        self.taken_fields.append(field_index)
        for direction_index in range(rules.NUMBER_OF_DIRECTIONS):
            color_index = card[direction_index]
            self.board[field_index, direction_index, color_index] = 1.
