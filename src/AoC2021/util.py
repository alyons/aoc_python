from typing import List, Tuple
from numpy import ndarray
import re


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
