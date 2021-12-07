from AoC2021.util import parse_int_count
from AoC2021.day_06 import lantern_fish_sim


def main():
    print('Welcome to Day 06 of Advent of Code 2021')

    fish_timer = parse_int_count('./data/day_06.txt')
    count = lantern_fish_sim(fish_timer, 256)

    print(f'Total Fish: {count!r}')


if __name__ == '__main__':
    main()
