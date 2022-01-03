from AoC2021.day_01 import increase_count, sum_increase_count
from AoC2021.util import parse_int_file

test_input = parse_int_file('./tests/data/day_01.txt')


def test_increase_count():
    actual = increase_count(test_input)
    assert actual == 7


def test_sum_increase_count():
    actual = sum_increase_count(test_input)
    assert actual == 5
