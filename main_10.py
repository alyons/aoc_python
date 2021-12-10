from AoC2021.util import parse_file
from AoC2021.day_10 import middle_score, syntax_error_score

def main():
    print('Welcome to Day 10 of Advent of Code 2021')

    lines = parse_file('./data/day_10.txt')

    score = syntax_error_score(lines)

    print(f'Syntax Error Score: {score!r}')

    middle = middle_score(lines)
    
    print(f'Middle Score: {middle!r}')


if __name__ == '__main__':
    main()
