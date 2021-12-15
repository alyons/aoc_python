from AoC2021.day_14 import apply_polymer_formula_cached
from AoC2021.util import parse_polymer_formula


def main():
    print('Welcome to Day 14 of Advent of Code 2021')

    template, rules, elements = parse_polymer_formula('./data/day_14.txt')

    counts = apply_polymer_formula_cached(template, rules, 40)
    print(counts)
    _min = min(counts.values())
    _max = max(counts.values())

    print(f'Parsed Value: {_max - _min}')


if __name__ == '__main__':
    main()
