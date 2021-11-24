import typing


def find_sum_pair(value: int, array: "typing.List[int]") -> int:
    for item in array:
        other = value - item
        if (other in array):
            return (item * other)

    return 0


def find_sum_triplets(value: int, array: "typing.List[int]") -> int:
    for item in array:
        secondSum = value - item
        for item2 in array:
            other = secondSum - item2
            if (other in array):
                return (item * item2 * other)

    return 0
