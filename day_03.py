from typing import List

def power_consumption(file: str, length: int) -> int:
    gamma = 0
    epsilon = 0

    zero_array = [0] * length
    one_array = [0] * length
    # zero_array = [0 for i in range(length)]
    # one_array = [0 for i in range(length)]


    with open(file) as f:
        for line in f:
            for i in range(length):
                if line[i] == '0':
                    zero_array[i] += 1
                elif line[i] == '1':
                    one_array[i] += 1

    gamma_string = ''
    epsilon_string = ''

    for j in range(length):
        if zero_array[j] > one_array[j]:
            gamma_string += '0'
            epsilon_string += '1'
        else:
            gamma_string += '1'
            epsilon_string += '0'

    gamma = int(gamma_string, 2)
    epsilon = int(epsilon_string, 2)

    return gamma * epsilon


def life_support_rating(file: str) -> int:
    oxygen = 0
    co2 = 0

    data = []
    with open(file) as f:
        for line in f:
            data.append(line)

    oxygen_data = data.copy()
    oxygen = oxygen_rating(oxygen_data)
    co2 = carbon_dioxide_rating(data)
    print(f'Oxygen: {oxygen}\nCO2: {co2}')

    return oxygen * co2


def oxygen_rating(values: List[str], index: int = 0) -> int:
    keep = 0

    for i in range(len(values)):
        if values[i][index] == '0':
            keep -= 1
        elif values[i][index] == '1':
            keep += 1
    
    # print(f'Index: {index}\nKeep: {keep}')

    filtered = []
    if keep >= 0:
        filtered = list(filter(lambda item: item[index] == '1', values))
    else:
        filtered = list(filter(lambda item: item[index] == '0', values))

    # print(filtered)

    if (len(filtered) == 1):
        return int(filtered[0], 2)

    return oxygen_rating(filtered, index + 1)


def carbon_dioxide_rating(values: List[str], index: int = 0) -> int:
    keep = 0

    for i in range(len(values)):
        if values[i][index] == '0':
            keep -= 1
        elif values[i][index] == '1':
            keep += 1
    
    # print(f'Index: {index}\nKeep: {keep}')

    filtered = []
    if keep < 0:
        filtered = list(filter(lambda item: item[index] == '1', values))
    else:
        filtered = list(filter(lambda item: item[index] == '0', values))

    # print(filtered)

    if (len(filtered) == 1):
        return int(filtered[0], 2)

    return carbon_dioxide_rating(filtered, index + 1)


def main():
    print('Welcome to Day 02 of Advent of Code 2021')

    power = power_consumption('./data/day_03.txt', 12)

    print(f'Power Consumption: {power!r}')

    lsr = life_support_rating('./data/day_03.txt')

    print(f'Life Support Rating: {lsr!r}')


if __name__ == '__main__':
    main()
