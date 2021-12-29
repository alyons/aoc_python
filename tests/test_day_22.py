from AoC2021.day_22 import Cuboid, get_cube_difference, initialize_reactor, parse_reactor_sequence


def test_parse_reactor_sequence():
    expected = [
        Cuboid((10, 10, 10), (12, 12, 12), True),
        Cuboid((11, 11, 11), (13, 13, 13), True),
        Cuboid((9, 9, 9), (11, 11, 11), False),
        Cuboid((10, 10, 10), (10, 10, 10), True)
    ]
    actual = parse_reactor_sequence('./tests/data/day_22_simple.txt')
    assert expected == actual


def test_get_cube_difference():
    expected = [
        Cuboid((13, 11, 11), (13, 13, 13), True),
        Cuboid((11, 13, 11), (12, 13, 13), True),
        Cuboid((11, 11, 13), (12, 12, 13), True)
    ]
    actual = get_cube_difference(Cuboid((11, 11, 11), (13, 13, 13), True), Cuboid((10, 10, 10), (12, 12, 12), True))
    assert expected == actual


def test_initialize_reactor_simple():
    instructions = parse_reactor_sequence('./tests/data/day_22_simple.txt')
    expected = 39
    actual = initialize_reactor(instructions)
    assert expected == actual


def test_initialize_reactor_full():
    instructions = parse_reactor_sequence('./tests/data/day_22.txt')
    expected = 590784
    actual = initialize_reactor(instructions)
    assert expected == actual