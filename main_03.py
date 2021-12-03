from AoC2021.day_03 import power_consumption, life_support_rating
from AoC2021.util import parse_file


def main():
    print('Welcome to Day 02 of Advent of Code 2021')

    data = parse_file('./data/day_03.txt')

    power = power_consumption(data)

    print(f'Power Consumption: {power!r}')

    lsr = life_support_rating(data)

    print(f'Life Support Rating: {lsr!r}')


if __name__ == '__main__':
    main()
