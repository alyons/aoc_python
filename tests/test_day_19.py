from AoC2021.day_19 import build_beacon_map, parse_scanners
from copy import deepcopy

test_data = parse_scanners('./tests/data/day_19.txt')


def test_build_beacon_map():
    scanners = deepcopy(test_data)
    beacons = build_beacon_map(scanners)
    assert len(beacons) == 79
