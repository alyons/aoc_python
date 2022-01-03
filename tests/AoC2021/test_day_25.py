from AoC2021.util import parse_sea_cucumbers
from AoC2021.day_25 import landing_step


def test_landing_step():
    east, south, x_max, y_max = parse_sea_cucumbers('./tests/data/day_25.txt')
    steps = landing_step(east, south, x_max, y_max)
    assert steps == 58
