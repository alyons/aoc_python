from AoC2021.util import parse_file, parse_int_file
from numpy import array_equal


def test_parse_file():
    expected = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    actual = parse_file('./tests/data/day_02.txt')
    assert array_equal(expected, actual)


def test_parse_int_file():
    expected = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    actual = parse_int_file('./tests/data/day_01.txt')
    assert array_equal(expected, actual)
