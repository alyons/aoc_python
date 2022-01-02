from AoC2021.day_23 import amphipod_str_to_list, amphipod_a_star, total_energy_used, render_map

test_values = [
    '(2,4,A)(6,3,A)(8,2,A)(8,4,A)(2,1,B)(4,3,B)(6,1,B)(6,2,B)(4,1,C)(4,2,C)(6,4,C)(8,3,C)(2,2,D)(2,3,D)(4,4,D)(10,0,D)',
    '(0,0,A)(2,4,A)(6,3,A)(8,4,A)(2,1,B)(4,3,B)(6,1,B)(6,2,B)(4,1,C)(4,2,C)(6,4,C)(8,3,C)(2,2,D)(2,3,D)(4,4,D)(10,0,D)',
    '(0,0,A)(2,4,A)(6,3,A)(8,4,A)(2,1,B)(4,3,B)(6,2,B)(9,0,B)(4,1,C)(4,2,C)(6,4,C)(8,3,C)(2,2,D)(2,3,D)(4,4,D)(10,0,D)',
    ''
]


def main():
    # Part 1
    # amphipod_str = '(2,2,A)(8,2,A)(2,1,B)(6,1,B)(4,1,C)(6,2,C)(4,2,D)(8,1,D)' # Test Value
    # amphipod_str = '(4,1,A)(8,2,A)(2,2,B)(6,2,B)(4,2,C)(6,1,C)(2,1,D)(8,1,D)' # Input Value

    # Part 2
    # amphipod_str= '(2,4,A)(6,3,A)(8,2,A)(8,4,A)(2,1,B)(4,3,B)(6,1,B)(6,2,B)(4,1,C)(4,2,C)(6,4,C)(8,3,C)(2,2,D)(2,3,D)(4,4,D)(8,1,D)' # Test Value
    amphipod_str = '(4,1,A)(6,3,A)(8,2,A)(8,4,A)(2,4,B)(4,3,B)(6,2,B)(6,4,B)(4,2,C)(4,4,C)(6,1,C)(8,3,C)(2,1,D)(2,2,D)(2,3,D)(8,1,D)' # Input Value
    # amphipod_str = '(2,4,A)(6,3,A)(7,0,A)(8,4,A)(1,0,B)(3,0,B)(4,3,B)(5,0,B)(6,1,C)(6,2,C)(6,4,C)(8,3,C)(0,0,D)(2,3,D)(4,4,D)(8,2,D)'

    amphipods = amphipod_str_to_list(amphipod_str)

    moves = amphipod_a_star(amphipod_str)
    energy = total_energy_used(amphipods, moves, 3)
    print(f'Energy Used: {energy}')


if __name__ == '__main__':
    main()
