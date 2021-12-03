from typing import List


def parse_file(file: str) -> List[str]:
    data = []

    with open(file) as f:
        for line in f:
            data.append(line.strip())

    return data


def parse_int_file(file: str) -> List[int]:
    data = []

    with open(file) as f:
        for line in f:
            data.append(int(line))

    return data
