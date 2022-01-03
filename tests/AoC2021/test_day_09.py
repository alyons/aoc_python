from AoC2021.day_09 import calculate_basin_size, calculate_maximum_basins, calculate_risk_level, find_low_points, find_low_point_coordinates
from AoC2021.util import parse_file

height_map = parse_file('./tests/data/day_09.txt')


def test_calculate_risk_level():
    expected = 15
    actual = calculate_risk_level([1, 0, 5, 5])
    assert expected == actual


def test_find_low_points():
    expected = [1, 0, 5, 5]
    actual = find_low_points(height_map)
    assert expected == actual


def test_find_low_point_coordinates():
    expected = [(1, 0), (9, 0), (2, 2), (6, 4)]
    actual = find_low_point_coordinates(height_map)
    assert expected == actual

def test_calculate_basin_size():
    expected_1_0 = 3
    actual_1_0 = calculate_basin_size((1, 0), height_map)
    assert expected_1_0 == actual_1_0

    expected_9_0 = 9
    actual_9_0 = calculate_basin_size((9, 0), height_map)
    assert expected_9_0 == actual_9_0

    expected_2_2 = 14
    actual_2_2 = calculate_basin_size((2, 2), height_map)
    assert expected_2_2 == actual_2_2

    expected_6_4 = 9
    actual_6_4 = calculate_basin_size((6, 4), height_map)
    assert expected_6_4 == actual_6_4


def test_calculate_maximum_basins():
    expected = 1134
    actual = calculate_maximum_basins(height_map)
    assert expected == actual
