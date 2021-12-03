from AoC2021.day_03 import power_consumption, oxygen_rating, carbon_dioxide_rating, life_support_rating
from AoC2021.util import parse_file

test_input = parse_file('./tests/data/day_03.txt')


def test_power_consumption():
    actual = power_consumption(test_input)
    assert actual == 198


def test_oxygen_rating():
    data = test_input.copy()
    actual = oxygen_rating(data)
    assert actual == 23


def test_carbon_dioxide_rating():
    data = test_input.copy()
    actual = carbon_dioxide_rating(data)
    assert actual == 10


def test_life_support_rating():
    data = test_input.copy()
    actual = life_support_rating(data)
    assert actual == 230
