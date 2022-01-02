from AoC2021.util import parse_chiton_cave, parse_file, parse_int_count, parse_int_file, parse_bingo_file, parse_manual, parse_octopus_grid, parse_cave_graph, parse_polymer_formula, parse_image, parse_sea_cucumbers, manhattan_distance
from numpy import array_equal, exp


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


def test_parse_int_count():
    expected = {
        1: 1,
        2: 1,
        3: 2,
        4: 1
    }
    actual = parse_int_count('./tests/data/day_06.txt')
    assert expected == actual


def test_parse_octopus_grid():
    expected = [5,4,8,3,1,4,3,2,2,3,
                2,7,4,5,8,5,4,7,1,1,
                5,2,6,4,5,5,6,1,7,3,
                6,1,4,1,3,3,6,1,4,6,
                6,3,5,7,3,8,5,4,7,8,
                4,1,6,7,5,2,4,6,4,5,
                2,1,7,6,8,4,1,7,2,1,
                6,8,8,2,8,8,1,1,3,4,
                4,8,4,6,8,4,8,5,5,4,
                5,2,8,3,7,5,1,5,2,6]
    actual = parse_octopus_grid('./tests/data/day_11.txt')
    assert expected == actual


def test_parse_cave_graph():
    expected = [['start', 'A'], ['start', 'b'], ['A', 'c'], ['A', 'b'], ['b', 'd'], ['A', 'end'], ['b', 'end']]
    actual = parse_cave_graph('./tests/data/day_12.txt')
    assert expected == actual


def test_parse_manual():
    expected_p =[[6,10], [0,14], [9,10], [0,3], [10,4], [4,11], [6,0], [6,12], [4,1], [0,13], [10,12], [3,4], [3,0], [8,4], [1,10], [2,14], [8,10], [9,0]]
    expected_f = [('y', 7), ('x', 5)]
    points, folds = parse_manual('./tests/data/day_13.txt')
    assert expected_p == points
    assert expected_f == folds


def test_parse_polymer_formula():
    expected_t = 'NNCB'
    expected_r = { 'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C' }
    expected_e = { 'B': 0, 'C': 0, 'H': 0, 'N': 0 }
    template, rules, elements = parse_polymer_formula('./tests/data/day_14.txt')
    assert expected_t == template
    assert expected_r == rules
    assert expected_e == elements


def test_parse_chiton_grid():
    expected = [1,1,6,3,7,5,1,7,4,2,
                1,3,8,1,3,7,3,6,7,2,
                2,1,3,6,5,1,1,3,2,8,
                3,6,9,4,9,3,1,5,6,9,
                7,4,6,3,4,1,7,1,1,1,
                1,3,1,9,1,2,8,1,3,7,
                1,3,5,9,9,1,2,4,2,1,
                3,1,2,5,4,2,1,6,3,9,
                1,2,9,3,1,3,8,5,2,1,
                2,3,1,1,9,4,4,5,8,1]
    expected_r_l = 10
    grid, row_len = parse_chiton_cave('./tests/data/day_15.txt')
    assert expected_r_l == row_len
    assert expected == grid

def test_parse_image():
    expected_algo = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
    expected_image = {
        (0,0): '#',
        (0,1): '#',
        (0,2): '#',
        (0,3): '.',
        (0,4): '.',
        (1,0): '.',
        (1,1): '.',
        (1,2): '#',
        (1,3): '.',
        (1,4): '.',
        (2,0): '.',
        (2,1): '.',
        (2,2): '.',
        (2,3): '#',
        (2,4): '#',
        (3,0): '#',
        (3,1): '.',
        (3,2): '.',
        (3,3): '.',
        (3,4): '#',
        (4,0): '.',
        (4,1): '.',
        (4,2): '#',
        (4,3): '.',
        (4,4): '#',
    }
    algo, image = parse_image('./tests/data/day_20.txt')
    assert algo == expected_algo
    assert image == expected_image


def test_parse_sea_cucumbers():
    e_east = [(4, 0), (5, 0), (9, 0), (3, 1), (4, 1), (0, 2), (1, 2), (3, 2), (5, 2), (0, 3), (1, 3), (3, 3), (4, 3), (6, 3), (1, 4), (0, 5), (2, 5), (3, 5), (5, 6), (7, 6), (5, 7), (6, 7), (9, 8)]
    e_south = [(0, 0), (7, 0), (8, 0), (1, 1), (2, 1), (6, 1), (7, 1), (4, 2), (9, 2), (2, 3), (8, 3), (0, 4), (2, 4), (4, 4), (5, 4), (7, 4), (6, 5), (1, 6), (2, 6), (8, 6), (0, 7), (2, 7), (7, 7), (9, 7), (4, 8), (7, 8)]
    e_x_max = 9
    e_y_max = 8
    east, south, x_max, y_max = parse_sea_cucumbers('./tests/data/day_25.txt')
    assert east == e_east
    assert south == e_south
    assert x_max == e_x_max
    assert y_max == e_y_max


def test_manhattan_distance():
    actual = manhattan_distance((1105,-1205,1229), (-92,-2380,-20))
    assert actual == 3621
