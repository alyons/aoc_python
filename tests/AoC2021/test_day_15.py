from AoC2021.util import parse_chiton_cave
from AoC2021.day_15 import navigate_cave, navigate_giga_cave

cave, row_len = parse_chiton_cave('./tests/data/day_15.txt')


def test_navigate_cave_a_star():
    expected = 40
    actual = navigate_cave(cave, row_len)
    assert expected == actual

def test_giga_cave():
    expected = 315
    actual = navigate_giga_cave(cave, row_len)
    assert expected == actual
