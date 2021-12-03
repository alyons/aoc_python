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

    return x * y
