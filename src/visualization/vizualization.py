import matplotlib.pyplot as plt
import rules
import board as board_module
import rules as rules_module
import game as game_module
import cv2 as cv
import numpy as np
from typing import Union, Tuple, Dict, Optional
import constants
import matplotlib.colors as mcolors


def string_to_color(color: str) -> Tuple[int, int, int]:
    normalized_color: Tuple[float, float, float] = mcolors.to_rgb(color)
    return int(normalized_color[0] * 255), int(normalized_color[1] * 255), int(
        normalized_color[2] * 255)


def rgb_color(
        color: Union[rules.UpColor, rules.LeftColor, rules.RightColor, Tuple[
            constants.FieldIndex, constants.ColorIndex]]) -> Tuple[int, int, int]:
    """TODO"""
    if isinstance(color, tuple):
        direction = rules.Direction(color[0])
        color_index = color[1]
        if direction == rules.Direction.UP:
            return rgb_color(rules.UpColor(color_index))
        if direction == rules.Direction.LEFT:
            return rgb_color(rules.LeftColor(color_index))
        if direction == rules.Direction.RIGHT:
            return rgb_color(rules.RightColor(color_index))

    if isinstance(color, rules.LeftColor):
        if color == rules.LeftColor.PURPLE:
            return string_to_color("purple")
        if color == rules.LeftColor.BLACK:
            return string_to_color("black")
        if color == rules.LeftColor.GRAY:
            return string_to_color("gray")

    if isinstance(color, rules.UpColor):
        if color == rules.UpColor.TURQUOISE:
            return string_to_color("turquoise")
        if color == rules.UpColor.RED:
            return string_to_color("red")
        if color == rules.UpColor.GOLD:
            return string_to_color("gold")

    if isinstance(color, rules.RightColor):
        if color == rules.RightColor.YELLOW:
            return string_to_color("yellow")
        if color == rules.RightColor.GREEN:
            return string_to_color("green")
        if color == rules.RightColor.BLUE:
            return string_to_color("blue")

    raise RuntimeError(f"Unreachable code. input: {color}")


# def _create_color_map() -> Dict[rules.Direction, Dict[rules.SomeColor, str]]:
#     colormap = {}
#     for direction_index in range(rules.NUMBER_OF_DIRECTIONS):
#         direction = rules.Direction(direction_index)
#         colormap[direction] = {}
#         for color_index in range(rules.NUMBER_OF_COLORS):
#             color = rules.get_color_enum_by_direction(direction)(color_index)
#             colormap[direction][color] = rules.color_str(color=color)
#     return colormap
#
#
# COLOR_MAP = _create_color_map()

def add_upright_line(canvas: np.ndarray, color_index: constants.ColorIndex,
                     center: np.ndarray) -> None:
    color = rgb_color(color=(rules.Direction.UP, color_index))
    delta = 25
    pt1 = (int(center[0]), int(center[1] - delta))
    pt2 = (int(center[0]), int(center[1] + delta))
    cv.line(canvas, pt1, pt2, color, 10)


def add_tilted_line(canvas: np.ndarray, color_index: constants.ColorIndex, center: np.ndarray,
                    direction: rules.Direction) -> None:
    color = rgb_color(color=(direction, color_index))
    sign = -1. if direction == rules.Direction.LEFT else 1.
    delta = 25 / 1.41
    pt1 = (int(center[0] - delta), int(center[1] - sign * delta))
    pt2 = (int(center[0] + delta), int(center[1] + sign * delta))
    cv.line(canvas, pt1, pt2, color, 10)


def visualize_board(board: board_module.BoardRepresentation,
                    card: Optional[game_module.CardRepresentation]) -> None:
    board_module.assert_board_validity(board)
    canvas = np.zeros((800, 600, 3), "uint8")
    offset = np.array([300, 650])

    delta = 120

    basis_1 = delta / 1.41 * np.array([-1., -0.7])
    basis_2 = delta / 1.41 * np.array([1., -0.7])

    base_coords = {
        1: [0, 0],
        2: [1, 0],
        3: [0, 1],
        4: [2, 0],
        5: [1, 1],
        6: [0, 2],
        7: [2, 1],
        8: [1, 2],
        9: [3, 1],
        10: [2, 2],
        11: [1, 3],
        12: [3, 2],
        13: [2, 3],
        14: [4, 2],
        15: [3, 3],
        16: [2, 4],
        17: [4, 3],
        18: [3, 4],
        19: [4, 4],
    }

    coordinates = {
        i: offset + arr[0] * basis_1 + arr[1] * basis_2 for i, arr in base_coords.items()
    }

    for index, coord in coordinates.items():
        x, y = int(coord[0]), int(coord[1])
        cv.circle(img=canvas, center=(x, y), radius=30, color=(255, 255, 255), thickness=-1)

    for field_index in range(board_module.NUMBER_OF_FIELDS):
        center = coordinates[field_index + 1]

        up_color_index = int(np.argmax(board[field_index, rules_module.Direction.UP, :]))
        if board[field_index, rules_module.Direction.UP, up_color_index] == constants.Float(1.):
            add_upright_line(canvas, up_color_index, center)

        left_color_index = int(np.argmax(board[field_index, rules_module.Direction.LEFT, :]))
        if board[field_index, rules_module.Direction.LEFT, left_color_index] == constants.Float(1.):
            add_tilted_line(canvas, left_color_index, center, rules.Direction.LEFT)

        right_color_index = int(np.argmax(board[field_index, rules_module.Direction.RIGHT, :]))
        if board[field_index, rules_module.Direction.RIGHT, right_color_index] == constants.Float(1.):
            add_tilted_line(canvas, right_color_index, center, rules.Direction.RIGHT)

    if card is not None:
        cv.rectangle(canvas, (450, 150), (600, 0), (150, 150, 150), -1)
        center_tup = (500, 100)
        center = np.array(center_tup)
        cv.circle(img=canvas, center=center_tup, radius=30, color=(255, 255, 255), thickness=-1)
        add_upright_line(canvas, card[rules.Direction.UP], center)
        add_tilted_line(canvas, card[rules.Direction.LEFT], center, rules.Direction.LEFT)
        add_tilted_line(canvas, card[rules.Direction.RIGHT], center, rules.Direction.RIGHT)

    plt.imshow(canvas)
    plt.show()
