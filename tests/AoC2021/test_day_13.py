from AoC2021.util import parse_manual
from AoC2021.day_13 import perform_folds

points, folds = parse_manual('./tests/data/day_13.txt')


def test_perform_folds():
    _points = points.copy()
    perform_folds(_points, [folds[0]])
    print(_points)
    assert len(_points) == 17
