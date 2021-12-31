from AoC2021.day_24 import run_program
from AoC2021.util import parse_file
from itertools import combinations_with_replacement, product, repeat
from concurrent.futures import ProcessPoolExecutor
import functools
import operator
from tqdm.contrib.concurrent import process_map
from copy import deepcopy


def segment_instructions(instructions: list[str]):
    segments = []
    indecies = [i for i,v in enumerate(instructions) if 'inp' in v]

    for i in range(len(indecies)):
        if i < len(indecies) - 1:
            segments.append(instructions[indecies[i]:indecies[i + 1]])
        else:
            segments.append(instructions[indecies[i]:])
    
    return segments


def run_segment(segment, input, variables):
    run_program(segment, [input], variables)
    
    return input, variables


def test_model_number(segment, number, state_dict):
    input = [int(c) for c in str(number)]
    if any(i == 0 for i in input): return None

    if number < 10:
        variables = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    else:
        variables = deepcopy(state_dict[int(number / 10)])

    return run_segment(segment, number, variables)



def test_two_halves(instructions, z, first, second):
    full = str(first) + str(second)
    input = [int(c) for c in full]
    if any(i == 0 for i in input): return None

    variables = { 'w': 0, 'x': 0, 'y': 0, 'z': z }
    run_program(instructions, input, variables)

    return int(full) if variables['z'] == 0 else None


def test_model_number_whole(instructions, number):
    input = [int(c) for c in str(number)]
    variables = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    run_program(instructions, input, variables)

    return number if variables['z'] == 0 else -1

def test_front(instructions, number):
    input = [int(c) for c in str(number)]
    if any(i == 0 for i in input): return None

    variables = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    run_program(instructions, input, variables)
    return (variables['z'], number)


def find_largest_model_number(instructions: list[str], print_debug: bool = False):
    if print_debug: print('Segmenting instructions...')
    segments = segment_instructions(instructions)

    front_instructions = functools.reduce(operator.iconcat, segments[7:], [])
    front_z: dict[int, int] = {}

    front_min = 1111111
    front_max = 10000000

    print('Building front half of numbers...')
    results = process_map(test_front, repeat(front_instructions), range(front_min, front_max), chunksize=100000)
    print('Finished building front half!')

    for r in results:
        if r:
            z, n = r
            if not z in front_z:
                front_z[z] = n
            else:
                front_z[z] = max(front_z[z], n)

    print('Begin processing back half...')
    valid_numbers = []
    for k, v in front_z.items():
        print(f'Testing for start {v}...')
        partial_test = functools.partial(test_two_halves, instructions, k, v)
        full_res = process_map(partial_test, range(front_min, front_max), chunksize=100000)
        valid_numbers.extend([r for r in full_res if r])
        print(f'Completed testing for {v}....')
        print(f'Valid numbers: {len(valid_numbers)}')
    
    print(valid_numbers)

    if valid_numbers:
        return max(valid_numbers)
    else:
        return -1

    # r_min = 11111111111111
    # r_i = 1000000
    # overlimit = 100000000000000
    # r_max = r_min + r_i
    # segment_index = 0
    # valid_numbers = []

    # # while r_min < 100:
    # while r_min < overlimit:
    #     print(f'Testing next range: [{r_min} - {r_max}]')
    #     # results = process_map(test_model_number, repeat(segments[segment_index]), range(r_min, r_max), repeat(state_dict), chunksize=int(r_max / 10)) # chunksize=min(100000, int(r_max/10)))
    #     results = process_map(test_model_number_whole, repeat(instructions), range(r_min, r_max), chunksize=int(r_i/10))
    #     # segment_index += 1
    #     r_min += r_i
    #     r_max = min(overlimit, r_max + r_i)

    #     valid_numbers.extend([r for r in results if r != -1])

    # # with ProcessPoolExecutor(max_workers=100) as executor:
    # #     results = list(tqdm(executor.map(test_model_number, range(11111111111111, 100000000000000), repeat(instructions))))
    # # results = process_map(test_model_number, range(11111111111111, 100000000000000), repeat(instructions), chunksize=5)

    # # if print_debug:
    # #     print('Completed processing values...')
    
    # # return max(valid_numbers)


def main():
    print('Welcome to Day 24')

    instructions = parse_file('./data/day_24.txt')

    model_number = find_largest_model_number(instructions, True)

    print(f'Model Number: {model_number}')


if __name__ == '__main__':
    main()
