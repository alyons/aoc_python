import re
from sys import maxsize
from copy import deepcopy
from time import clock_gettime_ns, CLOCK_REALTIME, sleep

from AoCUtils.utils import generate_time_string, manhattan_distance
from AoCUtils.rich import Header, make_default_layout

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.style import Style
from rich.syntax import Syntax
from rich.table import Column, Table
from rich.text import Text

Amphipod = tuple[int, int, str]
Move = tuple[int, int, int]

console = Console()
layout = make_default_layout()

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

def is_finished(amphipod_str: str, large_rooms: bool) -> bool:
    return all(t in amphipod_str for t in [f'({v[0]},{v[1]},{k})' for k, v in rooms[large_rooms].items()])

def energy_by_code(code: str) -> int:
    match code:
        case 'A': return 1
        case 'B': return 10
        case 'C': return 100
        case 'D': return 1000

def column_by_code(code: str) -> int:
    match code:
        case 'A': return 2
        case 'B': return 4
        case 'C': return 6
        case 'D': return 8

def amphipod_str_to_list(amphipod_string: str) -> list[Amphipod]:
    return [(int(a[0]), int(a[1]), a[2]) for a in re.findall(r'\((\d+),(\d+),([ABCD])\)', amphipod_string)]


def amphipod_list_to_str(amphipods: list[Amphipod]) -> str:
    key = ''
    for a in sorted(amphipods, key=lambda p: (p[2], p[0], p[1])): key += f'({a[0]},{a[1]},{a[2]})'
    # for a in amphipods: key += f'({a[0]},{a[1]},{a[2]})'
    return key


def manhattan_energy_all(amphipods: list[Amphipod], large_rooms: bool) -> int:
    energy = 0
    y_dict = { 'A': 4, 'B': 4, 'C': 4, 'D': 4 }

    for i, a in enumerate(sorted(amphipods, key =lambda p: (p[2], p[0], p[1]))):
    # for a in amphipods:
        x = column_by_code(a[2])
        y = y_dict[a[2]]
        y_dict[a[2]] -= 1
        distance = manhattan_distance((a[0], a[1]), (x, y))
        energy += distance * energy_by_code(a[2])

        # A Discount makes it finish quicker, but not necessarily correctly
        # if amphipod_in_correct_room(amphipods, a, large_rooms): energy -= energy_by_code(a[2]) # Will a discount help incentivise certain configurations

    return energy


def room_can_be_entered(code: str, amphipods: list[Amphipod], large_rooms: bool) -> bool:
    valid = True

    for space in reversed(rooms[large_rooms][code]):
        occupant = next((a for a in amphipods if a[0] == space[0] and a[1] == space[1]), None)
        if not occupant:
            valid &= True
        else:
            valid &= occupant[2] == code

    return valid


def amphipod_in_correct_room(amphipods: list[Amphipod], amphipod: Amphipod, large_rooms: bool) -> bool:
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

    if not room_can_be_entered(amphipod[2], amphipods, large_rooms):
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
    energy = manhattan_distance(start, end) * energy_by_code(amphipods[move[2]][2])
    
    return energy


def reconstruct_path(current: str, came_from: dict[str, tuple[str, Move]]) -> list[Move]:
    path = []

    while current in came_from:
        current, move = came_from[current]
        path.append(move)

    path.reverse()
    return path
        

