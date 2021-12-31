from itertools import repeat
from tqdm.contrib.concurrent import process_map
from AoC2021.day_21 import scores_from_string, universe_count


# Answer is too high: 444356092776315



def scores_from_string_helper(pos_1: int, pos_2: int, rolls: str) -> tuple[int, int, str]:
    score_1, score_2 = scores_from_string(pos_1, pos_2, rolls)
    return (score_1, score_2, rolls)


def play_quantum_game(pos_1: int, pos_2: int) -> tuple[int, int]:
    universes_1 = 0
    universes_2 = 0

    to_process = [c for c in 'abcdefg']

    while to_process:
        results = process_map(scores_from_string_helper, repeat(pos_1), repeat(pos_2), to_process, chunksize=max(1, int(len(to_process) / 1000)))
        to_process.clear()

        for r in results:
            score_1, score_2, rolls = r
            if score_1 >= 21:
                universes_1 += universe_count(rolls)
            elif score_2 >= 21:
                universes_2 += universe_count(rolls)
            else:
                to_process.extend([rolls + c for c in 'abcdefg'])

    return (universes_1, universes_2)


def main():
    print('Welcome to Day 21 Extreme')

    universes_1, universes_2 = play_quantum_game(3, 10)

    print(f'Universe 1: {universes_1}\nUniverse 2: {universes_2}')


if __name__ == '__main__':
    main()
