from reprint import output
from itertools import permutations
from sys import maxsize
from copy import deepcopy

_hallway_points = [
    (0, 0),
    (1, 0),
    (3, 0),
    (5, 0),
    (7, 0),
    (9, 0),
    (10, 0)
]

_room_a = [
    (2, 1),
    (2, 2)
]

_room_b = [
    (4, 1),
    (4, 2)
]

_room_c = [
    (6, 1),
    (6, 2)
]

_room_d = [
    (8, 1),
    (8, 2)
]

def complete_path(amphipods: list[tuple[str, int, int]]) -> bool:
    expected = [
        ('A', 2, 1),
        ('A', 2, 2),
        ('B', 4, 1),
        ('B', 4, 2),
        ('C', 6, 1),
        ('C', 6, 2),
        ('D', 8, 1),
        ('D', 8, 2)
    ]

    return amphipods == expected


def manhattan_distance(a: tuple[int, int], b: tuple[int, int]):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def apply_move(amphipods: list[tuple[str, int, int]], move: tuple[tuple[int, int], tuple[int, int]]) -> int:
    index = next(i for i, a in enumerate(amphipods) if a[1] == move[0][0] and a[2] == move[0][1])
    fuel = manhattan_distance(move[0], move[1])
    fuel *= 1000 if amphipods[index][0] == 'D' else 100 if amphipods[index][0] == 'C' else 10 if amphipods[index][0] == 'B' else 1
    amphipods[index] = (amphipods[index][0], move[1][0], move[1][1])
    return fuel


def room_available(amphipods: list[tuple[str, int, int]], room_code: str) -> bool:
    _occupied = []

    match room_code:
        case 'A': _occupied = [a for a in amphipods if a[1] == 2]
        case 'B': _occupied = [a for a in amphipods if a[1] == 4]
        case 'C': _occupied = [a for a in amphipods if a[1] == 6]
        case 'D': _occupied = [a for a in amphipods if a[1] == 8]

    return len(_occupied) == 0 or all(a[0] == room_code for a in _occupied)


def path_blocked(amphipods: list[tuple[str, int, int]], start: tuple[int, int], end: tuple[int, int]) -> bool:
    _base_x = start[0]
    _i_x = 1 if end[0] > start[0] else -1
    _end_x = end[0] + _i_x
    _base_y = start[1]
    _i_y = 1 if end[1] > start[1] else -1
    _end_y = end[1] + _i_y
    _path = []
    if start[1] == 0: # Hallway to Room
        for _dx in range(_base_x + _i_x, _end_x, _i_x):
            _path.append((_dx, start[1]))
        for _dy in range(_base_y + _i_y, _end_y, _i_y):
            _path.append((end[0], _dy))
    else: # Room to Hallway
        # print(f'Y Base: {_base_y}, End: {_end_y}, Iter: {_i_y}')
        for _dy in range(_base_y + _i_y, _end_y, _i_y):
            _path.append((start[0], _dy))
        for _dx in range(_base_x + _i_x, _end_x, _i_x):
            _path.append((_dx, end[1]))
    
    # print(_path)

    blocked = False

    for _p in _path:
        blocked = blocked or any(a[1] == _p[0] and a[2] == _p[1] for a in amphipods)

    return blocked


def room_moves(amphipods: list[tuple[str, int, int]], amphipod: tuple[str, int, int]) -> list[tuple[int, int]]:
    _potential = []
    _available = []

    match amphipod[0]:
        case 'A': _potential = deepcopy(_room_a)
        case 'B': _potential = deepcopy(_room_b)
        case 'C': _potential = deepcopy(_room_c)
        case 'D': _potential = deepcopy(_room_d)

    # print(f'Room Potential: {_potential}')
    # print(amphipods)
    
    for p in _potential:
        i = next((i for i,a in enumerate(amphipods) if a[1] == p[0] and a[2] == p[1]), -1)
        # print(f'{p}: {i}')
        if i == -1:
            _available.append(p)
        elif amphipods[i][0] != amphipod[0]:
            # print(amphipods[i])
            return []
    
    # print(f'Room Avial A: {_available}')

    return [a for a in _available if not path_blocked(amphipods, (amphipod[1], amphipod[2]), a)]


def hallway_moves(amphipods: list[tuple[str, int, int]], amphipod: tuple[str, int, int]) -> list[tuple[int, int]]:
    _potential = [h for h in _hallway_points if not any(a[1] == h[0] and a[2] == h[1] for a in amphipods)]
    _start = (amphipod[1], amphipod[2])
    # print(f'Hallway Potential: {_potential}')
    _available = [p for p in _potential if not path_blocked(amphipods, _start, p)]
    # print(f'Hallway Available: {_available}')

    return _available


def next_moves(amphipods: list[tuple[str, int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    _room = [a for a in amphipods if a[2] > 0]
    _hallway = [a for a in amphipods if a[2] == 0]

    # print(f'In Rooms: {_room}')
    # print(f'In Hallway: {_hallway}')
    next_moves = []

    for r in _room:
        _m = (r[1], r[2])
        next_moves.extend([(_m, h) for h in hallway_moves(amphipods, r)])
    
    for h in _hallway:
        _m = (h[1], h[2])
        next_moves.extend([(_m, r) for r in room_moves(amphipods, h)])

    return next_moves


def find_least_fuel(amphipods: list[tuple[str, int, int]]) -> int:
    fuel = maxsize
    move_lists = []

    # Initialize List
    moves = next_moves(amphipods)
    for m in moves:
        move_lists.append([m])

    while move_lists:
        moves: list = move_lists.pop()
        print(moves)
        _a = deepcopy(amphipods)
        _f = 0
        for m in moves:
            _f += apply_move(_a, m)
        if _f > fuel: continue # If it cost more fuel than the current best, why are we even trying?
        if complete_path(_a) and _f < fuel:
            fuel = _f
        else:
            for m in next_moves(_a):
                _to_add = deepcopy(moves)
                _to_add.append(m)
                move_lists.append(_to_add)

    return fuel


def render_map(amphipods: list[tuple[str, int, int]]):
    layers = [
        '#############',
        '#...........#',
        '###-#-#-#-###',
        '  #-#-#-#-#  ',
        '  #########  '
    ]

    for a in amphipods:
        layers[a[2] + 1] = layers[a[2] + 1][:a[1] + 1] + a[0] +  layers[a[2] + 1][a[1] + 2:]

    for l in layers:
        print(l)
