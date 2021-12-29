from AoC2021.day_22 import initialize_reactor, parse_reactor_sequence


def main():
    print('Welcome to Day 22')

    instructions = parse_reactor_sequence('./data/day_22.txt')

    cubes = initialize_reactor(instructions, False)

    print(f'Initialize Reactor: {cubes}')


if __name__ == '__main__':
    main()
