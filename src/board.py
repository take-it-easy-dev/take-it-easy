""" TODO
                   ----
                 //  0 \\
                 \\ __ //
              ----      ----
            //  1 \\  //  2 \\
            \\ __ //  \\ __ //
           ----     ----     ----
         //  3 \\ //  4 \\ //  5 \\
         \\ __ // \\ __ // \\ __ //
               ----      ----
             //  6 \\  //  7 \\
             \\ __ //  \\ __ //
           ----     ----     ----
         //  8 \\ // 9  \\ // 10 \\
         \\ __ // \\ __ // \\ __ //
               ----      ----
             // 11 \\  // 12 \\
             \\ __ //  \\ __ //
           ----     ----     ----
         // 13 \\ // 14 \\ // 15 \\
         \\ __ // \\ __ // \\ __ //
               ----      ----
             // 16 \\  // 17 \\
             \\ __ //  \\ __ //
                    ----
                  // 18 \\
                  \\ __ //
"""

from typing import Generator, List, Tuple, Union

import numpy as np

import constants
import rules

BoardRepresentation = Union[np.ndarray]
NUMBER_OF_FIELDS = 19
BOARD_SHAPE = (NUMBER_OF_FIELDS, rules.NUMBER_OF_DIRECTIONS, rules.NUMBER_OF_COLORS)
"""
Board: b_{field_index, direction_index, color_index} = {0., 1.}
"""


def assert_board_validity(board: BoardRepresentation) -> None:
    """TODO"""
    assert board.shape == BOARD_SHAPE, f"board shape ({board.shape}) is not {BOARD_SHAPE}."
    assert board.dtype == constants.Float, f"board dtype ({board.dtype}) is not {constants.Float}."
    for field_index in range(NUMBER_OF_FIELDS):
        for direction_index in range(rules.NUMBER_OF_DIRECTIONS):
            elements = board[field_index, direction_index, :]
            number_of_zeros = np.sum(elements == 0.)
            number_of_ones = np.sum(elements == 1.)
            only_zeros_and_ones = number_of_ones + number_of_zeros == rules.NUMBER_OF_COLORS
            if not (only_zeros_and_ones and number_of_ones <= 1.):
                raise AssertionError(f"Invalid values: {elements} at field index = {field_index}, "
                                     f"direction_index: {direction_index}"
                                     )


def is_board_complete(board: BoardRepresentation) -> bool:
    """TODO"""
    for field_index in range(NUMBER_OF_FIELDS):
        for direction_index in range(rules.NUMBER_OF_DIRECTIONS):
            elements = board[field_index, direction_index, :]
            number_of_zeros = np.sum(elements == 0.)
            number_of_ones = np.sum(elements == 1.)
            if not (number_of_ones == 1 and number_of_zeros == rules.NUMBER_OF_COLORS - 1):
                return False
    return True


def multiply(seq: Generator[constants.Float, None, None]) -> constants.Float:
    """TODO"""
    result = constants.Float(1.)
    for element in seq:
        result *= element
    return result


def _compute_evaluation_rules() -> List[List[Tuple[constants.FieldIndex, ...]]]:
    """TODO """
    eval_rules: List[List[Tuple[constants.FieldIndex, ...]]] = [[]] * rules.NUMBER_OF_DIRECTIONS
    eval_rules[rules.Direction.LEFT] = [
        (0, 1, 3),
        (2, 4, 6, 8),
        (5, 7, 9, 11, 13),
        (10, 12, 14, 16),
        (15, 17, 18),
    ]
    eval_rules[rules.Direction.RIGHT] = [
        (0, 2, 5),
        (1, 4, 7, 10),
        (3, 6, 9, 12, 15),
        (8, 11, 14, 17),
        (13, 16, 18),
    ]
    eval_rules[rules.Direction.UP] = [
        (3, 8, 13),
        (1, 6, 11, 16),
        (0, 4, 9, 14, 18),
        (2, 7, 12, 17),
        (5, 10, 15),
    ]
    return eval_rules


EVALUATION_RULES = _compute_evaluation_rules()


def evaluate_board(board: BoardRepresentation) -> float:
    """TODO"""
    score = 0.
    for direction in range(rules.NUMBER_OF_DIRECTIONS):
        eval_rules = EVALUATION_RULES[direction]
        for eval_rule in eval_rules:
            row_length = constants.Float(len(eval_rule))
            for color in range(rules.NUMBER_OF_COLORS):
                reward = rules.REWARDS[direction, color]
                board_elements: Generator[constants.Float, None, None] = (
                    board[idx, direction, color] for idx in eval_rule
                )
                score += row_length * reward * multiply(board_elements)
    return score


def create_blank_board() -> BoardRepresentation:
    """TODO"""
    return np.zeros(shape=BOARD_SHAPE, dtype=constants.Float)
