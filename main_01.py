from AoC2021.day_01 import increase_count, sum_increase_count
from AoC2021.util import parse_int_file

def main():
    print('Welcome to Day 01 of Advent of Code 2021')

    data = parse_int_file('./data/day_01.txt')

    count = increase_count(data)

    print('Increase Count: %d' % count)

    sum_count = sum_increase_count(data)

    print('Sum Increase Count: %d' % sum_count)


if __name__ == '__main__':
    main()
