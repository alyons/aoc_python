from AoC2021.util import parse_file, parse_int_file, parse_bingo_file
from numpy import array_equal


def test_parse_file():
    expected = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    actual = parse_file('./tests/data/day_02.txt')
    assert array_equal(expected, actual)


def test_parse_int_file():
    expected = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    actual = parse_int_file('./tests/data/day_01.txt')
    assert array_equal(expected, actual)


def test_parse_bingo_file():
    expected_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    expected_boards = [[[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]], [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]], [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]]
    actual_numbers, actual_boards = parse_bingo_file('./tests/data/day_04.txt')
    assert array_equal(expected_numbers, actual_numbers)
    assert array_equal(expected_boards, actual_boards)
