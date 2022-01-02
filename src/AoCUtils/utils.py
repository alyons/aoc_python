from typing import Iterable
from time import clock_gettime_ns, CLOCK_REALTIME


def parse_file(file: str) -> list[str]:
    data = []

    with open(file) as f:
        for line in f:
            data.append(line.strip())

    return data


def manhattan_distance(a: Iterable[int], b: Iterable[int]) -> int:
    return sum([abs(x - y) for (x, y) in zip(a, b)])


def generate_time_string(start_time: int, is_running: bool = True) -> str:
    diff = clock_gettime_ns(CLOCK_REALTIME) - start_time
    remainder = int(diff % 1e9)
    total_seconds = diff // 1e9
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)

    if is_running:
        return f'Time Running: {minutes:02}:{seconds:02}.{remainder}'
    else:
        return f'Ran in: {minutes:02}:{seconds:02}.{remainder}'
