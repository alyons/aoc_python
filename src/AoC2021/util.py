from typing import Dict, Iterable, List, Set, Tuple
from numpy import ndarray
import re
from time import clock_gettime_ns, CLOCK_REALTIME


def parse_file(file: str) -> List[str]:
    data = []

    with open(file) as f:
        for line in f:
            data.append(line.strip())

    return data


def parse_int_file(file: str) -> List[int]:
    data = []

    with open(file) as f:
        for line in f:
            data.append(int(line))

    return data


def parse_bingo_file(file: str) -> Tuple[List[int], List[ndarray]]:
    numbers = []
    boards = []
    temp_board = []
    
    with open(file) as f:
        for line in f:
            if len(numbers) == 0:
                numbers = list(map(int, line.split(',')))
            elif not line == '\n':
                temp_board.append(list(map(int, list(filter(None, line.strip().split(' '))))))
                if len(temp_board) == 5:
                    boards.append(temp_board.copy())
                    temp_board.clear()

    return (numbers, boards)


def parse_int_count(file: str) -> dict:
    values = {}

    with open(file) as f:
        for line in f:
            array = [int(item) for item in line.split(',')]
            for item in array:
                if item in values:
                    values[item] += 1
                else:
                    values[item] = 1

    return values


def parse_octopus_grid(file: str) -> List[List[int]]:
    grid = []

    with open(file) as f:
        for line in f:
            row = [int(x) for x in line.strip()]
            if row: grid.append(row)
    
    return sum(grid, [])


def parse_cave_graph(file: str) -> List[str]:
    edges = []

    with open(file) as f:
        for line in f:
            edge = line.strip().split('-')
            edges.append(edge)

    return edges


def parse_manual(file: str) -> Tuple:
    points = []
    folds = []

    fold_ptn = re.compile(r'fold along (?P<axis>[xy])=(?P<number>\d+)')

    with open(file) as f:
        for line in f:
            if ',' in line:
                point = [int(d) for d in line.strip().split(',')]
                points.append(point)
            else:
                m = fold_ptn.match(line.strip())
                if m:
                    fold = (m.group(1), int(m.group(2)))
                    folds.append(fold)

    return (points, folds)


def parse_polymer_formula(file: str) -> Tuple[str, Dict, Dict]:
    template = ''
    rules = {}
    elements = {}

    with open(file) as f:
        for line in f:
            if not template and not '->' in line:
                template = line.strip()
                for t in template:
                    elements[t] = 0
            elif '->' in line:
                pair = line.strip().split('->')
                rules[pair[0].strip()] = pair[1].strip()
                for p in pair:
                    for i in p.strip():
                        elements[i] = 0

    return (template, rules, elements)


def parse_chiton_cave(file: str) -> Tuple[List[int], int]:
    grid = []
    row_len = 0

    with open(file) as f:
        for line in f:
            if not row_len: row_len = len(line.strip())
            row = [int(x) for x in line.strip()]
            if row: grid.append(row)
    
    return (sum(grid, []), row_len)

def parse_image(file: str) -> tuple[str, dict[tuple[int,int],str]]:
    algorithm = None
    picture = {}
    _x = 0
    _y = 0

    with open(file) as f:
        for line in f:
            _l = line.strip()
            if not algorithm and _l:
                algorithm = _l
            elif _l:
                _x = 0
                for c in _l:
                    picture[(_x,_y)] = c
                    _x += 1
                _y += 1

    return (algorithm, picture)


def parse_sea_cucumbers(file: str) -> tuple[list[tuple[int, int]], list[tuple[int, int]], int, int]:
    east: list[tuple[int, int]] = []
    south:list[tuple[int, int]] = []
    _x = 0
    _y = 0
    _x_max = -1
    _y_max = -1

    with open(file) as f:
        for line in f:
            _l = line.strip()
            if _l:
                for c in _l:
                    if c == '>': east.append((_x, _y))
                    if c == 'v': south.append((_x, _y))
                    if _x > _x_max: _x_max = _x
                    _x += 1
                _x = 0
                if _y > _y_max: _y_max = _y
                _y += 1

    return (east, south, _x_max, _y_max)


def sort_string(value: str) -> str:
    _l = sorted(value)
    return ''.join(_l)


def manhattan_distance(a: Iterable[int], b: Iterable[int]) -> int:
    return sum([abs(x - y) for (x, y) in zip(a, b)])


def generate_time_string(start_time: int, is_running: bool = True) -> str:
    diff = clock_gettime_ns(CLOCK_REALTIME) - start_time
    remainder = int(diff % 1e9)
    total_seconds = diff // 1e9
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)

    if is_running:
        return f'Time Running: {minutes:02}:{seconds:02}.{remainder}'
    else:
        return f'Ran in: {minutes:02}:{seconds:02}.{remainder}'
