from enum import IntEnum
import numpy as np
from constants import Float


class Direction(IntEnum):
    """TODO"""
    LEFT = 0  # /
    UP = 1  # |
    RIGHT = 2  # \\


def dir_str(direction: Direction, short: bool = True) -> str:
    """TODO"""
    if direction == Direction.LEFT:
        return "/" if short else "LEFT"
    if direction == Direction.UP:
        return "|" if short else "UP"
    if direction == Direction.LEFT:
        return "\\" if short else "RIGHT"

    raise RuntimeError(f"Unreachable code. Input: {direction}, short: {short}")


class LeftColor(IntEnum):
    """TODO"""
    GRAY = 0
    PURPLE = 1
    BLACK = 2


class UpColor(IntEnum):
    """TODO"""
    GOLD = 0
    RED = 1
    TURQUOISE = 2


class RightColor(IntEnum):
    """TODO"""
    YELLOW = 0
    BLUE = 1
    GREEN = 2


# SomeColor = Union[LeftColor, UpColor, RightColor]
#
#
# def get_color_enum_by_direction(direction: Union[int, Direction]) -> Type[SomeColor]:
#     """TODO"""
#     direction_index = int(direction)
#     if direction_index == Direction.UP:
#         return UpColor
#     if direction_index == Direction.LEFT:
#         return LeftColor
#     if direction_index == Direction.RIGHT:
#         return RightColor
#
#     raise RuntimeError(f"Unreachable code. input: {direction}")


NUMBER_OF_COLORS = 3
NUMBER_OF_DIRECTIONS = 3


def _create_reward_array() -> np.ndarray:
    """
    TODO
    0th index: direction
    1st index: color
    """
    rewards = np.zeros(shape=(NUMBER_OF_DIRECTIONS, NUMBER_OF_COLORS), dtype=Float)
    rewards[Direction.LEFT][LeftColor.GRAY] = 6
    rewards[Direction.LEFT][LeftColor.BLACK] = 7
    rewards[Direction.LEFT][LeftColor.PURPLE] = 2

    rewards[Direction.UP][UpColor.GOLD] = 9
    rewards[Direction.UP][UpColor.RED] = 1
    rewards[Direction.UP][UpColor.TURQUOISE] = 5

    rewards[Direction.RIGHT][RightColor.BLUE] = 8
    rewards[Direction.RIGHT][RightColor.GREEN] = 4
    rewards[Direction.RIGHT][RightColor.YELLOW] = 3

    return rewards


REWARDS = _create_reward_array()
