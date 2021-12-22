from AoC2021.day_19 import Scanner, build_beacon_map, parse_scanners, apply_counter_clockwise_rotation


def main():
    print('Welcome to Day 01 of Advent of Code 2021')

    scanners = parse_scanners('./tests/data/day_19.txt')
    beacons = sorted(list(build_beacon_map(scanners)), key = lambda x: (x[0], x[1], x[2]))
    print(f'Number of Beacons: {len(beacons)}')
    # # # for b in beacons:
    # # #     print(b)

    # # for b in scanners[0].beacons:
    # #     print(b)


if __name__ == '__main__':
    main()
