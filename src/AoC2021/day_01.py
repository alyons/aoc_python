from typing import List


def increase_count(array: List[int]) -> int:
    count = 0
    i = 1

    while i < len(array):
        if (array[i] > array[i - 1]):
            count += 1
        i += 1

    return count


def sum_increase_count(array: List[int]) -> int:
    sums = []

    for i in range(len(array) - 2):
        second = i + 1
        third = i + 2

        sums.append(array[i])
        sums[i] += array[second]
        sums[i] += array[third]

    return increase_count(sums)


def parse_day_01(file: str) -> List[int]:
    data = []

    with open(file) as f:
        for line in f:
            data.append(int(line))

    return data
