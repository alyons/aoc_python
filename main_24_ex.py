from itertools import repeat
from tqdm.contrib.concurrent import process_map
from AoC2021.day_24 import run_program
from AoC2021.util import parse_file


def segment_instructions(instructions: list[str]):
    segments = []
    indecies = [i for i,v in enumerate(instructions) if 'inp' in v]

    for i in range(len(indecies)):
        if i < len(indecies) - 1:
            segments.append(instructions[indecies[i]:indecies[i + 1]])
        else:
            segments.append(instructions[indecies[i]:])
    
    return segments


def run_program_as_process(instructions: list[str], digit: int, dict_item: tuple[int, int]):
    z, base_number = dict_item
    variables = { 'w': 0, 'x': 0, 'y': 0, 'z': z }
    run_program(instructions, [digit], variables)

    return (variables['z'], int(str(base_number) + str(digit)))


def find_max_model_number(instructions: list[str]):
    print('Finding the appropriate model number...')

    best_z: dict[int, dict[int, int]] = { k:{} for k in range(1,15) }
    segments = segment_instructions(instructions)

    print('Step 1: Seed the dictionary with each starting value')
    for d in range(1, 10):
        variables = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
        run_program(segments[0], [d], variables)

        z = variables['z']
        if not z in best_z[1]:
            best_z[1][z] = d
        else:
            best_z[1][z] = max(d, best_z[1][z])

    print('Step 2: Iterate through signigicant digits....')
    for sd in range(2, 15):
        print(f'Step 2: Significant Digit: {sd}...')
        _prior = sd - 1
        for d in range(1, 10):
            results = process_map(run_program_as_process, repeat(segments[_prior]), repeat(d), best_z[_prior].items(), chunksize=max(1, int(len(best_z[_prior].items())/10)))

            for r in results:
                z, value = r
                if not z in best_z[sd]:
                    best_z[sd][z] = value
                else:
                    best_z[sd][z] = max(value, best_z[sd][z])
        print(f'Items found for SD ({sd}): {len(best_z[sd].values())}')

    if 0 not in best_z[14]:
        for k in best_z[14]:
            print(f'[{k}]: {best_z[14][k]}')
        return -1
    else:
        return best_z[14][0]


def find_min_model_number(instructions: list[str]):
    print('Finding the appropriate model number...')

    best_z: dict[int, dict[int, int]] = { k:{} for k in range(1,15) }
    segments = segment_instructions(instructions)

    print('Step 1: Seed the dictionary with each starting value')
    for d in range(1, 10):
        variables = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
        run_program(segments[0], [d], variables)

        z = variables['z']
        if not z in best_z[1]:
            best_z[1][z] = d
        else:
            best_z[1][z] = min(d, best_z[1][z])

    print('Step 2: Iterate through signigicant digits....')
    for sd in range(2, 15):
        print(f'Step 2: Significant Digit: {sd}...')
        _prior = sd - 1
        for d in range(1, 10):
            results = process_map(run_program_as_process, repeat(segments[_prior]), repeat(d), best_z[_prior].items(), chunksize=max(1, int(len(best_z[_prior].items())/10)))

            for r in results:
                z, value = r
                if not z in best_z[sd]:
                    best_z[sd][z] = value
                else:
                    best_z[sd][z] = min(value, best_z[sd][z])
        print(f'Items found for SD ({sd}): {len(best_z[sd].values())}')

    if 0 not in best_z[14]:
        for k in best_z[14]:
            print(f'[{k}]: {best_z[14][k]}')
        return -1
    else:
        return best_z[14][0]


def main():
    print('Welcome to Day 24 EX!')

    instructions = parse_file('./data/day_24.txt')

    # model_number = find_max_model_number(instructions)
    model_number = find_min_model_number(instructions)

    print(f'Model Number: {model_number}')


if __name__ == '__main__':
    main()
