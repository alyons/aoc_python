from AoC2021.util import parse_bingo_file
from AoC2021.day_04 import first_score, last_score

def main():
    print('Welcome to Day 04 of Advent of Code 2021')

    numbers, boards = parse_bingo_file('./data/day_04.txt')

    score = last_score(numbers, boards)

    print(f'Score: {score!r}')


if __name__ == '__main__':
    main()
