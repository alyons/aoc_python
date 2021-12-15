from AoC2021.day_15 import navigate_cave, navigate_giga_cave
from AoC2021.util import parse_chiton_cave


def main():
    print('Welcome to Day 15 of Advent of Code 2021')

    cave, row_len = parse_chiton_cave('./data/day_15.txt')

    risk_level = navigate_cave(cave, row_len)

    print(f'Risk Level: {risk_level!r}')

    giga_risk = navigate_giga_cave(cave, row_len)

    print(f'Giga Risk: {giga_risk!r}')


if __name__ == '__main__':
    main()
