from AoC2021.day_07 import align_crabs, align_crabs_ex
from AoC2021.util import parse_int_count

crabs = parse_int_count('./tests/data/day_07.txt')


def test_align_crabs():
    assert 37 == align_crabs(crabs)


def test_align_crabs_ex():
    assert 168 == align_crabs_ex(crabs)
