from AoC2021.day_02 import plot_course, plot_course_ex
from AoC2021.util import parse_file


def main():
    print('Welcome to Day 02 of Advent of Code 2021')

    data = parse_file('./data/day_02.txt')
    
    coordinates = plot_course(data)

    print(f'Destination: {coordinates!r}')

    aim_value = plot_course_ex(data)

    print(f'Aim Destination: {aim_value!r}')


if __name__ == '__main__':
    main()