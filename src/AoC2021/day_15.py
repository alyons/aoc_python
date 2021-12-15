from typing import Dict, List, Tuple, Callable
import sys


def get_next_nodes(pos: Tuple[int, int], row_len: int) -> List[Tuple[int, int]]:
    nodes = []

    if pos[0] > 0:
        nodes.append((pos[0] - 1, pos[1]))
    
    if pos[0] < row_len - 1:
        nodes.append((pos[0] + 1, pos[1]))

    if pos[1] > 0:
        nodes.append((pos[0], pos[1] - 1))
    
    if pos[1] < row_len - 1:
        nodes.append((pos[0], pos[1] + 1))

    return nodes


def reconstruct_path(came_from: Dict[Tuple[int, int], Tuple[int, int]], current: Tuple[int, int]):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def a_star(start: Tuple[int, int], end: Tuple[int, int], cave: List[int], row_len: int, hueristic: Callable, get_node_score: Callable) -> List[Tuple[int, int]]:
    open_nodes = set()
    open_nodes.add(start)
    came_from = {}

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = hueristic(start, end)

    while open_nodes:
        current = None
        hi_score = sys.maxsize

        for o in open_nodes:
            if f_score[o] < hi_score:
                hi_score = f_score[o]
                current = o

        if current == end:
            return reconstruct_path(came_from, current)
        
        open_nodes.discard(current)
        for n in get_next_nodes(current, row_len):
            _g_score = g_score[current] + get_node_score(n, cave, row_len)
            if not n in g_score or _g_score < g_score[n]:
                came_from[n] = current
                g_score[n] = _g_score
                f_score[n] = _g_score + hueristic(n, end)
                open_nodes.add(n)


def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def get_node_value(pos: Tuple[int, int], cave: List[int], row_len: int) -> int:
    return cave[pos[1] * row_len + pos[0]]


def calculate_risk_level(path: List[Tuple[int, int]], cave: List[int], row_len: int) -> int:
    risk_level = 0

    for i, p in enumerate(path):
        if not i: continue
        risk_level += get_node_value(p, cave, row_len)

    return risk_level


def navigate_cave(cave: List[int], row_len: int) -> int:
    start = (0, 0)
    end = (row_len - 1, row_len - 1)

    path = a_star(start, end, cave, row_len, manhattan_distance, get_node_value)
    print(path)
    path_score = [get_node_value(p, cave, row_len) for p in path]
    print(path_score)

    return calculate_risk_level(path, cave, row_len)


def get_giga_node_value(pos: Tuple[int, int], cave: List[int], row_len: int) -> int:
    og_len = int(row_len / 5)
    shift = (int(pos[0] / og_len), int(pos[1] / og_len))
    og_pos = (pos[0] % og_len, pos[1] % og_len)

    score = get_node_value(og_pos, cave, og_len)
    distance = manhattan_distance((0, 0), shift)
    score += distance
    if (score > 9): score -= 9

    return score


def calculate_giga_level(path: List[Tuple[int, int]], cave: List[int], row_len: int) -> int:
    giga_level = 0

    for i, p in enumerate(path):
        if not i: continue
        giga_level += get_giga_node_value(p, cave, row_len)

    return giga_level


def navigate_giga_cave(cave: List[int], row_len: int) -> int:
    giga_len = row_len * 5
    start = (0, 0)
    end = (giga_len - 1, giga_len - 1)

    path = a_star(start, end, cave, giga_len, manhattan_distance, get_giga_node_value)
    print(path)
    path_score = [get_giga_node_value(p, cave, giga_len) for p in path]
    print(path_score)

    return calculate_giga_level(path, cave, giga_len)
