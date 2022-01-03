from AoC2021.day_05 import calculate_vent_coverage, count_danger_points, generate_points, is_vertical_or_horizontal, parse_line_segment
from AoC2021.util import parse_file

input = parse_file('./tests/data/day_05.txt')


def test_parse_line_segment():
    expected = (0, 9, 5, 9)
    actual = parse_line_segment(input[0])
    assert expected == actual


def test_is_vertical_or_horizontal_true():
    actual = is_vertical_or_horizontal(parse_line_segment(input[0]))
    assert actual == True


def test_is_vertical_or_horizontal_false():
    actual = is_vertical_or_horizontal(parse_line_segment(input[5]))
    assert actual == False


def test_generate_points():
    expected = [(1,1), (1,2), (1,3)]
    actual = generate_points((1, 1, 1, 3))
    assert expected == actual


def test_count_danger_points():
    expected = 5
    vent_map = calculate_vent_coverage(input)
    actual = count_danger_points(vent_map)
    assert expected == actual

def test_generate_points_diagonal():
    expected = [(9,7), (8,8), (7,9)]
    actual = generate_points((9, 7, 7, 9))
    assert expected == actual

def test_complex_count_danger_points():
    expected = 12
    vent_map = calculate_vent_coverage(input, False)
    actual = count_danger_points(vent_map)
    assert expected == actual
