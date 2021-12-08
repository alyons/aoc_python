from AoC2021.util import parse_int_count
from AoC2021.day_07 import align_crabs, align_crabs_ex


def main():
    print('Welcome to Day 07 of Advent of Code 2021')

    crabs = parse_int_count('./data/day_07.txt')
    fuel = align_crabs(crabs)

    print(f'Fuel: {fuel!r}')

    fuel_ex = align_crabs_ex(crabs)

    print(f'Fuel EX: {fuel_ex!r}')


if __name__ == '__main__':
    main()
