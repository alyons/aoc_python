from typing import List, Tuple
import re


def parse_line_segment(input: str) -> Tuple:
    pattern = re.compile(r'(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)')
    matches = pattern.search(input)
    return tuple(int(num) for num in matches.groups())


def is_vertical_or_horizontal(line: Tuple) -> bool:
    x1, y1, x2, y2 = line
    return x1 == x2 or y1 == y2


def generate_points(line: Tuple) -> List[Tuple]:
    x1, y1, x2, y2 = line
    points = []

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points.append((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points.append((x, y1))
    else:
        mX = 1 if x1 < x2 else -1
        mY = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2 + mX, mX):
            points.append((x, y))
            y += mY

    return points


def calculate_vent_coverage(input: List[str], simple: bool = True) -> dict:
    vent_map = {}
    segments = [parse_line_segment(item) for item in input]
    if simple:
        segments = list(filter(lambda item: is_vertical_or_horizontal(item), segments))

    for item in segments:
            points = generate_points(item)
            for point in points:
                if point in vent_map:
                    vent_map[point] += 1
                else:
                    vent_map[point] = 1
    
    return vent_map


def count_danger_points(vent_map: dict) -> int:
    return sum(x > 1 for x in vent_map.values())
