from AoC2021.day_04 import board_score_index, board_score, first_score, last_score
from AoC2021.util import parse_bingo_file

test_numbers, test_boards = parse_bingo_file('./tests/data/day_04.txt')


def test_bingo_score_index():
    expected = 11
    actual = board_score_index(test_numbers, test_boards[2])
    assert expected == actual


def test_board_score():
    expected = 188
    actual = board_score(test_numbers, test_boards[2])
    assert expected == actual


def test_first_score():
    expected = 4512
    actual = first_score(test_numbers, test_boards)
    assert expected == actual


def test_last_score():
    expected = 1924
    actual = last_score(test_numbers, test_boards)
    assert expected == actual
