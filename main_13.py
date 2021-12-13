from AoC2021.day_13 import perform_folds
from AoC2021.util import parse_manual


def main():
    print('Welcome to Day 13 of Advent of Code 2021')

    points, folds = parse_manual('./data/day_13.txt')

    # Part 1: Perform a single fold
    # perform_folds(points, [folds[0]])

    # print(f'Number of points: {len(points)}')

    perform_folds(points, folds)
    x_max = max([p[0] for p in points])
    y_max = max([p[1] for p in points])

    display = [' ' * (x_max + 1)] * (y_max + 1)

    for p in points:
        display[p[1]] = display[p[1]][:p[0]] + '#' + display[p[1]][(p[0]+1):] 
    
    for d in display:
        print(d)


if __name__ == '__main__':
    main()
