from AoC2021.day_08 import build_digit_dictionary, count_simple_displays, display_sum, display_value
from AoC2021.util import parse_file

inputs = parse_file('./tests/data/day_08.txt')


def test_count_simple_displays():
    actual = count_simple_displays(inputs)
    assert actual == 26


def test_display_sum():
    actual = display_sum(inputs)
    assert actual == 61229


def test_build_digit_dictionary():
    expected = { 'abcdeg': 0, 'ab': 1, 'acdfg': 2,  'abcdf': 3, 'abef': 4, 'bcdef': 5, 'bcdefg': 6, 'abd': 7, 'abcdefg': 8, 'abcdef': 9 }
    actual = build_digit_dictionary(['abcdefg', 'bcdef', 'acdfg', 'abcdf', 'abd', 'abcdef', 'bcdefg', 'abef', 'abcdeg', 'ab'])
    assert actual == expected


def test_display_value():
    expected = 5353
    actual = display_value(['abcdefg', 'bcdef', 'acdfg', 'abcdf', 'abd', 'abcdef', 'bcdefg', 'abef', 'abcdeg', 'ab'], ['bcdef', 'abcdf', 'bcdef', 'abcdf'])
    assert actual == expected
