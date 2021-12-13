from typing import List, Tuple


def perform_fold(points: List[List[int]], fold: Tuple[str, int]):
    axis, line = fold

    # Find points to fold
    to_move = [p for p in points if (axis == 'x' and p[0] > line) or (axis == 'y' and p[1] > line)]

    # Remove points which will be moved and move the points
    for m in to_move:
        points.remove(m)
    
        # could be m[axis == 'y'] -= 2 *abs(m[axis == 'y'] - line) but that's not legible
        if axis == 'x':
            m[0] -= 2 * abs(m[0] - line)
        elif axis == 'y':
            m[1] -= 2 * abs(m[1] - line)
        
        if not m in points: points.append(m)


def perform_folds(points: List[List[int]], folds: List[Tuple[str, int]]):
    for point in points:
        for fold in folds:
            axis, line = fold
            if point[axis == 'y'] > line: point[axis == 'y'] -= 2 * abs(point[axis == 'y'] - line)
    
    _points = [list(t) for t in set([tuple(p) for p in points])]
    points.clear()
    points.extend(_points)
