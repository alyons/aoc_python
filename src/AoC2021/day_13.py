from typing import List, Tuple


def perform_folds(points: List[List[int]], folds: List[Tuple[str, int]]):
    for point in points:
        for fold in folds:
            axis, line = fold
            if point[axis == 'y'] > line: point[axis == 'y'] -= 2 * abs(point[axis == 'y'] - line)
    
    _points = [list(t) for t in set([tuple(p) for p in points])]
    points.clear()
    points.extend(_points)
