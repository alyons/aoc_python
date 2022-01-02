from AoC2021.util import generate_time_string, manhattan_distance
import re
from sys import maxsize
from copy import deepcopy
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.table import Table, Column
from rich.panel import Panel
from time import clock_gettime_ns, CLOCK_REALTIME

Amphipod = tuple[int, int, str]
Move = tuple[int, int, int]

console = Console()
layout = Layout()
table = Table(
    Column(header='Name', style='green'),
    Column(header='Value', justify='right'),
    title='Debug Info'
)

layout.split(
    Layout(name='header', size=3),
    Layout(ratio=1, name='main'),
    Layout(size=3, name='footer')
)

layout['main'].split_row(
    Layout(name='data_render'),
    Layout(name='debug')
)

layout['debug']

# A Quick way to check if a map is finished
_FINISHED_MAP = {
    False: '(2,1,A)(2,2,A)(4,1,B)(4,2,B)(6,1,C)(6,2,C)(8,1,D)(8,2,D)',
    True: '(2,1,A)(2,2,A)(2,3,A)(2,4,A)(4,1,B)(4,2,B)(4,3,B)(4,4,B)(6,1,C)(6,2,C)(6,3,C)(6,4,C)(8,1,D)(8,2,D)(8,3,D)(8,4,D)'
}

_hallway_points = [
    (0, 0),
    (1, 0),
    (3, 0),
    (5, 0),
    (7, 0),
    (9, 0),
    (10, 0)
]

rooms = {
    False: {
        'A': [(2, 1), (2, 2)],
        'B': [(4, 1), (4, 2)],
        'C': [(6, 1), (6, 2)],
        'D': [(8, 1), (8, 2)]
    },
    True: {
        'A': [(2, 1), (2, 2), (2, 3), (2, 4)],
        'B': [(4, 1), (4, 2), (4, 3), (4, 4)],
        'C': [(6, 1), (6, 2), (6, 3), (6, 4)],
        'D': [(8, 1), (8, 2), (8, 3), (8, 4)]
    }
}

def amphipod_str_to_list(amphipod_string: str) -> list[Amphipod]:
    return [(int(a[0]), int(a[1]), a[2]) for a in re.findall(r'\((\d+),(\d+),([ABCD])\)', amphipod_string)]


def amphipod_list_to_str(amphipods: list[Amphipod]) -> str:
    key = ''
    for a in sorted(amphipods, key =lambda p: (p[2], p[0], p[1])): key += f'({a[0]},{a[1]},{a[2]})'
    return key


def manhattan_energy_all(amphipods: list[Amphipod]) -> int:
    energy = 0

    for i, a in enumerate(sorted(amphipods, key =lambda p: (p[2], p[0], p[1]))):
        x = 8 if i > 5 else 6 if i > 3 else 4 if i > 1 else 2
        y = 1 if i % 2 == 0 else 2
        distance = manhattan_distance((a[0], a[1]), (x, y))
        energy += distance 

    return energy


def room_can_be_entered(code: str, amphipods: list[Amphipod], large_rooms: bool = False) -> bool:
    valid = True

    for space in reversed(rooms[large_rooms][code]):
        occupant = next((a for a in amphipods if a[0] == space[0] and a[1] == space[1]), None)
        if not occupant:
            valid &= True
        else:
            valid &= occupant[2] == code

    return valid


def amphipod_in_correct_room(amphipods: list[Amphipod], amphipod: Amphipod, large_rooms: bool = False) -> bool:
    others = [(amphipod[0], y, amphipod[2]) for y in range(amphipod[1] + 1, (5 if large_rooms else 3))]
    return (amphipod[0], amphipod[1]) in rooms[large_rooms][amphipod[2]] and all(other in amphipods and (other[0], other[1]) in rooms[large_rooms][other[2]] for other in others)


def path_blocked(amphipods: list[Amphipod], amphipod: Amphipod, position: tuple[int, int]):
    _base_x = amphipod[0]
    _i_x = 1 if position[0] > amphipod[0] else -1
    _end_x = position[0] + _i_x
    _base_y = amphipod[1]
    _i_y = 1 if position[1] > amphipod[1] else -1
    _end_y = position[1] + _i_y
    _path = []
    if amphipod[1] == 0: # Hallway to Room
        for _dx in range(_base_x + _i_x, _end_x, _i_x):
            _path.append((_dx, amphipod[1]))
        for _dy in range(_base_y + _i_y, _end_y, _i_y):
            _path.append((position[0], _dy))
    else: # Room to Hallway
        for _dy in range(_base_y + _i_y, _end_y, _i_y):
            _path.append((amphipod[0], _dy))
        for _dx in range(_base_x + _i_x, _end_x, _i_x):
            _path.append((_dx, position[1]))
    
    blocked = False

    for _p in _path:
        blocked = blocked or any(a[0] == _p[0] and a[1] == _p[1] for a in amphipods)

    return blocked


