from AoC2021.day_23 import find_least_fuel


def main():
    print('Welcome to Day 23')

    amphipods = [('B', 2, 1), ('A', 2, 2), ('C', 4, 1), ('D', 4, 2), ('B', 6, 1), ('C', 6, 2), ('D', 8, 1), ('A', 8, 2)]

    fuel = find_least_fuel(amphipods)

    print(f'Fuel Required: {fuel}')


if __name__ == '__main__':
    main()
