from AoC2021.day_23 import apply_move, find_least_fuel, hallway_moves, next_moves, room_moves
from copy import deepcopy

test_case = [('B', 2, 1), ('A', 2, 2), ('C', 4, 1), ('D', 4, 2), ('B', 6, 1), ('C', 6, 2), ('D', 8, 1), ('A', 8, 2)]


def test_apply_move():
    amphipods = deepcopy(test_case)
    fuel = apply_move(amphipods, ((6, 1), (3, 0)))
    expected = [('B', 2, 1), ('A', 2, 2), ('C', 4, 1), ('D', 4, 2), ('B', 3, 0), ('C', 6, 2), ('D', 8, 1), ('A', 8, 2)]
    assert fuel == 40
    assert expected == amphipods


def test_hallway_moves():
    amphipods = deepcopy(test_case)
    moves = hallway_moves(amphipods, ('B', 6, 1))
    assert len(moves) == 7
    assert (3, 0) in moves


def test_room_moves():
    amphipods = deepcopy(test_case)
    pre_moves = [
        ((6, 1), (3, 0)),
        ((4, 1), (5, 0)),
        # ((5, 0), (6, 1)),
        # ((4, 2), (5, 0)),
        # ((3, 0), (4, 2))
    ]
    for m in pre_moves: apply_move(amphipods, m)
    moves = room_moves(amphipods, ('C', 5, 0))
    assert len(moves) == 1
    assert (6, 1) in moves


def test_next_moves():
    moves = next_moves(test_case)
    assert len(moves) == 28
    assert ((4, 1), (3, 0)) in moves


def test_find_least_fuel():
    fuel = find_least_fuel(test_case)
    assert fuel == 12521