def amphipod_a_star(start: str, test_items: list[str] = []) -> list[Move]:
    large_rooms = len(start) >= 80
    open_burrows = set()
    open_burrows.add(start)
    came_from = {}
    potential_wins: dict[str, int] = {}
    win_min = maxsize

    dead_end_burrows = set()

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = manhattan_energy_all(amphipod_str_to_list(start), large_rooms)

    start_time = clock_gettime_ns(CLOCK_REALTIME)
    iterations = 0

    layout['header'].update(Header('Amphipod Sorting', 2021, 23))
    layout['footer'].update(Panel(generate_time_string(start_time), border_style='green'))

    with Live(layout, refresh_per_second=10, screen=True):
        while open_burrows:
            iterations += 1
            current = None
            hi_score = maxsize

            for o in open_burrows:
                if f_score[o] < hi_score:
                    hi_score = f_score[o]
                    current = o
            
            open_burrows.discard(current)

            if current == _FINISHED_MAP[large_rooms]:
            # if is_finished(current, large_rooms):
                potential_wins[current] = hi_score
                if hi_score < win_min: win_min = hi_score
                continue

            if hi_score > win_min:
                dead_end_burrows.add(current)

            if current in dead_end_burrows:
                continue    

            amphipods = amphipod_str_to_list(current)
            moves = next_moves(amphipods)

            if not moves:
                dead_end_burrows.add(current)
            else:
                for m in moves:
                    amphipod_str, energy = move_amphipod_to_string(amphipods, m)
                    _g_score = g_score[current] + energy
                    if not amphipod_str in dead_end_burrows and not amphipod_str in g_score or _g_score < g_score[amphipod_str]:
                        came_from[amphipod_str] = (current, m)
                        g_score[amphipod_str] = _g_score
                        f_score[amphipod_str] = _g_score + manhattan_energy_all(amphipod_str_to_list(amphipod_str), large_rooms)
                        open_burrows.add(amphipod_str)
            
            debug_data = [
                ('Iterations', str(iterations)),
                ('Open Burrows', str(len(open_burrows))),
                ('Dead Ends', str(len(dead_end_burrows)))
            ]

            n = 28 if large_rooms else 14
            
            debug_data.extend([(f'Current Data: {i}', a) for i, a in enumerate(current_to_renderable(current, large_rooms))])

            layout['data_vis'].update(render_map_panel(amphipods))
            layout['debug'].update(render_debug(debug_data))
            layout['footer'].update(Panel(generate_time_string(start_time), border_style='green'))
    
    layout['footer'].update(Panel(generate_time_string(start_time, False), border_style='green'))

    return reconstruct_path(min(potential_wins, key=potential_wins.get), came_from)


def current_to_renderable(current: str, large_rooms: bool) -> list[str]:
    current = current.replace('10', 'X')
    n = 28 if large_rooms else 14
    return [current[index: index + n] for index in range(0, len(current), n)]

def total_energy_internal(amphipods: list[Amphipod], moves: list[Move]) -> int:
    energy = 0

    for m in moves:
        energy += move_amphipod(amphipods, m)
        amphipods.sort(key =lambda p: (p[2], p[0], p[1]))

    return energy


def total_energy_used(amphipods: list[Amphipod], moves: list[Move], sleep_increment: int = 1, final_rest: int = 3) -> int:
    energy = 0

    table = Table(
        'Move',
        'Energy'
    )

    layout['header'].update(Panel('Amphipods', title='Advent of Code 2021', subtitle='23'))
    with Live(layout, refresh_per_second=10, screen=True):
        for m in moves:
            energy += move_amphipod(amphipods, m)
            table.add_row(str(m), str(energy))
            amphipods.sort(key =lambda p: (p[2], p[0], p[1]))
            layout['data_vis'].update(render_map_panel(amphipods))
            layout['footer'].update(Panel(f'Move: {m}', border_style='green'))
            layout['debug'].update(Panel(
                Align.center(table, vertical='middle'),
                box = box.ROUNDED,
                padding=(1,2),
                title="Moves",
                border_style='bright_blue'
            ))
            sleep(sleep_increment)
        
        sleep(final_rest) # Just to look at final map

    return energy


def render_debug(data: list[tuple] = []) -> Panel:
    table = Table(
        Column(header='Name', style='green'),
        Column(header='Value', justify='right'),
        title='Debug Info',
        expand=True
    )

    for item in data:
        table.add_row(
            item[0],
            item[1]
        )

    return Panel(
        Align.center(table, vertical='middle'),
        box = box.ROUNDED,
        padding=(1,2),
        title="Debug Data",
        border_style='bright_blue'
    )


def render_map_highlight_regex(matchObj) -> Style:
    style = Style()

    match matchObj:
        case 'A': style = Style(color='red')
        case 'B': style = Style(color='green')
        case 'C': style = Style(color='blue')
        case 'D': style = Style(color='yellow')
            
    return style


def render_map_panel(amphipods: list[Amphipod]) -> Panel:
    layers = [
        '#...........#',
        '###-#-#-#-###',
        '  #-#-#-#-#  ',
    ]
    if len(amphipods) == 16: layers.extend(['  #-#-#-#-#  ', '  #-#-#-#-#  '])

    for a in amphipods:
        layers[a[1]] = layers[a[1]][:a[0] + 1] + a[2] +  layers[a[1]][a[0] + 2:]

    grid = Table.grid(expand=True)
    grid.add_row('#############')
    for l in layers:
        text = Text(l)
        text.highlight_regex(r'([ABCD])', render_map_highlight_regex)
        grid.add_row(text)
    grid.add_row('  #########  ')

    return Panel(
        Align.center(grid, vertical='middle'),
        box = box.ROUNDED,
        padding=(1,2),
        title="Map",
        border_style='red'
    )


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