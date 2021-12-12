from AoC2021.util import parse_cave_graph
from AoC2021.day_12 import simple_paths, complex_paths, simple_paths_recursive, complex_paths_recursive

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


def test_simple_paths_recursive_a():
    expected = parse_result('./tests/data/day_12_a_1_result.txt')
    actual = simple_paths_recursive(edges_a, 'start', [], [])
    assert all(a in expected for a in actual)
    assert all(e in actual for e in expected)
    assert len(expected) == len(actual)


def test_simple_paths_recursive_b():
    expected = parse_result('./tests/data/day_12_b_1_result.txt')
    actual = simple_paths_recursive(edges_b, 'start', [], [])
    assert all(a in expected for a in actual)
    assert all(e in actual for e in expected)
    assert len(expected) == len(actual)


def test_simple_paths_recursive_c():
    expected = 226
    actual = simple_paths_recursive(edges_c, 'start', [], [])
    assert expected == len(actual)


def test_complex_paths_recursive():
    small_caves = {e for edge in edges_a for e in edge if e.islower()}
    expected = 36
    actual = len(complex_paths_recursive(edges_a, small_caves, 'start', [], []))
    assert expected == actual

    small_caves = {e for edge in edges_b for e in edge if e.islower()}
    expected = 103
    actual = len(complex_paths_recursive(edges_b, small_caves, 'start', [], []))
    assert expected == actual

    small_caves = {e for edge in edges_c for e in edge if e.islower()}
    expected = 3509
    actual = len(complex_paths_recursive(edges_c, small_caves, 'start', [], []))
    assert expected == actual
