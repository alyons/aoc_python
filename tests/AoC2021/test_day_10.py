from AoC2021.day_10 import middle_score, syntax_error_score
from AoC2021.util import parse_file

lines = parse_file('./tests/data/day_10.txt')

def test_syntax_error_score():
    expected = 26397
    actual = syntax_error_score(lines)
    assert expected == actual


def test_middle_score():
    expected = 288957
    actual = middle_score(lines)
    assert expected == actual
