from AoC2021.util import parse_cave_graph
from AoC2021.day_12 import complex_paths, complex_paths_recursive, simple_paths, simple_paths_recursive
from time import clock_gettime_ns, CLOCK_REALTIME



def main():
    print('Welcome to Day 12 of Advent of Code 2021')

    edges = parse_cave_graph('./data/day_12.txt')

    # start_time = clock_gettime_ns(CLOCK_REALTIME)
    # simple_i = simple_paths(edges)
    # end_time = clock_gettime_ns(CLOCK_REALTIME)
    # print(f'Total Time (ns): {end_time - start_time}')
    # print(f'Unique Paths (i): {len(simple_i)!r}')

    # start_time = clock_gettime_ns(CLOCK_REALTIME)
    # simple_r = simple_paths_recursive(edges)
    # end_time = clock_gettime_ns(CLOCK_REALTIME)
    # print(f'Total Time (ns): {end_time - start_time}')
    # print(f'Unique Paths (r): {len(simple_r)!r}')

    small_caves = {e for edge in edges for e in edge if e.islower()}

    start_time = clock_gettime_ns(CLOCK_REALTIME)
    complex_i = complex_paths(edges)
    end_time = clock_gettime_ns(CLOCK_REALTIME)
    print(f'Total Time (ns): {end_time - start_time}')
    print(f'Unique Paths (i): {len(complex_i)!r}')

    start_time = clock_gettime_ns(CLOCK_REALTIME)
    complex_r = complex_paths_recursive(edges, small_caves)
    end_time = clock_gettime_ns(CLOCK_REALTIME)
    print(f'Total Time (ns): {end_time - start_time}')
    print(f'Unique Paths (r): {len(complex_r)!r}')


if __name__ == '__main__':
    main()
