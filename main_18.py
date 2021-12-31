from AoC2021.day_18 import magnitude, snailfish_addition, find_largest_pair_magnitude
from AoC2021.util import parse_file


def main():
    print('Welcome to Day 18 of Advent of Code 2021')

    inputs = parse_file('./data/day_18.txt')

    sum = snailfish_addition(inputs)

    print(f'Sum: {sum}')
    
    mag = magnitude(sum)

    print(f'Magnitude: {mag}')

    pair = find_largest_pair_magnitude(inputs)

    print(f'Pair Magnitude: {pair}')

if __name__ == '__main__':
    main()
