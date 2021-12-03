from typing import List

def power_consumption(report: List[str]) -> int:
    length = len(report[0])

    zero_array = [0] * length
    one_array = [0] * length

    for item in report:
        for i in range(length):
            if item[i] == '0':
                zero_array[i] += 1
            elif item[i] == '1':
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


def oxygen_rating(values: List[str], index: int = 0) -> int:
    keep = 0

    for i in range(len(values)):
        if values[i][index] == '0':
            keep -= 1
        elif values[i][index] == '1':
            keep += 1
    
    filtered = []
    if keep >= 0:
        filtered = list(filter(lambda item: item[index] == '1', values))
    else:
        filtered = list(filter(lambda item: item[index] == '0', values))

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
    
    filtered = []
    if keep < 0:
        filtered = list(filter(lambda item: item[index] == '1', values))
    else:
        filtered = list(filter(lambda item: item[index] == '0', values))

    if (len(filtered) == 1):
        return int(filtered[0], 2)

    return carbon_dioxide_rating(filtered, index + 1)


def life_support_rating(report: List[str]) -> int:
    oxygen_data = report.copy()
    oxygen = oxygen_rating(oxygen_data)
    co2 = carbon_dioxide_rating(report)

    return oxygen * co2