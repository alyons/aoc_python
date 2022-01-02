from AoC2021.day_23 import amphipod_a_star, amphipod_str_to_list, total_energy_used


def test_total_energy_used():
    amphipod_str = '(2,2,A)(8,2,A)(2,1,B)(6,1,B)(4,1,C)(6,2,C)(4,2,D)(8,1,D)'
    expected = 12521
    moves = amphipod_a_star(amphipod_str)
    amphipods = amphipod_str_to_list(amphipod_str)
    actual = total_energy_used(amphipods, moves)
    assert expected == actual
