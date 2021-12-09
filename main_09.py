from AoC2021.util import parse_file
from AoC2021.day_09 import calculate_maximum_basins, calculate_risk_level, find_low_points


def main():
    print('Welcome to Day 09 of Advent of Code 2021')

    height_map = parse_file('./data/day_09.txt')

    low_points = find_low_points(height_map)

    risk_level = calculate_risk_level(low_points)

    print(f'Risk Level: {risk_level!r}')

    basin_score = calculate_maximum_basins(height_map)

    print(f'Basin Maximum: {basin_score!r}')


if __name__ == '__main__':
    main()
