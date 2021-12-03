from AoC2021.day_01 import parse_day_01, increase_count, sum_increase_count
from numpy import array_equal

test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def test_parse_day_01():
    actual = parse_day_01('./tests/data/day_01.txt')
    assert array_equal(test_input, actual)


def test_increase_count():
    actual = increase_count(test_input)
    assert actual == 7


def test_sum_increase_count():
    actual = sum_increase_count(test_input)
    assert actual == 5
