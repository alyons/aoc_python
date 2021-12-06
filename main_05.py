from AoC2021.util import parse_file
from AoC2021.day_05 import calculate_vent_coverage, count_danger_points

def main():
    print('Welcome to Day 05 of Advent of Code 2021')

    input = parse_file('./data/day_05.txt')
    vent_map = calculate_vent_coverage(input, False)
    count = count_danger_points(vent_map)

    print(f'Danger Zones: {count!r}')


if __name__ == '__main__':
    main()
