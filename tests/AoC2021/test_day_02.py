from AoC2021.day_02 import plot_course, plot_course_ex
from AoC2021.util import parse_file

test_input = parse_file('./tests/data/day_02.txt')


def test_plot_course():
    actual = plot_course(test_input)
    assert actual == 150


def test_plot_course_ex():
    actual = plot_course_ex(test_input)
    assert actual == 900
