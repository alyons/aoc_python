from AoC2021.day_17 import find_max_height, find_max_height_ex

target = (20, 30, -5, -10)


def test_find_max_height():
    expected = 45
    max_y, max_vel = find_max_height(target)
    assert expected == max_y


def test_find_max_height_ex():
    expected = 45
    max_y, max_vel = find_max_height_ex(target)
    assert expected == max_y