def room_to_hallway_moves(amphipods: list[Amphipod], index: int, large_rooms: bool) -> list[Move]:
    amphipod = amphipods[index]

    if amphipod_in_correct_room(amphipods, amphipod, large_rooms): return []

    _potential = [h for h in _hallway_points if not any(a[0] == h[0] and a[1] == h[1] for a in amphipods)]

    return [(p[0], p[1], index) for p in _potential if not path_blocked(amphipods, amphipod, p)]


def hallway_to_room_moves(amphipods: list[Amphipod], index: int, large_rooms: bool) -> list[Move]:
    amphipod = amphipods[index]

    if not room_can_be_entered(amphipod[2], amphipods):
        return []
    
    return [(p[0], p[1], index) for p in rooms[large_rooms][amphipod[2]] if not any(a[0] == p[0] and a[1] == p[1] for a in amphipods) and not path_blocked(amphipods, amphipod, p)]


def next_moves(amphipods: list[Amphipod]) -> list[Move]:
    large_rooms = len(amphipods) == 16
    room_amphipods = [a for a in amphipods if a[1] > 0 and not amphipod_in_correct_room(amphipods, a, large_rooms)]
    hallway_amphipods = [a for a in amphipods if a[1] == 0]

    moves = []

    for a in room_amphipods:
        index = amphipods.index(a)
        moves.extend(room_to_hallway_moves(amphipods, index, large_rooms))

    for a in hallway_amphipods:
        index = amphipods.index(a)
        _moves = hallway_to_room_moves(amphipods, index, large_rooms)
        if _moves: moves.append(_moves[-1])

    return moves


def move_amphipod_to_string(amphipods: list[Amphipod], move: Move) -> tuple[str, int]:
    working = deepcopy(amphipods)
    energy = move_amphipod(working, move)

    return (amphipod_list_to_str(working), energy)


def move_amphipod(amphipods: list[Amphipod], move: Move) -> int:
    start = (amphipods[move[2]][0], amphipods[move[2]][1])
    end = (move[0], move[1])
    amphipods[move[2]] = (move[0], move[1], amphipods[move[2]][2])
    energy = manhattan_distance(start, end) * (1000 if amphipods[move[2]][2] == 'D' else 100 if amphipods[move[2]][2] == 'C' else 10 if amphipods[move[2]][2] == 'B' else 1)
    
    return energy


def reconstruct_path(current: str, came_from: dict[str, tuple[str, Move]]) -> list[Move]:
    path = [came_from[current][1]]

    while current in came_from:
        current, move = came_from[current]
        path.append(move)

    path.reverse()
    return path
        

def amphipod_a_star(start: str, test_items: list[str] = []) -> list[Move]:
    large_rooms = len(start) == 80
    open_burrows = set()
    open_burrows.add(start)
    came_from = {}

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = manhattan_energy_all(amphipod_str_to_list(start))

    start_time = clock_gettime_ns(CLOCK_REALTIME)
    iterations = 0

    layout['header'].update(Panel('Amphipods', title='Advent of Code 2021', subtitle='23'))
    layout['footer'].update(Panel(generate_time_string(start_time)))

    path = []

    with Live(layout, refresh_per_second=10, screen=True):
        while open_burrows:
            iterations += 1
            current = None
            hi_score = maxsize

            for o in open_burrows:
                if f_score[o] < hi_score:
                    hi_score = f_score[o]
                    current = o
            
            if current == _FINISHED_MAP[large_rooms]:
                path = reconstruct_path(current, came_from)
                break

            open_burrows.discard(current)
            amphipods = amphipod_str_to_list(current)
            moves = next_moves(amphipods)
            for m in moves:
                amphipod_str, energy = move_amphipod_to_string(amphipods, m)
                _g_score = g_score[current] + energy
                if not amphipod_str in g_score or _g_score < g_score[amphipod_str]:
                    came_from[amphipod_str] = (current, m)
                    g_score[amphipod_str] = _g_score
                    f_score[amphipod_str] = _g_score + manhattan_energy_all(amphipod_str_to_list(amphipod_str))
                    open_burrows.add(amphipod_str)
            
            layout['footer'].update(Panel(generate_time_string(start_time)))
    
    layout['footer'].update(Panel(generate_time_string(start_time, False)))

    return path


def total_energy_used(amphipods: list[Amphipod], moves: list[Move], print_debug: bool = False) -> int:
    energy = 0

    for m in moves:
        energy += move_amphipod(amphipods, m)
        amphipods.sort(key =lambda p: (p[2], p[0], p[1]))
        if print_debug:
            print(f'Move: {m}')
            render_map(amphipods)

    return energy

def render_map(amphipods: list[Amphipod]):
    layers = [
        '#############',
        '#...........#',
        '###-#-#-#-###',
        '  #-#-#-#-#  ',
    ]
    if len(amphipods) == 16: layers.extend(['  #-#-#-#-#  ', '  #-#-#-#-#  '])
    layers.append('  #########  ')

    for a in amphipods:
        layers[a[1] + 1] = layers[a[1] + 1][:a[0] + 1] + a[2] +  layers[a[1] + 1][a[0] + 2:]

    for l in layers:
        print(l)


# def render_left_layout(amphipods: list[Amphipod], layout: Layout):


# def render_right_layout()