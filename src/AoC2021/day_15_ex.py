from AoCUtils.algorithms import a_star
from AoCUtils.utils import manhattan_distance

from rich.text import Text

Point = tuple[int, int]
Cave = dict[Point, int]


def parse_chiton_cave(file: str) -> Cave:
    cave: Cave = {}
    y = 0

    with open(file) as f:
        for line in f:
            row = line.strip()
            cave.update({(x, y):int(r) for x, r in enumerate(row)})
            y += 1
    
    return cave


def rich_cave_render(cave: Cave, path: list[Point]=[]) -> list[str]:
    max_x, max_y = max(cave.keys())
    text_objs = []

    for y in range(0, max_y + 1):
        row = ''
        for x in range(0, max_x + 1):
            color = 'green' if (x, y) in path else 'white'
            row += f'[{color}]{cave_score(cave, (x, y))}[/{color}]'
        text_objs.append(row)

    return text_objs


def bigger_rich_cave_render(cave: Cave, path: list[Point] = []) -> list[str]:
    max_x, max_y = get_bigger_end_point(cave)
    text_objs = []

    for y in range(0, max_y + 1):
        row = ''
        for x in range(0, max_x + 1):
            color = 'green' if (x, y) in path else 'white'
            row += f'[{color}]{bigger_cave_score(cave, (x, y))}[/{color}]'
        text_objs.append(row)

    return text_objs





def next_caves(cave: Cave, point: Point) -> list[Point]:
    nodes = []
    max_x, max_y = max(cave.keys())

    if point[0] > 0:
        nodes.append((point[0] - 1, point[1]))
    
    if point[0] < max_x:
        nodes.append((point[0] + 1, point[1]))

    if point[1] > 0:
        nodes.append((point[0], point[1] - 1))

    if point[1] < max_y:
        nodes.append((point[0], point[1] + 1))

    return nodes


def cave_score(cave: Cave, point: Point) -> int:
    return cave[point]


def chiton_a_star(cave: Cave) -> list[Point]:
    start = (0, 0)
    end = max(cave.keys())
    return a_star(start, end, cave, next_caves, manhattan_distance, cave_score)


def risk_score(cave: Cave, path: list[Point]) -> int:
    return sum(cave[p] for p in path) - cave[path[0]]


def bigger_next_caves(cave: Cave, point: Point) -> list[Point]:
    nodes = []
    max_x, max_y = get_bigger_end_point(cave)

    if point[0] > 0:
        nodes.append((point[0] - 1, point[1]))
    
    if point[0] < max_x:
        nodes.append((point[0] + 1, point[1]))

    if point[1] > 0:
        nodes.append((point[0], point[1] - 1))

    if point[1] < max_y:
        nodes.append((point[0], point[1] + 1))

    return nodes


def bigger_cave_score(cave: Cave, point: Point) -> int:
    og_x, og_y = max(cave.keys())
    og_x += 1
    og_y += 1
    x_overflow = int(point[0] // og_x)
    x = point[0] % og_x
    y_overflow = int(point[1] // og_y)
    y = point[1] % og_y
    
    score = cave_score(cave, (x, y)) + manhattan_distance((0, 0), (x_overflow, y_overflow))
    if score > 9: score -= 9

    return score


def get_bigger_end_point(cave: Cave) -> Point:
    x, y = max(cave.keys())
    return (((x + 1) * 5) - 1, ((y + 1) * 5) - 1)


def bigger_chiton_a_star(cave: Cave) -> list[Point]:
    start = (0, 0)
    end = get_bigger_end_point(cave)
    return a_star(start, end, cave, bigger_next_caves, manhattan_distance, bigger_cave_score)


def bigger_risk_score(cave: Cave, path: list[Point]) -> int:
    return sum(bigger_cave_score(cave, p) for p in path) - bigger_cave_score(cave, path[0])
