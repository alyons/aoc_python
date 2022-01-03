from AoC2021.day_06 import lantern_fish_sim
from AoC2021.util import parse_int_count

fish_timer = parse_int_count('./tests/data/day_06.txt')

def parse_expected(input: str) -> dict:
    output = {}
    for i in range(9):
        output[i] = 0
    
    for key in [int(item) for item in input.split(',')]:
        output[key] += 1

    return output


def test_latern_fish_sim():
    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('2,3,2,0,1')
    assert expected == fish_timer
    assert count == 5

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('1,2,1,6,0,8')
    assert expected == fish_timer
    assert count == 6

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('0,1,0,5,6,7,8')
    assert expected == fish_timer
    assert count == 7

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('6,0,6,4,5,6,7,8,8')
    assert expected == fish_timer
    assert count == 9

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('5,6,5,3,4,5,6,7,7,8')
    assert expected == fish_timer
    assert count == 10

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('4,5,4,2,3,4,5,6,6,7')
    assert expected == fish_timer
    assert count == 10

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('3,4,3,1,2,3,4,5,5,6')
    assert expected == fish_timer
    assert count == 10

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('2,3,2,0,1,2,3,4,4,5')
    assert expected == fish_timer
    assert count == 10

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('1,2,1,6,0,1,2,3,3,4,8')
    assert expected == fish_timer
    assert count == 11

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('0,1,0,5,6,0,1,2,2,3,7,8')
    assert expected == fish_timer
    assert count == 12

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('6,0,6,4,5,6,0,1,1,2,6,7,8,8,8')
    assert expected == fish_timer
    assert count == 15

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8')
    assert expected == fish_timer
    assert count == 17

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8')
    assert expected == fish_timer
    assert count == 19

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8')
    assert expected == fish_timer
    assert count == 20

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7')
    assert expected == fish_timer
    assert count == 20

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8')
    assert expected == fish_timer
    assert count == 21

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8')
    assert expected == fish_timer
    assert count == 22

    count = lantern_fish_sim(fish_timer, 1)
    expected = parse_expected('6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8')
    assert expected == fish_timer
    assert count == 26

    count = lantern_fish_sim(fish_timer, 62)
    assert count == 5934
