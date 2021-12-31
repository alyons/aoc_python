from AoC2021.day_25 import landing_step
from AoC2021.util import parse_sea_cucumbers


def main():
    print('Welcome to Day 25 of Advent of Code 2021')

    east, south, x_max, y_max = parse_sea_cucumbers('./data/day_25.txt')

    steps = landing_step(east, south, x_max, y_max)

    print(f'Can land on step: {steps}')


if __name__ == '__main__':
    main()
