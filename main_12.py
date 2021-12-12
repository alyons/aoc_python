from AoC2021.util import parse_cave_graph
from AoC2021.day_12 import complex_paths, simple_paths, simple_paths_recursive
from time import clock_gettime_ns, CLOCK_REALTIME



def main():
    print('Welcome to Day 12 of Advent of Code 2021')

    edges = parse_cave_graph('./data/day_12.txt')

    start_time = clock_gettime_ns(CLOCK_REALTIME)
    simple_i = simple_paths(edges)
    end_time = clock_gettime_ns(CLOCK_REALTIME)
    print(f'Total Time (ns): {end_time - start_time}')
    print(f'Unique Paths (i): {len(simple_i)!r}')

    start_time = clock_gettime_ns(CLOCK_REALTIME)
    simple_r = simple_paths_recursive(edges)
    end_time = clock_gettime_ns(CLOCK_REALTIME)
    print(f'Total Time (ns): {end_time - start_time}')
    print(f'Unique Paths (r): {len(simple_r)!r}')

    # complex_list = complex_paths(edges, True)

    # print(f'Complex Paths: {len(complex_list)}')


if __name__ == '__main__':
    main()
