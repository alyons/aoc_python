from AoC2021.util import parse_cave_graph
from AoC2021.day_12 import simple_paths, complex_paths

edges_a = parse_cave_graph('./tests/data/day_12.txt')
edges_b = parse_cave_graph('./tests/data/day_12_b.txt')
edges_c = parse_cave_graph('./tests/data/day_12_c.txt')


def parse_result(file: str):
    result = []

    with open(file) as f:
        for line in f:
            result.append(line.strip().split(','))

    return result


def test_simple_paths_a():
    expected = parse_result('./tests/data/day_12_a_1_result.txt')
    actual = simple_paths(edges_a)
    assert all(a in expected for a in actual)
    assert all(e in actual for e in expected)
    assert len(expected) == len(actual)

    
def test_simple_paths_b():
    expected = parse_result('./tests/data/day_12_b_1_result.txt')
    actual = simple_paths(edges_b)
    assert all(a in expected for a in actual)
    assert all(e in actual for e in expected)
    assert len(expected) == len(actual)


def test_simple_paths_c():
    expected = 226
    actual = simple_paths(edges_c)
    assert expected == len(actual)


def test_complex_paths_a():
    expected = parse_result('./tests/data/day_12_a_2_result.txt')
    actual = complex_paths(edges_a)
    assert all(a in expected for a in actual)
    assert all(e in actual for e in expected)
    assert len(expected) == len(actual)


def test_complex_paths_b():
    expected = 103
    actual = complex_paths(edges_b)
    assert expected == len(actual)


def test_complex_paths_a():
    expected = 3509
    actual = complex_paths(edges_c)
    assert expected == len(actual)
