from AoC2021.util import parse_file
from AoC2021.day_08 import count_simple_displays, display_sum


def main():
    print('Welcome to Day 08 of Advent of Code 2021')

    inputs = parse_file('./data/day_08.txt')

    count = count_simple_displays(inputs)

    print(f'Simple Digits: {count!r}')

    total = display_sum(inputs)
    
    print(f'Sum: {total!r}')


if __name__ == '__main__':
    main()
