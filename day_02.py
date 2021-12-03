from typing import List

def plot_course(input: List[str]) -> int:
    x = 0
    y = 0

    for item in input:
        match item.split():
            case ['forward', value]:
                x += int(value)
            case ['down', value]:
                y += int(value)
            case ['up', value]:
                y -= int(value)
            case _:
                print(f'Unable to process: {item!r}')

    return x * y

def plot_course_ex(input: List[str]) -> int:
    x = 0
    y = 0
    aim = 0

    for item in input:
        match item.split():
            case ['down', value]:
                aim += int(value)
            case ['up', value]:
                aim -= int(value)
            case ['forward', value]:
                x += int(value)
                y += aim * int(value)
            case _:
                print(f'Unable to process: {item!r}')

    return x * y


def main():
    print('Welcome to Day 02 of Advent of Code 2021')

    test_input = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

    data = []
    with open('./data/day_02.txt') as f:
        for line in f:
            data.append(line)
    
    coordinates = plot_course(data)

    print(f'Destination: {coordinates!r}')

    aim_value = plot_course_ex(data)

    print(f'Aim Destination: {aim_value!r}')


if __name__ == '__main__':
    main()