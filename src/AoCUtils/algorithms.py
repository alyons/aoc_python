from sys import maxsize
from typing import Callable


def reconstruct_path(current, came_from):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)
    
    path.reverse()
    return path


def a_star(start, end, nodes, next_nodes: Callable, hueristic: Callable, node_score: Callable):
    """ Run a* against the provided data
    node ids should be hashable (like converting all data to tuples or strings)

    """
    open_nodes = set()
    open_nodes.add(start)
    came_from = {}

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = hueristic(start, end)

    potential_wins = {}
    win_min = maxsize

    dead_end_nodes = set()

    while open_nodes:
        current = None
        hi_score = maxsize

        for o in open_nodes:
            if f_score[o] < hi_score:
                hi_score = f_score[o]
                current = o
        
        open_nodes.discard(current)

        if current == end:
            potential_wins[current] = hi_score
            if hi_score < win_min: win_min = hi_score
            continue

        if hi_score > win_min:
            dead_end_nodes.add(current)
        
        if current in dead_end_nodes:
            continue
        
        next_ = next_nodes(nodes, current)

        if not next_:
            dead_end_nodes.add(n)
            continue

        for n in next_:
            _g = g_score[current] + node_score(nodes, n)
            if not n in g_score or _g < g_score[n]:
                came_from[n] = current
                g_score[n] = _g
                f_score[n] = _g + hueristic(n, end)
                open_nodes.add(n)

    return reconstruct_path(min(potential_wins, key=potential_wins.get), came_from)
        