from AoC2021.day_17 import find_max_height_ex, find_max_height_tlm, find_unique_shots, fire, integer_sum, sum_consecutive_integers


# 990 was too low...

def main():
    print('Welcome to Day 17 of Advent of Code 2021')

    # target area: x=244..303, y=-91..-54

    # target = (20, 30, -5, -10)
    target = (244, 303, -54, -91)

    # Part 1
    # print(integer_sum(1, 9))
    # print(integer_sum(1, 10))
    # print(integer_sum(1, 91))
    # print(integer_sum(1, 90))

    # Part 2
    count = find_unique_shots(target)
    print(f'Unique Shots: {count}')

if __name__ == '__main__':
    main()
