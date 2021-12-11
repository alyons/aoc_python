from AoC2021.day_11 import flashes_after_steps, synchro_summon
from AoC2021.util import parse_octopus_grid

test_data = parse_octopus_grid('./tests/data/day_11.txt')

def test_flashes_after_steps():
    grid = test_data.copy()
    expected = 1656
    actual = flashes_after_steps(grid, 100)
    assert expected == actual

def test_synchro_summon():
    grid = test_data.copy()
    expected = 195
    actual = synchro_summon(grid)
    assert expected == actual
