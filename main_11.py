from AoC2021.util import parse_octopus_grid
from AoC2021.day_11 import flashes_after_steps, synchro_summon

def main():
    print('Welcome to Day 11 of Advent of Code 2021')

    grid = parse_octopus_grid('./data/day_11.txt')

    flashes = flashes_after_steps(grid, 100)

    print(f'Flashes: {flashes!r}')

    steps = synchro_summon(grid) + 100

    print(f'Steps: {steps!r}')


if __name__ == '__main__':
    main()
